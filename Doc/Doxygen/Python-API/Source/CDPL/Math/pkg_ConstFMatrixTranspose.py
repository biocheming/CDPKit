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
class ConstFMatrixTranspose(Boost.Python.instance):

    ##
    # \brief Initializes the \e %ConstFMatrixTranspose instance.
    # \param self The \e %ConstFMatrixTranspose instance to initialize.
    # \param mt 
    #
    def __init__(self: object, mt: ConstFMatrixTranspose) -> None: pass

    ##
    # \brief Initializes the \e %ConstFMatrixTranspose instance.
    # \param self The \e %ConstFMatrixTranspose instance to initialize.
    # \param e 
    #
    def __init__(self: object, e: ConstFMatrixExpression) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    #
    # Different Python \e %ConstFMatrixTranspose instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %ConstFMatrixTranspose instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: ConstFMatrixTranspose) -> int: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \return 
    #
    def getSize1(self: ConstFMatrixTranspose) -> int: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \return 
    #
    def getSize2(self: ConstFMatrixTranspose) -> int: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \return 
    #
    def isEmpty(self: ConstFMatrixTranspose) -> bool: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \param i 
    # \param j 
    # \return 
    #
    def getElement(self: ConstFMatrixTranspose, i: int, j: int) -> float: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \return 
    #
    def toArray(self: ConstFMatrixTranspose) -> object: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \return 
    #
    def getData(self: ConstFMatrixTranspose) -> ConstFMatrixExpression: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \param i 
    # \param j 
    # \return 
    #
    def __call__(self: ConstFMatrixTranspose, i: int, j: int) -> float: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \param ij 
    # \return 
    #
    def __getitem__(self: ConstFMatrixTranspose, ij: tuple) -> float: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \return 
    #
    def __len__(self: ConstFMatrixTranspose) -> int: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == mt</tt>.
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \param mt The \e %ConstFMatrixTranspose instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __eq__(self: ConstFMatrixTranspose, mt: ConstFMatrixTranspose) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == e</tt>.
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \param e The \e %ConstFMatrixTranspose instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __eq__(self: ConstFMatrixTranspose, e: ConstFMatrixExpression) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != mt</tt>.
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \param mt The \e %ConstFMatrixTranspose instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __ne__(self: ConstFMatrixTranspose, mt: ConstFMatrixTranspose) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != e</tt>.
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \param e The \e %ConstFMatrixTranspose instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __ne__(self: ConstFMatrixTranspose, e: ConstFMatrixExpression) -> bool: pass

    ##
    # \brief Returns a string representation of the \e %ConstFMatrixTranspose instance.
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \return The generated string representation.
    #
    def __str__(self: ConstFMatrixTranspose) -> str: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \return 
    #
    def __pos__(self: ConstFMatrixTranspose) -> ConstFMatrixTranspose: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \return 
    #
    def __neg__(self: object) -> ConstFMatrixExpression: pass

    ##
    # \brief Returns the result of the addition operation <tt>self + e</tt>.
    # \param self The \e %ConstFMatrixTranspose instance representing the first addend.
    # \param e Specifies the second addend.
    # \return A \e %ConstFMatrixTranspose instance holding the result of the addition.
    #
    def __add__(self: object, e: ConstFMatrixExpression) -> ConstFMatrixExpression: pass

    ##
    # \brief Returns the result of the subtraction operation <tt>self - e</tt>.
    # \param self The \e %ConstFMatrixTranspose instance acting as minuend.
    # \param e Specifies the subtrahend.
    # \return A \e %ConstFMatrixTranspose instance holding the result of the subtraction.
    #
    def __sub__(self: object, e: ConstFMatrixExpression) -> ConstFMatrixExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * t</tt>.
    # \param self The \e %ConstFMatrixTranspose instance acting as multiplicand.
    # \param t Specifies the multiplier.
    # \return A \e %ConstFMatrixTranspose instance holding the result of the multiplication.
    #
    def __mul__(self: object, t: float) -> ConstFMatrixExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * e</tt>.
    # \param self The \e %ConstFMatrixTranspose instance acting as multiplicand.
    # \param e Specifies the multiplier.
    # \return A \e %ConstFMatrixTranspose instance holding the result of the multiplication.
    #
    def __mul__(self: object, e: ConstFMatrixExpression) -> ConstFMatrixExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * e</tt>.
    # \param self The \e %ConstFMatrixTranspose instance acting as multiplicand.
    # \param e Specifies the multiplier.
    # \return A \e %ConstFMatrixTranspose instance holding the result of the multiplication.
    #
    def __mul__(self: object, e: ConstFVectorExpression) -> ConstFVectorExpression: pass

    ##
    # \brief Returns the result of the division operation <tt>self / t</tt>.
    # \param self The \e %ConstFMatrixTranspose instance acting as dividend.
    # \param t Specifies the divisor.
    # \return A \e %ConstFMatrixTranspose instance holding the result of the division.
    #
    def __div__(self: object, t: float) -> ConstFMatrixExpression: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \param t 
    # \return 
    #
    def __truediv__(self: object, t: float) -> ConstFMatrixExpression: pass

    ##
    # \brief 
    # \param self The \e %ConstFMatrixTranspose instance this method is called upon.
    # \param t 
    # \return 
    #
    def __rmul__(self: object, t: float) -> ConstFMatrixExpression: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief 
    #
    size1 = property(getSize1)

    ##
    # \brief 
    #
    size2 = property(getSize2)

    ##
    # \brief 
    #
    data = property(getData)
