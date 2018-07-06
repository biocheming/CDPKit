/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * MMFF94VanDerWaalsParameterTable.cpp 
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

#include <cstring>
#include <sstream>

#include "CDPL/Config.hpp"

#include <boost/bind.hpp>

#if defined(HAVE_BOOST_IOSTREAMS)

#include <boost/iostreams/device/array.hpp>
#include <boost/iostreams/stream.hpp>

#endif // defined(HAVE_BOOST_IOSTREAMS)

#include "CDPL/Forcefield/MMFF94VanDerWaalsParameterTable.hpp"
#include "CDPL/Base/Exceptions.hpp"

#include "MMFF94ParameterData.hpp"
#include "Utilities.hpp"


using namespace CDPL; 


namespace
{
 
    Forcefield::MMFF94VanDerWaalsParameterTable::SharedPointer builtinTable(new Forcefield::MMFF94VanDerWaalsParameterTable());

    struct Init
    {

		Init() {
			builtinTable->loadDefaults();
		}

    } init;

	const Forcefield::MMFF94VanDerWaalsParameterTable::Entry NOT_FOUND;
}


Forcefield::MMFF94VanDerWaalsParameterTable::SharedPointer Forcefield::MMFF94VanDerWaalsParameterTable::defaultTable = builtinTable;


Forcefield::MMFF94VanDerWaalsParameterTable::Entry::Entry():
	atomType(0), polarizability(0), effElNumber(0), factA(0), factG(0), 
	donAccType(HDonorAcceptorType::NONE), initialized(false)
{}

Forcefield::MMFF94VanDerWaalsParameterTable::Entry::Entry(unsigned int atom_type, double atom_pol, double eff_el_num, 
														  double fact_a, double fact_g, HDonorAcceptorType don_acc_type):
	atomType(atom_type), polarizability(atom_pol), effElNumber(eff_el_num), factA(fact_a), 
	factG(fact_g), donAccType(HDonorAcceptorType::NONE), initialized(true)
{}

unsigned int Forcefield::MMFF94VanDerWaalsParameterTable::Entry::getAtomType() const
{
	return atomType;
}

double Forcefield::MMFF94VanDerWaalsParameterTable::Entry::getAtomicPolarizability() const
{
	return polarizability;
}
			
double Forcefield::MMFF94VanDerWaalsParameterTable::Entry::getEffectiveElectronNumber() const
{
	return effElNumber;
}
			
double Forcefield::MMFF94VanDerWaalsParameterTable::Entry::getFactorA() const
{
	return factA;
}
  		
double Forcefield::MMFF94VanDerWaalsParameterTable::Entry::getFactorG() const
{
	return factG;
}
  
Forcefield::MMFF94VanDerWaalsParameterTable::HDonorAcceptorType
Forcefield::MMFF94VanDerWaalsParameterTable::Entry::getHDonorAcceptorType() const
{
	return donAccType;
}

Forcefield::MMFF94VanDerWaalsParameterTable::Entry::operator bool() const
{
	return initialized;
}


Forcefield::MMFF94VanDerWaalsParameterTable::MMFF94VanDerWaalsParameterTable()
{}

void Forcefield::MMFF94VanDerWaalsParameterTable::addEntry(unsigned int atom_type, double atom_pol, double eff_el_num, 
														   double fact_a, double fact_g, HDonorAcceptorType don_acc_type)
{
    entries.insert(DataStorage::value_type(atom_type, Entry(atom_type, atom_pol, eff_el_num, fact_a, fact_g, don_acc_type)));
}

const Forcefield::MMFF94VanDerWaalsParameterTable::Entry& Forcefield::MMFF94VanDerWaalsParameterTable::getEntry(unsigned int atom_type) const
{
	DataStorage::const_iterator it = entries.find(atom_type);

	if (it == entries.end())
		return NOT_FOUND;

	return it->second;
}

std::size_t Forcefield::MMFF94VanDerWaalsParameterTable::getNumEntries() const
{
    return entries.size();
}

void Forcefield::MMFF94VanDerWaalsParameterTable::clear()
{
    entries.clear();
}

bool Forcefield::MMFF94VanDerWaalsParameterTable::removeEntry(unsigned int atom_type)
{
	return entries.erase(atom_type);
}

Forcefield::MMFF94VanDerWaalsParameterTable::EntryIterator 
Forcefield::MMFF94VanDerWaalsParameterTable::removeEntry(const EntryIterator& it)
{
	return EntryIterator(entries.erase(it.base()), boost::bind<Entry&>(&DataStorage::value_type::second, _1));
}

Forcefield::MMFF94VanDerWaalsParameterTable::ConstEntryIterator 
Forcefield::MMFF94VanDerWaalsParameterTable::getEntriesBegin() const
{
	return ConstEntryIterator(entries.begin(), boost::bind(&DataStorage::value_type::second, _1));
}

Forcefield::MMFF94VanDerWaalsParameterTable::ConstEntryIterator 
Forcefield::MMFF94VanDerWaalsParameterTable::getEntriesEnd() const
{
	return ConstEntryIterator(entries.end(), boost::bind(&DataStorage::value_type::second, _1));
}
	
Forcefield::MMFF94VanDerWaalsParameterTable::EntryIterator 
Forcefield::MMFF94VanDerWaalsParameterTable::getEntriesBegin()
{
	return EntryIterator(entries.begin(), boost::bind<Entry&>(&DataStorage::value_type::second, _1));
}

Forcefield::MMFF94VanDerWaalsParameterTable::EntryIterator 
Forcefield::MMFF94VanDerWaalsParameterTable::getEntriesEnd()
{
	return EntryIterator(entries.end(), boost::bind<Entry&>(&DataStorage::value_type::second, _1));
}

void Forcefield::MMFF94VanDerWaalsParameterTable::setExponent(double value)
{
	exponent = value;
}

void Forcefield::MMFF94VanDerWaalsParameterTable::setBeta(double value)
{
	beta = value;
}

void Forcefield::MMFF94VanDerWaalsParameterTable::setFactorB(double value)
{
	factB = value;
}

void Forcefield::MMFF94VanDerWaalsParameterTable::setFactorDARAD(double value)
{
	factDARAD = value;
}

void Forcefield::MMFF94VanDerWaalsParameterTable::setFactorDAEPS(double value)
{
	factDAEPS = value;
}

double Forcefield::MMFF94VanDerWaalsParameterTable::getExponent() const
{
	return exponent;
}
		
double Forcefield::MMFF94VanDerWaalsParameterTable::getFactorB() const
{
	return factB;
}
		
double Forcefield::MMFF94VanDerWaalsParameterTable::getBeta() const
{
	return beta;
}
		
double Forcefield::MMFF94VanDerWaalsParameterTable::getFactorDARAD() const
{
	return factDARAD;
}

double Forcefield::MMFF94VanDerWaalsParameterTable::getFactorDAEPS() const
{
	return factDAEPS;
}

void Forcefield::MMFF94VanDerWaalsParameterTable::load(std::istream& is)
{
    std::string line;
    unsigned int atom_type;
	double atom_pol;
	double eff_el_num;
	double fact_a;
	double fact_g;
	char don_acc_type_ch;

	if (!readMMFF94DataLine(is, line, "MMFF94VanDerWaalsParameterTable: error while reading van der Waals parameter entry"))
		return;

	std::istringstream line_iss(line);

	if (!(line_iss >> exponent))
		throw Base::IOError("MMFF94VanDerWaalsParameterTable: error while reading exponent parameter");
	
	if (!(line_iss >> factB))
		throw Base::IOError("MMFF94VanDerWaalsParameterTable: error while reading B factor parameter");
	
	if (!(line_iss >> beta))
		throw Base::IOError("MMFF94VanDerWaalsParameterTable: error while reading beta parameter");

	if (!(line_iss >> factDARAD))
		throw Base::IOError("MMFF94VanDerWaalsParameterTable: error while reading DARAD parameter");	

	if (!(line_iss >> factDAEPS))
		throw Base::IOError("MMFF94VanDerWaalsParameterTable: error while reading DEPS parameter");	

    while (readMMFF94DataLine(is, line, "MMFF94VanDerWaalsParameterTable: error while reading van der Waals parameter entry")) {
		std::istringstream line_iss(line);

		if (!(line_iss >> atom_type))
			throw Base::IOError("MMFF94VanDerWaalsParameterTable: error while reading atom type");
	
		if (!(line_iss >> atom_pol))
			throw Base::IOError("MMFF94VanDerWaalsParameterTable: error while reading atomic polarizability alpha");

		if (!(line_iss >> eff_el_num))
			throw Base::IOError("MMFF94VanDerWaalsParameterTable: error while reading effective electron number N");
	
		if (!(line_iss >> fact_a))
			throw Base::IOError("MMFF94VanDerWaalsParameterTable: error while reading scaling factor A");

		if (!(line_iss >> fact_g))
			throw Base::IOError("MMFF94VanDerWaalsParameterTable: error while reading scaling factor G");

		if (!(line_iss >> don_acc_type_ch))
			throw Base::IOError("MMFF94VanDerWaalsParameterTable: error while reading donor/acceptor type");

		HDonorAcceptorType don_acc_type = HDonorAcceptorType::NONE;

		switch (don_acc_type_ch) {

			case 'A':
				don_acc_type = HDonorAcceptorType::ACCEPTOR;
				break;
				
			case 'D':
				don_acc_type = HDonorAcceptorType::DONOR;
				break;
			
			case '-':
				break;

			default:
				throw Base::IOError("MMFF94VanDerWaalsParameterTable: invalid donor/acceptor type specification");
		}

		addEntry(atom_type, atom_pol, eff_el_num, fact_a, fact_g, don_acc_type);
    }
}

void Forcefield::MMFF94VanDerWaalsParameterTable::loadDefaults()
{
#if defined(HAVE_BOOST_IOSTREAMS)

    boost::iostreams::stream<boost::iostreams::array_source> is(MMFF94ParameterData::VAN_DER_WAALS_PARAMETERS, 
																std::strlen(MMFF94ParameterData::VAN_DER_WAALS_PARAMETERS));
#else // defined(HAVE_BOOST_IOSTREAMS)

	std::istringstream is(std::string(MMFF94ParameterData::VAN_DER_WAALS_PARAMETERS));

#endif // defined(HAVE_BOOST_IOSTREAMS)

    load(is);
}

void Forcefield::MMFF94VanDerWaalsParameterTable::set(const SharedPointer& table)
{	
    defaultTable = (!table ? builtinTable : table);
}

const Forcefield::MMFF94VanDerWaalsParameterTable::SharedPointer& Forcefield::MMFF94VanDerWaalsParameterTable::get()
{
    return defaultTable;
}
