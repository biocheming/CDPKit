/* 
 * BondOrderCalculatorExport.cpp 
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


#include <boost/python.hpp>

#include "CDPL/Chem/BondOrderCalculator.hpp"
#include "CDPL/Chem/MolecularGraph.hpp"

#include "Base/ObjectIdentityCheckVisitor.hpp"

#include "ClassExports.hpp"


void CDPLPythonChem::exportBondOrderCalculator()
{
    using namespace boost;
    using namespace CDPL;

    bool (Chem::BondOrderCalculator::*undefOnlyGetterFunc)() const = &Chem::BondOrderCalculator::undefinedOnly;
    void (Chem::BondOrderCalculator::*undefOnlySetterFunc)(bool) = &Chem::BondOrderCalculator::undefinedOnly;

    python::class_<Chem::BondOrderCalculator, boost::noncopyable>("BondOrderCalculator", python::no_init)
        .def(python::init<>(python::arg("self")))
        .def(python::init<const Chem::MolecularGraph&, Util::STArray&, bool>(
                 (python::arg("self"), python::arg("molgraph"), python::arg("orders"), python::arg("undef_only") = true)))
        .def(CDPLPythonBase::ObjectIdentityCheckVisitor<Chem::BondOrderCalculator>())    
        .def("undefinedOnly", undefOnlySetterFunc, (python::arg("self"), python::arg("undef_only")))
        .def("undefinedOnly", undefOnlyGetterFunc, python::arg("self"))
        .def("calculate", &Chem::BondOrderCalculator::calculate, 
             (python::arg("self"), python::arg("molgraph"), python::arg("orders")))
        .add_property("undefOnly", undefOnlyGetterFunc, undefOnlySetterFunc);
}
