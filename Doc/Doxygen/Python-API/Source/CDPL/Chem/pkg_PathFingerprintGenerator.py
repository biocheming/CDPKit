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
class PathFingerprintGenerator(Boost.Python.instance):

    ##
    # \brief 
    #
    class DefAtomDescriptorFunctor(Boost.Python.instance):

        ##
        # \brief Initializes the \e %DefAtomDescriptorFunctor instance.
        # \param self The \e %DefAtomDescriptorFunctor instance to initialize.
        # \param flags 
        #
        def __init__(self: object, flags: int = 142) -> None: pass

        ##
        # \brief 
        # \param self The \e %DefAtomDescriptorFunctor instance this method is called upon.
        # \param atom 
        # \return 
        #
        def __call__(self: DefAtomDescriptorFunctor, atom: Atom) -> int: pass

    ##
    # \brief 
    #
    class DefBondDescriptorFunctor(Boost.Python.instance):

        ##
        # \brief Initializes the \e %DefBondDescriptorFunctor instance.
        # \param self The \e %DefBondDescriptorFunctor instance to initialize.
        # \param flags 
        #
        def __init__(self: object, flags: int = 14) -> None: pass

        ##
        # \brief 
        # \param self The \e %DefBondDescriptorFunctor instance this method is called upon.
        # \param bond 
        # \return 
        #
        def __call__(self: DefBondDescriptorFunctor, bond: Bond) -> int: pass

    ##
    # \brief 
    #
    DEF_ATOM_PROPERTY_FLAGS = 142

    ##
    # \brief 
    #
    DEF_BOND_PROPERTY_FLAGS = 14

    ##
    # \brief Initializes the \e %PathFingerprintGenerator instance.
    # \param self The \e %PathFingerprintGenerator instance to initialize.
    #
    def __init__(self: object) -> None: pass

    ##
    # \brief Initializes the \e %PathFingerprintGenerator instance.
    # \param self The \e %PathFingerprintGenerator instance to initialize.
    # \param molgraph 
    # \param fp 
    #
    def __init__(self: object, molgraph: MolecularGraph, fp: CDPL.Util.BitSet) -> None: pass

    ##
    # \brief Initializes the \e %PathFingerprintGenerator instance.
    # \param self The \e %PathFingerprintGenerator instance to initialize.
    # \param gen 
    #
    def __init__(self: object, gen: PathFingerprintGenerator) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %PathFingerprintGenerator instance this method is called upon.
    #
    # Different Python \e %PathFingerprintGenerator instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %PathFingerprintGenerator instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: PathFingerprintGenerator) -> int: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %PathFingerprintGenerator instance \a gen.
    # \param self The \e %PathFingerprintGenerator instance this method is called upon.
    # \param gen The \e %PathFingerprintGenerator instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: PathFingerprintGenerator, gen: PathFingerprintGenerator) -> PathFingerprintGenerator: pass

    ##
    # \brief 
    # \param self The \e %PathFingerprintGenerator instance this method is called upon.
    # \param func 
    #
    def setAtomDescriptorFunction(self: PathFingerprintGenerator, func: SizeTypeAtomFunctor) -> None: pass

    ##
    # \brief 
    # \param self The \e %PathFingerprintGenerator instance this method is called upon.
    # \param func 
    #
    def setBondDescriptorFunction(self: PathFingerprintGenerator, func: UInt64BondFunctor) -> None: pass

    ##
    # \brief 
    # \param self The \e %PathFingerprintGenerator instance this method is called upon.
    # \param min_length 
    #
    def setMinPathLength(self: PathFingerprintGenerator, min_length: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %PathFingerprintGenerator instance this method is called upon.
    # \param max_length 
    #
    def setMaxPathLength(self: PathFingerprintGenerator, max_length: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %PathFingerprintGenerator instance this method is called upon.
    # \param num_bits 
    #
    def setNumBits(self: PathFingerprintGenerator, num_bits: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %PathFingerprintGenerator instance this method is called upon.
    # \return 
    #
    def getMinPathLength(self: PathFingerprintGenerator) -> int: pass

    ##
    # \brief 
    # \param self The \e %PathFingerprintGenerator instance this method is called upon.
    # \return 
    #
    def getMaxPathLength(self: PathFingerprintGenerator) -> int: pass

    ##
    # \brief 
    # \param self The \e %PathFingerprintGenerator instance this method is called upon.
    # \return 
    #
    def getNumBits(self: PathFingerprintGenerator) -> int: pass

    ##
    # \brief 
    # \param self The \e %PathFingerprintGenerator instance this method is called upon.
    # \param molgraph 
    # \param fp 
    #
    def generate(self: PathFingerprintGenerator, molgraph: MolecularGraph, fp: CDPL.Util.BitSet) -> None: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief 
    #
    minPathLength = property(getMinPathLength, setMinPathLength)

    ##
    # \brief 
    #
    maxPathLength = property(getMaxPathLength, setMaxPathLength)

    ##
    # \brief 
    #
    numBits = property(getNumBits, setNumBits)
