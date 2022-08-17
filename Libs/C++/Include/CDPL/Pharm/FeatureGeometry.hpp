/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * FeatureGeometry.hpp 
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

/**
 * \file
 * \brief Definition of constants in namespace CDPL::Pharm::FeatureGeometry.
 */

#ifndef CDPL_PHARM_FEATUREGEOMETRY_HPP
#define CDPL_PHARM_FEATUREGEOMETRY_HPP


namespace CDPL 
{

    namespace Pharm 
    {

		/**
		 * \brief Provides constants for the specification of the generic geometry of a pharmacophore feature.
		 */
		namespace FeatureGeometry 
		{
		
			const unsigned int UNDEF    = 0;

			const unsigned int SPHERE   = 1;

			const unsigned int VECTOR   = 2;

			const unsigned int PLANE    = 3;
		}
    }
}

#endif // CDPL_PHARM_FEATUREGEOMETRY_HPP
