/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * CDFFormatData.hpp
 *
 * This file is part of the Chemical Data Processing Toolkit
 *
 * Copyright (C) 2003-2020 Thomas A. Seidel <thomas.seidel@univie.ac.at>
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


#ifndef CDPL_GRAILS_CDFFORMATDATA_HPP
#define CDPL_GRAILS_CDFFORMATDATA_HPP

#include "CDPL/Base/IntegerTypes.hpp"
#include "CDPL/Internal/CDFFormatData.hpp"


namespace CDPL
{

    namespace GRAILS
    {

		namespace CDF
		{
			
			using namespace Internal::CDF;

			typedef Base::uint32 UIntType;

			const Base::uint8 INTERACTION_SCORE_GRID_RECORD_ID     = 4;
			const Base::uint8 INTERACTION_SCORE_GRID_SET_RECORD_ID = 5;

			const Base::uint8 CURR_FORMAT_VERSION  = 1;

			namespace AttributedGridProperty
			{

				const unsigned int PROPERTY_HANDLER_ID = 1;

				const unsigned int FEATURE_TYPE        = 1;
				const unsigned int TARGET_FEATURE_TYPE = 2;
			}
		}
    }
}

#endif // CDPL_GRAILS_CDFFORMATDATA_HPP
