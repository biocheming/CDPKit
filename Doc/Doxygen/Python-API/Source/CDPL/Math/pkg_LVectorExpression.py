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
class LVectorExpression(ConstLVectorExpression):

    ##
    # \brief 
    # \param e 
    #
    def swap(e: LVectorExpression) -> None: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %LVectorExpression instance \a e.
    # \param e The \e %LVectorExpression instance to copy.
    # \return \a self
    #
    def assign(e: LVectorExpression) -> LVectorExpression: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstFVectorExpression instance \a e.
    # \param e The \e %ConstFVectorExpression instance to copy.
    # \return \a self
    #
    def assign(e: ConstFVectorExpression) -> LVectorExpression: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstDVectorExpression instance \a e.
    # \param e The \e %ConstDVectorExpression instance to copy.
    # \return \a self
    #
    def assign(e: ConstDVectorExpression) -> LVectorExpression: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstLVectorExpression instance \a e.
    # \param e The \e %ConstLVectorExpression instance to copy.
    # \return \a self
    #
    def assign(e: ConstLVectorExpression) -> LVectorExpression: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ConstULVectorExpression instance \a e.
    # \param e The \e %ConstULVectorExpression instance to copy.
    # \return \a self
    #
    def assign(e: ConstULVectorExpression) -> LVectorExpression: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %object instance \a a.
    # \param a The \e %object instance to copy.
    # \return \a self
    #
    def assign(a: object) -> None: pass

    ##
    # \brief 
    # \param i 
    # \param v 
    #
    def setElement(i: int, v: int) -> None: pass

    ##
    # \brief 
    # \param i 
    # \param v 
    #
    def __setitem__(i: int, v: int) -> None: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param e Specifies the second addend.
    # \return The updated \e %LVectorExpression instance \a self.
    #
    def __iadd__(e: LVectorExpression) -> LVectorExpression: pass

    ##
    # \brief Performs the in-place addition operation <tt>self += e</tt>.
    # \param e Specifies the second addend.
    # \return The updated \e %LVectorExpression instance \a self.
    #
    def __iadd__(e: ConstLVectorExpression) -> LVectorExpression: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param e Specifies the subtrahend.
    # \return The updated \e %LVectorExpression instance \a self.
    #
    def __isub__(e: LVectorExpression) -> LVectorExpression: pass

    ##
    # \brief Performs the in-place subtraction operation <tt>self -= e</tt>.
    # \param e Specifies the subtrahend.
    # \return The updated \e %LVectorExpression instance \a self.
    #
    def __isub__(e: ConstLVectorExpression) -> LVectorExpression: pass

    ##
    # \brief Performs the in-place multiplication operation <tt>self *= t</tt>.
    # \param t Specifies the multiplier.
    # \return The updated \e %LVectorExpression instance \a self.
    #
    def __imul__(t: int) -> LVectorExpression: pass

    ##
    # \brief Performs the in-place division operation <tt>self /= t</tt>.
    # \param t Specifies the divisor.
    # \return The updated \e %LVectorExpression instance \a self.
    #
    def __idiv__(t: int) -> LVectorExpression: pass

    ##
    # \brief 
    # \param t 
    # \return 
    #
    def __itruediv__(t: int) -> LVectorExpression: pass
