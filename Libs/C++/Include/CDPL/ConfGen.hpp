/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * ConfGen.hpp 
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

/**
 * \file
 * \brief A convenience header including everything that is defined in namespace CDPL::ConfGen.
 */

#ifndef CDPL_CONFGEN_HPP
#define CDPL_CONFGEN_HPP

#include "CDPL/Config.hpp"

#include "CDPL/ConfGen/DGConstraintGenerator.hpp"
#include "CDPL/ConfGen/Raw3DCoordinatesGenerator.hpp"
#include "CDPL/ConfGen/FragmentList.hpp"
#include "CDPL/ConfGen/FragmentLibraryEntry.hpp"
#include "CDPL/ConfGen/FragmentLibrary.hpp"
#include "CDPL/ConfGen/TorsionRule.hpp"
#include "CDPL/ConfGen/TorsionCategory.hpp"
#include "CDPL/ConfGen/TorsionLibrary.hpp"
#include "CDPL/ConfGen/TorsionRuleMatch.hpp"
#include "CDPL/ConfGen/TorsionRuleMatcher.hpp"
#include "CDPL/ConfGen/UtilityFunctions.hpp"
#include "CDPL/ConfGen/FragmentType.hpp"
#include "CDPL/ConfGen/ForceFieldType.hpp"

#if defined(HAVE_BOOST_TIMER) && defined(HAVE_BOOST_CHRONO)

#include "CDPL/ConfGen/RandomConformerGenerator.hpp"
#include "CDPL/ConfGen/SystematiconformerGenerator.hpp"
#include "CDPL/ConfGen/FragmentConformerGenerator.hpp"
#include "CDPL/ConfGen/FragmentLibraryGenerator.hpp"

#endif // defined(HAVE_BOOST_TIMER) && defined(HAVE_BOOST_CHRONO)
#endif // CDPL_CONFGEN_HPP