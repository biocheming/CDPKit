/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * AutoCorrelationVectorCalculator.hpp 
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
 * \brief Definition of the class CDPL::Chem::AutoCorrelationVectorCalculator.
 */

#ifndef CDPL_CHEM_AUTOCORRELATIONVECTORCALCULATOR_HPP
#define CDPL_CHEM_AUTOCORRELATIONVECTORCALCULATOR_HPP

#include <boost/function.hpp>

#include "CDPL/Chem/APIPrefix.hpp"
#include "CDPL/Math/Vector.hpp"


namespace CDPL 
{

	namespace Chem
	{

		class MolecularGraph;
		class Atom;

		/**
		 * \addtogroup CDPL_CHEM_2D_AUTOCORRELATION
		 * @{
		 */

		/**
		 * \brief AutoCorrelationVectorCalculator.
		 * \see [\ref AUCOR, \ref HBMD]
		 */
		class CDPL_CHEM_API AutoCorrelationVectorCalculator
		{

		public:
			/**
			 * \brief Type of the generic functor class used to store user-defined atom pair weight functions.
			 *
			 * The provided atom pair weight function (or function object) is required to take the two atoms (as a
			 * \c const reference to Chem::Atom) as its arguments and return the weight of the atom pair as
			 * a floating-point value of type \c double. For details refer to the <em>Boost.Function</em>
			 * documentation [\ref BFUN]. 
			 */
			typedef boost::function2<double, const Atom&, const Atom&> AtomPairWeightFunction;

			/**
			 * \brief Constructs the \c %AutoCorrelationVectorCalculator instance.
			 */
			AutoCorrelationVectorCalculator();

			/**
			 * \brief Constructs the \c %AutoCorrelationVectorCalculator instance and calculates the autocorrelation
			 *        vector of the molecular graph \a molgraph.
			 *
			 * The calculated autocorrelation vector can be retrieved by a call to getResult().
			 *
			 * \param molgraph The molecular graph for which to calculate the autocorrelation vector.
			 */
			AutoCorrelationVectorCalculator(const MolecularGraph& molgraph);

			/**
			 * \brief Allows to specify a custom atom pair weight function.
			 * \param func An AutoCorrelationVectorCalculator::AtomPairWeightFunction instance that wraps the target function.
			 * \note The default atom pair weight function returns the product of the atom types (see namespace
			 *       Chem::AtomType).
			 */
			void setAtomPairWeightFunction(const AtomPairWeightFunction& func);

			/**
			 * \brief Calculates the topological autocorrelation vector of the molecular graph \a molgraph.
			 *
			 * The elements of the calculated vector provide the sum of the weights of all atom pairs with a
			 * topological distance equal to the element index. The size of the vector is limited by the
			 * topological diameter of the molecular graph.
			 *
			 * \param molgraph The molecular graph for which to calculate the autocorrelation vector.
			 * \return The calculated autocorrelation vector. 
			 */
			const Math::DVector& calculate(const MolecularGraph& molgraph);

			/**
			 * \brief Returns the result of the last autocorrelation vector calculation.
			 * \return The calculated autocorrelation vector. The length of the returned vector is zero if
			 *         a calculation has not yet been performed.
			 * \see calculate()
			 */
			const Math::DVector& getResult() const;

		private:
			AutoCorrelationVectorCalculator(const AutoCorrelationVectorCalculator&);

			AutoCorrelationVectorCalculator& operator=(const AutoCorrelationVectorCalculator&);

			AtomPairWeightFunction weightFunc;
			Math::DVector          autoCorrVector;
		}; 

		/**
		 * @}
		 */
	}
}

#endif // CDPL_CHEM_AUTOCORRELATIONVECTORCALCULATOR_HPP
