#
# This file is part of the Chemical Data Processing Toolkit
#
# Copyright (C) Thomas A. Seidel <thomas.seidel@univie.ac.at>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; see the file COPYING. If not, write to
# the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.
#

##
# \brief 
#
class PharmacophoreGenerator(Boost.Python.instance):

    ##
    # \brief Initializes the \e %PharmacophoreGenerator instance.
    # \param self The \e %PharmacophoreGenerator instance to initialize.
    #
    def __init__(self: object) -> None: pass

    ##
    # \brief Initializes the \e %PharmacophoreGenerator instance.
    # \param self The \e %PharmacophoreGenerator instance to initialize.
    # \param gen 
    #
    def __init__(self: object, gen: PharmacophoreGenerator) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %PharmacophoreGenerator instance this method is called upon.
    #
    # Different Python \e %PharmacophoreGenerator instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %PharmacophoreGenerator instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: PharmacophoreGenerator) -> int: pass

    ##
    # \brief 
    # \param self The \e %PharmacophoreGenerator instance this method is called upon.
    # \param molgraph 
    # \param pharm 
    # \param append 
    #
    def generate(self: PharmacophoreGenerator, molgraph: CDPL.Chem.MolecularGraph, pharm: Pharmacophore, append: bool = False) -> None: pass

    ##
    # \brief 
    # \param self The \e %PharmacophoreGenerator instance this method is called upon.
    # \return 
    #
    def clone(self: PharmacophoreGenerator) -> PharmacophoreGenerator: pass

    ##
    # \brief 
    # \param self The \e %PharmacophoreGenerator instance this method is called upon.
    # \param func 
    #
    def setAtom3DCoordinatesFunction(self: PharmacophoreGenerator, func: CDPL.Chem.Atom3DCoordinatesFunction) -> None: pass

    ##
    # \brief 
    # \param self The \e %PharmacophoreGenerator instance this method is called upon.
    # \return 
    #
    def getAtom3DCoordinatesFunction(self: PharmacophoreGenerator) -> CDPL.Chem.Atom3DCoordinatesFunction: pass

    ##
    # \brief 
    # \param self The \e %PharmacophoreGenerator instance this method is called upon.
    # \param type 
    # \param ftr_gen 
    #
    def setFeatureGenerator(self: PharmacophoreGenerator, type: int, ftr_gen: FeatureGenerator) -> None: pass

    ##
    # \brief 
    # \param self The \e %PharmacophoreGenerator instance this method is called upon.
    # \param type 
    #
    def removeFeatureGenerator(self: PharmacophoreGenerator, type: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %PharmacophoreGenerator instance this method is called upon.
    # \param type 
    # \return 
    #
    def getFeatureGenerator(self: PharmacophoreGenerator, type: int) -> FeatureGenerator: pass

    ##
    # \brief 
    # \param self The \e %PharmacophoreGenerator instance this method is called upon.
    # \param type 
    # \param enable 
    #
    def enableFeature(self: PharmacophoreGenerator, type: int, enable: bool) -> None: pass

    ##
    # \brief 
    # \param self The \e %PharmacophoreGenerator instance this method is called upon.
    # \param ft_type 
    # \return 
    #
    def isFeatureEnabled(self: PharmacophoreGenerator, ft_type: int) -> bool: pass

    ##
    # \brief 
    # \param self The \e %PharmacophoreGenerator instance this method is called upon.
    # \param arg1 
    # \return 
    #
    def clearEnabledFeatures(arg1: PharmacophoreGenerator, self: int) -> bool: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %PharmacophoreGenerator instance \a gen.
    # \param self The \e %PharmacophoreGenerator instance this method is called upon.
    # \param gen The \e %PharmacophoreGenerator instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: PharmacophoreGenerator, gen: PharmacophoreGenerator) -> PharmacophoreGenerator: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief FIXME!
    #
    atom3DCoordsFunc = property(getAtom3DCoordsFunc, setAtom3DCoordsFunc)