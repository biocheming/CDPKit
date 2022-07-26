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
class ANDBondMatchExpressionList(BondMatchExpressionList):

    ##
    # \brief Initializes the \e %ANDBondMatchExpressionList instance.
    # \param self The \e %ANDBondMatchExpressionList instance to initialize.
    #
    def __init__(self: object) -> None: pass

    ##
    # \brief Initializes the \e %ANDBondMatchExpressionList instance.
    # \param self The \e %ANDBondMatchExpressionList instance to initialize.
    # \param expr 
    #
    def __init__(self: object, expr: ANDBondMatchExpressionList) -> None: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ANDBondMatchExpressionList instance \a expr.
    # \param self The \e %ANDBondMatchExpressionList instance this method is called upon.
    # \param expr The \e %ANDBondMatchExpressionList instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: ANDBondMatchExpressionList, expr: ANDBondMatchExpressionList) -> ANDBondMatchExpressionList: pass
