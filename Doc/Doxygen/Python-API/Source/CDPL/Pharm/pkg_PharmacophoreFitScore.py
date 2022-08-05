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
class PharmacophoreFitScore(Boost.Python.instance):

    ##
    # \brief 
    #
    DEF_FTR_MATCH_COUNT_FACTOR = 0.8

    ##
    # \brief 
    #
    DEF_FTR_POS_MATCH_FACTOR = 0.1

    ##
    # \brief 
    #
    DEF_FTR_GEOM_MATCH_FACTOR = 0.1

    ##
    # \brief Initializes the \e %PharmacophoreFitScore instance.
    # \param score 
    #
    def __init__(score: PharmacophoreFitScore) -> None: pass

    ##
    # \brief Initializes the \e %PharmacophoreFitScore instance.
    # \param match_cnt_factor 
    # \param pos_match_factor 
    # \param geom_match_factor 
    #
    def __init__(match_cnt_factor: float = 0.8, pos_match_factor: float = 0.1, geom_match_factor: float = 0.1) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    #
    # Different Python \e %PharmacophoreFitScore instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %PharmacophoreFitScore instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID() -> int: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %PharmacophoreFitScore instance \a score.
    # \param score The \e %PharmacophoreFitScore instance to copy.
    # \return The assignment target \a self.
    #
    def assign(score: PharmacophoreFitScore) -> PharmacophoreFitScore: pass

    ##
    # \brief 
    # \param ref_ftrs 
    # \param algnd_ftrs 
    # \param xform 
    # \return 
    #
    def __call__(ref_ftrs: FeatureContainer, algnd_ftrs: FeatureContainer, xform: CDPL.Math.Matrix4D) -> float: pass

    ##
    # \brief 
    # \param ref_ftrs 
    # \param mapping 
    # \return 
    #
    def __call__(ref_ftrs: FeatureContainer, mapping: SpatialFeatureMapping) -> float: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief FIXME!
    #
    featureMatchCountFactor = property(getFeatureMatchCountFactor, setFeatureMatchCountFactor)

    ##
    # \brief FIXME!
    #
    featurePositionMatchFactor = property(getFeaturePositionMatchFactor, setFeaturePositionMatchFactor)

    ##
    # \brief FIXME!
    #
    featureGeometryMatchFactor = property(getFeatureGeometryMatchFactor, setFeatureGeometryMatchFactor)
