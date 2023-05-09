/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * TriangularMatrixTypeExport.cpp 
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

#include "CDPL/Math/MatrixAdapter.hpp"

#include "ClassExports.hpp"


namespace
{

	template <typename TriangType>
	struct TriangularityTypeExport
	{

		TriangularityTypeExport(const char* name) {
			using namespace boost;
			using namespace CDPLPythonMath;

			python::class_<TriangType>(name, python::no_init)
				.def(python::init<>(python::arg("self")))
				.def(python::init<const TriangType&>((python::arg("self"), python::arg("t"))));
		}
	};
}


void CDPLPythonMath::exportTriangularMatrixTypes()
{
	using namespace CDPL;

	TriangularityTypeExport<Math::Upper>("Upper");
	TriangularityTypeExport<Math::Lower>("Lower");
	TriangularityTypeExport<Math::UnitUpper>("UnitUpper");
	TriangularityTypeExport<Math::UnitLower>("UnitLower");
}
