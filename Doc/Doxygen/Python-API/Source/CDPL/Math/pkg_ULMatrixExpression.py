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
class ULMatrixExpression(ConstULMatrixExpression):

    ##
    # \brief 
    # \param e 
    #
    def swap(e: ULMatrixExpression) -> None: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ULMatrixExpression) -> ULMatrixExpression: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ConstFMatrixExpression) -> ULMatrixExpression: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ConstDMatrixExpression) -> ULMatrixExpression: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ConstLMatrixExpression) -> ULMatrixExpression: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ConstULMatrixExpression) -> ULMatrixExpression: pass

    ##
    # \brief 
    # \param a 
    #
    def assign(a: object) -> None: pass

    ##
    # \brief 
    # \param i 
    # \param j 
    # \param v 
    #
    def setElement(i: int, j: int, v: int) -> None: pass

    ##
    # \brief 
    # \param ij 
    # \param v 
    #
    def __setitem__(ij: tuple, v: int) -> None: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param self The \e %ULMatrixExpression instance acting as in-place addend.
    # \param e Specifies the second addend.
    # \return The updated \e %ULMatrixExpression instance \a self.
    # 
    def __iadd__(e: ULMatrixExpression) -> ULMatrixExpression: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param self The \e %ULMatrixExpression instance acting as in-place addend.
    # \param e Specifies the second addend.
    # \return The updated \e %ULMatrixExpression instance \a self.
    # 
    def __iadd__(e: ConstULMatrixExpression) -> ULMatrixExpression: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param self The \e %ULMatrixExpression instance acting as in-place minuend.
    # \param e Specifies the subtrahend.
    # \return The updated \e %ULMatrixExpression instance \a self.
    # 
    def __isub__(e: ULMatrixExpression) -> ULMatrixExpression: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param self The \e %ULMatrixExpression instance acting as in-place minuend.
    # \param e Specifies the subtrahend.
    # \return The updated \e %ULMatrixExpression instance \a self.
    # 
    def __isub__(e: ConstULMatrixExpression) -> ULMatrixExpression: pass

    ##
    # \brief Performs the in-place multiplication operation <tt>self *= t</tt>.
    # \param self The \e %ULMatrixExpression instance acting as in-place multiplicand.
    # \param t Specifies the multiplier.
    # \return The updated \e %ULMatrixExpression instance \a self.
    # 
    def __imul__(t: int) -> ULMatrixExpression: pass

    ##
    # \brief Performs the in-place division operation <tt>self /= t</tt>.
    # \param self The \e %ULMatrixExpression instance acting as in-place dividend.
    # \param t Specifies the divisor.
    # \return The updated \e %ULMatrixExpression instance \a self.
    # 
    def __idiv__(t: int) -> ULMatrixExpression: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __itruediv__(t: int) -> ULMatrixExpression: pass
