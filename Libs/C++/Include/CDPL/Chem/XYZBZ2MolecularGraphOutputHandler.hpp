/* 
 * XYZBZ2MolecularGraphOutputHandler.hpp 
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

/**
 * \file
 * \brief Definition of the class CDPL::Chem::XYZBZ2MolecularGraphOutputHandler.
 */

#ifndef CDPL_CHEM_XYZBZ2MOLECULARGRAPHOUTPUTHANDLER_HPP
#define CDPL_CHEM_XYZBZ2MOLECULARGRAPHOUTPUTHANDLER_HPP

#include "CDPL/Chem/DataFormat.hpp"
#include "CDPL/Chem/XYZBZ2MolecularGraphWriter.hpp"
#include "CDPL/Util/DefaultDataOutputHandler.hpp"


namespace CDPL
{

    namespace Chem
    {

        /**
         * \brief A handler for the output of bzip2-compressed molecular graph data in the <em>XYZ</em> format.
         */
        typedef Util::DefaultDataOutputHandler<XYZBZ2MolecularGraphWriter, DataFormat::XYZ_BZ2> XYZBZ2MolecularGraphOutputHandler;
    } // namespace Chem
} // namespace CDPL

#endif // CDPL_CHEM_XYZBZ2MOLECULARGRAPHOUTPUTHANDLER_HPP
