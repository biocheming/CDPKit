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
class DVectorExpression(ConstDVectorExpression):

    ##
    # \brief 
    # \param e 
    #
    def swap(e: DVectorExpression) -> None: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: DVectorExpression) -> DVectorExpression: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ConstFVectorExpression) -> DVectorExpression: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ConstDVectorExpression) -> DVectorExpression: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ConstLVectorExpression) -> DVectorExpression: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def assign(e: ConstULVectorExpression) -> DVectorExpression: pass

    ##
    # \brief 
    # \param a 
    #
    def assign(a: object) -> None: pass

    ##
    # \brief 
    # \param i 
    # \param v 
    #
    def setElement(i: int, v: float) -> None: pass

    ##
    # \brief 
    # \param i 
    # \param v 
    #
    def __setitem__(i: int, v: float) -> None: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param self The \e %DVectorExpression instance acting as in-place addend.
    # \param e Specifies the second addend.
    # \return The updated \e %DVectorExpression instance \a self.
    # 
    def __iadd__(e: DVectorExpression) -> DVectorExpression: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param self The \e %DVectorExpression instance acting as in-place addend.
    # \param e Specifies the second addend.
    # \return The updated \e %DVectorExpression instance \a self.
    # 
    def __iadd__(e: ConstDVectorExpression) -> DVectorExpression: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param self The \e %DVectorExpression instance acting as in-place minuend.
    # \param e Specifies the subtrahend.
    # \return The updated \e %DVectorExpression instance \a self.
    # 
    def __isub__(e: DVectorExpression) -> DVectorExpression: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param self The \e %DVectorExpression instance acting as in-place minuend.
    # \param e Specifies the subtrahend.
    # \return The updated \e %DVectorExpression instance \a self.
    # 
    def __isub__(e: ConstDVectorExpression) -> DVectorExpression: pass

    ##
    # \brief Performs the in-place multiplication operation <tt>self *= t</tt>.
    # \param self The \e %DVectorExpression instance acting as in-place multiplicand.
    # \param t Specifies the multiplier.
    # \return The updated \e %DVectorExpression instance \a self.
    # 
    def __imul__(t: float) -> DVectorExpression: pass

    ##
    # \brief Performs the in-place division operation <tt>self /= t</tt>.
    # \param self The \e %DVectorExpression instance acting as in-place dividend.
    # \param t Specifies the divisor.
    # \return The updated \e %DVectorExpression instance \a self.
    # 
    def __idiv__(t: float) -> DVectorExpression: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __itruediv__(t: float) -> DVectorExpression: pass
