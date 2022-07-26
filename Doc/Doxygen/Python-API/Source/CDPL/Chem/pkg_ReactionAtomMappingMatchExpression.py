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
class ReactionAtomMappingMatchExpression(ReactionMatchExpression):

    ##
    # \brief Initializes the \e %ReactionAtomMappingMatchExpression instance.
    # \param self The \e %ReactionAtomMappingMatchExpression instance to initialize.
    # \param expr 
    #
    def __init__(self: object, expr: ReactionAtomMappingMatchExpression) -> None: pass

    ##
    # \brief Initializes the \e %ReactionAtomMappingMatchExpression instance.
    # \param self The \e %ReactionAtomMappingMatchExpression instance to initialize.
    # \param atom_mapping 
    #
    def __init__(self: object, atom_mapping: AtomMapping) -> None: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %ReactionAtomMappingMatchExpression instance \a expr.
    # \param self The \e %ReactionAtomMappingMatchExpression instance this method is called upon.
    # \param expr The \e %ReactionAtomMappingMatchExpression instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: ReactionAtomMappingMatchExpression, expr: ReactionAtomMappingMatchExpression) -> ReactionAtomMappingMatchExpression: pass
