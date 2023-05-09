/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * FeatureInteractionScoreCombinerExport.cpp 
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


#include <boost/python.hpp>

#include "CDPL/Pharm/FeatureInteractionScoreCombiner.hpp"

#include "Base/CopyAssOp.hpp"

#include "ClassExports.hpp"


void CDPLPythonPharm::exportFeatureInteractionScoreCombiner()
{
    using namespace boost;
    using namespace CDPL;

    python::class_<Pharm::FeatureInteractionScoreCombiner, Pharm::FeatureInteractionScoreCombiner::SharedPointer,
				   python::bases<Pharm::FeatureInteractionScore>, boost::noncopyable>("FeatureInteractionScoreCombiner", python::no_init)
		.def(python::init<const Pharm::FeatureInteractionScoreCombiner&>(
				 (python::arg("self"), python::arg("comb"))))
		.def(python::init<const Pharm::FeatureInteractionScoreCombiner::InteractionScore&, 
			 const Pharm::FeatureInteractionScoreCombiner::InteractionScore&, const Pharm::FeatureInteractionScoreCombiner::CombinationFunction&>(
				 (python::arg("self"), python::arg("score1"), python::arg("score2"), python::arg("comb_func"))))
		.def(python::init<const Pharm::FeatureInteractionScoreCombiner::InteractionScore&, const Pharm::FeatureInteractionScoreCombiner::InteractionScore&>(
				 (python::arg("self"), python::arg("score1"), python::arg("score2"))))
		.def("assign", CDPLPythonBase::copyAssOp(&Pharm::FeatureInteractionScoreCombiner::operator=), 
			 (python::arg("self"), python::arg("con")), python::return_self<>());
}
