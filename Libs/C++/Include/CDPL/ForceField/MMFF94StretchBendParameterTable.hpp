/* 
 * MMFF94StretchBendParameterTable.hpp 
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
 * \brief Definition of the class CDPL::ForceField::MMFF94StretchBendParameterTable.
 */

#ifndef CDPL_FORCEFIELD_MMFF94STRETCHBENDPARAMETERTABLE_HPP
#define CDPL_FORCEFIELD_MMFF94STRETCHBENDPARAMETERTABLE_HPP

#include <cstddef>
#include <cstdint>
#include <iosfwd>
#include <unordered_map>
#include <memory>
#include <functional>

#include <boost/iterator/transform_iterator.hpp>

#include "CDPL/ForceField/APIPrefix.hpp"


namespace CDPL 
{

    namespace ForceField 
    {

		class CDPL_FORCEFIELD_API MMFF94StretchBendParameterTable
		{

		  public:
			class Entry;

		  private:
			typedef std::unordered_map<std::uint32_t, Entry> DataStorage;

		  public:
			typedef std::shared_ptr<MMFF94StretchBendParameterTable> SharedPointer;
	
			class CDPL_FORCEFIELD_API Entry
			{

			  public:
				Entry();
 
				Entry(unsigned int sb_type_idx, unsigned int term_atom1_type, unsigned int ctr_atom_type, 
					  unsigned int term_atom2_type, double ijk_force_const, double kji_force_const);

				unsigned int getStretchBendTypeIndex() const;

				unsigned int getTerminalAtom1Type() const;

				unsigned int getCenterAtomType() const;

				unsigned int getTerminalAtom2Type() const;

				double getIJKForceConstant() const;

				double getKJIForceConstant() const;

				operator bool() const;

			  private:
				unsigned int sbTypeIdx;
				unsigned int termAtom1Type;
				unsigned int ctrAtomType;
				unsigned int termAtom2Type;
				double       ijkForceConst;
				double       kjiForceConst;
				bool         initialized;
			};			

			typedef boost::transform_iterator<std::function<const Entry&(const DataStorage::value_type&)>, 
											  DataStorage::const_iterator> ConstEntryIterator;

			typedef boost::transform_iterator<std::function<Entry&(DataStorage::value_type&)>, 
											  DataStorage::iterator> EntryIterator;
	
			MMFF94StretchBendParameterTable();

			void addEntry(unsigned int sb_type_idx, unsigned int term_atom1_type, unsigned int ctr_atom_type, 
						  unsigned int term_atom2_type, double ijk_force_const, double kji_force_const);

			const Entry& getEntry(unsigned int sb_type_idx, unsigned int term_atom1_type, unsigned int ctr_atom_type, 
								  unsigned int term_atom2_type) const;

			std::size_t getNumEntries() const;

			void clear();

			bool removeEntry(unsigned int sb_type_idx, unsigned int term_atom1_type, unsigned int ctr_atom_type, 
							 unsigned int term_atom2_type);

			EntryIterator removeEntry(const EntryIterator& it);

			ConstEntryIterator getEntriesBegin() const;

			ConstEntryIterator getEntriesEnd() const;
	
			EntryIterator getEntriesBegin();

			EntryIterator getEntriesEnd();

			ConstEntryIterator begin() const;

			ConstEntryIterator end() const;
	
			EntryIterator begin();

			EntryIterator end();

			void load(std::istream& is);

			void loadDefaults();

			static void set(const SharedPointer& table);

			static const SharedPointer& get();

		  private:
			static SharedPointer defaultTable;
			DataStorage          entries;
		};
    }
}

#endif // CDPL_FORCEFIELD_MMFF94STRETCHBENDPARAMETERTABLE_HPP
