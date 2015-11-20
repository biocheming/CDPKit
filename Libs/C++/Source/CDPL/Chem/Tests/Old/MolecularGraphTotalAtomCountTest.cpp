/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * MolecularGraphTotalAtomCountTest.cpp 
 *
 * This file is part of the Chemical Data Processing Toolkit
 *
 * Copyright (C) 2003-2010 Thomas A. Seidel <thomas.seidel@univie.ac.at>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program; see the file COPYING. If not, write to
 * the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 */


#include <string>
#include <cstdlib>
#include <fstream>

#include <boost/test/auto_unit_test.hpp>

#include "CDPL/Chem/Molecule.hpp"
#include "CDPL/Chem/JMEMoleculeReader.hpp"
#include "CDPL/Chem/MolecularGraphProperties.hpp"
#include "CDPL/Chem/AtomContainerProperties.hpp"

#include "TestUtils.hpp"


BOOST_AUTO_TEST_CASE(MolecularGraphAtomCountTest)
{
	using namespace CDPL;
	using namespace Chem;

	Molecule mol;

//-----

	BOOST_CHECK(mol.getProperty(MolecularGraphProperty::TOTAL_ATOM_COUNT, false, false).isEmpty());

	BOOST_CHECK(mol.getProperty<std::size_t>(MolecularGraphProperty::TOTAL_ATOM_COUNT) == 0);

	BOOST_CHECK(!mol.getProperty(MolecularGraphProperty::TOTAL_ATOM_COUNT, false, false).isEmpty());

//-----

	std::ifstream ifs(std::string(std::string(std::getenv("CDPTK_DATA_DIR")) + "/Morphine.jme").c_str());

	BOOST_CHECK(ifs);

	BOOST_CHECK(JMEMoleculeReader(ifs).read(mol));

//-----

	BOOST_CHECK(mol.getProperty(MolecularGraphProperty::TOTAL_ATOM_COUNT, false, false).isEmpty());

	BOOST_CHECK(mol.getProperty<std::size_t>(MolecularGraphProperty::TOTAL_ATOM_COUNT) == 40);

	BOOST_CHECK(!mol.getProperty(MolecularGraphProperty::TOTAL_ATOM_COUNT, false, false).isEmpty());

//-----

	TestUtils::checkDependency(mol, MolecularGraphProperty::TOTAL_ATOM_COUNT, mol, AtomContainerProperty::ATOM_COUNT);
	TestUtils::checkDependency(mol, MolecularGraphProperty::TOTAL_ATOM_COUNT, mol, MolecularGraphProperty::IMPLICIT_H_COUNT);
}
