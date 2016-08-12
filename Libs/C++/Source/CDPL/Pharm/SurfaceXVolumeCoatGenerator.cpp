/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * SurfaceXVolumeCoatGenerator.cpp 
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

#include <limits>
#include <algorithm>
#include <cmath>

#include "CDPL/Pharm/SurfaceXVolumeCoatGenerator.hpp"
#include "CDPL/Pharm/Pharmacophore.hpp"
#include "CDPL/Pharm/Feature.hpp"
#include "CDPL/Pharm/FeatureFunctions.hpp"
#include "CDPL/Chem/MolecularGraph.hpp"
#include "CDPL/Chem/Atom.hpp"
#include "CDPL/Chem/AtomFunctions.hpp"
#include "CDPL/Chem/Entity3DFunctions.hpp"
#include "CDPL/Chem/Entity3DContainerFunctions.hpp"
#include "CDPL/Chem/AtomType.hpp"
#include "CDPL/Chem/AtomDictionary.hpp"
#include "CDPL/Math/SVDecomposition.hpp"


using namespace CDPL; 


const unsigned int Pharm::SurfaceXVolumeCoatGenerator::DEF_FEATURE_TYPE;
const unsigned int Pharm::SurfaceXVolumeCoatGenerator::DEF_FEATURE_GEOM;
const double       Pharm::SurfaceXVolumeCoatGenerator::DEF_PROBE_RADIUS;
const double       Pharm::SurfaceXVolumeCoatGenerator::DEF_GRID_OVERSIZE;
const double       Pharm::SurfaceXVolumeCoatGenerator::DEF_GRID_STEP_SIZE;
const double       Pharm::SurfaceXVolumeCoatGenerator::DEF_MIN_SURFACE_ACC;
const std::size_t  Pharm::SurfaceXVolumeCoatGenerator::DEF_NUM_TEST_POINTS;


Pharm::SurfaceXVolumeCoatGenerator::SurfaceXVolumeCoatGenerator(): 
    featureType(DEF_FEATURE_TYPE), featureGeom(DEF_FEATURE_GEOM), probeRadius(DEF_PROBE_RADIUS),
	gridOversize(DEF_GRID_OVERSIZE), gridStepSize(DEF_GRID_STEP_SIZE), minSurfAcc(DEF_MIN_SURFACE_ACC),
	numTestPoints(DEF_NUM_TEST_POINTS)
{}

Pharm::SurfaceXVolumeCoatGenerator::SurfaceXVolumeCoatGenerator(
	const Chem::AtomContainer& cntnr, const Chem::MolecularGraph& parent_molgraph, Pharmacophore& pharm):
    featureType(DEF_FEATURE_TYPE), featureGeom(DEF_FEATURE_GEOM), probeRadius(DEF_PROBE_RADIUS),
	gridOversize(DEF_GRID_OVERSIZE), gridStepSize(DEF_GRID_STEP_SIZE), minSurfAcc(DEF_MIN_SURFACE_ACC),
	numTestPoints(DEF_NUM_TEST_POINTS) 
{
    generate(cntnr, parent_molgraph, pharm);
}

void Pharm::SurfaceXVolumeCoatGenerator::setFeatureType(unsigned int type)
{
    featureType = type;
}

unsigned int Pharm::SurfaceXVolumeCoatGenerator::getFeatureType() const
{
    return featureType;
}

void Pharm::SurfaceXVolumeCoatGenerator::setFeatureGeometry(unsigned int geom)
{
    featureGeom = geom;
}

unsigned int Pharm::SurfaceXVolumeCoatGenerator::getFeatureGeometry() const
{
    return featureGeom;
}

void Pharm::SurfaceXVolumeCoatGenerator::setProbeRadius(double radius)
{
	probeRadius = radius;
}

double Pharm::SurfaceXVolumeCoatGenerator::getProbeRadius() const
{
	return probeRadius;
}

void Pharm::SurfaceXVolumeCoatGenerator::setGridStepSize(double size)
{
	gridStepSize = size;
}

double Pharm::SurfaceXVolumeCoatGenerator::getGridStepSize() const
{
	return gridStepSize;
}

void Pharm::SurfaceXVolumeCoatGenerator::setGridOversize(double size)
{
	gridOversize = size;
}

double Pharm::SurfaceXVolumeCoatGenerator::getGridOversize() const
{
	return gridOversize;
}

void Pharm::SurfaceXVolumeCoatGenerator::setMinSurfaceAccessibility(double min_acc)
{
	minSurfAcc = min_acc;
}

double Pharm::SurfaceXVolumeCoatGenerator::getMinSurfaceAccessibility() const
{
	return minSurfAcc;
}

void Pharm::SurfaceXVolumeCoatGenerator::setNumTestPoints(std::size_t num_points)
{
	numTestPoints = num_points;
}

std::size_t Pharm::SurfaceXVolumeCoatGenerator::getNumTestPoints() const
{
	return numTestPoints;
}

void Pharm::SurfaceXVolumeCoatGenerator::generate(const Chem::AtomContainer& cntnr, const Chem::MolecularGraph& parent_molgraph, Pharmacophore& pharm)
{
	if (!init(cntnr, parent_molgraph))
		return;

	xformCoordinates();
	calcBoundingBox();
    initGridAtomLookupTable();
	extractSurfaceAtoms();
	generateXVolumes(pharm);
}

bool Pharm::SurfaceXVolumeCoatGenerator::init(const Chem::AtomContainer& cntnr, const Chem::MolecularGraph& parent_molgraph)
{
	using namespace Chem;

	std::size_t num_prnt_atoms = parent_molgraph.getNumAtoms();
	std::size_t num_atoms = cntnr.getNumAtoms();

	if (num_atoms == 0 || num_prnt_atoms == 0)
		return false;

	atomContainer = &cntnr;
	parentMolGraph = &parent_molgraph;

	atomRadii.clear();
	atomRadii.reserve(num_prnt_atoms);

	for (MolecularGraph::ConstAtomIterator it = parent_molgraph.getAtomsBegin(), end = parent_molgraph.getAtomsEnd(); it != end; ++it)
		atomRadii.push_back(getVdWRadius(*it) + probeRadius);

	atomCoords.clear();	
	atomCoords.reserve(num_prnt_atoms);	

	get3DCoordinates(parent_molgraph, atomCoords);

	atomIndices.clear();
	atomIndices.reserve(num_atoms);

	surfaceAtoms.clear();

	surfAtomMask.resize(num_prnt_atoms);
	surfAtomMask.reset();

	for (MolecularGraph::ConstAtomIterator it = cntnr.getAtomsBegin(), end = cntnr.getAtomsEnd(); it != end; ++it)
		atomIndices.push_back(parent_molgraph.getAtomIndex(*it));

	return true;
}

void Pharm::SurfaceXVolumeCoatGenerator::xformCoordinates()
{
	Math::Vector3D ctr;
	std::size_t num_atoms = atomContainer->getNumAtoms();

	for (std::size_t i = 0; i < num_atoms; i++)
		ctr.plusAssign(atomCoords[atomIndices[i]]);
	
	ctr /= num_atoms; 

	svdU.resize(num_atoms, 3, false);

	for (std::size_t i = 0; i < num_atoms; i++) {
		const Math::Vector3D& pos = atomCoords[atomIndices[i]];

		svdU(i, 0) = pos(0) - ctr(0);
		svdU(i, 1) = pos(1) - ctr(1);
		svdU(i, 2) = pos(2) - ctr(2);
	}

	Math::Matrix3D svd_v;
	Math::Vector3D svd_w;
	Math::Matrix3D xform;

	Math::svDecompose(svdU, svd_w, svd_v);

	row(xform, 0) = column(svd_v, 0) / length(column(svd_v, 0));
	row(xform, 1) = column(svd_v, 1) / length(column(svd_v, 1));
	row(xform, 2) = column(svd_v, 2) / length(column(svd_v, 2));

	std::size_t num_prnt_atoms = parentMolGraph->getNumAtoms();
	Math::Vector3D tmp;

	for (std::size_t i = 0; i < num_prnt_atoms; i++) {
		tmp.assign(atomCoords[i] - ctr);
		prod(xform, tmp, atomCoords[i]);
	}
}

void Pharm::SurfaceXVolumeCoatGenerator::calcBoundingBox()
{
	bBoxMin.clear(std::numeric_limits<double>::max());
	bBoxMax.clear(-std::numeric_limits<double>::max());

	for (AtomIndexList::const_iterator it = atomIndices.begin(), end = atomIndices.end(); it != end; ++it) {
		std::size_t atom_idx = *it;
		double radius = atomRadii[atom_idx];
		const Math::Vector3D& coords = atomCoords[atom_idx];

		bBoxMin(0) = std::min(bBoxMin(0), coords(0) - radius);
		bBoxMin(1) = std::min(bBoxMin(1), coords(1) - radius);
		bBoxMin(2) = std::min(bBoxMin(2), coords(2) - radius);

		bBoxMax(0) = std::max(bBoxMax(0), coords(0) + radius);
		bBoxMax(1) = std::max(bBoxMax(1), coords(1) + radius);
		bBoxMax(2) = std::max(bBoxMax(2), coords(2) + radius);
	}

	gridXSize = std::ceil((bBoxMax(0) - bBoxMin(0) + 2.0 * gridOversize) / gridStepSize);
	gridYSize = std::ceil((bBoxMax(1) - bBoxMin(1) + 2.0 * gridOversize) / gridStepSize);
	gridZSize = std::ceil((bBoxMax(2) - bBoxMin(2) + 2.0 * gridOversize) / gridStepSize);

	bBoxMin(0) = 0.5 * (bBoxMax(0) + bBoxMin(0) - gridXSize * gridStepSize);
	bBoxMin(1) = 0.5 * (bBoxMax(1) + bBoxMin(1) - gridYSize * gridStepSize);
	bBoxMin(2) = 0.5 * (bBoxMax(2) + bBoxMin(2) - gridZSize * gridStepSize);

	bBoxMax(0) = bBoxMin(0) + gridXSize * gridStepSize;
	bBoxMax(1) = bBoxMin(1) + gridYSize * gridStepSize;
	bBoxMax(2) = bBoxMin(2) + gridZSize * gridStepSize;

}

void Pharm::SurfaceXVolumeCoatGenerator::initGridAtomLookupTable()
{
	gridAtomLookup.assign(gridXSize * gridYSize * gridZSize, AtomIndexListPtr());

	std::size_t num_prnt_atoms = parentMolGraph->getNumAtoms();

	for (std::size_t i = 0; i < num_prnt_atoms; i++) {
		double radius = atomRadii[i];
		const Math::Vector3D& coords = atomCoords[i];

		if ((coords(0) + radius) < bBoxMin(0))
			continue;

		if ((coords(1) + radius) < bBoxMin(1))
			continue;
	
		if ((coords(2) + radius) < bBoxMin(2))
			continue;

		if ((coords(0) - radius) > bBoxMax(0))
			continue;

		if ((coords(1) - radius) > bBoxMax(1))
			continue;
	
		if ((coords(2) - radius) > bBoxMax(2))
			continue;

		std::size_t grid_span = std::ceil(2 * radius / gridStepSize);
		double x = coords(0) - 0.5 * grid_span * gridStepSize - bBoxMin(0);

		for (std::size_t j = 0; j <= grid_span; j++, x += gridStepSize) {
			if (x < 0.0)
				continue;

			std::size_t x_idx = x / gridStepSize;

			if (x_idx > gridXSize - 1)
				continue;

			double y = coords(1) - 0.5 * grid_span * gridStepSize - bBoxMin(1);

			for (std::size_t k = 0; k <= grid_span; k++, y += gridStepSize) {
				if (y < 0.0)
					continue;

				std::size_t y_idx = y / gridStepSize;

				if (y_idx > gridYSize - 1)
					continue;

				double z = coords(2) - 0.5 * grid_span * gridStepSize - bBoxMin(2);

				for (std::size_t l = 0; l <= grid_span; l++, z += gridStepSize) {
					if (z < 0.0)
						continue;

					std::size_t z_idx = z / gridStepSize;

					if (z_idx > gridZSize - 1)
						continue;

					AtomIndexListPtr& alist_ptr = gridAtomLookup[z_idx * gridXSize * gridYSize + y_idx * gridXSize + x_idx];

					if (!alist_ptr)
						alist_ptr.reset(new AtomIndexList());

					alist_ptr->push_back(i);
				}
			}
		}
	}
}

void Pharm::SurfaceXVolumeCoatGenerator::extractSurfaceAtoms()
{
	initTestPoints();

	Math::Vector3D test_pos;
	Math::Vector3D tmp;

	for (AtomIndexList::const_iterator it = atomIndices.begin(), end = atomIndices.end(); it != end; ++it) {
		std::size_t atom_idx = *it;
		double radius = atomRadii[atom_idx];
		const Math::Vector3D& coords = atomCoords[atom_idx];

		std::size_t num_acc_pts = 0; //

		for (std::size_t i = 0; i < numTestPoints; i++) {
			test_pos.assign(coords + testPoints[i] * radius);

			std::size_t x_idx = (test_pos(0) - bBoxMin(0)) / gridStepSize;
			std::size_t y_idx = (test_pos(1) - bBoxMin(1)) / gridStepSize;
			std::size_t z_idx = (test_pos(2) - bBoxMin(2)) / gridStepSize;

			AtomIndexListPtr& alist_ptr = gridAtomLookup[z_idx * gridXSize * gridYSize + y_idx * gridXSize + x_idx];

			if (!alist_ptr) {
				num_acc_pts++;
				continue;
			}

			bool found_coll = false;

			for (AtomIndexList::const_iterator al_it = alist_ptr->begin(), al_end = alist_ptr->end(); al_it != al_end; ++al_it) {
				std::size_t nbr_atom_idx = *al_it;

				if (nbr_atom_idx == atom_idx)
					continue;

				tmp.assign(atomCoords[nbr_atom_idx] - test_pos);

				if (length(tmp) <= atomRadii[nbr_atom_idx]) {
					found_coll = true;
					break;
				}
			} 

			if (!found_coll) 
				num_acc_pts++;
		}

		if ((double(num_acc_pts) / numTestPoints) >= minSurfAcc) {
			surfaceAtoms.push_back(atom_idx);
			surfAtomMask.set(atom_idx);
		}
	}
}

void Pharm::SurfaceXVolumeCoatGenerator::initTestPoints()
{
	if (testPoints.getSize() == numTestPoints)
		return;

	testPoints.resize(numTestPoints);

	double inc = M_PI * (3.0 - std::sqrt(5.0));
	double off = 2.0 / numTestPoints;

	for (std::size_t i = 0; i < numTestPoints; i++) {
		double y = i * off - 1.0 + off * 0.5;
		double r = std::sqrt(1.0 - y * y);
		double phi = i * inc;
		
		Math::Vector3D& pt = testPoints[i];

		pt(0) = std::cos(phi) * r;
		pt(1) = y;
		pt(2) = std::sin(phi) * r;
	}
}

void Pharm::SurfaceXVolumeCoatGenerator::generateXVolumes(Pharmacophore& pharm)
{
	using namespace Chem;

	std::size_t num_surf_atoms = surfaceAtoms.size();

	for (std::size_t i = 0; i < num_surf_atoms; i++) {
		std::size_t atom_idx = surfaceAtoms[i];
		const Atom& atom = parentMolGraph->getAtom(atom_idx);
	
		if (atom.getNumAtoms() != 1)
			continue;

		if (getType(atom) != AtomType::H)
			continue;

		const Atom& nbr_atom = atom.getAtom(0);

		if (!parentMolGraph->containsAtom(nbr_atom))
			continue;
		
		if (!parentMolGraph->containsBond(atom.getBond(0)))
			continue;
		
		if (getType(nbr_atom) == AtomType::H)
			continue;

		surfAtomMask.reset(atom_idx);

		std::size_t nbr_atom_idx = parentMolGraph->getAtomIndex(nbr_atom);

		if (!surfAtomMask.test(nbr_atom_idx)) {
			surfaceAtoms.push_back(nbr_atom_idx);
			surfAtomMask.set(nbr_atom_idx);
		}
	}

	std::size_t new_num_surf_atoms = surfaceAtoms.size();
	double h_cov_rad = AtomDictionary::getCovalentRadius(AtomType::H, 1);
	double h_vdw_rad = AtomDictionary::getVdWRadius(AtomType::H);

	for (std::size_t i = 0; i < new_num_surf_atoms; i++) {
		std::size_t atom_idx = surfaceAtoms[i];
		
		if (!surfAtomMask.test(atom_idx))
			continue;
		
		const Atom& atom = parentMolGraph->getAtom(atom_idx);

		atomCoords[atom_idx].assign(get3DCoordinates(atom));

		if (i >= num_surf_atoms) 
			atomRadii[atom_idx] = getCovalentRadius(atom, 1) + h_cov_rad + h_vdw_rad * 0.75;
		else 
			atomRadii[atom_idx] -= probeRadius;
	}

	for (std::size_t i = 0; i < new_num_surf_atoms; i++) {
		std::size_t atom_idx = surfaceAtoms[i];
		
		if (!surfAtomMask.test(atom_idx))
			continue;

		Feature& xvol = pharm.addFeature();

		setType(xvol, featureType);
		setGeometry(xvol, featureGeom);
		set3DCoordinates(xvol, atomCoords[atom_idx]);
		setTolerance(xvol, atomRadii[atom_idx]);	
	}
}
