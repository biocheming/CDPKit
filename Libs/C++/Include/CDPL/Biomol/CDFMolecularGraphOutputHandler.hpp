/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * CDFMolecularGraphOutputHandler.hpp 
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
 * \brief Definition of the class CDPL::Biomol::CDFMolecularGraphOutputHandler.
 */

#ifndef CDPL_BIOMOL_CDFMOLECULARGRAPHOUTPUTHANDLER_HPP
#define CDPL_BIOMOL_CDFMOLECULARGRAPHOUTPUTHANDLER_HPP

#include "CDPL/Biomol/APIPrefix.hpp"
#include "CDPL/Base/DataOutputHandler.hpp"


namespace CDPL 
{

	namespace Chem
	{

		class MolecularGraph;
	}

	namespace Biomol
	{

		/**
		 * \addtogroup CDPL_BIOMOL_CDF_IO
		 * @{
		 */

		/**
		 * \brief A handler for the output of molecular graph data in the native I/O format of the <em>CDPL</em>.
		 */
		class CDPL_BIOMOL_API CDFMolecularGraphOutputHandler : public Base::DataOutputHandler<Chem::MolecularGraph>
		{

		public:
			CDFMolecularGraphOutputHandler() {}

			const Base::DataFormat& getDataFormat() const;

			Base::DataWriter<Chem::MolecularGraph>::SharedPointer createWriter(std::ostream& os) const;
		};

		/**
		 * @}
		 */
	}
}

#endif // CDPL_BIOMOL_CDFMOLECULARGRAPHOUTPUTHANDLER_HPP
