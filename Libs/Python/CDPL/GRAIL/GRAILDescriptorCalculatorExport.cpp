/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * GRAILDescriptorCalculatorExport.cpp 
 *
 * This file is part of the Chemical Data Processing Toolkit
 *
 * Copyright (C) 2003 Thomas Seidel <thomas.seidel@univie.ac.at>
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

#include "CDPL/GRAIL/GRAILDescriptorCalculator.hpp"
#include "CDPL/Pharm/FeatureContainer.hpp"
#include "CDPL/Chem/MolecularGraph.hpp"

#include "Base/CopyAssOp.hpp"
#include "Base/ObjectIdentityCheckVisitor.hpp"

#include "ClassExports.hpp"


void CDPLPythonGRAIL::exportGRAILDescriptorCalculator()
{
    using namespace boost;
    using namespace CDPL;
  
    python::class_<GRAIL::GRAILDescriptorCalculator, GRAIL::GRAILDescriptorCalculator::SharedPointer,
				   boost::noncopyable>("GRAILDescriptorCalculator", python::no_init)
		.def(python::init<>(python::arg("self")))
		.def(python::init<const GRAIL::GRAILDescriptorCalculator&>((python::arg("self"), python::arg("calc"))))
		.def(CDPLPythonBase::ObjectIdentityCheckVisitor<GRAIL::GRAILDescriptorCalculator>())
		.def("assign", CDPLPythonBase::copyAssOp(&GRAIL::GRAILDescriptorCalculator::operator=), 
			 (python::arg("self"), python::arg("calc")), python::return_self<>())
		.def("initTargetData", &GRAIL::GRAILDescriptorCalculator::initTargetData,
			 (python::arg("self"), python::arg("tgt_env"), python::arg("coords_func"), python::arg("tgt_env_changed") = true))
		;
}