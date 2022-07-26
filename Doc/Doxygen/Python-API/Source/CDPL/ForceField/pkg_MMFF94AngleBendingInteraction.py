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
class MMFF94AngleBendingInteraction(Boost.Python.instance):

    ##
    # \brief Initializes the \e %MMFF94AngleBendingInteraction instance.
    # \param self The \e %MMFF94AngleBendingInteraction instance to initialize.
    # \param iactn 
    #
    def __init__(self: object, iactn: MMFF94AngleBendingInteraction) -> None: pass

    ##
    # \brief Initializes the \e %MMFF94AngleBendingInteraction instance.
    # \param self The \e %MMFF94AngleBendingInteraction instance to initialize.
    # \param term_atom1_idx 
    # \param ctr_atom_idx 
    # \param term_atom2_idx 
    # \param angle_type_idx 
    # \param linear 
    # \param force_const 
    # \param ref_angle 
    #
    def __init__(self: object, term_atom1_idx: int, ctr_atom_idx: int, term_atom2_idx: int, angle_type_idx: int, linear: bool, force_const: float, ref_angle: float) -> None: pass

    ##
    # \brief 
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    # \return 
    #
    def getTerminalAtom1Index(self: MMFF94AngleBendingInteraction) -> int: pass

    ##
    # \brief 
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    # \return 
    #
    def getTerminalAtom2Index(self: MMFF94AngleBendingInteraction) -> int: pass

    ##
    # \brief 
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    # \return 
    #
    def getCenterAtomIndex(self: MMFF94AngleBendingInteraction) -> int: pass

    ##
    # \brief 
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    # \return 
    #
    def getAtom1Index(self: MMFF94AngleBendingInteraction) -> int: pass

    ##
    # \brief 
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    # \return 
    #
    def getAtom2Index(self: MMFF94AngleBendingInteraction) -> int: pass

    ##
    # \brief 
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    # \return 
    #
    def getAtom3Index(self: MMFF94AngleBendingInteraction) -> int: pass

    ##
    # \brief 
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    # \return 
    #
    def getAngleTypeIndex(self: MMFF94AngleBendingInteraction) -> int: pass

    ##
    # \brief 
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    # \return 
    #
    def isLinearAngle(self: MMFF94AngleBendingInteraction) -> bool: pass

    ##
    # \brief 
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    # \return 
    #
    def getForceConstant(self: MMFF94AngleBendingInteraction) -> float: pass

    ##
    # \brief 
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    # \return 
    #
    def getReferenceAngle(self: MMFF94AngleBendingInteraction) -> float: pass

    ##
    # \brief 
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    # \param angle 
    #
    def setReferenceAngle(self: MMFF94AngleBendingInteraction, angle: float) -> None: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %MMFF94AngleBendingInteraction instance \a iactn.
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    # \param iactn The \e %MMFF94AngleBendingInteraction instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: MMFF94AngleBendingInteraction, iactn: MMFF94AngleBendingInteraction) -> MMFF94AngleBendingInteraction: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %MMFF94AngleBendingInteraction instance this method is called upon.
    #
    # Different Python \e %MMFF94AngleBendingInteraction instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %MMFF94AngleBendingInteraction instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: MMFF94AngleBendingInteraction) -> int: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief FIXME!
    #
    termAtom1Index = property(getTermAtom1Index)

    ##
    # \brief FIXME!
    #
    termAtom2Index = property(getTermAtom2Index)

    ##
    # \brief FIXME!
    #
    ctrAtomIndex = property(getCtrAtomIndex)

    ##
    # \brief 
    #
    atom1Index = property(getAtom1Index)

    ##
    # \brief 
    #
    atom2Index = property(getAtom2Index)

    ##
    # \brief 
    #
    atom3Index = property(getAtom3Index)

    ##
    # \brief 
    #
    angleTypeIndex = property(getAngleTypeIndex)

    ##
    # \brief FIXME!
    #
    linear = property(getLinear)

    ##
    # \brief 
    #
    forceConstant = property(getForceConstant)

    ##
    # \brief 
    #
    referenceAngle = property(getReferenceAngle, setReferenceAngle)
