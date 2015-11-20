/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * MolecularGraphSSSRFunctions.cpp 
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

#include "CDPL/Chem/MolecularGraphFunctions.hpp"
#include "CDPL/Chem/Atom.hpp"
#include "CDPL/Chem/Bond.hpp"
#include "CDPL/Chem/MolecularGraphProperty.hpp"
#include "CDPL/Chem/SmallestSetOfSmallestRings.hpp"


using namespace CDPL; 


const Chem::FragmentList::SharedPointer& Chem::getSSSR(const MolecularGraph& molgraph)
{
   return molgraph.getProperty<FragmentList::SharedPointer>(MolecularGraphProperty::SSSR);
}

void Chem::setSSSR(MolecularGraph& molgraph, const FragmentList::SharedPointer& sssr)
{
	molgraph.setProperty(MolecularGraphProperty::SSSR, sssr);
}

void Chem::clearSSSR(MolecularGraph& molgraph)
{
	molgraph.removeProperty(MolecularGraphProperty::SSSR);
}

bool Chem::hasSSSR(const MolecularGraph& molgraph)
{
	return molgraph.isPropertySet(MolecularGraphProperty::SSSR);
}

Chem::FragmentList::SharedPointer Chem::perceiveSSSR(const MolecularGraph& molgraph)
{
	FragmentList::SharedPointer sssr_ptr(new SmallestSetOfSmallestRings(molgraph));

	return sssr_ptr;
}

Chem::FragmentList::SharedPointer Chem::perceiveSSSR(MolecularGraph& molgraph, bool overwrite)
{
	if (!overwrite) {
		Base::Variant prev_sssr = molgraph.getProperty(MolecularGraphProperty::SSSR, false);
	
		if (!prev_sssr.isEmpty())
			return prev_sssr.getData<FragmentList::SharedPointer>();
	}

	FragmentList::SharedPointer sssr_ptr(new SmallestSetOfSmallestRings(molgraph));

	molgraph.setProperty(MolecularGraphProperty::SSSR, sssr_ptr);

	return sssr_ptr;
}
