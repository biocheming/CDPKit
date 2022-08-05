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
class Molecule(MolecularGraph):

    ##
    # \brief 
    #
    class AtomSequence(Boost.Python.instance):

        ##
        # \brief 
        # \return 
        #
        def __len__() -> int: pass

        ##
        # \brief 
        # \param idx 
        # \return 
        #
        def __getitem__(idx: int) -> Atom: pass

        ##
        # \brief 
        # \param idx 
        #
        def __delitem__(idx: int) -> None: pass

        ##
        # \brief Returns the result of the membership test operation <tt>atom in self</tt>.
        # \param atom The value to test for membership.
        # \return The result of the membership test operation.
        #
        def __contains__(atom: Atom) -> bool: pass

    ##
    # \brief 
    #
    class BondSequence(Boost.Python.instance):

        ##
        # \brief 
        # \return 
        #
        def __len__() -> int: pass

        ##
        # \brief 
        # \param idx 
        # \return 
        #
        def __getitem__(idx: int) -> Bond: pass

        ##
        # \brief 
        # \param idx 
        #
        def __delitem__(idx: int) -> None: pass

        ##
        # \brief Returns the result of the membership test operation <tt>bond in self</tt>.
        # \param bond The value to test for membership.
        # \return The result of the membership test operation.
        #
        def __contains__(bond: Bond) -> bool: pass

    ##
    # \brief Initializes the \e %Molecule instance.
    #
    def __init__() -> None: pass

    ##
    # \brief 
    # \param num_atoms 
    #
    def reserveMemoryForAtoms(num_atoms: int) -> None: pass

    ##
    # \brief 
    # \param num_bonds 
    #
    def reserveMemoryForBonds(num_bonds: int) -> None: pass

    ##
    # \brief 
    #
    def clear() -> None: pass

    ##
    # \brief 
    # \return 
    #
    def addAtom() -> Atom: pass

    ##
    # \brief 
    # \param atom1_idx 
    # \param atom2_idx 
    # \return 
    #
    def addBond(atom1_idx: int, atom2_idx: int) -> Bond: pass

    ##
    # \brief 
    # \param idx 
    #
    def removeAtom(idx: int) -> None: pass

    ##
    # \brief 
    # \param idx 
    #
    def removeBond(idx: int) -> None: pass

    ##
    # \brief 
    # \param mol 
    #
    def copy(mol: Molecule) -> None: pass

    ##
    # \brief 
    # \param molgraph 
    #
    def copy(molgraph: MolecularGraph) -> None: pass

    ##
    # \brief 
    # \param mol 
    #
    def append(mol: Molecule) -> None: pass

    ##
    # \brief 
    # \param molgraph 
    #
    def append(molgraph: MolecularGraph) -> None: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %Molecule instance \a mol.
    # \param mol The \e %Molecule instance to copy.
    # \return The assignment target \a self.
    #
    def assign(mol: Molecule) -> Molecule: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %Molecule instance \a molgraph.
    # \param molgraph The \e %Molecule instance to copy.
    # \return The assignment target \a self.
    #
    def assign(molgraph: MolecularGraph) -> Molecule: pass

    ##
    # \brief 
    # \return 
    #
    def getAtoms() -> AtomSequence: pass

    ##
    # \brief 
    # \return 
    #
    def getBonds() -> BondSequence: pass

    ##
    # \brief 
    # \param idx 
    # \return 
    #
    def getAtom(idx: int) -> Atom: pass

    ##
    # \brief 
    # \param atom 
    # \return 
    #
    def containsAtom(atom: Atom) -> bool: pass

    ##
    # \brief 
    # \param arg1 
    # \param arg2 
    #
    def containsAtom(arg2: Atom) -> None: pass

    ##
    # \brief 
    # \param atom 
    # \return 
    #
    def getAtomIndex(atom: Atom) -> int: pass

    ##
    # \brief 
    # \param arg1 
    # \param arg2 
    #
    def getAtomIndex(arg2: Atom) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getNumAtoms() -> int: pass

    ##
    # \brief 
    # \param func 
    #
    def orderAtoms(func: CDPL.ForceField.InteractionFilterFunction2) -> None: pass

    ##
    # \brief 
    # \param idx 
    # \return 
    #
    def getEntity(idx: int) -> Entity3D: pass

    ##
    # \brief 
    # \return 
    #
    def getNumEntities() -> int: pass

    ##
    # \brief 
    # \param idx 
    # \return 
    #
    def getBond(idx: int) -> Bond: pass

    ##
    # \brief 
    # \param bond 
    # \return 
    #
    def containsBond(bond: Bond) -> bool: pass

    ##
    # \brief 
    # \param arg1 
    # \param arg2 
    #
    def containsBond(arg2: Bond) -> None: pass

    ##
    # \brief 
    # \param func 
    #
    def orderBonds(func: BoolBond2Functor) -> None: pass

    ##
    # \brief 
    # \param bond 
    # \return 
    #
    def getBondIndex(bond: Bond) -> int: pass

    ##
    # \brief 
    # \param arg1 
    # \param arg2 
    #
    def getBondIndex(arg2: Bond) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getNumBonds() -> int: pass

    ##
    # \brief 
    # \param key 
    # \param value 
    #
    def setProperty(key: CDPL.Base.LookupKey, value: CDPL.Base.Variant) -> None: pass

    ##
    # \brief 
    # \param key 
    # \return 
    #
    def removeProperty(key: CDPL.Base.LookupKey) -> bool: pass

    ##
    # \brief 
    # \param key 
    # \param throw_ 
    # \return 
    #
    def getProperty(key: CDPL.Base.LookupKey, throw_: bool = False) -> CDPL.Base.Variant: pass

    ##
    # \brief 
    # \param key 
    # \return 
    #
    def isPropertySet(key: CDPL.Base.LookupKey) -> bool: pass

    ##
    # \brief 
    #
    def clearProperties() -> None: pass

    ##
    # \brief 
    # \param cntnr 
    #
    def addProperties(cntnr: CDPL.Base.PropertyContainer) -> None: pass

    ##
    # \brief 
    # \param cntnr 
    #
    def copyProperties(cntnr: CDPL.Base.PropertyContainer) -> None: pass

    ##
    # \brief 
    # \param cntnr 
    #
    def swap(cntnr: CDPL.Base.PropertyContainer) -> None: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += mol</tt>.
    # \param mol Specifies the second addend.
    # \return The updated \e %Molecule instance \a self.
    #
    def __iadd__(mol: Molecule) -> Molecule: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += molgraph</tt>.
    # \param molgraph Specifies the second addend.
    # \return The updated \e %Molecule instance \a self.
    #
    def __iadd__(molgraph: MolecularGraph) -> Molecule: pass

    ##
    # \brief Returns the result of the membership test operation <tt>atom in self</tt>.
    # \param atom The value to test for membership.
    # \return The result of the membership test operation.
    #
    def __contains__(atom: Atom) -> bool: pass

    ##
    # \brief Returns the result of the membership test operation <tt>bond in self</tt>.
    # \param bond The value to test for membership.
    # \return The result of the membership test operation.
    #
    def __contains__(bond: Bond) -> bool: pass

    ##
    # \brief Returns the result of the membership test operation <tt>key in self</tt>.
    # \param key The value to test for membership.
    # \return The result of the membership test operation.
    #
    def __contains__(key: CDPL.Base.LookupKey) -> bool: pass

    ##
    # \brief 
    # \param key 
    # \return 
    #
    def __getitem__(key: CDPL.Base.LookupKey) -> CDPL.Base.Variant: pass

    ##
    # \brief 
    # \param key 
    # \param value 
    #
    def __setitem__(key: CDPL.Base.LookupKey, value: CDPL.Base.Variant) -> None: pass

    ##
    # \brief 
    # \param key 
    # \return 
    #
    def __delitem__(key: CDPL.Base.LookupKey) -> bool: pass

    ##
    # \brief 
    # \return 
    #
    def __len__() -> int: pass

    ##
    # \brief 
    #
    atoms = property(getAtoms)

    ##
    # \brief 
    #
    bonds = property(getBonds)
