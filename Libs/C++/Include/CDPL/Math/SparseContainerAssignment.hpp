/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * SparseContainerAssignment.hpp 
 *
 * Copyright (C) 2010-2011 Thomas A. Seidel <thomas.seidel@univie.ac.at>
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

/**
 * \file
 * \brief Implementation of special sparse data type assignment routines.
 */

#ifndef CDPL_MATH_SPARSECONTAINERASSIGNMENT_HPP
#define CDPL_MATH_SPARSECONTAINERASSIGNMENT_HPP

#include <boost/swap.hpp>

#include "CDPL/Math/Check.hpp"
#include "CDPL/Math/CommonType.hpp"
#include "CDPL/Base/Exceptions.hpp"


namespace CDPL
{

	namespace Math
	{
	
		template <template <typename T1, typename T2> class F, typename C, typename T>
		void sparseContainerAssignScalar(C& c, const T& t)
		{
			typedef F<typename C::ValueType&, T> FunctorType;
			typedef typename C::ArrayType::iterator ArrayIter;

			FunctorType::apply(c.getDefaultValue(), t);

			for (ArrayIter it = c.getData().begin(), end = c.getData().end(); it != end; ++it)
				FunctorType::apply(it->second, t);
		}
	}
}

#endif // CDPL_MATH_SPARSECONTAINERASSIGNMENT_HPP