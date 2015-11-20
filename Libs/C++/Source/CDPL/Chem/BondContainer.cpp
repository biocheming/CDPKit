/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * BondContainer.cpp 
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

#include "CDPL/Chem/BondContainer.hpp"
#include "CDPL/Chem/Bond.hpp"


using namespace CDPL;


Chem::BondContainer::ConstBondIterator Chem::BondContainer::getBondsBegin() const
{
	return ConstBondIterator(*this, 0);
}

Chem::BondContainer::ConstBondIterator Chem::BondContainer::getBondsEnd() const
{
	return ConstBondIterator(*this, getNumBonds());
}

Chem::BondContainer::BondIterator Chem::BondContainer::getBondsBegin()
{
	return BondIterator(*this, 0);
}

Chem::BondContainer::BondIterator Chem::BondContainer::getBondsEnd()
{
	return BondIterator(*this, getNumBonds());
}

Chem::BondContainer& Chem::BondContainer::operator=(const BondContainer& cntnr) 
{
	return *this;
}


const Chem::Bond& Chem::BondContainer::ConstBondAccessor::operator()(std::size_t idx) const
{
	return container.get().getBond(idx);
}

bool Chem::BondContainer::ConstBondAccessor::operator==(const ConstBondAccessor& accessor) const 
{
	return (container.get_pointer() == accessor.container.get_pointer());
}

Chem::BondContainer::ConstBondAccessor& Chem::BondContainer::ConstBondAccessor::operator=(const BondAccessor& accessor) 
{
	container = boost::reference_wrapper<const BondContainer>(accessor.container);
	return *this;
}


Chem::Bond& Chem::BondContainer::BondAccessor::operator()(std::size_t idx) const
{
	return container.get().getBond(idx);
}

bool Chem::BondContainer::BondAccessor::operator==(const BondAccessor& accessor) const 
{
	return (container.get_pointer() == accessor.container.get_pointer());
}
