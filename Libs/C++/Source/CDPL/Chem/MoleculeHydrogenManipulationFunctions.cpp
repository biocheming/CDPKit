/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * MoleculeHydrogenManipulationFunctions.cpp 
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

#include "CDPL/Chem/MoleculeFunctions.hpp"
#include "CDPL/Chem/AtomFunctions.hpp"
#include "CDPL/Chem/BondFunctions.hpp"
#include "CDPL/Chem/Molecule.hpp"
#include "CDPL/Chem/Atom.hpp"
#include "CDPL/Chem/AtomType.hpp"


using namespace CDPL; 


void Chem::makeHydrogenDeplete(Molecule& mol)
{
	std::size_t num_atoms = mol.getNumAtoms();

	for (std::size_t i = 0; i < num_atoms; ) {
		const Atom& atom = mol.getAtom(i);

		if (getType(atom) != AtomType::H) {
			i++;
			continue;
		}

		mol.removeAtom(i);
		num_atoms--;
	}
}
	
void Chem::makeOrdinaryHydrogenDeplete(Molecule& mol, unsigned int flags)
{
	std::size_t num_atoms = mol.getNumAtoms();

	for (std::size_t i = 0; i < num_atoms; ) {
		const Atom& atom = mol.getAtom(i);

		if (!isOrdinaryHydrogen(atom, mol, flags)) {
			i++;
			continue;
		}

		mol.removeAtom(i);
		num_atoms--;
	}
}

void Chem::makeHydrogenComplete(Molecule& mol)
{
	std::size_t num_atoms = mol.getNumAtoms();

	for (std::size_t i = 0; i < num_atoms; i++) {
		std::size_t impl_h_cnt = getImplicitHydrogenCount(mol.getAtom(i));

		for (std::size_t j = 0; j < impl_h_cnt; j++) {
			Atom& new_atom = mol.addAtom();
			Bond& new_bond = mol.addBond(i, mol.getAtomIndex(new_atom));
			
			setType(new_atom, AtomType::H);
			setOrder(new_bond, 1);
		} 
	}
}
