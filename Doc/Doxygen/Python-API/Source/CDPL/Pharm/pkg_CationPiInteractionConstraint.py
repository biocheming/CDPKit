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
class CationPiInteractionConstraint(Boost.Python.instance):

    ##
    # \brief 
    #
    DEF_MIN_DISTANCE = 3.5

    ##
    # \brief 
    #
    DEF_MAX_DISTANCE = 5.5

    ##
    # \brief 
    #
    DEF_MAX_ANGLE = 45.0

    ##
    # \brief Initializes the \e %CationPiInteractionConstraint instance.
    # \param constr 
    #
    def __init__(constr: CationPiInteractionConstraint) -> None: pass

    ##
    # \brief Initializes the \e %CationPiInteractionConstraint instance.
    # \param aro_cat 
    # \param min_dist 
    # \param max_dist 
    # \param max_ang 
    #
    def __init__(aro_cat: bool, min_dist: float = 3.5, max_dist: float = 5.5, max_ang: float = 45.0) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    #
    # Different Python \e %CationPiInteractionConstraint instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %CationPiInteractionConstraint instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID() -> int: pass

    ##
    # \brief 
    # \return 
    #
    def getMinDistance() -> float: pass

    ##
    # \brief 
    # \return 
    #
    def getMaxDistance() -> float: pass

    ##
    # \brief 
    # \return 
    #
    def getMaxAngle() -> float: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %CationPiInteractionConstraint instance \a constr.
    # \param constr The \e %CationPiInteractionConstraint instance to copy.
    # \return \a self
    #
    def assign(constr: CationPiInteractionConstraint) -> CationPiInteractionConstraint: pass

    ##
    # \brief 
    # \param ftr1 
    # \param ftr2 
    # \return 
    #
    def __call__(ftr1: Feature, ftr2: Feature) -> bool: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief 
    #
    minDistance = property(getMinDistance)

    ##
    # \brief 
    #
    maxDistance = property(getMaxDistance)

    ##
    # \brief 
    #
    maxAngle = property(getMaxAngle)
