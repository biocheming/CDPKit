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
class HydrophobicInteractionScore(FeatureDistanceScore):

    ##
    # \brief 
    #
    DEF_MIN_DISTANCE = 2.0

    ##
    # \brief 
    #
    DEF_MAX_DISTANCE = 6.0

    ##
    # \brief Initializes the \e %HydrophobicInteractionScore instance.
    # \param self The \e %HydrophobicInteractionScore instance to initialize.
    # \param score 
    #
    def __init__(self: object, score: HydrophobicInteractionScore) -> None: pass

    ##
    # \brief Initializes the \e %HydrophobicInteractionScore instance.
    # \param self The \e %HydrophobicInteractionScore instance to initialize.
    # \param min_dist 
    # \param max_dist 
    #
    def __init__(self: object, min_dist: float = 2.0, max_dist: float = 6.0) -> None: pass