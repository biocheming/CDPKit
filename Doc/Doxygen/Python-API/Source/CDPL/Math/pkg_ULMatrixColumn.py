#
# This file is part of the Chemical Data Processing Toolkit
#
# Copyright (C) Thomas Seidel <thomas.seidel@univie.ac.at>
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
class ULMatrixColumn(Boost.Python.instance):

    ##
    # \brief Initializes the \e %ULMatrixColumn instance.
    # \param self The \e %ULMatrixColumn instance to initialize.
    # \param mc 
    # 
    def __init__(mc: ULMatrixColumn) -> None: pass

    ##
    # \brief Initializes the \e %ULMatrixColumn instance.
    # \param self The \e %ULMatrixColumn instance to initialize.
    # \param e 
    # \param i 
    # 
    def __init__(e: ULMatrixExpression, i: int) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getIndex() -> int: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %ULMatrixColumn instance this method is called upon.
    # 
    # Different Python \e %ULMatrixColumn instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %ULMatrixColumn instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    # 
    # \return The numeric ID of the internally referenced C++ class instance.
    # 
    def getObjectID() -> int: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ConstFVectorExpression) -> ULMatrixColumn: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ConstDVectorExpression) -> ULMatrixColumn: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ConstLVectorExpression) -> ULMatrixColumn: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ConstULVectorExpression) -> ULMatrixColumn: pass

    ##
    # \brief 
    # \param c 
    # \return 
    #
    def assign(c: ULMatrixColumn) -> ULMatrixColumn: pass

    ##
    # \brief 
    # \param a 
    #
    def assign(a: object) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def isEmpty() -> bool: pass

    ##
    # \brief 
    # \return 
    #
    def getSize() -> int: pass

    ##
    # \brief 
    # \param i 
    # \return 
    #
    def getElement(i: int) -> int: pass

    ##
    # \brief 
    # \return 
    #
    def toArray() -> object: pass

    ##
    # \brief 
    # \param c 
    #
    def swap(c: ULMatrixColumn) -> None: pass

    ##
    # \brief 
    # \param i 
    # \param v 
    #
    def setElement(i: int, v: int) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getData() -> ULMatrixExpression: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == c</tt>.
    # \param self The \e %ULMatrixColumn instance this method is called upon.
    # \param c The \e %ULMatrixColumn instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __eq__(c: ULMatrixColumn) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == e</tt>.
    # \param self The \e %ULMatrixColumn instance this method is called upon.
    # \param e The \e %ConstULVectorExpression instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __eq__(e: ConstULVectorExpression) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != c</tt>.
    # \param self The \e %ULMatrixColumn instance this method is called upon.
    # \param c The \e %ULMatrixColumn instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __ne__(c: ULMatrixColumn) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != e</tt>.
    # \param self The \e %ULMatrixColumn instance this method is called upon.
    # \param e The \e %ConstULVectorExpression instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __ne__(e: ConstULVectorExpression) -> bool: pass

    ##
    # \brief 
    # \param i 
    # \return 
    #
    def __call__(i: int) -> int: pass

    ##
    # \brief 
    # \param i 
    # \return 
    #
    def __getitem__(i: int) -> int: pass

    ##
    # \brief 
    # \return 
    #
    def __len__() -> int: pass

    ##
    # \brief Returns a string representation of the \e %ULMatrixColumn instance.
    # \param self The \e %ULMatrixColumn instance this method is called upon.
    # \return The generated string representation.
    # 
    def __str__() -> str: pass

    ##
    # \brief 
    # \return 
    #
    def __pos__() -> ULMatrixColumn: pass

    ##
    # \brief 
    # \return 
    #
    def __neg__() -> ConstULVectorExpression: pass

    ##
    # \brief Returns the result of the addition operation <tt>self + e</tt>.
    # \param self The \e %ULMatrixColumn instance representing the first addend.
    # \param e Specifies the second addend.
    # \return A \e %ConstULVectorExpression instance holding the result of the addition.
    # 
    def __add__(e: ConstULVectorExpression) -> ConstULVectorExpression: pass

    ##
    # \brief Returns the result of the subtraction operation <tt>self - e</tt>.
    # \param self The \e %ULMatrixColumn instance acting as minuend.
    # \param e Specifies the subtrahend.
    # \return A \e %ULMatrixColumn instance holding the result of the subtraction.
    # 
    def __sub__(e: ConstULVectorExpression) -> ConstULVectorExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * t</tt>.
    # \param self The \e %ULMatrixColumn instance acting as multiplicand.
    # \param t Specifies the multiplier.
    # \return A \e %ConstULVectorExpression instance holding the result of the multiplication.
    # 
    def __mul__(t: int) -> ConstULVectorExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * e</tt>.
    # \param self The \e %ULMatrixColumn instance acting as multiplicand.
    # \param e Specifies the multiplier.
    # \return A \e %ConstULVectorExpression instance holding the result of the multiplication.
    # 
    def __mul__(e: ConstULMatrixExpression) -> ConstULVectorExpression: pass

    ##
    # \brief Returns the result of the division operation <tt>self / t</tt>.
    # \param self The \e %ULMatrixColumn instance acting as dividend.
    # \param t Specifies the divisor.
    # \return A \e %ConstULVectorExpression instance holding the result of the division.
    # 
    def __div__(t: int) -> ConstULVectorExpression: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __truediv__(t: int) -> ConstULVectorExpression: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __rmul__(t: int) -> ConstULVectorExpression: pass

    ##
    # \brief 
    # \param i 
    # \param v 
    #
    def __setitem__(i: int, v: int) -> None: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += c</tt>.
    # \param self The \e %ULMatrixColumn instance acting as in-place addend.
    # \param c Specifies the second addend.
    # \return The updated \e %ULMatrixColumn instance \a self.
    # 
    def __iadd__(c: ULMatrixColumn) -> ULMatrixColumn: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param self The \e %ULMatrixColumn instance acting as in-place addend.
    # \param e Specifies the second addend.
    # \return The updated \e %ULMatrixColumn instance \a self.
    # 
    def __iadd__(e: ConstULVectorExpression) -> ULMatrixColumn: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= c</tt>.
    # \param self The \e %ULMatrixColumn instance acting as in-place minuend.
    # \param c Specifies the subtrahend.
    # \return The updated \e %ULMatrixColumn instance \a self.
    # 
    def __isub__(c: ULMatrixColumn) -> ULMatrixColumn: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param self The \e %ULMatrixColumn instance acting as in-place minuend.
    # \param e Specifies the subtrahend.
    # \return The updated \e %ULMatrixColumn instance \a self.
    # 
    def __isub__(e: ConstULVectorExpression) -> ULMatrixColumn: pass

    ##
    # \brief Performs the in-place multiplication operation <tt>self *= t</tt>.
    # \param self The \e %ULMatrixColumn instance acting as in-place multiplicand.
    # \param t Specifies the multiplier.
    # \return The updated \e %ULMatrixColumn instance \a self.
    # 
    def __imul__(t: int) -> ULMatrixColumn: pass

    ##
    # \brief Performs the in-place division operation <tt>self /= t</tt>.
    # \param self The \e %ULMatrixColumn instance acting as in-place dividend.
    # \param t Specifies the divisor.
    # \return The updated \e %ULMatrixColumn instance \a self.
    # 
    def __idiv__(t: int) -> ULMatrixColumn: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __itruediv__(t: int) -> ULMatrixColumn: pass

    objectID = property(getObjectID)

    size = property(getSize)

    data = property(getData)

    index = property(getIndex)
