/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * Raw3DStructureGeneratorExport.cpp 
 *
 * This file is part of the Utilical Data Processing Toolkit
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

#include "CDPL/ConfGen/Raw3DStructureGenerator.hpp"
#include "CDPL/Chem/MolecularGraph.hpp"
#include "CDPL/ForceField/MMFF94InteractionData.hpp"

#include "Base/ObjectIdentityCheckVisitor.hpp"
#include "Base/CopyAssOp.hpp"

#include "ClassExports.hpp"


void CDPLPythonConfGen::exportRaw3DStructureGenerator()
{
    using namespace boost;
    using namespace CDPL;

	python::class_<ConfGen::Raw3DStructureGenerator>("Raw3DStructureGenerator", python::no_init)
		.def(python::init<>(python::arg("self")))
		.def(python::init<const ConfGen::Raw3DStructureGenerator&>((python::arg("self"), python::arg("gen"))))
		.def(CDPLPythonBase::ObjectIdentityCheckVisitor<ConfGen::Raw3DStructureGenerator>())
		.def("assign", CDPLPythonBase::copyAssOp(&ConfGen::Raw3DStructureGenerator::operator=), 
			 (python::arg("self"), python::arg("gen")), python::return_self<>())
		.def("calculateHydrogenPositions", &ConfGen::Raw3DStructureGenerator::calculateHydrogenPositions, 
			 (python::arg("self"), python::arg("calc")))
		.def("hydrogenPositionsCalculated", &ConfGen::Raw3DStructureGenerator::hydrogenPositionsCalculated, python::arg("self"))
		.def("regardAtomConfiguration", &ConfGen::Raw3DStructureGenerator::regardAtomConfiguration, 
			 (python::arg("self"), python::arg("regard")))
		.def("atomConfigurationRegarded", &ConfGen::Raw3DStructureGenerator::atomConfigurationRegarded, python::arg("self"))
		.def("regardBondConfiguration", &ConfGen::Raw3DStructureGenerator::regardBondConfiguration, 
			 (python::arg("self"), python::arg("regard")))
		.def("bondConfigurationRegarded", &ConfGen::Raw3DStructureGenerator::bondConfigurationRegarded, python::arg("self"))
			.def("setup", static_cast<void (ConfGen::Raw3DStructureGenerator::*)(const Chem::MolecularGraph&)>
			 (&ConfGen::Raw3DStructureGenerator::setup), (python::arg("self"), python::arg("molgraph")))
		.def("setup", static_cast<void (ConfGen::Raw3DStructureGenerator::*)(const Chem::MolecularGraph&, const ForceField::MMFF94InteractionData&)>
			 (&ConfGen::Raw3DStructureGenerator::setup), 
			 (python::arg("self"), python::arg("molgraph"), python::arg("ia_data")))
		.def("generate", &ConfGen::Raw3DStructureGenerator::generate, (python::arg("self"), python::arg("coords")))
		.add_property("calcHydrogenPositions", &ConfGen::Raw3DStructureGenerator::hydrogenPositionsCalculated, 
					  &ConfGen::Raw3DStructureGenerator::calculateHydrogenPositions)
		.add_property("regardAtomConfig", &ConfGen::Raw3DStructureGenerator::atomConfigurationRegarded, 
					  &ConfGen::Raw3DStructureGenerator::regardAtomConfiguration)
		.add_property("regardBondConfig", &ConfGen::Raw3DStructureGenerator::bondConfigurationRegarded, 
					  &ConfGen::Raw3DStructureGenerator::regardBondConfiguration);
}
