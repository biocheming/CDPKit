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
class DQuaternionExpression(ConstDQuaternionExpression):

    ##
    # \brief 
    # \param e 
    #
    def swap(e: DQuaternionExpression) -> None: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %DQuaternionExpression instance \a e.
    # \param self The \e %DQuaternionExpression instance this method is called upon.
    # \param e The \e %DQuaternionExpression instance to copy.
    # \return \a self
    # 
    def assign(e: DQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstFQuaternionExpression instance \a e.
    # \param self The \e %DQuaternionExpression instance this method is called upon.
    # \param e The \e %ConstFQuaternionExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstFQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstDQuaternionExpression instance \a e.
    # \param self The \e %DQuaternionExpression instance this method is called upon.
    # \param e The \e %ConstDQuaternionExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstDQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstLQuaternionExpression instance \a e.
    # \param self The \e %DQuaternionExpression instance this method is called upon.
    # \param e The \e %ConstLQuaternionExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstLQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstULQuaternionExpression instance \a e.
    # \param self The \e %DQuaternionExpression instance this method is called upon.
    # \param e The \e %ConstULQuaternionExpression instance to copy.
    # \return \a self
    # 
    def assign(e: ConstULQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %object instance \a a.
    # \param self The \e %DQuaternionExpression instance this method is called upon.
    # \param a The \e %object instance to copy.
    # \return \a self
    # 
    def assign(a: object) -> None: pass

    ##
    # \brief 
    # \param v 
    #
    def setC1(v: float) -> None: pass

    ##
    # \brief 
    # \param v 
    #
    def setC2(v: float) -> None: pass

    ##
    # \brief 
    # \param v 
    #
    def setC3(v: float) -> None: pass

    ##
    # \brief 
    # \param v 
    #
    def setC4(v: float) -> None: pass

    ##
    # \brief 
    # \param c1 
    # \param c2 
    # \param c3 
    # \param c4 
    #
    def set(c1: float = 0.0, c2: float = 0.0, c3: float = 0.0, c4: float = 0.0) -> None: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += t</tt>.
    # \param self The \e %DQuaternionExpression instance acting as in-place addend.
    # \param t Specifies the second addend.
    # \return The updated \e %DQuaternionExpression instance \a self.
    # 
    def __iadd__(t: float) -> DQuaternionExpression: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param self The \e %DQuaternionExpression instance acting as in-place addend.
    # \param e Specifies the second addend.
    # \return The updated \e %DQuaternionExpression instance \a self.
    # 
    def __iadd__(e: DQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += q</tt>.
    # \param self The \e %DQuaternionExpression instance acting as in-place addend.
    # \param q Specifies the second addend.
    # \return The updated \e %DQuaternionExpression instance \a self.
    # 
    def __iadd__(q: ConstDQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= t</tt>.
    # \param self The \e %DQuaternionExpression instance acting as in-place minuend.
    # \param t Specifies the subtrahend.
    # \return The updated \e %DQuaternionExpression instance \a self.
    # 
    def __isub__(t: float) -> DQuaternionExpression: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param self The \e %DQuaternionExpression instance acting as in-place minuend.
    # \param e Specifies the subtrahend.
    # \return The updated \e %DQuaternionExpression instance \a self.
    # 
    def __isub__(e: DQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= q</tt>.
    # \param self The \e %DQuaternionExpression instance acting as in-place minuend.
    # \param q Specifies the subtrahend.
    # \return The updated \e %DQuaternionExpression instance \a self.
    # 
    def __isub__(q: ConstDQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief Performs the in-place multiplication operation <tt>self *= t</tt>.
    # \param self The \e %DQuaternionExpression instance acting as in-place multiplicand.
    # \param t Specifies the multiplier.
    # \return The updated \e %DQuaternionExpression instance \a self.
    # 
    def __imul__(t: float) -> DQuaternionExpression: pass

    ##
    # \brief Performs the in-place multiplication operation <tt>self *= e</tt>.
    # \param self The \e %DQuaternionExpression instance acting as in-place multiplicand.
    # \param e Specifies the multiplier.
    # \return The updated \e %DQuaternionExpression instance \a self.
    # 
    def __imul__(e: DQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief Performs the in-place multiplication operation <tt>self *= q</tt>.
    # \param self The \e %DQuaternionExpression instance acting as in-place multiplicand.
    # \param q Specifies the multiplier.
    # \return The updated \e %DQuaternionExpression instance \a self.
    # 
    def __imul__(q: ConstDQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief Performs the in-place division operation <tt>self /= t</tt>.
    # \param self The \e %DQuaternionExpression instance acting as in-place dividend.
    # \param t Specifies the divisor.
    # \return The updated \e %DQuaternionExpression instance \a self.
    # 
    def __idiv__(t: float) -> DQuaternionExpression: pass

    ##
    # \brief Performs the in-place division operation <tt>self /= e</tt>.
    # \param self The \e %DQuaternionExpression instance acting as in-place dividend.
    # \param e Specifies the divisor.
    # \return The updated \e %DQuaternionExpression instance \a self.
    # 
    def __idiv__(e: DQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief Performs the in-place division operation <tt>self /= q</tt>.
    # \param self The \e %DQuaternionExpression instance acting as in-place dividend.
    # \param q Specifies the divisor.
    # \return The updated \e %DQuaternionExpression instance \a self.
    # 
    def __idiv__(q: ConstDQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __itruediv__(t: float) -> DQuaternionExpression: pass

    ##
    # \brief 
    # \param e 
    # \return 
    #
    def __itruediv__(e: DQuaternionExpression) -> DQuaternionExpression: pass

    ##
    # \brief 
    # \param q 
    # \return 
    #
    def __itruediv__(q: ConstDQuaternionExpression) -> DQuaternionExpression: pass
