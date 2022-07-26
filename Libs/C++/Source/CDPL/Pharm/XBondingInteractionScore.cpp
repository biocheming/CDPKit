/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * XBondingInteractionConstraint.cpp 
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

 
#include "StaticInit.hpp"

#include <cmath>

#include <boost/bind.hpp>

#include "CDPL/Pharm/XBondingInteractionScore.hpp"
#include "CDPL/Pharm/Feature.hpp"
#include "CDPL/Pharm/FeatureFunctions.hpp"
#include "CDPL/Pharm/FeatureGeometry.hpp"
#include "CDPL/Math/SpecialFunctions.hpp"
#include "CDPL/Chem/Entity3DFunctions.hpp"


using namespace CDPL;


namespace
{

	const double DEF_LP_TO_AXIS_ANGLE = 65.0;
}


const double Pharm::XBondingInteractionScore::DEF_MIN_AX_DISTANCE = 1.6;
const double Pharm::XBondingInteractionScore::DEF_MAX_AX_DISTANCE = 3.75;
const double Pharm::XBondingInteractionScore::DEF_MIN_AXB_ANGLE = 140.0;
const double Pharm::XBondingInteractionScore::DEF_ACC_ANGLE_TOLERANCE = 45.0;


Pharm::XBondingInteractionScore::XBondingInteractionScore(bool don_acc, double min_ax_dist, double max_ax_dist,
														  double min_axb_ang, double acc_ang_tol): 
	donAccOrder(don_acc), minAXDist(min_ax_dist), maxAXDist(max_ax_dist), minAXBAngle(min_axb_ang),
	accAngleTol(acc_ang_tol), normFunc(boost::bind(&Math::generalizedBell<double>, _1, 0.5, 10, 0.0)) {}

double Pharm::XBondingInteractionScore::getMinAXDistance() const
{
	return minAXDist;
}

double Pharm::XBondingInteractionScore::getMaxAXDistance() const
{
	return maxAXDist;
}

double Pharm::XBondingInteractionScore::getMinAXBAngle() const
{
	return minAXBAngle;
}

double Pharm::XBondingInteractionScore::getAcceptorAngleTolerance() const
{
	return accAngleTol;
}

void Pharm::XBondingInteractionScore::setNormalizationFunction(const NormalizationFunction& func)
{
    normFunc = func;
}

double Pharm::XBondingInteractionScore::operator()(const Feature& ftr1, const Feature& ftr2) const
{
	const Feature& don_ftr = (donAccOrder ? ftr1 : ftr2);
	const Feature& acc_ftr = (donAccOrder ? ftr2 : ftr1);

	const Math::Vector3D& don_pos = get3DCoordinates(don_ftr);
	const Math::Vector3D& acc_pos = get3DCoordinates(acc_ftr);

	Math::Vector3D x_acc_vec(acc_pos - don_pos);
	double ax_dist = length(x_acc_vec);

	double score = normFunc((ax_dist - (maxAXDist + minAXDist) * 0.5) / (maxAXDist - minAXDist));
	
	if (hasOrientation(don_ftr)) {
		double axb_ang = std::acos(angleCos(x_acc_vec, getOrientation(don_ftr), ax_dist)) * 180.0 / M_PI;
		
		score *= normFunc(axb_ang * 0.5 / (180.0 - minAXBAngle));
	}
	
	if (hasOrientation(acc_ftr)) {
		const Math::Vector3D& acc_orient = getOrientation(acc_ftr);
		double acc_ang_dev = std::acos(angleCos(x_acc_vec, acc_orient, ax_dist)) * 180.0 / M_PI;
			
		if (getGeometry(acc_ftr) != FeatureGeometry::VECTOR) 
			acc_ang_dev = std::abs(acc_ang_dev - DEF_LP_TO_AXIS_ANGLE);

		score *= normFunc(acc_ang_dev * 0.5 / accAngleTol);
	}

	return score * getWeight(ftr2);
}

double Pharm::XBondingInteractionScore::operator()(const Math::Vector3D& ftr1_pos, const Feature& ftr2) const
{
	const Math::Vector3D& ftr2_pos = get3DCoordinates(ftr2);
	Math::Vector3D x_acc_vec(ftr2_pos - ftr1_pos);
	double ax_dist = length(x_acc_vec);

	double score = normFunc((ax_dist - (maxAXDist + minAXDist) * 0.5) / (maxAXDist - minAXDist));

	if (donAccOrder) { 
		if (hasOrientation(ftr2)) {
			const Math::Vector3D& acc_orient = getOrientation(ftr2);
			double acc_ang_dev = std::acos(angleCos(x_acc_vec, acc_orient, ax_dist)) * 180.0 / M_PI;
			
			if (getGeometry(ftr2) != FeatureGeometry::VECTOR) 
				acc_ang_dev = std::abs(acc_ang_dev - DEF_LP_TO_AXIS_ANGLE);

			score *= normFunc(acc_ang_dev * 0.5 / accAngleTol);
		}

	} else if (hasOrientation(ftr2)) {
		double axb_ang = 180.0 - std::acos(angleCos(x_acc_vec, getOrientation(ftr2), ax_dist)) * 180.0 / M_PI;
		
		score *= normFunc(axb_ang * 0.5 / (180.0 - minAXBAngle));
	}
	
	return score * getWeight(ftr2);
}