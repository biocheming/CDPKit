/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * MolecularGraphBondDirectionsFunction.cpp 
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


#include "StaticInit.hpp"

#include <algorithm>
#include <functional>

#include <boost/bind.hpp>

#include "CDPL/Chem/MolecularGraphFunctions.hpp"
#include "CDPL/Chem/BondFunctions.hpp"
#include "CDPL/Chem/Bond.hpp"
#include "CDPL/Chem/BondDirectionCalculator.hpp"
#include "CDPL/Util/SequenceFunctions.hpp"


using namespace CDPL; 


void Chem::calcBondDirections(MolecularGraph& molgraph, bool overwrite, bool ring_bonds,
							  std::size_t min_ring_size)
{
	if (!overwrite && std::find_if(molgraph.getBondsBegin(), molgraph.getBondsEnd(),
								   boost::bind(std::equal_to<bool>(), false,
											   boost::bind(&hasDirection, _1))) == molgraph.getBondsEnd())
		return;

	BondDirectionCalculator calculator;
	Util::UIArray dirs;

	calculator.includeRingBonds(ring_bonds);
	calculator.setRingSizeLimit(min_ring_size);
	calculator.calculate(molgraph, dirs);

	Util::forEachPair(molgraph.getBondsBegin(), molgraph.getBondsEnd(), dirs.getElementsBegin(), &setDirection);
}
	
