/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * PSDScreeningDBAccessorImpl.hpp 
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


#ifndef CDPL_PHARM_PSDSCREENINGDBACCESSORIMPL_HPP
#define CDPL_PHARM_PSDSCREENINGDBACCESSORIMPL_HPP

#include <vector>
#include <utility>

#include <boost/unordered_map.hpp>

#include "CDPL/Pharm/SQLiteDataIOBase.hpp"
#include "CDPL/Pharm/FeatureTypeHistogram.hpp"
#include "CDPL/Pharm/CDFPharmacophoreDataReader.hpp"
#include "CDPL/Chem/CDFDataReader.hpp"
#include "CDPL/Base/ControlParameterList.hpp"
#include "CDPL/Base/IntTypes.hpp"
#include "CDPL/Internal/ByteBuffer.hpp"


namespace CDPL 
{

    namespace Chem
    {

		class Molecule;
    }

    namespace Pharm
    {
	
		class PSDScreeningDBAccessorImpl : private SQLiteDataIOBase
		{

		public:
			PSDScreeningDBAccessorImpl();

			void open(const std::string& name);

			void close();

			const std::string& getDatabaseName() const;

			std::size_t getNumMolecules();

			std::size_t getNumPharmacophores();

			std::size_t getNumPharmacophores(std::size_t mol_idx);

			void getMolecule(std::size_t mol_idx, Chem::Molecule& mol);

			void getPharmacophore(std::size_t pharm_idx, Pharmacophore& pharm);

			void getPharmacophore(std::size_t mol_idx, std::size_t mol_conf_idx, Pharmacophore& pharm);

			std::size_t getMoleculeIndex(std::size_t pharm_idx);

			std::size_t getConformationIndex(std::size_t pharm_idx);

			const FeatureTypeHistogram& getFeatureCounts(std::size_t pharm_idx);

			const FeatureTypeHistogram& getFeatureCounts(std::size_t mol_idx, std::size_t mol_conf_idx); 

		private:
			void initControlParams();

			void closeDBConnection();

			void loadPharmacophore(Base::int64 mol_id, int conf_idx, Pharmacophore& pharm);

			void initMolIdxIDMappings();
			void initPharmIdxMolIDConfIdxMappings();
			void loadFeatureCounts();
	
			typedef std::vector<FeatureTypeHistogram> FeatureCountsArray;
			typedef std::pair<Base::int64, std::size_t> MolIDConfIdxPair;
			typedef std::vector<Base::int64> MolIDArray;
			typedef std::vector<MolIDConfIdxPair> MolIDConfIdxPairArray;
			typedef boost::unordered_map<Base::int64, std::size_t> MolIDToUIntMap;
			typedef boost::unordered_map<MolIDConfIdxPair, std::size_t> MolIDConfIdxToPharmIdxMap;

			SQLite3StmtPointer               selMolDataStmt;
			SQLite3StmtPointer               selPharmDataStmt;
			SQLite3StmtPointer               selMolIDStmt;
			SQLite3StmtPointer               selMolIDConfIdxStmt;
			SQLite3StmtPointer               selFtrCountsStmt;
			FeatureCountsArray               featureCounts;
			MolIDArray                       molIdxToIDMap;
			MolIDToUIntMap                   molIDToIdxMap;
			MolIDToUIntMap                   molIDConfCountMap;
			MolIDConfIdxPairArray            pharmIdxToMolIDConfIdxMap;
			MolIDConfIdxToPharmIdxMap        molIDConfIdxToPharmIdxMap;
			Internal::ByteBuffer             byteBuffer;
			CDFPharmacophoreDataReader       pharmReader;
			Chem::CDFDataReader              molReader;
			Base::ControlParameterList       controlParams;
		};
    }
}

#endif // CDPL_PHARM_PSDSCREENINGDBACCESSORIMPL_HPP
