/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * AtomContainerMassCompositionFunctions.cpp 
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

#include <sstream>
#include <string>
#include <iomanip>

#include "CDPL/Chem/AtomContainerFunctions.hpp"
#include "CDPL/Chem/AtomFunctions.hpp"
#include "CDPL/Chem/AtomContainer.hpp"
#include "CDPL/Chem/Atom.hpp"
#include "CDPL/Chem/AtomDictionary.hpp"
#include "CDPL/Chem/AtomType.hpp"


using namespace CDPL; 


double Chem::calcExplicitMass(const AtomContainer& cntnr)
{
	double mass = 0.0;

	for (AtomContainer::ConstAtomIterator it = cntnr.getAtomsBegin(), end = cntnr.getAtomsEnd(); it != end; ++it)
		mass += getAtomicWeight(*it);

	return mass;
}

void Chem::calcExplicitMassComposition(const AtomContainer& cntnr, MassComposition& comp)
{
	double mass = 0.0;
	
	AtomContainer::ConstAtomIterator atoms_end = cntnr.getAtomsEnd();

	for (AtomContainer::ConstAtomIterator it = cntnr.getAtomsBegin(); it != atoms_end; ++it) {
		const Atom& atom = *it;
		unsigned int atom_type = getType(atom);

		if (atom_type > AtomType::MAX_ATOMIC_NO)
			atom_type = AtomType::UNKNOWN;

		double atomic_wt = getAtomicWeight(atom);

		comp[atom_type] += atomic_wt;
		mass += atomic_wt;
	}

	MassComposition::EntryIterator entries_end = comp.getEntriesEnd();

	for (MassComposition::EntryIterator it = comp.getEntriesBegin(); it != entries_end; ++it) 
		it->second /= mass;
}

void Chem::buildExplicitMassCompositionString(const AtomContainer& cntnr, std::string& comp_str)
{
	MassComposition mass_comp;

	calcExplicitMassComposition(cntnr, mass_comp);

	std::ostringstream comp_str_os;
	const std::string unknown_type_sym = "?";
	MassComposition::ConstEntryIterator entries_end = mass_comp.getEntriesEnd();

	for (MassComposition::ConstEntryIterator it = mass_comp.getEntriesBegin(); it != entries_end; ) {
		const std::string& symbol = (it->first == AtomType::UNKNOWN ? unknown_type_sym : 
									 AtomDictionary::getSymbol(it->first));

		comp_str_os << symbol << ": " << std::fixed << std::showpoint << std::setprecision(3) << std::right 
					<< (it->second * 100) << '%';

		if (++it != entries_end)
			comp_str_os << ' ';	
	}

	comp_str.append(comp_str_os.str());
}
