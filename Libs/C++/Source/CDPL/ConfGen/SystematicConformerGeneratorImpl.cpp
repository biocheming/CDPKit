/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * SystematicConformerGeneratorImpl.cpp 
 *
 * This file is part of the Chemical Data Processing Toolkit
 *
 * Copyright (C) 2003-2010 Thomas A. Seidel <thomas.seidel@univie.ac.at>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; see the file COPYING. If not, write to
 * the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 */


#include "StaticInit.hpp"

#include <algorithm>
#include <functional>
#include <iterator>

#include <boost/bind.hpp>

#include "CDPL/ConfGen/UtilityFunctions.hpp"
#include "CDPL/ConfGen/FragmentType.hpp"
#include "CDPL/Chem/MolecularGraph.hpp"
#include "CDPL/Chem/Bond.hpp"
#include "CDPL/Chem/AtomFunctions.hpp"
#include "CDPL/Chem/AtomContainerFunctions.hpp"
#include "CDPL/Chem/BondFunctions.hpp"
#include "CDPL/Chem/Entity3DFunctions.hpp"
#include "CDPL/Chem/MolecularGraphFunctions.hpp"
#include "CDPL/Chem/AtomType.hpp"
#include "CDPL/ForceField/InteractionType.hpp"
#include "CDPL/Base/Exceptions.hpp"

#include "SystematicConformerGeneratorImpl.hpp"


using namespace CDPL;


namespace
{

	template <typename InteractionData>
	void extractFragmentMMFF94InteractionData2(const InteractionData& src_ia_data, InteractionData& frag_ia_data, InteractionData& non_frag_ia_data, 
											   const Chem::MolecularGraph& src_molgraph, const Chem::MolecularGraph& frag)
	{
		for (typename InteractionData::ConstElementIterator it = src_ia_data.getElementsBegin(), end = src_ia_data.getElementsEnd(); it != end; ++it) {
			const typename InteractionData::ElementType& params = *it;

			if (frag.containsAtom(src_molgraph.getAtom(params.getAtom1Index())) && 
				frag.containsAtom(src_molgraph.getAtom(params.getAtom2Index())))

				frag_ia_data.addElement(params);
			else
				non_frag_ia_data.addElement(params);
		}
	}

	template <typename InteractionData>
	void extractFragmentMMFF94InteractionData3(const InteractionData& src_ia_data, InteractionData& frag_ia_data, InteractionData& non_frag_ia_data, 
											   const Chem::MolecularGraph& src_molgraph, const Chem::MolecularGraph& frag)
	{
		for (typename InteractionData::ConstElementIterator it = src_ia_data.getElementsBegin(), end = src_ia_data.getElementsEnd(); it != end; ++it) {
			const typename InteractionData::ElementType& params = *it;

			if (frag.containsAtom(src_molgraph.getAtom(params.getAtom1Index())) &&
				frag.containsAtom(src_molgraph.getAtom(params.getAtom2Index())) && 
				frag.containsAtom(src_molgraph.getAtom(params.getAtom3Index())))

				frag_ia_data.addElement(params);
			else
				non_frag_ia_data.addElement(params);
		}
	}

	template <typename InteractionData>
	void extractFragmentMMFF94InteractionData4(const InteractionData& src_ia_data, InteractionData& frag_ia_data, InteractionData& non_frag_ia_data, 
											   const Chem::MolecularGraph& src_molgraph, const Chem::MolecularGraph& frag)
	{
		for (typename InteractionData::ConstElementIterator it = src_ia_data.getElementsBegin(), end = src_ia_data.getElementsEnd(); it != end; ++it) {
			const typename InteractionData::ElementType& params = *it;

			if (frag.containsAtom(src_molgraph.getAtom(params.getAtom1Index())) &&
				frag.containsAtom(src_molgraph.getAtom(params.getAtom2Index())) && 
				frag.containsAtom(src_molgraph.getAtom(params.getAtom3Index())) &&
				frag.containsAtom(src_molgraph.getAtom(params.getAtom4Index())))

				frag_ia_data.addElement(params);
			else
				non_frag_ia_data.addElement(params);
		}
	}
}


ConfGen::SystematicConformerGeneratorImpl::SystematicConformerGeneratorImpl()
{
	fragConfGen.reuseExistingCoordinates(false);
}

ConfGen::SystematicConformerGeneratorImpl::~SystematicConformerGeneratorImpl() {}

void ConfGen::SystematicConformerGeneratorImpl::applySettings(const Settings& settings)
{
	this->settings = settings;
}

const ConfGen::SystematicConformerGeneratorImpl::Settings& 
ConfGen::SystematicConformerGeneratorImpl::getSettings() const
{
	return settings;
}

ConfGen::SystematicConformerGeneratorImpl::Status 
ConfGen::SystematicConformerGeneratorImpl::generate(const Chem::MolecularGraph& molgraph)
{
	timer.start();	

	freeVector3DArrays();
	buildTree(molgraph);
	buildAtomIndexMaps(fragTree);
	genConfSearchMMFF94InteractionData();
	clearNodeConformers(fragTree);

	if (timeoutExceeded())
		return Status::TIMEOUT_EXCEEDED;
	
	if (!setupBuildFragmentConformers()) {
		if (timeoutExceeded())
			return Status::TIMEOUT_EXCEEDED;

		return Status::ERROR;
	}

	distFragmentMMFF94InteractionData(fragTree);
	calcLeafNodeConformerEnergies(fragTree);

	return Status::SUCCESS;
}

void ConfGen::SystematicConformerGeneratorImpl::freeVector3DArrays()
{
	freeCoordArrays.clear();

	std::for_each(allocCoordArrays.begin(), allocCoordArrays.end(), 
				  boost::bind(&SystematicConformerGeneratorImpl::freeVector3DArray, this, 
							  boost::bind<Math::Vector3DArray*>(&Math::Vector3DArray::SharedPointer::get, _1)));
}

void ConfGen::SystematicConformerGeneratorImpl::buildTree(const Chem::MolecularGraph& molgraph)
{
	buildFragNodes.clear();

	getFragmentLinkBonds(molgraph);

	fragTree.splitRecursive(molgraph, bondList); // build tree according to build fragment link bonds

	getBuildFragmentNodes(fragTree);

	genChainBuildFragmentSubtrees();

/*
	std::cerr << "digraph FragmentTree" << std::endl;
	std::cerr << '{' << std::endl;

	fragTree.printTree(std::cerr);

	std::cerr << '}' << std::endl;
*/
}

void ConfGen::SystematicConformerGeneratorImpl::buildAtomIndexMaps(FragmentTreeNode& node) const
{
	FragmentTreeNode::AtomIndexMap& idx_map = node.getAtomIndexMap();
	
	idx_map.clear();

	std::transform(node.getFragment().getAtomsBegin(), node.getFragment().getAtomsEnd(), std::back_inserter(idx_map),
				   boost::bind(&Chem::MolecularGraph::getAtomIndex, &fragTree.getFragment(), _1));

	if (!node.hasChildren())
		return;

	buildAtomIndexMaps(*node.getLeftChild());
	buildAtomIndexMaps(*node.getRightChild());
}

void ConfGen::SystematicConformerGeneratorImpl::genConfSearchMMFF94InteractionData()
{
	genMMFF94InteractionData(fragTree.getFragment(), settings.getSearchForceFieldType(), fragTree.getMMFF94InteractionData());
}

void ConfGen::SystematicConformerGeneratorImpl::clearNodeConformers(FragmentTreeNode& node) const
{
	node.clearConformers();

	if (!node.hasChildren())
		return;

	clearNodeConformers(*node.getLeftChild());
	clearNodeConformers(*node.getRightChild());
}

bool ConfGen::SystematicConformerGeneratorImpl::setupBuildFragmentConformers()
{
	for (NodeList::const_iterator it = buildFragNodes.begin(), end = buildFragNodes.end(); it != end; ++it) {
		FragmentTreeNode* node = *it;

		if (settings.existingCoordinatesReused() && 
			(!settings.ringsEnumerated() || node->getFragmentType() != FragmentType::FLEXIBLE_RING_SYSTEM) && 
			setExistingCoordinates(*node))
			continue;
		
		fragLibEntry.create(node->getFragment());
		buildFragmentLibraryEntryAtomIndexMap(*node);

		if (setFragmentLibraryConformers(*node))
			continue;

		if (!genFragmentConformers(*node))
			return false;
	}

	return true;
}

void ConfGen::SystematicConformerGeneratorImpl::calcLeafNodeConformerEnergies(FragmentTreeNode& node)
{
	if (node.hasChildren()) {
		calcLeafNodeConformerEnergies(*node.getLeftChild());
		calcLeafNodeConformerEnergies(*node.getRightChild());
		return;
	}

	mmff94EnergyCalc.setup(node.getMMFF94InteractionData());

	for (FragmentTreeNode::ConformerIterator it = node.getConformersBegin(), end = node.getConformersEnd(); it != end; ++it) 
		it->second = mmff94EnergyCalc(*it->first);

	if (node.getNumConformers() > 1)
		std::sort(node.getConformersBegin(), node.getConformersEnd(), boost::bind(std::less<double>(),
																				  boost::bind(&FragmentTreeNode::ConfData::second, _1),
																				  boost::bind(&FragmentTreeNode::ConfData::second, _2)));
}

void ConfGen::SystematicConformerGeneratorImpl::getBuildFragmentNodes(FragmentTreeNode& node)
{
	if (!node.hasChildren()) {
		buildFragNodes.push_back(&node);
		return;
	}

	getBuildFragmentNodes(*node.getLeftChild());
	getBuildFragmentNodes(*node.getRightChild());
}

void ConfGen::SystematicConformerGeneratorImpl::genChainBuildFragmentSubtrees()
{
	using namespace Chem;

	for (NodeList::const_iterator it = buildFragNodes.begin(), end = buildFragNodes.end(); it != end; ++it) {
		FragmentTreeNode* node = *it;
		const MolecularGraph& frag = node->getFragment();
		unsigned int frag_type = perceiveFragmentType(frag);

		node->setFragmentType(frag_type);

		if (frag_type != FragmentType::CHAIN)
			continue;

		getRotatableBonds(frag);

		if (!bondList.empty())
			node->splitRecursive(frag, bondList);
	}
}

bool ConfGen::SystematicConformerGeneratorImpl::setExistingCoordinates(FragmentTreeNode& node)
{
	using namespace Chem;

	try {
		Math::Vector3DArray* coords = allocVector3DArray();
		Vec3DArrayDeallocator dealloc_guard(this, coords);

		const MolecularGraph& frag = node.getFragment();
		const AtomIndexMap& atom_idx_map = node.getAtomIndexMap();

		for (std::size_t i = 0, num_atoms = frag.getNumAtoms(); i < num_atoms; i++) {
			const Atom& atom = frag.getAtom(i);

			(*coords)[atom_idx_map[i]] = get3DCoordinates(atom);
		}

		if (node.getFragmentType() == FragmentType::CHAIN && node.hasChildren())
			distChainBuildFragmentCoordinates(node, *coords, false);

		else {
			node.addConformer(coords);
			dealloc_guard.release();

			enumNitrogens(node);
		}

		return true;

	} catch (const Base::ItemNotFound& e) {}

	return false;
}

bool ConfGen::SystematicConformerGeneratorImpl::setFragmentLibraryConformers(FragmentTreeNode& node)
{
	using namespace Chem;

	if (!settings.getFragmentLibrary())
		return false;

	const MolecularGraph::SharedPointer& entry_ptr = settings.getFragmentLibrary()->getEntry(fragLibEntry.getHashCode());

	if (!entry_ptr)
		return false;

	if (entry_ptr->getNumAtoms() != fragLibEntry.getNumAtoms())  // sanity check
		return false;

	std::size_t num_confs = getNumConformations(*entry_ptr);

	if (num_confs == 0)
		return false;

	switch (node.getFragmentType()) {

		case FragmentType::CHAIN: {
			Math::Vector3DArray* coords = allocVector3DArray();
			Vec3DArrayDeallocator dealloc_guard(this, coords);

			getLibraryFragmentConformation(*entry_ptr, 0, *coords);

			if (node.hasChildren())
				distChainBuildFragmentCoordinates(node, *coords, true);

			else {
				node.addConformer(coords);
				dealloc_guard.release();

				enumNitrogens(node);
			}

			return true;
		}

		case FragmentType::RIGID_RING_SYSTEM:
		case FragmentType::FLEXIBLE_RING_SYSTEM: {
			setupAromRingSubstituentBondLengthList(node);

			for (std::size_t  i = 0; i < num_confs; i++) {
				Math::Vector3DArray* coords = allocVector3DArray();
				Vec3DArrayDeallocator dealloc_guard(this, coords);

				getLibraryFragmentConformation(*entry_ptr, i, *coords);
				fixAromRingSubstituentBondLengths(*coords);

				node.addConformer(coords);
				dealloc_guard.release();
			}

			enumNitrogens(node);

			return true;
		}
	}

	return false;
}

bool ConfGen::SystematicConformerGeneratorImpl::genFragmentConformers(FragmentTreeNode& node)
{
	std::size_t frag_build_to = settings.getMaxFragmentBuildTime();

	if (settings.getTimeout() > 0) {
		std::size_t elapsed_time = timer.elapsed().wall / 1000000;

		if (elapsed_time >= settings.getTimeout())
			return false;

		if (frag_build_to > 0)
			frag_build_to = std::min(frag_build_to, settings.getTimeout() - elapsed_time);
		else
			frag_build_to = settings.getTimeout() - elapsed_time;
	}

	fragConfGen.setTimeout(frag_build_to);

	if (!fragSSSR)
		fragSSSR.reset(new Chem::SmallestSetOfSmallestRings());

	fragSSSR->perceive(fragLibEntry);
	setSSSR(fragLibEntry, fragSSSR);

	genMMFF94InteractionData(fragLibEntry, settings.getBuildForceFieldType(), fragBuildMMFF94Data);

	fragConfGen.generate(fragLibEntry, fragBuildMMFF94Data, node.getFragmentType());

	std::size_t num_confs = fragConfGen.getNumConformers();

	if (num_confs == 0) 
		return false;

	if (node.getFragmentType() == FragmentType::CHAIN) {
		Math::Vector3DArray* coords = allocVector3DArray();
		Vec3DArrayDeallocator dealloc_guard(this, coords);
		const Math::Vector3DArray& gen_coords = fragConfGen.getCoordinates(0);

		for (IndexPairList::const_iterator it = fragLibEntryAtomIdxMap.begin(), end = fragLibEntryAtomIdxMap.end(); it != end; ++it) {
			const IndexPair& idx_mapping = *it;

			(*coords)[idx_mapping.second].assign(gen_coords[idx_mapping.first]);
		}

		if (node.hasChildren())
			distChainBuildFragmentCoordinates(node, *coords, false);

		else {
			node.addConformer(coords);
			dealloc_guard.release();

			enumNitrogens(node);
		}

		return true;
	}

	setupAromRingSubstituentBondLengthList(node);

	for (std::size_t i = 0; i < num_confs; i++) {
		Math::Vector3DArray* coords = allocVector3DArray();
		Vec3DArrayDeallocator dealloc_guard(this, coords);
		const Math::Vector3DArray& gen_coords = fragConfGen.getCoordinates(i);

		for (IndexPairList::const_iterator it = fragLibEntryAtomIdxMap.begin(), end = fragLibEntryAtomIdxMap.end(); it != end; ++it) {
			const IndexPair& idx_mapping = *it;

			(*coords)[idx_mapping.second].assign(gen_coords[idx_mapping.first]);
		}

		fixAromRingSubstituentBondLengths(*coords);

		node.addConformer(coords);
		dealloc_guard.release();
	}

	enumNitrogens(node);

	return true;
}

void ConfGen::SystematicConformerGeneratorImpl::buildFragmentLibraryEntryAtomIndexMap(const FragmentTreeNode& node)
{
	using namespace Chem;

	const AtomIndexMap& atom_idx_map = node.getAtomIndexMap();
	const FragmentLibraryEntry::AtomMapping& entry_atom_map = fragLibEntry.getAtomMapping();

	fragLibEntryAtomIdxMap.clear();

	for (std::size_t i = 0, num_atoms = node.getFragment().getNumAtoms(); i < num_atoms; i++)
		fragLibEntryAtomIdxMap.push_back(IndexPair(fragLibEntry.getAtomIndex(*entry_atom_map[i]), atom_idx_map[i]));
}

void ConfGen::SystematicConformerGeneratorImpl::distChainBuildFragmentCoordinates(FragmentTreeNode& node, const Math::Vector3DArray& coords, 
																				  bool fix_stereo)
{
	if (node.hasChildren()) {
		distChainBuildFragmentCoordinates(*node.getLeftChild(), coords, fix_stereo);
		distChainBuildFragmentCoordinates(*node.getRightChild(), coords, fix_stereo);
		return;
	}

	const AtomIndexMap& atom_idx_map = node.getAtomIndexMap();

	Math::Vector3DArray* node_coords = allocVector3DArray();
	Vec3DArrayDeallocator dealloc_guard(this, node_coords);

	for (AtomIndexMap::const_iterator idx_it = atom_idx_map.begin(), idx_end = atom_idx_map.end(); idx_it != idx_end; ++idx_it) {
		std::size_t atom_idx = *idx_it;

		(*node_coords)[atom_idx] = coords[atom_idx];
	}
		
	node.addConformer(node_coords);
	dealloc_guard.release();

	if (fix_stereo)
		fixAtomAndBondConfigurations(node);

	enumNitrogens(node);
}

void ConfGen::SystematicConformerGeneratorImpl::getLibraryFragmentConformation(const Chem::MolecularGraph& lib_frag, 
																			   std::size_t conf_idx, Math::Vector3DArray& coords) const
{
	for (IndexPairList::const_iterator it = fragLibEntryAtomIdxMap.begin(), end = fragLibEntryAtomIdxMap.end(); it != end; ++it) {
		const IndexPair& idx_mapping = *it;

		coords[idx_mapping.second].assign((*get3DCoordinatesArray(lib_frag.getAtom(idx_mapping.first)))[conf_idx]);
	}
}

void ConfGen::SystematicConformerGeneratorImpl::setupAromRingSubstituentBondLengthList(FragmentTreeNode& node)
{
	using namespace Chem;
	using namespace ForceField;

	const MolecularGraph& frag = node.getFragment();
	const MolecularGraph& root_frag = fragTree.getFragment();
	const MMFF94BondStretchingInteractionData& bs_params = fragTree.getMMFF94InteractionData().getBondStretchingInteractions();

	aromRingSubstBondLens.clear();

	for (MolecularGraph::ConstBondIterator it = frag.getBondsBegin(), end = frag.getBondsEnd(); it != end; ++it) {
		const Bond& bond = *it;

		if (getRingFlag(bond))
			continue;

		const Atom* atom1 = &bond.getBegin();
		const Atom* atom2 = &bond.getEnd();

		if (getAromaticityFlag(*atom2) && getType(*atom1) != AtomType::H && getAromaticBondCount(*atom2, frag) == 2 && getExplicitBondCount(*atom1, frag) == 1) {
			std::swap(atom1, atom2);

		} else if (!(getAromaticityFlag(*atom1) && getType(*atom2) != AtomType::H && getAromaticBondCount(*atom1, frag) == 2 && getExplicitBondCount(*atom2, frag) == 1))
			continue;

		std::size_t atom1_idx = root_frag.getAtomIndex(*atom1);
		std::size_t atom2_idx = root_frag.getAtomIndex(*atom2);

		for (MMFF94BondStretchingInteractionData::ConstElementIterator bs_ia_it = bs_params.getElementsBegin(), 
				 bs_ia_end = bs_params.getElementsEnd(); bs_ia_it != bs_ia_end; ++bs_ia_it) {

			const MMFF94BondStretchingInteraction& bs_ia = *bs_ia_it;

			if ((bs_ia.getAtom1Index() == atom1_idx && bs_ia.getAtom2Index() == atom2_idx) ||
				(bs_ia.getAtom1Index() == atom2_idx && bs_ia.getAtom2Index() == atom1_idx)) {

				aromRingSubstBondLens.push_back(boost::make_tuple(atom1_idx, atom2_idx, bs_ia.getReferenceLength()));
				break;
			}
		}
	}
}

void ConfGen::SystematicConformerGeneratorImpl::fixAromRingSubstituentBondLengths(Math::Vector3DArray& coords) const
{
	if (aromRingSubstBondLens.empty())
		return;

	for (BondLengthDescriptorList::const_iterator it = aromRingSubstBondLens.begin(), end = aromRingSubstBondLens.end(); it != end; ++it) {
		const BondLengthDescriptor& descr = *it;

		std::size_t atom1_idx = descr.get<0>();
		std::size_t atom2_idx = descr.get<1>();

		coords[atom2_idx].minusAssign(coords[atom1_idx]);
		coords[atom2_idx] *= descr.get<2>() / length(coords[atom2_idx]);
		coords[atom2_idx].plusAssign(coords[atom1_idx]);
	}
}

void ConfGen::SystematicConformerGeneratorImpl::fixAtomAndBondConfigurations(FragmentTreeNode& node) const
{
	// TODO
}

void ConfGen::SystematicConformerGeneratorImpl::enumNitrogens(FragmentTreeNode& node)
{
	if (!settings.nitrogensEnumerated())
		return;

	// TODO
}

void ConfGen::SystematicConformerGeneratorImpl::getFragmentLinkBonds(const Chem::MolecularGraph& molgraph)
{
	using namespace Chem;

	bool h_rotors = settings.hydrogenRotorsEnabled();

	bondList.clear();

	for (MolecularGraph::ConstBondIterator it = molgraph.getBondsBegin(), end = molgraph.getBondsEnd(); it != end; ++it) {
		const Bond& bond = *it;

		if (!isFragmentLinkBond(bond, molgraph))
			continue;

		if (isHydrogenRotor(bond, molgraph)) {
			const Atom& atom1 = bond.getBegin();
			const Atom& atom2 = bond.getEnd();

			if (!getRingFlag(atom1) && !getRingFlag(atom2))
				continue;

			if (!h_rotors && !getAromaticityFlag(atom1) && !getAromaticityFlag(atom2)) 
				continue;
		}

		bondList.push_back(&bond);
	}
}

void ConfGen::SystematicConformerGeneratorImpl::getRotatableBonds(const Chem::MolecularGraph& molgraph)
{
	using namespace Chem;

	bondList.clear();	

	bool h_rotors = settings.hydrogenRotorsEnabled();

	for (MolecularGraph::ConstBondIterator it = molgraph.getBondsBegin(), end = molgraph.getBondsEnd(); it != end; ++it) {
		const Bond& bond = *it;
	
		if (isRotatable(bond, molgraph, h_rotors, false, true)) 
			bondList.push_back(&bond);
	}
}

void ConfGen::SystematicConformerGeneratorImpl::genMMFF94InteractionData(const Chem::MolecularGraph& molgraph, unsigned int ff_type, 
																		 ForceField::MMFF94InteractionData& ia_data)
{
 	unsigned int ia_types = ForceField::InteractionType::ALL;

	switch (ff_type) {

		case ForceFieldType::MMFF94S:
			mmff94Parameterizer.setStaticParameterDefaults();
			break;

		case ForceFieldType::MMFF94:
			mmff94Parameterizer.setDynamicParameterDefaults();
			break;

		case ForceFieldType::MMFF94S_NO_ESTAT:
			ia_types ^= ForceField::InteractionType::ELECTROSTATIC;
			mmff94Parameterizer.setStaticParameterDefaults();
			break;

		case ForceFieldType::MMFF94_NO_ESTAT:
			ia_types ^= ForceField::InteractionType::ELECTROSTATIC;
			mmff94Parameterizer.setDynamicParameterDefaults();
			break;

		default:
			throw Base::ValueError("SystematicConformerGeneratorImpl: invalid forcefield type");
	}

	mmff94Parameterizer.performStrictAtomTyping(settings.strictAtomTypingPerformed());
	mmff94Parameterizer.parameterize(molgraph, ia_data, ia_types);
}

void ConfGen::SystematicConformerGeneratorImpl::distFragmentMMFF94InteractionData(FragmentTreeNode& node)
{
	if (node.hasChildren()) {
		distFragmentMMFF94InteractionData(*node.getLeftChild());
		distFragmentMMFF94InteractionData(*node.getRightChild());
	}

	if (&node != &fragTree)
		extractFragmentMMFF94InteractionData(node);
}

void ConfGen::SystematicConformerGeneratorImpl::extractFragmentMMFF94InteractionData(FragmentTreeNode& node)
{
	using namespace Chem;
	using namespace ForceField;

	const MolecularGraph& root_frag = fragTree.getFragment();
	const MolecularGraph& node_frag = node.getFragment();

	MMFF94InteractionData& root_ia_data = fragTree.getMMFF94InteractionData();
	MMFF94InteractionData& node_ia_data = node.getMMFF94InteractionData();

	node_ia_data.clear();
	tmpMMFF94Data.clear();

	extractFragmentMMFF94InteractionData2(root_ia_data.getBondStretchingInteractions(), node_ia_data.getBondStretchingInteractions(), 
										  tmpMMFF94Data.getBondStretchingInteractions(), root_frag, node_frag);
	extractFragmentMMFF94InteractionData2(root_ia_data.getElectrostaticInteractions(), node_ia_data.getElectrostaticInteractions(), 
										  tmpMMFF94Data.getElectrostaticInteractions(), root_frag, node_frag);
	extractFragmentMMFF94InteractionData2(root_ia_data.getVanDerWaalsInteractions(), node_ia_data.getVanDerWaalsInteractions(), 
										  tmpMMFF94Data.getVanDerWaalsInteractions(), root_frag, node_frag);
	extractFragmentMMFF94InteractionData3(root_ia_data.getAngleBendingInteractions(), node_ia_data.getAngleBendingInteractions(), 
										  tmpMMFF94Data.getAngleBendingInteractions(), root_frag, node_frag);
	extractFragmentMMFF94InteractionData3(root_ia_data.getStretchBendInteractions(), node_ia_data.getStretchBendInteractions(), 
										  tmpMMFF94Data.getStretchBendInteractions(), root_frag, node_frag);
	extractFragmentMMFF94InteractionData4(root_ia_data.getOutOfPlaneBendingInteractions(), node_ia_data.getOutOfPlaneBendingInteractions(), 
										  tmpMMFF94Data.getOutOfPlaneBendingInteractions(), root_frag, node_frag);
	extractFragmentMMFF94InteractionData4(root_ia_data.getTorsionInteractions(), node_ia_data.getTorsionInteractions(), 
										  tmpMMFF94Data.getTorsionInteractions(), root_frag, node_frag);

	root_ia_data.swap(tmpMMFF94Data);
}

bool ConfGen::SystematicConformerGeneratorImpl::timeoutExceeded() const
{
	if (settings.getTimeout() == 0)
		return false;

	return (timer.elapsed().wall > (boost::timer::nanosecond_type(settings.getTimeout()) * 1000000));
}

Math::Vector3DArray* ConfGen::SystematicConformerGeneratorImpl::allocVector3DArray()
{
	if (!freeCoordArrays.empty()) {
		Math::Vector3DArray* vec_array = freeCoordArrays.back();

		vec_array->resize(fragTree.getFragment().getNumAtoms());
		freeCoordArrays.pop_back();

		return vec_array;
	}

	Math::Vector3DArray::SharedPointer vec_array(new Math::Vector3DArray());

	vec_array->resize(fragTree.getFragment().getNumAtoms());
	allocCoordArrays.push_back(vec_array);

	return vec_array.get();
}

void ConfGen::SystematicConformerGeneratorImpl::freeVector3DArray(Math::Vector3DArray* vec_array)
{
	freeCoordArrays.push_back(vec_array);
}
