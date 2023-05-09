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
class Vector4UL(Boost.Python.instance):

    ##
    # \brief Initializes the \e %Vector4UL instance.
    #
    def __init__() -> None: pass

    ##
    # \brief Initializes the \e %Vector4UL instance.
    # \param v 
    #
    def __init__(v: Vector4UL) -> None: pass

    ##
    # \brief Initializes the \e %Vector4UL instance.
    # \param v 
    #
    def __init__(v: int) -> None: pass

    ##
    # \brief Initializes the \e %Vector4UL instance.
    # \param e 
    #
    def __init__(e: ConstFVectorExpression) -> None: pass

    ##
    # \brief Initializes the \e %Vector4UL instance.
    # \param e 
    #
    def __init__(e: ConstDVectorExpression) -> None: pass

    ##
    # \brief Initializes the \e %Vector4UL instance.
    # \param e 
    #
    def __init__(e: ConstLVectorExpression) -> None: pass

    ##
    # \brief Initializes the \e %Vector4UL instance.
    # \param e 
    #
    def __init__(e: ConstULVectorExpression) -> None: pass

    ##
    # \brief Initializes the \e %Vector4UL instance.
    # \param a 
    #
    def __init__(a: object) -> None: pass

    ##
    # \brief 
    # \param v 
    #
    def clear(v: int = 0) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    #
    # Different Python \e %Vector4UL instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %Vector4UL instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID() -> int: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstFVectorExpression instance \a e.
    # \param e The \e %ConstFVectorExpression instance to copy.
    # \return \a self
    #
    def assign(e: ConstFVectorExpression) -> Vector4UL: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstDVectorExpression instance \a e.
    # \param e The \e %ConstDVectorExpression instance to copy.
    # \return \a self
    #
    def assign(e: ConstDVectorExpression) -> Vector4UL: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstLVectorExpression instance \a e.
    # \param e The \e %ConstLVectorExpression instance to copy.
    # \return \a self
    #
    def assign(e: ConstLVectorExpression) -> Vector4UL: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstULVectorExpression instance \a e.
    # \param e The \e %ConstULVectorExpression instance to copy.
    # \return \a self
    #
    def assign(e: ConstULVectorExpression) -> Vector4UL: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %Vector4UL instance \a v.
    # \param v The \e %Vector4UL instance to copy.
    # \return \a self
    #
    def assign(v: Vector4UL) -> Vector4UL: pass

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
    # \param v 
    #
    def swap(v: Vector4UL) -> None: pass

    ##
    # \brief 
    # \param i 
    # \param v 
    #
    def setElement(i: int, v: int) -> None: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == v</tt>.
    # \param v The \e %Vector4UL instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __eq__(v: Vector4UL) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == e</tt>.
    # \param e The \e %ConstULVectorExpression instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __eq__(e: ConstULVectorExpression) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != v</tt>.
    # \param v The \e %Vector4UL instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __ne__(v: Vector4UL) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != e</tt>.
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
    # \brief Returns a string representation of the \e %Vector4UL instance.
    # \return The generated string representation.
    #
    def __str__() -> str: pass

    ##
    # \brief 
    # \return 
    #
    def __pos__() -> Vector4UL: pass

    ##
    # \brief 
    # \return 
    #
    def __neg__() -> ConstULVectorExpression: pass

    ##
    # \brief Returns the result of the addition operation <tt>self + e</tt>.
    # \param e Specifies the second addend.
    # \return A \e %ConstULVectorExpression instance holding the result of the addition.
    #
    def __add__(e: ConstULVectorExpression) -> ConstULVectorExpression: pass

    ##
    # \brief Returns the result of the subtraction operation <tt>self - e</tt>.
    # \param e Specifies the subtrahend.
    # \return A \e %Vector4UL instance holding the result of the subtraction.
    #
    def __sub__(e: ConstULVectorExpression) -> ConstULVectorExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * t</tt>.
    # \param t Specifies the multiplier.
    # \return A \e %ConstULVectorExpression instance holding the result of the multiplication.
    #
    def __mul__(t: int) -> ConstULVectorExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * e</tt>.
    # \param e Specifies the multiplier.
    # \return A \e %ConstULVectorExpression instance holding the result of the multiplication.
    #
    def __mul__(e: ConstULMatrixExpression) -> ConstULVectorExpression: pass

    ##
    # \brief Returns the result of the division operation <tt>self / t</tt>.
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
    # \brief Performs the in-place addition operation <tt>self += v</tt>.
    # \param v Specifies the second addend.
    # \return The updated \e %Vector4UL instance \a self.
    #
    def __iadd__(v: Vector4UL) -> Vector4UL: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param e Specifies the second addend.
    # \return The updated \e %Vector4UL instance \a self.
    #
    def __iadd__(e: ConstULVectorExpression) -> Vector4UL: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= v</tt>.
    # \param v Specifies the subtrahend.
    # \return The updated \e %Vector4UL instance \a self.
    #
    def __isub__(v: Vector4UL) -> Vector4UL: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param e Specifies the subtrahend.
    # \return The updated \e %Vector4UL instance \a self.
    #
    def __isub__(e: ConstULVectorExpression) -> Vector4UL: pass

    ##
    # \brief Performs the in-place multiplication operation <tt>self *= t</tt>.
    # \param t Specifies the multiplier.
    # \return The updated \e %Vector4UL instance \a self.
    #
    def __imul__(t: int) -> Vector4UL: pass

    ##
    # \brief Performs the in-place division operation <tt>self /= t</tt>.
    # \param t Specifies the divisor.
    # \return The updated \e %Vector4UL instance \a self.
    #
    def __idiv__(t: int) -> Vector4UL: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __itruediv__(t: int) -> Vector4UL: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief 
    #
    size = property(getSize)
