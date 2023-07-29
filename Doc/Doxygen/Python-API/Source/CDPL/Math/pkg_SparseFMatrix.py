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
# \brief An unbounded sparse matrix holding floating point values of type <tt>float</tt>..
# 
class SparseFMatrix(Boost.Python.instance):

    ##
    # \brief Initializes the \e %SparseFMatrix instance.
    # 
    def __init__() -> None: pass

    ##
    # \brief Initializes the \e %SparseFMatrix instance.
    # \param m 
    # 
    def __init__(m: SparseFMatrix) -> None: pass

    ##
    # \brief Initializes the \e %SparseFMatrix instance.
    # \param m 
    # \param n 
    # 
    def __init__(m: int, n: int) -> None: pass

    ##
    # \brief Initializes the \e %SparseFMatrix instance.
    # \param e 
    # 
    def __init__(e: ConstFMatrixExpression) -> None: pass

    ##
    # \brief Initializes the \e %SparseFMatrix instance.
    # \param e 
    # 
    def __init__(e: ConstDMatrixExpression) -> None: pass

    ##
    # \brief Initializes the \e %SparseFMatrix instance.
    # \param e 
    # 
    def __init__(e: ConstLMatrixExpression) -> None: pass

    ##
    # \brief Initializes the \e %SparseFMatrix instance.
    # \param e 
    # 
    def __init__(e: ConstULMatrixExpression) -> None: pass

    ##
    # \brief Initializes the \e %SparseFMatrix instance.
    # \param a 
    # 
    def __init__(a: object) -> None: pass

    ##
    # \brief 
    # \param m 
    # \param n 
    #
    def resize(m: int, n: int) -> None: pass

    ##
    # \brief 
    #
    def clear() -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getNumElements() -> int: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # 
    # Different Python \e %SparseFMatrix instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %SparseFMatrix instances \e a and \e b reference different C++ objects. 
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
    def assign(e: ConstFMatrixExpression) -> SparseFMatrix: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstDMatrixExpression instance \a e.
    # \param e The \e %ConstDMatrixExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstDMatrixExpression) -> SparseFMatrix: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstLMatrixExpression instance \a e.
    # \param e The \e %ConstLMatrixExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstLMatrixExpression) -> SparseFMatrix: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstULMatrixExpression instance \a e.
    # \param e The \e %ConstULMatrixExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstULMatrixExpression) -> SparseFMatrix: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %SparseFMatrix instance \a m.
    # \param m The \e %SparseFMatrix instance to copy.
    # \return \a self
    # 
    def assign(m: SparseFMatrix) -> SparseFMatrix: pass

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
    def getElement(i: int, j: int) -> float: pass

    ##
    # \brief 
    # \return 
    #
    def toArray() -> object: pass

    ##
    # \brief 
    # \param m 
    #
    def swap(m: SparseFMatrix) -> None: pass

    ##
    # \brief 
    # \param i 
    # \param j 
    # \param v 
    #
    def setElement(i: int, j: int, v: float) -> None: pass

    ##
    # \brief 
    # \param i 
    # \param j 
    # \return 
    #
    def __call__(i: int, j: int) -> float: pass

    ##
    # \brief 
    # \param ij 
    # \return 
    #
    def __getitem__(ij: tuple) -> float: pass

    ##
    # \brief 
    # \return 
    #
    def __len__() -> int: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == m</tt>.
    # \param m The \e %SparseFMatrix instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __eq__(m: SparseFMatrix) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == e</tt>.
    # \param e The \e %ConstFMatrixExpression instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __eq__(e: ConstFMatrixExpression) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != m</tt>.
    # \param m The \e %SparseFMatrix instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __ne__(m: SparseFMatrix) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != e</tt>.
    # \param e The \e %ConstFMatrixExpression instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __ne__(e: ConstFMatrixExpression) -> bool: pass

    ##
    # \brief Returns a string representation of the \e %SparseFMatrix instance.
    # \return The generated string representation.
    # 
    def __str__() -> str: pass

    ##
    # \brief 
    # \return 
    #
    def __pos__() -> SparseFMatrix: pass

    ##
    # \brief 
    # \return 
    #
    def __neg__() -> ConstFMatrixExpression: pass

    ##
    # \brief Returns the result of the addition operation <tt>self + e</tt>.
    # \param e Specifies the second addend.
    # \return A \e %ConstFMatrixExpression instance holding the result of the addition.
    # 
    def __add__(e: ConstFMatrixExpression) -> ConstFMatrixExpression: pass

    ##
    # \brief Returns the result of the subtraction operation <tt>self - e</tt>.
    # \param e Specifies the subtrahend.
    # \return A \e %SparseFMatrix instance holding the result of the subtraction.
    # 
    def __sub__(e: ConstFMatrixExpression) -> ConstFMatrixExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * t</tt>.
    # \param t Specifies the multiplier.
    # \return A \e %ConstFMatrixExpression instance holding the result of the multiplication.
    # 
    def __mul__(t: float) -> ConstFMatrixExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * e</tt>.
    # \param e Specifies the multiplier.
    # \return A \e %ConstFMatrixExpression instance holding the result of the multiplication.
    # 
    def __mul__(e: ConstFMatrixExpression) -> ConstFMatrixExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * e</tt>.
    # \param e Specifies the multiplier.
    # \return A \e %ConstFVectorExpression instance holding the result of the multiplication.
    # 
    def __mul__(e: ConstFVectorExpression) -> ConstFVectorExpression: pass

    ##
    # \brief Returns the result of the division operation <tt>self / t</tt>.
    # \param t Specifies the divisor.
    # \return A \e %ConstFMatrixExpression instance holding the result of the division.
    # 
    def __div__(t: float) -> ConstFMatrixExpression: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __truediv__(t: float) -> ConstFMatrixExpression: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __rmul__(t: float) -> ConstFMatrixExpression: pass

    ##
    # \brief 
    # \param ij 
    # \param v 
    #
    def __setitem__(ij: tuple, v: float) -> None: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += m</tt>.
    # \param m Specifies the second addend.
    # \return The updated \e %SparseFMatrix instance \a self.
    # 
    def __iadd__(m: SparseFMatrix) -> SparseFMatrix: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param e Specifies the second addend.
    # \return The updated \e %SparseFMatrix instance \a self.
    # 
    def __iadd__(e: ConstFMatrixExpression) -> SparseFMatrix: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= m</tt>.
    # \param m Specifies the subtrahend.
    # \return The updated \e %SparseFMatrix instance \a self.
    # 
    def __isub__(m: SparseFMatrix) -> SparseFMatrix: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param e Specifies the subtrahend.
    # \return The updated \e %SparseFMatrix instance \a self.
    # 
    def __isub__(e: ConstFMatrixExpression) -> SparseFMatrix: pass

    ##
    # \brief Performs the in-place multiplication operation <tt>self *= t</tt>.
    # \param t Specifies the multiplier.
    # \return The updated \e %SparseFMatrix instance \a self.
    # 
    def __imul__(t: float) -> SparseFMatrix: pass

    ##
    # \brief Performs the in-place division operation <tt>self /= t</tt>.
    # \param t Specifies the divisor.
    # \return The updated \e %SparseFMatrix instance \a self.
    # 
    def __idiv__(t: float) -> SparseFMatrix: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __itruediv__(t: float) -> SparseFMatrix: pass

    objectID = property(getObjectID)

    size1 = property(getSize1)

    size2 = property(getSize2)

    numElements = property(getNumElements)
