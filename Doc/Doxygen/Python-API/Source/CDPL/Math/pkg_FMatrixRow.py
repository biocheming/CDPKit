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
class FMatrixRow(Boost.Python.instance):

    ##
    # \brief Initializes the \e %FMatrixRow instance.
    # \param self The \e %FMatrixRow instance to initialize.
    # \param mr 
    # 
    def __init__(mr: FMatrixRow) -> None: pass

    ##
    # \brief Initializes the \e %FMatrixRow instance.
    # \param self The \e %FMatrixRow instance to initialize.
    # \param e 
    # \param i 
    # 
    def __init__(e: FMatrixExpression, i: int) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getIndex() -> int: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %FMatrixRow instance this method is called upon.
    # 
    # Different Python \e %FMatrixRow instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %FMatrixRow instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    # 
    # \return The numeric ID of the internally referenced C++ class instance.
    # 
    def getObjectID() -> int: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstFVectorExpression instance \a e.
    # \param self The \e %FMatrixRow instance this method is called upon.
    # \param e The \e %ConstFVectorExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstFVectorExpression) -> FMatrixRow: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstDVectorExpression instance \a e.
    # \param self The \e %FMatrixRow instance this method is called upon.
    # \param e The \e %ConstDVectorExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstDVectorExpression) -> FMatrixRow: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstLVectorExpression instance \a e.
    # \param self The \e %FMatrixRow instance this method is called upon.
    # \param e The \e %ConstLVectorExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstLVectorExpression) -> FMatrixRow: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstULVectorExpression instance \a e.
    # \param self The \e %FMatrixRow instance this method is called upon.
    # \param e The \e %ConstULVectorExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstULVectorExpression) -> FMatrixRow: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %FMatrixRow instance \a r.
    # \param self The \e %FMatrixRow instance this method is called upon.
    # \param r The \e %FMatrixRow instance to copy.
    # \return \a self
    # 
    def assign(r: FMatrixRow) -> FMatrixRow: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %object instance \a a.
    # \param self The \e %FMatrixRow instance this method is called upon.
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
    def getElement(i: int) -> float: pass

    ##
    # \brief 
    # \return 
    #
    def toArray() -> object: pass

    ##
    # \brief 
    # \param r 
    #
    def swap(r: FMatrixRow) -> None: pass

    ##
    # \brief 
    # \param i 
    # \param v 
    #
    def setElement(i: int, v: float) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getData() -> FMatrixExpression: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == r</tt>.
    # \param self The \e %FMatrixRow instance this method is called upon.
    # \param r The \e %FMatrixRow instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __eq__(r: FMatrixRow) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == e</tt>.
    # \param self The \e %FMatrixRow instance this method is called upon.
    # \param e The \e %ConstFVectorExpression instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __eq__(e: ConstFVectorExpression) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != r</tt>.
    # \param self The \e %FMatrixRow instance this method is called upon.
    # \param r The \e %FMatrixRow instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __ne__(r: FMatrixRow) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != e</tt>.
    # \param self The \e %FMatrixRow instance this method is called upon.
    # \param e The \e %ConstFVectorExpression instance to be compared with.
    # \return The result of the comparison operation.
    # 
    def __ne__(e: ConstFVectorExpression) -> bool: pass

    ##
    # \brief 
    # \param i 
    # \return 
    #
    def __call__(i: int) -> float: pass

    ##
    # \brief 
    # \param i 
    # \return 
    #
    def __getitem__(i: int) -> float: pass

    ##
    # \brief 
    # \return 
    #
    def __len__() -> int: pass

    ##
    # \brief Returns a string representation of the \e %FMatrixRow instance.
    # \param self The \e %FMatrixRow instance this method is called upon.
    # \return The generated string representation.
    # 
    def __str__() -> str: pass

    ##
    # \brief 
    # \return 
    #
    def __pos__() -> FMatrixRow: pass

    ##
    # \brief 
    # \return 
    #
    def __neg__() -> ConstFVectorExpression: pass

    ##
    # \brief Returns the result of the addition operation <tt>self + e</tt>.
    # \param self The \e %FMatrixRow instance representing the first addend.
    # \param e Specifies the second addend.
    # \return A \e %ConstFVectorExpression instance holding the result of the addition.
    # 
    def __add__(e: ConstFVectorExpression) -> ConstFVectorExpression: pass

    ##
    # \brief Returns the result of the subtraction operation <tt>self - e</tt>.
    # \param self The \e %FMatrixRow instance acting as minuend.
    # \param e Specifies the subtrahend.
    # \return A \e %FMatrixRow instance holding the result of the subtraction.
    # 
    def __sub__(e: ConstFVectorExpression) -> ConstFVectorExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * t</tt>.
    # \param self The \e %FMatrixRow instance acting as multiplicand.
    # \param t Specifies the multiplier.
    # \return A \e %ConstFVectorExpression instance holding the result of the multiplication.
    # 
    def __mul__(t: float) -> ConstFVectorExpression: pass

    ##
    # \brief Returns the result of the multiplication operation <tt>self * e</tt>.
    # \param self The \e %FMatrixRow instance acting as multiplicand.
    # \param e Specifies the multiplier.
    # \return A \e %ConstFVectorExpression instance holding the result of the multiplication.
    # 
    def __mul__(e: ConstFMatrixExpression) -> ConstFVectorExpression: pass

    ##
    # \brief Returns the result of the division operation <tt>self / t</tt>.
    # \param self The \e %FMatrixRow instance acting as dividend.
    # \param t Specifies the divisor.
    # \return A \e %ConstFVectorExpression instance holding the result of the division.
    # 
    def __div__(t: float) -> ConstFVectorExpression: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __truediv__(t: float) -> ConstFVectorExpression: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __rmul__(t: float) -> ConstFVectorExpression: pass

    ##
    # \brief 
    # \param i 
    # \param v 
    #
    def __setitem__(i: int, v: float) -> None: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += r</tt>.
    # \param self The \e %FMatrixRow instance acting as in-place addend.
    # \param r Specifies the second addend.
    # \return The updated \e %FMatrixRow instance \a self.
    # 
    def __iadd__(r: FMatrixRow) -> FMatrixRow: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param self The \e %FMatrixRow instance acting as in-place addend.
    # \param e Specifies the second addend.
    # \return The updated \e %FMatrixRow instance \a self.
    # 
    def __iadd__(e: ConstFVectorExpression) -> FMatrixRow: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= r</tt>.
    # \param self The \e %FMatrixRow instance acting as in-place minuend.
    # \param r Specifies the subtrahend.
    # \return The updated \e %FMatrixRow instance \a self.
    # 
    def __isub__(r: FMatrixRow) -> FMatrixRow: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param self The \e %FMatrixRow instance acting as in-place minuend.
    # \param e Specifies the subtrahend.
    # \return The updated \e %FMatrixRow instance \a self.
    # 
    def __isub__(e: ConstFVectorExpression) -> FMatrixRow: pass

    ##
    # \brief Performs the in-place multiplication operation <tt>self *= t</tt>.
    # \param self The \e %FMatrixRow instance acting as in-place multiplicand.
    # \param t Specifies the multiplier.
    # \return The updated \e %FMatrixRow instance \a self.
    # 
    def __imul__(t: float) -> FMatrixRow: pass

    ##
    # \brief Performs the in-place division operation <tt>self /= t</tt>.
    # \param self The \e %FMatrixRow instance acting as in-place dividend.
    # \param t Specifies the divisor.
    # \return The updated \e %FMatrixRow instance \a self.
    # 
    def __idiv__(t: float) -> FMatrixRow: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __itruediv__(t: float) -> FMatrixRow: pass

    objectID = property(getObjectID)

    size = property(getSize)

    data = property(getData)

    index = property(getIndex)
