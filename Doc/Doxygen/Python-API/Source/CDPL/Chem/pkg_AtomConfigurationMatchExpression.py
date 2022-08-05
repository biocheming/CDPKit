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
class AtomConfigurationMatchExpression(AtomMatchExpression):

    ##
    # \brief Initializes the \e %AtomConfigurationMatchExpression instance.
    # \param expr 
    #
    def __init__(expr: AtomConfigurationMatchExpression) -> None: pass

    ##
    # \brief Initializes the \e %AtomConfigurationMatchExpression instance.
    # \param query_stereo_descr 
    # \param query_atom 
    # \param not_match 
    # \param allow_part_maps 
    #
    def __init__(query_stereo_descr: StereoDescriptor, query_atom: Atom, not_match: bool, allow_part_maps: bool) -> None: pass
