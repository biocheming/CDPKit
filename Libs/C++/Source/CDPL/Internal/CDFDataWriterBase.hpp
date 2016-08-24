/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * CDFDataWriterBase.hpp 
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


#ifndef CDPL_INTERNAL_CDFDATAWRITERBASE_HPP
#define CDPL_INTERNAL_CDFDATAWRITERBASE_HPP

#include <cstddef>
#include <iosfwd>
#include <string>

#include <boost/static_assert.hpp>

#include "CDPL/Internal/CDFFormatData.hpp"
#include "CDPL/Internal/ByteBuffer.hpp"


namespace CDPL 
{

	namespace Internal
	{

		class CDFDataWriterBase
		{

		public:
			CDFDataWriterBase(): strictErrorChecks(true) {}

			virtual ~CDFDataWriterBase() {}

			bool writeHeader(std::ostream& os, const CDF::Header& header);

			template <typename T>
			void putIntProperty(unsigned int prop_id, const T& value, ByteBuffer& bbuf, bool compress = true) const;

			template <typename T>
			void putFloatProperty(unsigned int prop_id, const T& value, ByteBuffer& bbuf) const;

			void putStringProperty(unsigned int prop_id, const std::string& str, ByteBuffer& bbuf) const;

            template <typename Vec>
			void putVectorProperty(unsigned int prop_id, const Vec& vec, ByteBuffer& bbuf) const;

			bool strictErrorChecking() const;

			void strictErrorChecking(bool strict);

		private:
            CDF::PropertySpec composePropertySpec(unsigned int prop_id, std::size_t length) const;

			bool       strictErrorChecks;
			ByteBuffer hdrBuffer;
		};
	}
}


// Implementation

template <typename T>
void CDPL::Internal::CDFDataWriterBase::putIntProperty(unsigned int prop_id, const T& value, 
													   ByteBuffer& bbuf, bool compress) const
{
    BOOST_STATIC_ASSERT_MSG((sizeof(T) - 1) < (1 << CDF::NUM_PROP_VALUE_LENGTH_BITS), 
							"CDFDataWriterBase: maximum size of primitive IO data type exceeded");

	std::size_t last_pos = bbuf.getIOPointer();

	bbuf.setIOPointer(last_pos + 1);

	std::size_t num_bytes = bbuf.putInt(value, compress);

	bbuf.setIOPointer(last_pos);
	bbuf.putInt(composePropertySpec(prop_id, num_bytes), false);
	bbuf.setIOPointer(last_pos + 1 + num_bytes);
}

template <typename T>
void CDPL::Internal::CDFDataWriterBase::putFloatProperty(unsigned int prop_id, const T& value, ByteBuffer& bbuf) const
{
    BOOST_STATIC_ASSERT_MSG((sizeof(T) - 1) < (1 << CDF::NUM_PROP_VALUE_LENGTH_BITS), 
							"CDFDataWriterBase: maximum size of primitive IO data type exceeded");

	bbuf.putInt(composePropertySpec(prop_id, sizeof(T)), false);
	bbuf.putFloat(value);
}

template <typename Vec>
void CDPL::Internal::CDFDataWriterBase::putVectorProperty(unsigned int prop_id, const Vec& vec, ByteBuffer& bbuf) const
{
    typedef typename Vec::ValueType T;

    BOOST_STATIC_ASSERT_MSG((sizeof(T) - 1) < (1 << CDF::NUM_PROP_VALUE_LENGTH_BITS), 
							"CDFDataWriterBase: maximum size of primitive IO data type exceeded");

	bbuf.putInt(composePropertySpec(prop_id, sizeof(T)), false);

	for (std::size_t i = 0; i < vec.getSize(); i++)
		bbuf.putFloat(vec[i]);
}

#endif // CDPL_INTERNAL_CDFDATAWRITERBASE_HPP