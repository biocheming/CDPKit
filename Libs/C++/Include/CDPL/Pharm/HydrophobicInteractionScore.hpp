/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * HydrophobicInteractionScore.hpp 
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
 * \brief Definition of the class CDPL::Pharm::HydrophobicInteractionScore.
 */

#ifndef CDPL_PHARM_HYDROPHOBICINTERACTIONSCORE_HPP
#define CDPL_PHARM_HYDROPHOBICINTERACTIONSCORE_HPP

#include "CDPL/Pharm/APIPrefix.hpp"
#include "CDPL/Pharm/FeatureDistanceScore.hpp"


namespace CDPL 
{

    namespace Pharm
    {

		/**
		 * \brief HydrophobicInteractionScore.
		 */
		class CDPL_PHARM_API HydrophobicInteractionScore : public FeatureDistanceScore
		{

		  public:
			static const double DEF_MIN_DISTANCE;
			static const double DEF_MAX_DISTANCE;

			/**	
			 * \brief A reference-counted smart pointer [\ref BSHPTR] for dynamically allocated \c %HydrophobicInteractionScore instances.
			 */
			typedef boost::shared_ptr<HydrophobicInteractionScore> SharedPointer;
			
			/**
			 * \brief Constructs a \c %HydrophobicInteractionScore functor with a 
			 *        minimum hydrophobic-feature pair distance of \a min_dist and a maximum distance of \a max_dist.
			 * \param min_dist The minimum allowed feature pair distance.
			 * \param max_dist The maximum allowed feature pair distance.
			 */
			HydrophobicInteractionScore(double min_dist = DEF_MIN_DISTANCE, double max_dist = DEF_MAX_DISTANCE): 
				FeatureDistanceScore(min_dist, max_dist) {}
		};
    }
}

#endif // CDPL_PHARM_HYDROPHOBICINTERACTIONSCORE_HPP
