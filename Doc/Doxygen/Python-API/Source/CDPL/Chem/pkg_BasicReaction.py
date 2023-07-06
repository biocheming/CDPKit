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
class BasicReaction(Reaction):

    ##
    # \brief Initializes the \e %BasicReaction instance.
    #
    def __init__() -> None: pass

    ##
    # \brief Initializes the \e %BasicReaction instance.
    # \param mol 
    #
    def __init__(mol: BasicReaction) -> None: pass

    ##
    # \brief Initializes the \e %BasicReaction instance.
    # \param mol 
    #
    def __init__(mol: Reaction) -> None: pass

    ##
    # \brief 
    # \param role 
    # \return 
    #
    def addComponent(role: int) -> BasicMolecule: pass

    ##
    # \brief 
    # \param role 
    # \param mol 
    # \return 
    #
    def addComponent(role: int, mol: Molecule) -> BasicMolecule: pass

    ##
    # \brief 
    # \param rxn 
    #
    def copy(rxn: BasicReaction) -> None: pass

    ##
    # \brief 
    # \param rxn 
    #
    def copy(rxn: Reaction) -> None: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %BasicReaction instance \a rxn.
    # \param rxn The \e %BasicReaction instance to copy.
    # \return \a self
    #
    def assign(rxn: BasicReaction) -> BasicReaction: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %Reaction instance \a rxn.
    # \param rxn The \e %Reaction instance to copy.
    # \return \a self
    #
    def assign(rxn: Reaction) -> BasicReaction: pass

    ##
    # \brief 
    # \param arg1 
    # \return 
    #
    def __getstate__() -> tuple: pass
