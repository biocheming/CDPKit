/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * AddressOf.hpp 
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

#ifndef CDPL_INTERNAL_ADDRESSOF_HPP
#define CDPL_INTERNAL_ADDRESSOF_HPP

#include <functional>


namespace CDPL
{

	namespace Internal
	{

		/**
		 * \brief An unary functor for the conversion of object references to
		 *        corresponding object addresses.
		 * \tparam ArgType The type of the referenced objects.
		 * \tparam ResType The type of the pointed-to objects.
		 * \note <tt>ArgType*</tt> must be convertible to <tt>ResType*</tt>.
		 */
		template <typename ArgType, typename ResType = ArgType>
		class AddressOf : public std::unary_function<ArgType, ResType*>
		{

		public:
			/**
			 * \brief Returns a pointer to the object referenced by the argument.
			 * \param ref A reference to an object of type \a ArgType.
			 * \return A pointer to the argument object of type <tt>ResType*</tt>.
			 */
			ResType* operator()(ArgType& ref) const;
		};
	}
}


// Implementation

template <typename ArgType, typename ResType>
ResType* CDPL::Internal::AddressOf<ArgType, ResType>::operator()(ArgType& ref) const
{
	return &ref;
}

#endif // CDPL_INTERNAL_ADDRESSOF_HPP
