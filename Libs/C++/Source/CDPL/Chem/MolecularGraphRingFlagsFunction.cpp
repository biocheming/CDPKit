/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * MolecularGraphRingFlagsFunction.cpp 
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


#include "StaticInit.hpp"

#include <algorithm>
#include <functional>

#include <boost/bind.hpp>

#include "CDPL/Chem/MolecularGraphFunctions.hpp"
#include "CDPL/Chem/AtomFunctions.hpp"
#include "CDPL/Chem/BondFunctions.hpp"
#include "CDPL/Chem/Atom.hpp"
#include "CDPL/Chem/Bond.hpp"


using namespace CDPL; 


void Chem::setRingFlags(MolecularGraph& molgraph, bool overwrite)
{
	if (!overwrite && std::find_if(molgraph.getAtomsBegin(), molgraph.getAtomsEnd(),
								   boost::bind(std::equal_to<bool>(), false,
											   boost::bind(static_cast<bool (*)(const Atom&)>(&hasRingFlag), _1))) == molgraph.getAtomsEnd() &&
		std::find_if(molgraph.getBondsBegin(), molgraph.getBondsEnd(),
					 boost::bind(std::equal_to<bool>(), false,
								 boost::bind(static_cast<bool (*)(const Bond&)>(&hasRingFlag), _1))) == molgraph.getBondsEnd())
		return;

	const Fragment::SharedPointer& cyclic_substruct = perceiveCyclicSubstructure(molgraph);

	setCyclicSubstructure(molgraph, cyclic_substruct);

	std::for_each(molgraph.getAtomsBegin(), molgraph.getAtomsEnd(),
				  boost::bind(static_cast<void (*)(Atom&, bool)>(&setRingFlag), _1, 
							  boost::bind(&Fragment::containsAtom, boost::ref(*cyclic_substruct), _1)));

	std::for_each(molgraph.getBondsBegin(), molgraph.getBondsEnd(),
				  boost::bind(static_cast<void (*)(Bond&, bool)>(&setRingFlag), _1, 
							  boost::bind(&Fragment::containsBond, boost::ref(*cyclic_substruct), _1)));
}
