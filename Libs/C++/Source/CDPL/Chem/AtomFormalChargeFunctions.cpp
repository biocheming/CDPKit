/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * AtomFormalChargeFunctions.cpp 
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

#include <cmath>

#include "CDPL/Chem/AtomFunctions.hpp"
#include "CDPL/Chem/Atom.hpp"
#include "CDPL/Chem/AtomProperty.hpp"
#include "CDPL/Chem/AtomTypeFunctions.hpp"


using namespace CDPL; 


long Chem::getFormalCharge(const Atom& atom)
{
	static long DEF_CHARGE = 0;

    return atom.getPropertyOrDefault<long>(AtomProperty::FORMAL_CHARGE, DEF_CHARGE);
}

void Chem::setFormalCharge(Atom& atom, long charge)
{
    atom.setProperty(AtomProperty::FORMAL_CHARGE, charge);
}

void Chem::clearFormalCharge(Atom& atom)
{
    atom.removeProperty(AtomProperty::FORMAL_CHARGE);
}

bool Chem::hasFormalCharge(const Atom& atom)
{
    return atom.isPropertySet(AtomProperty::FORMAL_CHARGE);
}

long Chem::calcFormalCharge(const Atom& atom, const MolecularGraph& molgraph)
{
	unsigned int atom_type = getType(atom);
	long valence = calcValence(atom, molgraph) + getUnpairedElectronCount(atom);

	const int* val_states = getValenceStates(atom_type);
	int nearest_val_state = -1;

	for (int i = 0; val_states[i] >= 0; i++)
		if (std::abs(val_states[i] - valence) < std::abs(nearest_val_state - valence))
			nearest_val_state = val_states[i];

	if (nearest_val_state == -1)
		return 0;

	switch (getIUPACGroup(atom_type)) {
		
		case 1: 
		case 2:
		case 13:
		case 14:
			return (nearest_val_state - valence);

		case 15:
		case 16:
		case 17: 
			return (valence - nearest_val_state);

		default:
			return 0;
	}
}
