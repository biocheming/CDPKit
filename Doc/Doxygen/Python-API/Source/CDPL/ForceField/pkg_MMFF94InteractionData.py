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
class MMFF94InteractionData(Boost.Python.instance):

    ##
    # \brief Initializes the \e %MMFF94InteractionData instance.
    # \param self The \e %MMFF94InteractionData instance to initialize.
    #
    def __init__(self: object) -> None: pass

    ##
    # \brief Initializes the \e %MMFF94InteractionData instance.
    # \param self The \e %MMFF94InteractionData instance to initialize.
    # \param ia_data 
    #
    def __init__(self: object, ia_data: MMFF94InteractionData) -> None: pass

    ##
    # \brief 
    # \param self The \e %MMFF94InteractionData instance this method is called upon.
    #
    def clear(self: MMFF94InteractionData) -> None: pass

    ##
    # \brief 
    # \param self The \e %MMFF94InteractionData instance this method is called upon.
    # \return 
    #
    def getBondStretchingInteractions(self: MMFF94InteractionData) -> MMFF94BondStretchingInteractionData: pass

    ##
    # \brief 
    # \param self The \e %MMFF94InteractionData instance this method is called upon.
    # \return 
    #
    def getAngleBendingInteractions(self: MMFF94InteractionData) -> MMFF94AngleBendingInteractionData: pass

    ##
    # \brief 
    # \param self The \e %MMFF94InteractionData instance this method is called upon.
    # \return 
    #
    def getStretchBendInteractions(self: MMFF94InteractionData) -> MMFF94StretchBendInteractionData: pass

    ##
    # \brief 
    # \param self The \e %MMFF94InteractionData instance this method is called upon.
    # \return 
    #
    def getOutOfPlaneBendingInteractions(self: MMFF94InteractionData) -> MMFF94OutOfPlaneBendingInteractionData: pass

    ##
    # \brief 
    # \param self The \e %MMFF94InteractionData instance this method is called upon.
    # \return 
    #
    def getTorsionInteractions(self: MMFF94InteractionData) -> MMFF94TorsionInteractionData: pass

    ##
    # \brief 
    # \param self The \e %MMFF94InteractionData instance this method is called upon.
    # \return 
    #
    def getElectrostaticInteractions(self: MMFF94InteractionData) -> MMFF94ElectrostaticInteractionData: pass

    ##
    # \brief 
    # \param self The \e %MMFF94InteractionData instance this method is called upon.
    # \return 
    #
    def getVanDerWaalsInteractions(self: MMFF94InteractionData) -> MMFF94VanDerWaalsInteractionData: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %MMFF94InteractionData instance \a ia_data.
    # \param self The \e %MMFF94InteractionData instance this method is called upon.
    # \param ia_data The \e %MMFF94InteractionData instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: MMFF94InteractionData, ia_data: MMFF94InteractionData) -> MMFF94InteractionData: pass

    ##
    # \brief 
    # \param self The \e %MMFF94InteractionData instance this method is called upon.
    # \param ia_data 
    #
    def swap(self: MMFF94InteractionData, ia_data: MMFF94InteractionData) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %MMFF94InteractionData instance this method is called upon.
    #
    # Different Python \e %MMFF94InteractionData instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %MMFF94InteractionData instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: MMFF94InteractionData) -> int: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief 
    #
    bondStretchingInteractions = property(getBondStretchingInteractions)

    ##
    # \brief 
    #
    angleBendingInteractions = property(getAngleBendingInteractions)

    ##
    # \brief 
    #
    stretchBendInteractions = property(getStretchBendInteractions)

    ##
    # \brief 
    #
    outOfPlaneBendingInteractions = property(getOutOfPlaneBendingInteractions)

    ##
    # \brief 
    #
    torsionInteractions = property(getTorsionInteractions)

    ##
    # \brief 
    #
    electrostaticInteractions = property(getElectrostaticInteractions)

    ##
    # \brief 
    #
    vanDerWaalsInteractions = property(getVanDerWaalsInteractions)