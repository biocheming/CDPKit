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
class InteractionConstraintConnector(Boost.Python.instance):

    ##
    # \brief Initializes the \e %InteractionConstraintConnector instance.
    # \param self The \e %InteractionConstraintConnector instance to initialize.
    # \param con 
    #
    def __init__(self: object, con: InteractionConstraintConnector) -> None: pass

    ##
    # \brief Initializes the \e %InteractionConstraintConnector instance.
    # \param self The \e %InteractionConstraintConnector instance to initialize.
    # \param and_expr 
    # \param func2 
    # \param func1 
    #
    def __init__(self: object, and_expr: bool, func2: BoolFeature2Functor, func1: BoolFeature2Functor) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %InteractionConstraintConnector instance this method is called upon.
    #
    # Different Python \e %InteractionConstraintConnector instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %InteractionConstraintConnector instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: InteractionConstraintConnector) -> int: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %InteractionConstraintConnector instance \a con.
    # \param self The \e %InteractionConstraintConnector instance this method is called upon.
    # \param con The \e %InteractionConstraintConnector instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: InteractionConstraintConnector, con: InteractionConstraintConnector) -> InteractionConstraintConnector: pass

    ##
    # \brief 
    # \param self The \e %InteractionConstraintConnector instance this method is called upon.
    # \param ftr1 
    # \param ftr2 
    # \return 
    #
    def __call__(self: InteractionConstraintConnector, ftr1: Feature, ftr2: Feature) -> bool: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)