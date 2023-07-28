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
# \brief ReactionComponentGroupingMatchExpression.
# 
# \see [\ref SMARTS]
# 
class ReactionComponentGroupingMatchExpression(ReactionMatchExpression):

    ##
    # \brief Initializes the \e %ReactionComponentGroupingMatchExpression instance.
    # \param self The \e %ReactionComponentGroupingMatchExpression instance to initialize.
    # \param expr 
    # 
    def __init__(expr: ReactionComponentGroupingMatchExpression) -> None: pass

    ##
    # \brief Constructs a <tt>ReactionComponentGroupingMatchExpression</tt> instance for the specified component-level grouping.
    # 
    # \param comp_grouping Specifies the component-level grouping constraints that must be fulfilled by matching target reactions.
    # 
    def __init__(comp_grouping: FragmentList) -> None: pass

    ##
    # \brief 
    # \param expr 
    # \return 
    #
    def assign(expr: ReactionComponentGroupingMatchExpression) -> ReactionComponentGroupingMatchExpression: pass
