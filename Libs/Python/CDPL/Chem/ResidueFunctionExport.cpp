/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * ResidueFunctionExport.cpp 
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


#include <boost/python.hpp>

#include "CDPL/Chem/ResidueFunctions.hpp"
#include "CDPL/Chem/MolecularGraph.hpp"

#include "FunctionExports.hpp"


void CDPLPythonChem::exportResidueFunctions()
{
    using namespace boost;
    using namespace CDPL;

	python::def("getResidueType", &Chem::getResidueType, python::arg("code"));
    python::def("getResidueName", &Chem::getResidueName, python::arg("code"),
				python::return_value_policy<python::copy_const_reference>());
    python::def("isStandardResidue", &Chem::isStandardResidue, python::arg("code"));
	python::def("getResidueStructure", &Chem::getResidueStructure, python::arg("code"),
				python::return_value_policy<python::reference_existing_object>());
}
