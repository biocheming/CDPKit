/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * ImplicitConverterRegistration.hpp 
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


#ifndef CDPL_PYTHON_MATH_IMPLICITCONVERTERREGISTRATION_HPP
#define CDPL_PYTHON_MATH_IMPLICITCONVERTERREGISTRATION_HPP

#include <boost/python.hpp>
#include <boost/mpl/bool.hpp>
#include <boost/type_traits/is_same.hpp>


namespace CDPLPythonMath
{

    template <typename TargetType, typename SourceTypeList, typename Empty> 
    struct ImplicitConverterRegistrationHelper
    {

		static void apply() {
			using namespace boost;

			typedef typename mpl::front<SourceTypeList>::type SourceType;
			typedef typename mpl::pop_front<SourceTypeList>::type NewSourceTypeList;
			typedef typename mpl::empty<NewSourceTypeList>::type IsEmpty;

			if (!boost::is_same<SourceType, TargetType>::value)
				python::implicitly_convertible<SourceType, TargetType>();

			ImplicitConverterRegistrationHelper<TargetType, NewSourceTypeList, IsEmpty>::apply();
		}
    };

    template <typename TargetType, typename SourceTypeList> 
    struct ImplicitConverterRegistrationHelper<TargetType, SourceTypeList, boost::mpl::true_>
    {

		static void apply() {}
    };

    template <typename TargetType, typename SourceTypeList> 
    struct ImplicitConverterRegistration
    {

		ImplicitConverterRegistration() {
			typedef typename boost::mpl::empty<SourceTypeList>::type IsEmpty;

			ImplicitConverterRegistrationHelper<TargetType, SourceTypeList, IsEmpty>::apply();
		}
    };
}

#endif // CDPL_PYTHON_MATH_IMPLICITCONVERTERREGISTRATION_HPP
