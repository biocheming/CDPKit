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
class XBondingInteractionScore(Boost.Python.instance):

    ##
    # \brief 
    #
    DEF_MIN_AX_DISTANCE = 1.6

    ##
    # \brief 
    #
    DEF_MAX_AX_DISTANCE = 3.75

    ##
    # \brief 
    #
    DEF_MIN_AXB_ANGLE = 140.0

    ##
    # \brief 
    #
    DEF_ACC_ANGLE_TOLERANCE = 45.0

    ##
    # \brief Initializes the \e %XBondingInteractionScore instance.
    # \param self The \e %XBondingInteractionScore instance to initialize.
    # \param score 
    #
    def __init__(self: object, score: XBondingInteractionScore) -> None: pass

    ##
    # \brief Initializes the \e %XBondingInteractionScore instance.
    # \param self The \e %XBondingInteractionScore instance to initialize.
    # \param don_acc 
    # \param min_ax_dist 
    # \param max_ax_dist 
    # \param min_axb_ang 
    # \param acc_ang_tol 
    #
    def __init__(self: object, don_acc: bool, min_ax_dist: float = 1.6, max_ax_dist: float = 1.6, min_axb_ang: float = 140.0, acc_ang_tol: float = 45.0) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %XBondingInteractionScore instance this method is called upon.
    #
    # Different Python \e %XBondingInteractionScore instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %XBondingInteractionScore instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: XBondingInteractionScore) -> int: pass

    ##
    # \brief 
    # \param self The \e %XBondingInteractionScore instance this method is called upon.
    # \param func 
    #
    def setNormalizationFunction(self: XBondingInteractionScore, func: DoubleDoubleFunctor) -> None: pass

    ##
    # \brief 
    # \param self The \e %XBondingInteractionScore instance this method is called upon.
    # \return 
    #
    def getMinAXDistance(self: XBondingInteractionScore) -> float: pass

    ##
    # \brief 
    # \param self The \e %XBondingInteractionScore instance this method is called upon.
    # \return 
    #
    def getMaxAXDistance(self: XBondingInteractionScore) -> float: pass

    ##
    # \brief 
    # \param self The \e %XBondingInteractionScore instance this method is called upon.
    # \return 
    #
    def getMinAXBAngle(self: XBondingInteractionScore) -> float: pass

    ##
    # \brief 
    # \param self The \e %XBondingInteractionScore instance this method is called upon.
    # \return 
    #
    def getAcceptorAngleTolerance(self: XBondingInteractionScore) -> float: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %XBondingInteractionScore instance \a constr.
    # \param self The \e %XBondingInteractionScore instance this method is called upon.
    # \param constr The \e %XBondingInteractionScore instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: XBondingInteractionScore, constr: XBondingInteractionScore) -> XBondingInteractionScore: pass

    ##
    # \brief 
    # \param self The \e %XBondingInteractionScore instance this method is called upon.
    # \param ftr1 
    # \param ftr2 
    # \return 
    #
    def __call__(self: XBondingInteractionScore, ftr1: Feature, ftr2: Feature) -> float: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief 
    #
    minAXDistance = property(getMinAXDistance)

    ##
    # \brief 
    #
    maxAXDistance = property(getMaxAXDistance)

    ##
    # \brief 
    #
    minAXBAngle = property(getMinAXBAngle)

    ##
    # \brief 
    #
    acceptorAngleTolerance = property(getAcceptorAngleTolerance)
