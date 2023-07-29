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
# \brief An unbounded dense matrix holding unsigned integers of type <tt>unsigned long</tt>.
# 
class ULMatrix(Boost.Python.instance):

    ##
    # \brief Initializes the \e %ULMatrix instance.
    # 
    def __init__() -> None: pass

    ##
    # \brief Initializes the \e %ULMatrix instance.
    # \param m 
    # 
    def __init__(m: ULMatrix) -> None: pass

    ##
    # \brief Initializes the \e %ULMatrix instance.
    # \param m 
    # \param n 
    # 
    def __init__(m: int, n: int) -> None: pass

    ##
    # \brief Initializes the \e %ULMatrix instance.
    # \param m 
    # \param n 
    # \param v 
    # 
    def __init__(m: int, n: int, v: int) -> None: pass

    ##
    # \brief Initializes the \e %ULMatrix instance.
    # \param e 
    # 
    def __init__(e: ConstFMatrixExpression) -> None: pass

    ##
    # \brief Initializes the \e %ULMatrix instance.
    # \param e 
    # 
    def __init__(e: ConstDMatrixExpression) -> None: pass

    ##
    # \brief Initializes the \e %ULMatrix instance.
    # \param e 
    # 
    def __init__(e: ConstLMatrixExpression) -> None: pass

    ##
    # \brief Initializes the \e %ULMatrix instance.
    # \param e 
    # 
    def __init__(e: ConstULMatrixExpression) -> None: pass

    ##
    # \brief Initializes the \e %ULMatrix instance.
    # \param a 
    # 
    def __init__(a: object) -> None: pass

    ##
    # \brief 
    # \param m 
    # \param n 
    # \param preserve 
    # \param v 
    #
    def resize(m: int, n: int, preserve: bool = True, v: int = 0) -> None: pass

    ##
    # \brief 
    # \param v 
    #
    def clear(v: int = 0) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # 
    # Different Python \e %ULMatrix instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %ULMatrix instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    # 
    # \return The numeric ID of the internally referenced C++ class instance.
    # 
    def getObjectID() -> int: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstFMatrixExpression instance \a e.
    # \param e The \e %ConstFMatrixExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstFMatrixExpression) -> ULMatrix: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstDMatrixExpression instance \a e.
    # \param e The \e %ConstDMatrixExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstDMatrixExpression) -> ULMatrix: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstLMatrixExpression instance \a e.
    # \param e The \e %ConstLMatrixExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstLMatrixExpression) -> ULMatrix: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstULMatrixExpression instance \a e.
    # \param e The \e %ConstULMatrixExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstULMatrixExpression) -> ULMatrix: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ULMatrix instance \a m.
    # \param m The \e %ULMatrix instance to copy.
    # \return \a self
    # 
    def assign(m: ULMatrix) -> ULMatrix: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %object instance \a a.
    # \param a The \e %object instance to copy.
    # \return \a self
    # 
    def assign(a: object) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getSize1() -> int: pass

    ##
    # \brief 
    # \return 
    #
    def getSize2() -> int: pass

    ##
    # \brief 
    # \return 
    #
    def isEmpty() -> bool: pass

    ##
    # \brief 
    # \param i 
    # \param j 
    # \return 
    #
    def getElement(i: int, j: int) -> int: pass

    ##
    # \brief 
    # \return 
    #
    def toArray() -> object: pass

    ##
    # \brief 
    # \param m 
    #
    def swap(m: ULMatrix) -> None: pass

    ##
    # \brief 
    # \param i 
    # \param j 
    # \param v 
    #
    def setElement(i: int, j: int, v: int) -> None: pass

    ##
    # \brief 
    # \param i 
    # \param j 
    # \return 
    #
    def __call__(i: int, j: int) -> int: pass

    ##
    # \brief 
    # \param ij 
    # \return 
    #
    def __getitem__(ij: tuple) -> int: pass

    ##
    # \brief 
    # \return 
    #
    def __len__() -> int: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == m</tt>.
    # \param m The \e %ULMatrix instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __eq__(m: ULMatrix) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == e</tt>.
    # \param e The \e %ConstULMatrixExpression instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __eq__(e: ConstULMatrixExpression) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != m</tt>.
    # \param m The \e %ULMatrix instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __ne__(m: ULMatrix) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != e</tt>.
    # \param e The \e %ConstULMatrixExpression instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __ne__(e: ConstULMatrixExpression) -> bool: pass

    ##
    # \brief Returns a string representation of the \e %ULMatrix instance.
    # \return The generated string representation.
    # 
    def __str__() -> str: pass

    ##
    # \brief 
    # \return 
    #
    def __pos__() -> ULMatrix: pass

    ##
    # \brief 
    # \return 
    #
    def __neg__() -> ConstULMatrixExpression: pass

    ##
    # \brief Returns the result of the addition operation <tt>self + e</tt>.
    # \param e Specifies the second addend.
    # \return A \e %ConstULMatrixExpression instance holding the result of the addition.
    # 
    def __add__(e: ConstULMatrixExpression) -> ConstULMatrixExpression: pass

    ##
    # \brief Returns the result of the subtraction operation <tt>self - e</tt>.
    # \param e Specifies the subtrahend.
    # \return A \e %ULMatrix instance holding the result of the subtraction.
    # 
    def __sub__(e: ConstULMatrixExpression) -> ConstULMatrixExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * t</tt>.
    # \param t Specifies the multiplier.
    # \return A \e %ConstULMatrixExpression instance holding the result of the multiplication.
    # 
    def __mul__(t: int) -> ConstULMatrixExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * e</tt>.
    # \param e Specifies the multiplier.
    # \return A \e %ConstULMatrixExpression instance holding the result of the multiplication.
    # 
    def __mul__(e: ConstULMatrixExpression) -> ConstULMatrixExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * e</tt>.
    # \param e Specifies the multiplier.
    # \return A \e %ConstULVectorExpression instance holding the result of the multiplication.
    # 
    def __mul__(e: ConstULVectorExpression) -> ConstULVectorExpression: pass

    ##
    # \brief Returns the result of the division operation <tt>self / t</tt>.
    # \param t Specifies the divisor.
    # \return A \e %ConstULMatrixExpression instance holding the result of the division.
    # 
    def __div__(t: int) -> ConstULMatrixExpression: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __truediv__(t: int) -> ConstULMatrixExpression: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __rmul__(t: int) -> ConstULMatrixExpression: pass

    ##
    # \brief 
    # \param ij 
    # \param v 
    #
    def __setitem__(ij: tuple, v: int) -> None: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += m</tt>.
    # \param m Specifies the second addend.
    # \return The updated \e %ULMatrix instance \a self.
    # 
    def __iadd__(m: ULMatrix) -> ULMatrix: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param e Specifies the second addend.
    # \return The updated \e %ULMatrix instance \a self.
    # 
    def __iadd__(e: ConstULMatrixExpression) -> ULMatrix: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= m</tt>.
    # \param m Specifies the subtrahend.
    # \return The updated \e %ULMatrix instance \a self.
    # 
    def __isub__(m: ULMatrix) -> ULMatrix: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param e Specifies the subtrahend.
    # \return The updated \e %ULMatrix instance \a self.
    # 
    def __isub__(e: ConstULMatrixExpression) -> ULMatrix: pass

    ##
    # \brief Performs the in-place multiplication operation <tt>self *= t</tt>.
    # \param t Specifies the multiplier.
    # \return The updated \e %ULMatrix instance \a self.
    # 
    def __imul__(t: int) -> ULMatrix: pass

    ##
    # \brief Performs the in-place division operation <tt>self /= t</tt>.
    # \param t Specifies the divisor.
    # \return The updated \e %ULMatrix instance \a self.
    # 
    def __idiv__(t: int) -> ULMatrix: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __itruediv__(t: int) -> ULMatrix: pass

    objectID = property(getObjectID)

    size1 = property(getSize1)

    size2 = property(getSize2)
