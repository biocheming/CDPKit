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
class Vector2FArrayAlignmentCalculator(Boost.Python.instance):

    ##
    # \brief Initializes the \e %Vector2FArrayAlignmentCalculator instance.
    # \param self The \e %Vector2FArrayAlignmentCalculator instance to initialize.
    #
    def __init__(self: object) -> None: pass

    ##
    # \brief Initializes the \e %Vector2FArrayAlignmentCalculator instance.
    # \param self The \e %Vector2FArrayAlignmentCalculator instance to initialize.
    # \param algo 
    #
    def __init__(self: object, algo: Vector2FArrayAlignmentCalculator) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %Vector2FArrayAlignmentCalculator instance this method is called upon.
    #
    # Different Python \e %Vector2FArrayAlignmentCalculator instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %Vector2FArrayAlignmentCalculator instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: Vector2FArrayAlignmentCalculator) -> int: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %Vector2FArrayAlignmentCalculator instance \a algo.
    # \param self The \e %Vector2FArrayAlignmentCalculator instance this method is called upon.
    # \param algo The \e %Vector2FArrayAlignmentCalculator instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: Vector2FArrayAlignmentCalculator, algo: Vector2FArrayAlignmentCalculator) -> Vector2FArrayAlignmentCalculator: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArrayAlignmentCalculator instance this method is called upon.
    # \return 
    #
    def getTransform(self: Vector2FArrayAlignmentCalculator) -> FMatrix: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArrayAlignmentCalculator instance this method is called upon.
    # \param points 
    # \param ref_points 
    # \param do_center 
    # \param max_svd_iter 
    # \return 
    #
    def calculate(self: Vector2FArrayAlignmentCalculator, points: Vector2FArray, ref_points: Vector2FArray, do_center: bool = True, max_svd_iter: int = 0) -> bool: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArrayAlignmentCalculator instance this method is called upon.
    # \param points 
    # \param ref_points 
    # \param weights 
    # \param do_center 
    # \param max_svd_iter 
    # \return 
    #
    def calculate(self: Vector2FArrayAlignmentCalculator, points: Vector2FArray, ref_points: Vector2FArray, weights: ConstFVectorExpression, do_center: bool = True, max_svd_iter: int = 0) -> bool: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArrayAlignmentCalculator instance this method is called upon.
    # \param points 
    # \param ref_points 
    # \param weights 
    # \param do_center 
    # \param max_svd_iter 
    # \return 
    #
    def calculate(self: Vector2FArrayAlignmentCalculator, points: Vector2FArray, ref_points: Vector2FArray, weights: ConstDVectorExpression, do_center: bool = True, max_svd_iter: int = 0) -> bool: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief 
    #
    transform = property(getTransform)
