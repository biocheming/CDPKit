/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * PSDScreeningDBAccessor.cpp 
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

#include "CDPL/Pharm/ControlParameterFunctions.hpp"

#include "CDPL/Chem/ControlParameterFunctions.hpp"

#include "PSDAccessorImplementation.hpp"
#include "SQLScreeningDBMetaData.hpp"


using namespace CDPL;


namespace
{

	const std::string MOL_DATA_QUERY_SQL = "SELECT " +
		Pharm::SQLScreeningDB::MOL_DATA_COLUMN_NAME + " FROM " +
		Pharm::SQLScreeningDB::MOL_TABLE_NAME + " WHERE " +
		Pharm::SQLScreeningDB::MOL_ID_COLUMN_NAME + " = ?1;";

	const std::string PHARM_DATA_QUERY_SQL = "SELECT " +
		Pharm::SQLScreeningDB::PHARM_DATA_COLUMN_NAME + " FROM " +
		Pharm::SQLScreeningDB::PHARM_TABLE_NAME + " WHERE " +
		Pharm::SQLScreeningDB::MOL_ID_COLUMN_NAME + " = ?1 AND " +
		Pharm::SQLScreeningDB::MOL_CONF_IDX_COLUMN_NAME + " = ?2;";

	const std::string MOL_ID_FROM_MOL_TABLE_QUERY_SQL = "SELECT " +
		Pharm::SQLScreeningDB::MOL_ID_COLUMN_NAME + " FROM " +
		Pharm::SQLScreeningDB::MOL_TABLE_NAME + ";";

	const std::string MOL_ID_CONF_IDX_FROM_PHARM_TABLE_QUERY_SQL = "SELECT " +
		Pharm::SQLScreeningDB::MOL_ID_COLUMN_NAME + ", " +
		Pharm::SQLScreeningDB::MOL_CONF_IDX_COLUMN_NAME + " FROM " +
		Pharm::SQLScreeningDB::PHARM_TABLE_NAME + ";";

	const std::string FTR_COUNT_TABLE_QUERY_SQL = "SELECT " +
		Pharm::SQLScreeningDB::MOL_ID_COLUMN_NAME + ", " +
		Pharm::SQLScreeningDB::MOL_CONF_IDX_COLUMN_NAME + ", " +
		Pharm::SQLScreeningDB::FTR_TYPE_COLUMN_NAME + ", " +
		Pharm::SQLScreeningDB::FTR_COUNT_COLUMN_NAME + " FROM " +
		Pharm::SQLScreeningDB::FTR_COUNT_TABLE_NAME + ";";
}


Pharm::PSDAccessorImplementation::PSDAccessorImplementation():
	pharmReader(controlParams), molReader(controlParams)
{
	initControlParams();
}

void Pharm::PSDAccessorImplementation::open(const std::string& name)
{
	openDBConnection(name, SQLITE_OPEN_READONLY);
}

void Pharm::PSDAccessorImplementation::close()
{
	closeDBConnection();
}

const std::string& Pharm::PSDAccessorImplementation::getDatabaseName() const
{
	return getDBName();
}

std::size_t Pharm::PSDAccessorImplementation::getNumMolecules()
{
	if (!getDBConnection())
		return 0;

	initMolIdxIDMappings();

	return molIdxToIDMap.size();
}

std::size_t Pharm::PSDAccessorImplementation::getNumPharmacophores()
{
	if (!getDBConnection())
		return 0;

	initPharmIdxMolIDConfIdxMappings();

	return pharmIdxToMolIDConfIdxMap.size();
}

void Pharm::PSDAccessorImplementation::getMolecule(std::size_t mol_idx, Chem::Molecule& mol)
{
	if (!getDBConnection())
		throw Base::IOError("PSDAccessorImplementation: no open database connection");

	initMolIdxIDMappings();

	if (mol_idx >= molIdxToIDMap.size())
		throw Base::IndexError("PSDAccessorImplementation: molecule index out of bounds");

	setupStatement(selMolDataStmt, MOL_DATA_QUERY_SQL, true);

	if (sqlite3_bind_int64(selMolDataStmt.get(), 1, molIdxToIDMap[mol_idx]) != SQLITE_OK)
		throwSQLiteIOError("PSDAccessorImplementation: error while binding molecule id to prepared statement");

	int res = sqlite3_step(selMolDataStmt.get());

	if (res != SQLITE_ROW && res != SQLITE_DONE)
		throwSQLiteIOError("PSDAccessorImplementation: error while loading requested molecule");

	if (res != SQLITE_ROW)
		throw Base::IOError("PSDAccessorImplementation: requested molecule not found");

	const void* blob = sqlite3_column_blob(selMolDataStmt.get(), 0);
	std::size_t num_bytes = sqlite3_column_bytes(selMolDataStmt.get(), 0);
	
	byteBuffer.setIOPointer(0);
	byteBuffer.putBytes(reinterpret_cast<const char*>(blob), num_bytes);

	molReader.readMolecule(mol, byteBuffer);
}

void Pharm::PSDAccessorImplementation::getPharmacophore(std::size_t pharm_idx, Pharmacophore& pharm)
{
	if (!getDBConnection())
		throw Base::IOError("PSDAccessorImplementation: no open database connection");

	initPharmIdxMolIDConfIdxMappings();

	if (pharm_idx >= pharmIdxToMolIDConfIdxMap.size())
		throw Base::IndexError("PSDAccessorImplementation: pharmacophore index out of bounds");

	loadPharmacophore(pharmIdxToMolIDConfIdxMap[pharm_idx].first, pharmIdxToMolIDConfIdxMap[pharm_idx].second, pharm);
} 

void Pharm::PSDAccessorImplementation::getPharmacophore(std::size_t mol_idx, std::size_t conf_idx, Pharmacophore& pharm)
{
	if (!getDBConnection())
		throw Base::IOError("PSDAccessorImplementation: no open database connection");

	initMolIdxIDMappings();

	if (mol_idx >= molIdxToIDMap.size())
		throw Base::IndexError("PSDAccessorImplementation: pharmacophore molecule index out of bounds");

	loadPharmacophore(molIdxToIDMap[mol_idx], conf_idx, pharm);
} 

std::size_t Pharm::PSDAccessorImplementation::getMoleculeIndex(std::size_t pharm_idx)
{
	if (!getDBConnection())
		throw Base::IOError("PSDAccessorImplementation: no open database connection");

	initPharmIdxMolIDConfIdxMappings();
	initMolIdxIDMappings();

	if (pharm_idx >= pharmIdxToMolIDConfIdxMap.size())
		throw Base::IndexError("PSDAccessorImplementation: pharmacophore index out of bounds");

	MolIDToIdxMap::const_iterator it = molIDToIdxMap.find(pharmIdxToMolIDConfIdxMap[pharm_idx].first);

	if (it == molIDToIdxMap.end())
		throw Base::IOError("PSDAccessorImplementation: requested molecule index for pharmacophore not found");

	return it->second;
}

std::size_t Pharm::PSDAccessorImplementation::getConformationIndex(std::size_t pharm_idx)
{
	if (!getDBConnection())
		throw Base::IOError("PSDAccessorImplementation: no open database connection");

	initPharmIdxMolIDConfIdxMappings();

	if (pharm_idx >= pharmIdxToMolIDConfIdxMap.size())
		throw Base::IndexError("PSDAccessorImplementation: pharmacophore index out of bounds");

	return pharmIdxToMolIDConfIdxMap[pharm_idx].second;
}

const Pharm::FeatureTypeHistogram& Pharm::PSDAccessorImplementation::getFeatureCounts(std::size_t pharm_idx)
{
	if (!getDBConnection())
		throw Base::IOError("PSDAccessorImplementation: no open database connection");

	loadFeatureCounts();

	if (pharm_idx >= featureCounts.size())
		throw Base::IndexError("PSDAccessorImplementation: pharmacophore index out of bounds");

	return featureCounts[pharm_idx];
}

void Pharm::PSDAccessorImplementation::loadPharmacophore(Base::int64 mol_id, int conf_idx, Pharmacophore& pharm)
{
	setupStatement(selPharmDataStmt, PHARM_DATA_QUERY_SQL, true);

	if (sqlite3_bind_int64(selPharmDataStmt.get(), 1, mol_id) != SQLITE_OK)
		throwSQLiteIOError("PSDAccessorImplementation: error while binding pharmacophore molecule id to prepared statement");

	if (sqlite3_bind_int(selPharmDataStmt.get(), 2, conf_idx) != SQLITE_OK)
		throwSQLiteIOError("PSDAccessorImplementation: error while binding pharmacophore molecule conformation index to prepared statement");

	int res = sqlite3_step(selPharmDataStmt.get());

	if (res != SQLITE_ROW && res != SQLITE_DONE)
		throwSQLiteIOError("PSDAccessorImplementation: error while loading requested pharmacophore");

	if (res != SQLITE_ROW)
		throw Base::IOError("PSDAccessorImplementation: requested pharmacophore not found");

	const void* blob = sqlite3_column_blob(selPharmDataStmt.get(), 0);
	std::size_t num_bytes = sqlite3_column_bytes(selPharmDataStmt.get(), 0);
	
	byteBuffer.setIOPointer(0);
	byteBuffer.putBytes(reinterpret_cast<const char*>(blob), num_bytes);

	pharmReader.readPharmacophore(pharm, byteBuffer);
} 

void Pharm::PSDAccessorImplementation::initControlParams()
{
	Pharm::setStrictErrorCheckingParameter(controlParams, true);
	Chem::setStrictErrorCheckingParameter(controlParams, true);
}

void Pharm::PSDAccessorImplementation::closeDBConnection()
{
	selMolDataStmt.reset();
	selPharmDataStmt.reset();
	selMolIDStmt.reset();
	selMolIDConfIdxStmt.reset();
	selFtrCountsStmt.reset();

	SQLiteDataIOBase::closeDBConnection();

	featureCounts.clear();
	molIdxToIDMap.clear();
	molIDToIdxMap.clear();
	pharmIdxToMolIDConfIdxMap.clear();
    molIDConfIdxToPharmIdxMap.clear();
}

void Pharm::PSDAccessorImplementation::initMolIdxIDMappings()
{
	if (!molIdxToIDMap.empty())
		return;

	setupStatement(selMolIDStmt, MOL_ID_FROM_MOL_TABLE_QUERY_SQL, false);

	int res;

	for (std::size_t i = 0; (res = sqlite3_step(selMolIDStmt.get())) == SQLITE_ROW; i++) {
		sqlite3_int64 mol_id = sqlite3_column_int64(selMolIDStmt.get(), 0);

		molIdxToIDMap.push_back(mol_id);
		molIDToIdxMap.insert(MolIDToIdxMap::value_type(mol_id, i));
	}

	if (res != SQLITE_DONE)
		throwSQLiteIOError("PSDAccessorImplementation: error while loading molecule IDs");
}

void Pharm::PSDAccessorImplementation::initPharmIdxMolIDConfIdxMappings()
{
	if (!pharmIdxToMolIDConfIdxMap.empty())
		return;

	setupStatement(selMolIDConfIdxStmt, MOL_ID_CONF_IDX_FROM_PHARM_TABLE_QUERY_SQL, false);

	int res;

	for (std::size_t i = 0; (res = sqlite3_step(selMolIDConfIdxStmt.get())) == SQLITE_ROW; i++) {
		sqlite3_int64 mol_id = sqlite3_column_int64(selMolIDConfIdxStmt.get(), 0);
		int conf_idx = sqlite3_column_int(selMolIDConfIdxStmt.get(), 1);

		MolIDConfIdxPair mol_id_conf_idx(mol_id, conf_idx);

		pharmIdxToMolIDConfIdxMap.push_back(mol_id_conf_idx);
		molIDConfIdxToPharmIdxMap.insert(MolIDConfIdxToPharmIdxMap::value_type(mol_id_conf_idx, i));
	}

	if (res != SQLITE_DONE)
		throwSQLiteIOError("PSDAccessorImplementation: error while loading pharmacophore molecule IDs and conformer indices");
}

void Pharm::PSDAccessorImplementation::loadFeatureCounts()
{
	if (!featureCounts.empty())
		return;

	initPharmIdxMolIDConfIdxMappings();
	setupStatement(selFtrCountsStmt, FTR_COUNT_TABLE_QUERY_SQL, false);

	featureCounts.resize(pharmIdxToMolIDConfIdxMap.size());
	int res;

	while ((res = sqlite3_step(selFtrCountsStmt.get())) == SQLITE_ROW) {
		sqlite3_int64 mol_id = sqlite3_column_int64(selFtrCountsStmt.get(), 0);
		int conf_idx = sqlite3_column_int(selFtrCountsStmt.get(), 1);
		int ftr_type = sqlite3_column_int(selFtrCountsStmt.get(), 2);
		int ftr_count = sqlite3_column_int(selFtrCountsStmt.get(), 3);

		MolIDConfIdxPair mol_id_conf_idx(mol_id, conf_idx);
		MolIDConfIdxToPharmIdxMap::const_iterator it = molIDConfIdxToPharmIdxMap.find(mol_id_conf_idx);

		if (it == molIDConfIdxToPharmIdxMap.end())
			throw Base::IOError("PSDAccessorImplementation: error while loading feature counts: pharmacophore index for molecule-ID/conf. index pair not found");

		std::size_t pharm_idx = it->second;

		if (pharm_idx >= featureCounts.size())
			throw Base::IndexError("PSDAccessorImplementation: error while loading feature counts: pharmacophore index out of bounds");

		featureCounts[pharm_idx].insertEntry(FeatureTypeHistogram::Entry(ftr_type, ftr_count));
	}

	if (res != SQLITE_DONE)
		throwSQLiteIOError("PSDAccessorImplementation: error while loading feature counts");
}
