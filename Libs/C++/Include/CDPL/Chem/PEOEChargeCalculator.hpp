/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * PEOEChargeCalculator.hpp 
 * 
 * Charge calculation by partial equalization of orbital electronegativities (PEOE)
 * (J. Gasteiger, M. Marsili, Tetrahedron 1980, 36, 3219-3228) 
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
 * \brief Definition of the class CDPL::Chem::PEOEChargeCalculator.
 */

#ifndef CDPL_CHEM_PEOECHARGECALCULATOR_HPP
#define CDPL_CHEM_PEOECHARGECALCULATOR_HPP

#include <cstddef>
#include <vector>

#include <boost/shared_ptr.hpp>

#include "CDPL/Chem/APIPrefix.hpp"
#include "CDPL/Util/Array.hpp"


namespace CDPL 
{

	namespace Chem
	{

		class MolecularGraph;
		class Atom;

		/**
		 * \addtogroup CDPL_CHEM_PEOE_CHARGES
		 * @{
		 */

		/**
		 * \brief PEOEChargeCalculator.
		 * \see [\ref PEOE]
		 */
		class CDPL_CHEM_API PEOEChargeCalculator
		{

		public:
			typedef boost::shared_ptr<PEOEChargeCalculator> SharedPointer;

			/**
			 * \brief Constructs the \c %PEOEChargeCalculator instance.
			 */
			PEOEChargeCalculator();

			/**
			 * \brief Constructs the \c %PEOEChargeCalculator instance and calculates the \e PEOE charges of
			 *        the atoms in the molecular graph \a molgraph.
			 *
			 * The calculated partial atomic charges can be retrieved by a call to getResult().
			 *
			 * \param molgraph The molecular graph for which to calculate the \e PEOE charges.
			 */
			PEOEChargeCalculator(const MolecularGraph& molgraph);

			/**
			 * \brief Allows to specify the number of charge shifting iterations that have to be performed.
			 * \param num_iter The number of iterations to perform.
			 * \note By default, \e 6 iterations are performed.
			 */
			void setNumIterations(std::size_t num_iter);

			/**
			 * \brief Returns the number of performed charge shifting iterations.
			 * \return The number of performed iterations.
			 */
			std::size_t getNumIterations() const;

			/**
			 * \brief Allows to specify the applied damping factor.
			 * \param factor The damping factor to apply.
			 * \note The default damping factor is <em>0.5</em>.
			 */
			void setDampingFactor(double factor);

			/**
			 * \brief Returns the applied damping factor.
			 * \return The applied damping factor.
			 */
			double getDampingFactor() const;

			/**
			 * \brief Calculates the \e PEOE charges of the atoms in the molecular graph \a molgraph.
			 * \param molgraph The molecular graph for which to calculate the \e PEOE charges.  
			 * \return An array containing the calculated partial atomic charges. The charges
			 *         are stored in the same order as the atoms appear in the atom list of the
			 *         molecular graph (i.e. the partial charge of an atom is accessible via its index).
			 */
			const Util::DArray& calculate(const MolecularGraph& molgraph);

			/**
			 * \brief Returns the result of the last \e PEOE charge calculation.
			 * \return An array containing the calculated partial atomic charges. If a calculation has not yet
			 *         been performed, the returned array is empty.
			 * \see calculate()
			 */
			const Util::DArray& getResult() const;

			/**
			 * \brief Returns the residual atom electronegativities resulting from the last \e PEOE charge calculation.
			 * \return An array containing the residual electronegativities. If a calculation has not yet
			 *         been performed, the returned array is empty. The electronegativities
			 *         are stored in the same order as the atoms appear in the atom list of the
			 *         molecular graph (i.e. the residual electronegativity of an atom is accessible via
			 *         its index).
			 */
			const Util::DArray& getElectronegativities() const;

		private:
			/** \cond CDPL_PRIVATE_SECTION_DOC */

			PEOEChargeCalculator(const PEOEChargeCalculator&);

			PEOEChargeCalculator& operator=(const PEOEChargeCalculator&);

			void init(const MolecularGraph&);
			void calcCharges();

			class PEOEAtomState
			{

			public:
				typedef boost::shared_ptr<PEOEAtomState> SharedPointer;

				PEOEAtomState();
				PEOEAtomState(const Atom&, const MolecularGraph&);

				void linkTo(PEOEAtomState*);

				double getCharge() const;
				double getElectronegativity() const;

				void shiftCharges(double);
				void updateElectronegativity();

			private:
				typedef std::vector<PEOEAtomState*> PEOEAtomStateList;

				PEOEAtomStateList  nbrAtomStates;
				double             a;
				double             b;
				double             c;
				double             enegativity;
				double             enegativityP1;
				double             charge;
			};

			typedef std::vector<PEOEAtomState::SharedPointer> PEOEAtomStateList;
		
			std::size_t        numIterations;
			double             dampingFactor;
			PEOEAtomStateList  atomStates;
			PEOEAtomStateList  implHStates;
			Util::DArray       resCharges;
			Util::DArray       resEnegativities;

			/** \endcond */
		};

		/**
		 * @}
		 */
	}
}

#endif // CDPL_CHEM_PEOECHARGECALCULATOR_HPP
