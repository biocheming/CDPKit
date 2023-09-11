/* 
 * FragmentLibraryData.cpp 
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

#ifdef _MSC_VER
# include <winbase.h>
#endif

#include "CDPL/Base/Exceptions.hpp"

#include "FragmentLibraryData.hpp"


namespace CDPL
{

    namespace ConfGen
    {

        namespace FragmentLibraryData
        {
            // clang-format off

#ifndef _MSC_VER

            const char BUILTIN_FRAG_LIB_DATA[] =
                #include "FragmentLibrary.cfl.str"
                ;

            std::pair<const char*, std::size_t> get()
            {
                return std::make_pair(BUILTIN_FRAG_LIB_DATA, sizeof(BUILTIN_FRAG_LIB_DATA) - 1);
            }
#else
            std::pair<const char*, std::size_t> getStructureData()
            {
                // NOTE: providing g_hInstance is important, NULL might not work
                HRSRC res = FindResource(g_hInstance, "FRAG_LIB_DATA", RT_RCDATA);

                if (!res)
                    throw Base::IOError(std::string("FragmentLibraryData: could not find builtin fragment library data resource record");

                HGLOBAL res_handle = LoadResource(NULL, res);

                if (!res_handle)
                    throw Base::IOError(std::string("FragmentLibraryData: could not load builtin fragment library data");

                const char* res_data = static_cast<const char*>(LockResource(res_handle));

                DWORD res_data_len = SizeofResource(NULL, res);

                return std::make_pair(res_data, res_data_len);
            }

#endif // !_MSC_VER            

            // clang-format on
   
        } // namespace FragmentLibraryData
    }     // namespace ConfGen
} // namespace CDPL
