/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * MDLDataBlockExport.cpp 
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

#include "CDPL/Chem/MDLDataBlock.hpp"

#include "Util/ArrayVisitor.hpp"

#include "ClassExports.hpp"


void CDPLPythonChem::exportMDLDataBlock()
{
	using namespace boost;
	using namespace CDPL;

	python::class_<Chem::MDLDataBlockItem>("MDLDataBlockItem", python::no_init)
		.def(python::init<>(python::arg("self")))
		.def(python::init<const Chem::MDLDataBlockItem&>((python::arg("self"), python::arg("item"))))
		.def(python::init<const std::string&, const std::string&>((python::arg("self"), python::arg("header"),
																   python::arg("data"))))
		.def("assign", &Chem::MDLDataBlockItem::operator=, (python::arg("self"), python::arg("item")),
			 python::return_self<>())
		.def("getHeader", &Chem::MDLDataBlockItem::getHeader, python::arg("self"),  
			 python::return_value_policy<python::copy_const_reference>())
		.def("setHeader", &Chem::MDLDataBlockItem::setHeader, (python::arg("self"), python::arg("header")))
		.def("getData", &Chem::MDLDataBlockItem::getData, python::arg("self"), 
			 python::return_value_policy<python::copy_const_reference>())
		.def("setData", &Chem::MDLDataBlockItem::setData, (python::arg("self"), python::arg("data")))
		.def("__eq__", &Chem::MDLDataBlockItem::operator==, (python::arg("self"), python::arg("item")))
		.def("__ne__", &Chem::MDLDataBlockItem::operator!=, (python::arg("self"), python::arg("item")))
		.add_property("header", python::make_function(&Chem::MDLDataBlockItem::getHeader, 
													  python::return_value_policy<python::copy_const_reference>()),
					  &Chem::MDLDataBlockItem::setHeader)
		.add_property("data", python::make_function(&Chem::MDLDataBlockItem::getData, 
													  python::return_value_policy<python::copy_const_reference>()),
					  &Chem::MDLDataBlockItem::setData);

	python::class_<Chem::MDLDataBlock, Chem::MDLDataBlock::SharedPointer>("MDLDataBlock", python::no_init)
		.def(python::init<>(python::arg("self")))
		.def(python::init<const Chem::MDLDataBlock&>((python::arg("self"), python::arg("data_block"))))
		.def(CDPLPythonUtil::ArrayVisitor<Chem::MDLDataBlock, 
			 python::return_internal_reference<>, python::default_call_policies,
			 python::default_call_policies, python::default_call_policies>())
		.def("__eq__", &Chem::MDLDataBlock::operator==, (python::arg("self"), python::arg("data_block")))
		.def("__ne__", &Chem::MDLDataBlock::operator!=, (python::arg("self"), python::arg("data_block")));
}
