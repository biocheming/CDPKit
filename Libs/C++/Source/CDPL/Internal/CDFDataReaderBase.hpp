/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * CDFDataReaderBase.hpp 
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


#ifndef CDPL_INTERNAL_CDFDATAREADERBASE_HPP
#define CDPL_INTERNAL_CDFDATAREADERBASE_HPP

#include <iosfwd>
#include <cstddef>
#include <cstdint>
#include <string>

#include "CDPL/Math/VectorArray.hpp"
#include "CDPL/Base/Exceptions.hpp"

#include "CDPL/Internal/CDFFormatData.hpp"
#include "CDPL/Internal/ByteBuffer.hpp"


namespace CDPL 
{
 
    namespace Internal
    {

		class CDFDataReaderBase
		{

		public:
			CDFDataReaderBase(): strictErrorChecks(true)	{}

			virtual ~CDFDataReaderBase() {}

			bool skipToRecord(std::istream& is, CDF::Header& header, std::uint8_t rec_type, bool seek_beg, ByteBuffer& bbuf) const;

			bool skipNextRecord(std::istream& is, std::uint8_t rec_type, ByteBuffer& bbuf) const;

			bool readHeader(std::istream& is, CDF::Header& header, ByteBuffer& bbuf) const;

			void readData(std::istream& is,	std::size_t length, ByteBuffer& bbuf) const;

			unsigned int extractPropertyID(CDF::PropertySpec prop_spec) const;

			std::size_t extractPropertyValueLength(CDF::PropertySpec prop_spec) const;

			bool getHeader(CDF::Header& header, ByteBuffer& bbuf) const;

			template <typename T>
			void getIntProperty(CDF::PropertySpec prop_spec, T& value, ByteBuffer& bbuf) const;

			template <typename T>
			void getFloatProperty(CDF::PropertySpec prop_spec, T& value, ByteBuffer& bbuf) const;

			template <typename Array>
			void getFloatArrayProperty(CDF::PropertySpec prop_spec, Array& array, ByteBuffer& bbuf) const;

			void getStringProperty(CDF::PropertySpec prop_spec, std::string& str, ByteBuffer& bbuf) const;

			template <typename Vec, typename ValueType = typename Vec::ValueType>
			void getVectorProperty(CDF::PropertySpec prop_spec, Vec& vec, ByteBuffer& bbuf) const;

			template <typename Vec>
			void getCVectorProperty(CDF::PropertySpec prop_spec, Vec& vec, ByteBuffer& bbuf) const;

			template <typename Vec>
			void getCVectorArrayProperty(CDF::PropertySpec prop_spec, Math::VectorArray<Vec>& vec_array, ByteBuffer& bbuf) const;

			template <typename Mtx>
			void getCMatrix(Mtx& mtx, ByteBuffer& bbuf) const;

			template <typename Mtx>
			void getCMatrix(Mtx& mtx, ByteBuffer& bbuf, std::size_t fp_len) const;

			template <typename Grid>
			void getGrid(Grid& grid, ByteBuffer& bbuf) const;

			template <typename Grid>
			void getGrid(Grid& grid, ByteBuffer& bbuf, std::size_t fp_len) const;

			void getString(std::string& str, ByteBuffer& bbuf) const;

			unsigned int getPropertySpec(CDF::PropertySpec& prop_spec, ByteBuffer& bbuf) const;

			bool strictErrorChecking() const;

			void strictErrorChecking(bool strict);
			
		private:
			bool       strictErrorChecks;
		};
    }
}


// Implementation

inline unsigned int CDPL::Internal::CDFDataReaderBase::extractPropertyID(CDF::PropertySpec prop_spec) const
{
	return (prop_spec >> CDF::NUM_PROP_VALUE_LENGTH_BITS);
}

inline std::size_t CDPL::Internal::CDFDataReaderBase::extractPropertyValueLength(CDF::PropertySpec prop_spec) const
{
	return ((prop_spec & CDF::PROP_VALUE_LENGTH_MASK) + 1);
}

template <typename T>
void CDPL::Internal::CDFDataReaderBase::getIntProperty(CDF::PropertySpec prop_spec, T& value, ByteBuffer& bbuf) const
{
	std::size_t len = extractPropertyValueLength(prop_spec);

	if (len > sizeof(T))
		throw Base::IOError("CDFDataReaderBase: integer property read error, output type size exceeded");

	bbuf.getInt(value, len);
}

template <typename T>
void CDPL::Internal::CDFDataReaderBase::getFloatProperty(CDF::PropertySpec prop_spec, T& value, ByteBuffer& bbuf) const
{
	std::size_t len = extractPropertyValueLength(prop_spec);

	if (len != sizeof(T)) {
		if (len == sizeof(float)) {
			float tmp;

			bbuf.getFloat(tmp);

			value = tmp;
			return;
		}

		throw Base::IOError("CDFDataReaderBase: float property read error, output type size mismatch");
	}

	bbuf.getFloat(value);
}

template <typename Array>
void CDPL::Internal::CDFDataReaderBase::getFloatArrayProperty(CDF::PropertySpec prop_spec, Array& array, ByteBuffer& bbuf) const
{
	try {
		getVectorProperty<Array, typename Array::ElementType>(prop_spec, array, bbuf);

	} catch (const Base::IOError&) {
		throw Base::IOError("CDFDataReaderBase: float array property read error, output type size mismatch");
	}
}

template <typename Vec, typename ValueType>
void CDPL::Internal::CDFDataReaderBase::getVectorProperty(CDF::PropertySpec prop_spec, Vec& vec, ByteBuffer& bbuf) const
{
	std::size_t len = extractPropertyValueLength(prop_spec);
	CDF::SizeType vec_size;

	bbuf.getInt(vec_size);
	vec.resize(vec_size);

	if (len != sizeof(ValueType)) {
		if (len == sizeof(float)) {
			float tmp;

			for (CDF::SizeType i = 0; i < vec_size; i++) {
				bbuf.getFloat(tmp);
				vec[i] = tmp;
			}

			return;
		}

		throw Base::IOError("CDFDataReaderBase: float vector property read error, output type size mismatch");
	}

	for (CDF::SizeType i = 0; i < vec_size; i++)
		bbuf.getFloat(vec[i]);
}

template <typename Vec>
void CDPL::Internal::CDFDataReaderBase::getCVectorProperty(CDF::PropertySpec prop_spec, Vec& vec, ByteBuffer& bbuf) const
{
	std::size_t len = extractPropertyValueLength(prop_spec);

	if (len != sizeof(typename Vec::ValueType)) {
		if (len == sizeof(float)) {
			float tmp;

			for (std::size_t i = 0; i < Vec::Size; i++) {
				bbuf.getFloat(tmp);
				vec[i] = tmp;
			}

			return;
		}

		throw Base::IOError("CDFDataReaderBase: float vector property read error, output type size mismatch");
	}

	for (std::size_t i = 0; i < Vec::Size; i++)
		bbuf.getFloat(vec[i]);
}

template <typename Vec>
void CDPL::Internal::CDFDataReaderBase::getCVectorArrayProperty(CDF::PropertySpec prop_spec, Math::VectorArray<Vec>& vec_array, ByteBuffer& bbuf) const
{
	std::size_t len = extractPropertyValueLength(prop_spec);
	CDF::SizeType arr_size;

	bbuf.getInt(arr_size);
	vec_array.resize(arr_size);

	if (len != sizeof(typename Vec::ValueType)) {
		if (len == sizeof(float)) {
			float tmp;

			for (CDF::SizeType i = 0; i < arr_size; i++) {
				for (std::size_t j = 0; j < Vec::Size; j++) {
					bbuf.getFloat(tmp);
					vec_array[i][j] = tmp;
				}
			}

			return;
		}

		throw Base::IOError("CDFDataReaderBase: vector array property read error, vector element type size mismatch");
	}

	for (CDF::SizeType i = 0; i < arr_size; i++)
		for (std::size_t j = 0; j < Vec::Size; j++)
			bbuf.getFloat(vec_array[i][j]);
}

template <typename Mtx>
void CDPL::Internal::CDFDataReaderBase::getCMatrix(Mtx& mtx, ByteBuffer& bbuf) const
{
	std::uint8_t len;
	bbuf.getInt(len);

	getCMatrix(mtx, bbuf, len);
}

template <typename Mtx>
void CDPL::Internal::CDFDataReaderBase::getCMatrix(Mtx& mtx, ByteBuffer& bbuf, std::size_t fp_len) const
{
	if (fp_len != sizeof(typename Mtx::ValueType)) {
		if (fp_len == sizeof(float)) {
			float tmp;

			for (std::size_t i = 0; i < Mtx::Size1; i++)
				for (std::size_t j = 0; j < Mtx::Size2; j++) {
					bbuf.getFloat(tmp);
					mtx(i, j) = tmp;
				}

			return;
		}

		throw Base::IOError("CDFDataReaderBase: matrix read error, matrix element type size mismatch");
	}

	for (std::size_t i = 0; i < Mtx::Size1; i++)
		for (std::size_t j = 0; j < Mtx::Size2; j++)
			bbuf.getFloat(mtx(i, j));
}

template <typename Grid>
void CDPL::Internal::CDFDataReaderBase::getGrid(Grid& grid, ByteBuffer& bbuf) const
{
	std::uint8_t len;
	bbuf.getInt(len);

	getGrid(grid, bbuf, len);
}

template <typename Grid>
void CDPL::Internal::CDFDataReaderBase::getGrid(Grid& grid, ByteBuffer& bbuf, std::size_t fp_len) const
{
	CDF::SizeType size1;
	CDF::SizeType size2;
	CDF::SizeType size3;

	bbuf.getInt(size1);
	bbuf.getInt(size2);
	bbuf.getInt(size3);

	grid.resize(size1, size2, size3, false);

	if (fp_len != sizeof(typename Grid::ValueType)) {
		if (fp_len == sizeof(float)) {
			float tmp;

			for (CDF::SizeType i = 0; i < size1; i++)
				for (CDF::SizeType j = 0; j < size2; j++)
					for (CDF::SizeType k = 0; k < size3; k++) {
						bbuf.getFloat(tmp);
						grid(i, j, k) = tmp;
					}

			return;
		}

		throw Base::IOError("CDFDataReaderBase: grid read error, grid element type size mismatch");
	}

	for (CDF::SizeType i = 0; i < size1; i++)
		for (CDF::SizeType j = 0; j < size2; j++)
			for (CDF::SizeType k = 0; k < size3; k++) 
				bbuf.getFloat(grid(i, j, k));
}

#endif // CDPL_INTERNAL_CDFDATAREADERBASE_HPP
