/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * FeatureContainerFunctionExport.cpp 
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

#include "CDPL/Pharm/FeatureContainerFunctions.hpp"
#include "CDPL/Pharm/FeatureContainer.hpp"
#include "CDPL/Pharm/FeatureTypeHistogram.hpp"
#include "CDPL/Chem/Fragment.hpp"

#include "FunctionExports.hpp"
#include "FunctionWrapper.hpp"


#define MAKE_FTRCONTAINER_FUNC_WRAPPERS(TYPE, FUNC_SUFFIX)          \
TYPE get##FUNC_SUFFIX##Wrapper(CDPL::Pharm::FeatureContainer& cntnr)\
{                                                                   \
	return get##FUNC_SUFFIX(cntnr);                                 \
}                                                                   \
                                                                    \
bool has##FUNC_SUFFIX##Wrapper(CDPL::Pharm::FeatureContainer& cntnr)\
{                                                                   \
	return has##FUNC_SUFFIX(cntnr);                                 \
}

#define EXPORT_FTRCONTAINER_FUNCS_COPY_REF(FUNC_SUFFIX, ARG_NAME)                                             \
python::def("get"#FUNC_SUFFIX, &get##FUNC_SUFFIX##Wrapper, python::arg("cntnr"),                              \
            python::return_value_policy<python::copy_const_reference>());                                     \
python::def("has"#FUNC_SUFFIX, &has##FUNC_SUFFIX##Wrapper, python::arg("cntnr"));                             \
python::def("clear"#FUNC_SUFFIX, &Pharm::clear##FUNC_SUFFIX, python::arg("cntnr"));                           \
python::def("set"#FUNC_SUFFIX, &Pharm::set##FUNC_SUFFIX, (python::arg("cntnr"), python::arg(#ARG_NAME))); 


namespace
{

	MAKE_FTRCONTAINER_FUNC_WRAPPERS(const std::string&, Name)
	MAKE_FUNCTION_WRAPPER5(bool, checkExclusionVolumeClash, const CDPL::Pharm::FeatureContainer&, CDPL::Chem::AtomContainer&,
						   const CDPL::Chem::Atom3DCoordinatesFunction&, const CDPL::Math::Matrix4D&, bool);
}


void CDPLPythonPharm::exportFeatureContainerFunctions()
{
    using namespace boost;
    using namespace CDPL;
	
	python::def("getFeatureCount", static_cast<std::size_t (*)(const Pharm::FeatureContainer&)>(&Pharm::getFeatureCount), 
				python::arg("cntnr"));
	python::def("getFeatureCount", static_cast<std::size_t (*)(const Pharm::FeatureContainer&, unsigned int)>(&Pharm::getFeatureCount), 
				(python::arg("cntnr"), python::arg("type")));
	python::def("buildFeatureTypeHistogram", &Pharm::buildFeatureTypeHistogram, 
				(python::arg("cntnr"), python::arg("hist")));
	python::def("checkExclusionVolumeClash", &checkExclusionVolumeClashWrapper5, 
				(python::arg("ftr_cntnr"), python::arg("atom_cntnr"), python::arg("coords_func"), 
				 python::arg("xform"), python::arg("vdw") = true));
	python::def("getFeatureAtoms", &Pharm::getFeatureAtoms, (python::arg("cntnr"), python::arg("atoms")));

	EXPORT_FTRCONTAINER_FUNCS_COPY_REF(Name, name)
}