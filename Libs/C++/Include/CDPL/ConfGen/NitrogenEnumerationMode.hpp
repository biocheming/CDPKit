/* 
 * NitrogenEnumerationMode.hpp 
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
 * \brief Definition of constants in namespace CDPL::Confgen::NitrogenEnumerationMode.
 */

#ifndef CDPL_CONFGEN_NITROGENENUMERATIONMODE_HPP
#define CDPL_CONFGEN_NITROGENENUMERATIONMODE_HPP


namespace CDPL
{

    namespace ConfGen
    {

        /**
         * \brief Provides constants that are used to specify the mode of invertible nitrogen enumeration.
         */
        namespace NitrogenEnumerationMode
        {

            const int NONE = 0;

            const int ALL = 1;

            const int UNSPECIFIED_STEREO = 2;
        } // namespace NitrogenEnumerationMode
    } // namespace ConfGen
} // namespace CDPL

#endif // CDPL_CONFGEN_NITROGENENUMERATIONMODE_HPP
