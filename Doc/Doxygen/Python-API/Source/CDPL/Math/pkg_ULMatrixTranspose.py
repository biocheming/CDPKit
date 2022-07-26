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
class ULMatrixTranspose(Boost.Python.instance):

    ##
    # \brief Initializes the \e %ULMatrixTranspose instance.
    # \param self The \e %ULMatrixTranspose instance to initialize.
    # \param mt 
    #
    def __init__(self: object, mt: ULMatrixTranspose) -> None: pass

    ##
    # \brief Initializes the \e %ULMatrixTranspose instance.
    # \param self The \e %ULMatrixTranspose instance to initialize.
    # \param e 
    #
    def __init__(self: object, e: ULMatrixExpression) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    #
    # Different Python \e %ULMatrixTranspose instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %ULMatrixTranspose instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: ULMatrixTranspose) -> int: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ULMatrixTranspose instance \a e.
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param e The \e %ULMatrixTranspose instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: ULMatrixTranspose, e: ConstFMatrixExpression) -> ULMatrixTranspose: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ULMatrixTranspose instance \a e.
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param e The \e %ULMatrixTranspose instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: ULMatrixTranspose, e: ConstDMatrixExpression) -> ULMatrixTranspose: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ULMatrixTranspose instance \a e.
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param e The \e %ULMatrixTranspose instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: ULMatrixTranspose, e: ConstLMatrixExpression) -> ULMatrixTranspose: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ULMatrixTranspose instance \a e.
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param e The \e %ULMatrixTranspose instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: ULMatrixTranspose, e: ConstULMatrixExpression) -> ULMatrixTranspose: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ULMatrixTranspose instance \a mt.
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param mt The \e %ULMatrixTranspose instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: ULMatrixTranspose, mt: ULMatrixTranspose) -> ULMatrixTranspose: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ULMatrixTranspose instance \a a.
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param a The \e %ULMatrixTranspose instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: ULMatrixTranspose, a: object) -> None: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \return 
    #
    def getSize1(self: ULMatrixTranspose) -> int: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \return 
    #
    def getSize2(self: ULMatrixTranspose) -> int: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \return 
    #
    def isEmpty(self: ULMatrixTranspose) -> bool: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param i 
    # \param j 
    # \return 
    #
    def getElement(self: ULMatrixTranspose, i: int, j: int) -> int: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \return 
    #
    def toArray(self: ULMatrixTranspose) -> object: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param mt 
    #
    def swap(self: ULMatrixTranspose, mt: ULMatrixTranspose) -> None: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param i 
    # \param j 
    # \param v 
    #
    def setElement(self: ULMatrixTranspose, i: int, j: int, v: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \return 
    #
    def getData(self: ULMatrixTranspose) -> ULMatrixExpression: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param i 
    # \param j 
    # \return 
    #
    def __call__(self: ULMatrixTranspose, i: int, j: int) -> int: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param ij 
    # \return 
    #
    def __getitem__(self: ULMatrixTranspose, ij: tuple) -> int: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \return 
    #
    def __len__(self: ULMatrixTranspose) -> int: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == mt</tt>.
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param mt The \e %ULMatrixTranspose instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __eq__(self: ULMatrixTranspose, mt: ULMatrixTranspose) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == e</tt>.
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param e The \e %ULMatrixTranspose instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __eq__(self: ULMatrixTranspose, e: ConstULMatrixExpression) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != mt</tt>.
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param mt The \e %ULMatrixTranspose instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __ne__(self: ULMatrixTranspose, mt: ULMatrixTranspose) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != e</tt>.
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param e The \e %ULMatrixTranspose instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __ne__(self: ULMatrixTranspose, e: ConstULMatrixExpression) -> bool: pass

    ##
    # \brief Returns a string representation of the \e %ULMatrixTranspose instance.
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \return The generated string representation.
    #
    def __str__(self: ULMatrixTranspose) -> str: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \return 
    #
    def __pos__(self: ULMatrixTranspose) -> ULMatrixTranspose: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \return 
    #
    def __neg__(self: object) -> ConstULMatrixExpression: pass

    ##
    # \brief Returns the result of the addition operation <tt>self + e</tt>.
    # \param self The \e %ULMatrixTranspose instance representing the first addend.
    # \param e Specifies the second addend.
    # \return A \e %ULMatrixTranspose instance holding the result of the addition.
    #
    def __add__(self: object, e: ConstULMatrixExpression) -> ConstULMatrixExpression: pass

    ##
    # \brief Returns the result of the subtraction operation <tt>self - e</tt>.
    # \param self The \e %ULMatrixTranspose instance acting as minuend.
    # \param e Specifies the subtrahend.
    # \return A \e %ULMatrixTranspose instance holding the result of the subtraction.
    #
    def __sub__(self: object, e: ConstULMatrixExpression) -> ConstULMatrixExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * t</tt>.
    # \param self The \e %ULMatrixTranspose instance acting as multiplicand.
    # \param t Specifies the multiplier.
    # \return A \e %ULMatrixTranspose instance holding the result of the multiplication.
    #
    def __mul__(self: object, t: int) -> ConstULMatrixExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * e</tt>.
    # \param self The \e %ULMatrixTranspose instance acting as multiplicand.
    # \param e Specifies the multiplier.
    # \return A \e %ULMatrixTranspose instance holding the result of the multiplication.
    #
    def __mul__(self: object, e: ConstULMatrixExpression) -> ConstULMatrixExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * e</tt>.
    # \param self The \e %ULMatrixTranspose instance acting as multiplicand.
    # \param e Specifies the multiplier.
    # \return A \e %ULMatrixTranspose instance holding the result of the multiplication.
    #
    def __mul__(self: object, e: ConstULVectorExpression) -> ConstULVectorExpression: pass

    ##
    # \brief Returns the result of the division operation <tt>self / t</tt>.
    # \param self The \e %ULMatrixTranspose instance acting as dividend.
    # \param t Specifies the divisor.
    # \return A \e %ULMatrixTranspose instance holding the result of the division.
    #
    def __div__(self: object, t: int) -> ConstULMatrixExpression: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param t 
    # \return 
    #
    def __truediv__(self: object, t: int) -> ConstULMatrixExpression: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param t 
    # \return 
    #
    def __rmul__(self: object, t: int) -> ConstULMatrixExpression: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param ij 
    # \param v 
    #
    def __setitem__(self: ULMatrixTranspose, ij: tuple, v: int) -> None: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += mt</tt>.
    # \param self The \e %ULMatrixTranspose instance acting as in-place addend.
    # \param mt Specifies the second addend.
    # \return The updated \e %ULMatrixTranspose instance \a self.
    #
    def __iadd__(self: ULMatrixTranspose, mt: ULMatrixTranspose) -> ULMatrixTranspose: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param self The \e %ULMatrixTranspose instance acting as in-place addend.
    # \param e Specifies the second addend.
    # \return The updated \e %ULMatrixTranspose instance \a self.
    #
    def __iadd__(self: ULMatrixTranspose, e: ConstULMatrixExpression) -> ULMatrixTranspose: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= mt</tt>.
    # \param self The \e %ULMatrixTranspose instance acting as in-place minuend.
    # \param mt Specifies the subtrahend.
    # \return The updated \e %ULMatrixTranspose instance \a self.
    #
    def __isub__(self: ULMatrixTranspose, mt: ULMatrixTranspose) -> ULMatrixTranspose: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param self The \e %ULMatrixTranspose instance acting as in-place minuend.
    # \param e Specifies the subtrahend.
    # \return The updated \e %ULMatrixTranspose instance \a self.
    #
    def __isub__(self: ULMatrixTranspose, e: ConstULMatrixExpression) -> ULMatrixTranspose: pass

    ##
    # \brief Performs the in-place multiplication operation <tt>self *= t</tt>.
    # \param self The \e %ULMatrixTranspose instance acting as in-place multiplicand.
    # \param t Specifies the multiplier.
    # \return The updated \e %ULMatrixTranspose instance \a self.
    #
    def __imul__(self: ULMatrixTranspose, t: int) -> ULMatrixTranspose: pass

    ##
    # \brief Performs the in-place division operation <tt>self /= t</tt>.
    # \param self The \e %ULMatrixTranspose instance acting as in-place dividend.
    # \param t Specifies the divisor.
    # \return The updated \e %ULMatrixTranspose instance \a self.
    #
    def __idiv__(self: ULMatrixTranspose, t: int) -> ULMatrixTranspose: pass

    ##
    # \brief 
    # \param self The \e %ULMatrixTranspose instance this method is called upon.
    # \param t 
    # \return 
    #
    def __itruediv__(self: ULMatrixTranspose, t: int) -> ULMatrixTranspose: pass

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