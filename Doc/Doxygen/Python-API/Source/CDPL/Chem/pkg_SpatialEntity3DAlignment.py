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
class SpatialEntity3DAlignment(Boost.Python.instance):

    ##
    # \brief Initializes the \e %SpatialEntity3DAlignment instance.
    #
    def __init__() -> None: pass

    ##
    # \brief Initializes the \e %SpatialEntity3DAlignment instance.
    # \param alignment 
    #
    def __init__(alignment: SpatialEntity3DAlignment) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    #
    # Different Python \e %SpatialEntity3DAlignment instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %SpatialEntity3DAlignment instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID() -> int: pass

    ##
    # \brief 
    # \param func 
    #
    def setEntityMatchFunction(func: BoolEntity3D2Functor) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getEntityMatchFunction() -> BoolEntity3D2Functor: pass

    ##
    # \brief 
    # \param func 
    #
    def setEntityPairMatchFunction(func: BoolEntity3D4Functor) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getEntityPairMatchFunction() -> BoolEntity3D4Functor: pass

    ##
    # \brief 
    # \param func 
    #
    def setTopAlignmentConstraintFunction(func: BoolSTPairArrayFunctor) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getTopAlignmentConstraintFunction() -> BoolSTPairArrayFunctor: pass

    ##
    # \brief 
    # \param func 
    #
    def setEntity3DCoordinatesFunction(func: Vector3DEntity3DFunctor) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getEntity3DCoordinatesFunction() -> Vector3DEntity3DFunctor: pass

    ##
    # \brief 
    # \param func 
    #
    def setEntityWeightFunction(func: DoubleEntity3DFunctor) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getEntityWeightFunction() -> DoubleEntity3DFunctor: pass

    ##
    # \brief 
    # \param entity 
    # \param first_set 
    #
    def addEntity(entity: Entity3D, first_set: bool) -> None: pass

    ##
    # \brief 
    # \param first_set 
    #
    def clearEntities(first_set: bool) -> None: pass

    ##
    # \brief 
    # \param first_set 
    # \return 
    #
    def getNumEntities(first_set: bool) -> int: pass

    ##
    # \brief 
    # \param first_set 
    # \return 
    #
    def getEntities(first_set: bool) -> object: pass

    ##
    # \brief 
    # \param idx 
    # \param first_set 
    # \return 
    #
    def getEntity(idx: int, first_set: bool) -> Entity3D: pass

    ##
    # \brief 
    # \param min_size 
    #
    def setMinTopologicalMappingSize(min_size: int) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getMinTopologicalMappingSize() -> int: pass

    ##
    # \brief 
    # \param reset 
    #
    def reset() -> None: pass

    ##
    # \brief 
    # \return 
    #
    def nextAlignment() -> bool: pass

    ##
    # \brief 
    # \return 
    #
    def getTransform() -> CDPL.Math.Matrix4D: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %SpatialEntity3DAlignment instance \a alignment.
    # \param alignment The \e %SpatialEntity3DAlignment instance to copy.
    # \return The assignment target \a self.
    #
    def assign(alignment: SpatialEntity3DAlignment) -> SpatialEntity3DAlignment: pass

    ##
    # \brief 
    # \return 
    #
    def getTopologicalMapping() -> CDPL.Util.STPairArray: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief FIXME!
    #
    topMapping = property(getTopMapping)

    ##
    # \brief 
    #
    minTopologicalMappingSize = property(getMinTopologicalMappingSize, setMinTopologicalMappingSize)

    ##
    # \brief 
    #
    transform = property(getTransform)

    ##
    # \brief 
    #
    entityMatchFunction = property(getEntityMatchFunction, setEntityMatchFunction)

    ##
    # \brief 
    #
    entityPairMatchFunction = property(getEntityPairMatchFunction, setEntityPairMatchFunction)

    ##
    # \brief 
    #
    topAlignmentConstraintFunction = property(getTopAlignmentConstraintFunction, setTopAlignmentConstraintFunction)

    ##
    # \brief 
    #
    entity3DCoordinatesFunction = property(getEntity3DCoordinatesFunction, setEntity3DCoordinatesFunction)

    ##
    # \brief 
    #
    entityWeightFunction = property(getEntityWeightFunction, setEntityWeightFunction)
