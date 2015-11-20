/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * BCUTDescriptorCalculator.hpp 
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
 * \brief Definition of the class CDPL::Chem::BCUTDescriptorCalculator.
 */

#ifndef CDPL_CHEM_BCUTDESCRIPTORCALCULATOR_HPP
#define CDPL_CHEM_BCUTDESCRIPTORCALCULATOR_HPP

#include "CDPL/Chem/APIPrefix.hpp"
#include "CDPL/Chem/BurdenMatrixGenerator.hpp"
#include "CDPL/Math/Vector.hpp"
#include "CDPL/Math/Matrix.hpp"


namespace CDPL 
{

	namespace Chem
	{

		/**
		 * \addtogroup CDPL_CHEM_BCUT_DESCRIPTORS
		 * @{
		 */

		/**
		 * \brief BCUTDescriptorCalculator.
		 * \see [\ref BCUT]
		 */
		class CDPL_CHEM_API BCUTDescriptorCalculator
		{
			 
		public:
			/**
			 * \brief Type of the generic functor class used to store user-defined atom weight functions for the initialization
			 *        of the underlying \e Burden matrix [\ref BURMA].
			 *
			 * An atom weight function (or function object) is required to take the atom (as a
			 * \c const reference to Chem::Atom) as argument and return the weight of the atom as
			 * a floating-point value of type \c double.
			 */
			typedef BurdenMatrixGenerator::AtomWeightFunction AtomWeightFunction;

			/**
			 * \brief Constructs the \c %BCUTDescriptorCalculator instance.
			 */
			BCUTDescriptorCalculator() {}

			/**
			 * \brief Constructs the \c %BCUTDescriptorCalculator instance and calculates the \e BCUT descriptor of
			 *        the molecular graph \a molgraph.
			 *
			 * The calculated descriptor can be retrieved by a call to getResult().
			 *
			 * \param molgraph The molecular graph for which to calculate the \e BCUT descriptor.
			 */
			BCUTDescriptorCalculator(const MolecularGraph& molgraph);

			/**
			 * \brief Allows to specify a custom atom weight function for the initialization of the
			 *        underlying \e Burden matrix [\ref BURMA].
			 * \param func A BCUTDescriptorCalculator::AtomWeightFunction instance that wraps the target function.
			 * \see Chem::BurdenMatrixGenerator::setAtomWeightFunction()
			 */
			void setAtomWeightFunction(const AtomWeightFunction& func);

			/**
			 * \brief Calculates the \e BCUT descriptor of the molecular graph \a molgraph.
			 *
			 * The returned \e BCUT descriptor is a vector that contains the calculated eigenvalues of the
			 * underlying \e Burden matrix [\ref BURMA]. The elements of the vector are sorted in ascending order.
			 * Note that explicit hydrogen atoms are included in the calculation of the \e BCUT descriptor.
			 * To calculate the descriptor for a hydrogen depleted molecular graph, any hydrogen atoms have
			 * to be removed from the molecular graph \e before the calculation is performed.
			 *
			 * \param molgraph The molecular graph for which to calculate the \e BCUT descriptor.
			 * \return The calculated \e BCUT descriptor. 
			 */
			const Math::DVector& calculate(const MolecularGraph& molgraph);

			/**
			 * \brief Returns the result of the last \e BCUT descriptor calculation.
			 * \return The calculated \e BCUT descriptor. The vector is empty if a calculation has not yet been
			 *         performed.
			 * \see calculate()
			 */
			const Math::DVector& getResult() const;

		private:
			BCUTDescriptorCalculator(const BCUTDescriptorCalculator&);

			BCUTDescriptorCalculator& operator=(const BCUTDescriptorCalculator&);

			BurdenMatrixGenerator  burdenMatrixGenerator;
			Math::DVector          bcutDescriptor;
			Math::DMatrix          tmpBurdenMatrix;
			Math::DMatrix          eigenVectors;
		}; 

		/**
		 * @}
		 */
	}
}

#endif // CDPL_CHEM_BCUTDESCRIPTORCALCULATOR_HPP
