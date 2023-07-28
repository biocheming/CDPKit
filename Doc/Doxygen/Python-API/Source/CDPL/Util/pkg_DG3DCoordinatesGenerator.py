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
class DG3DCoordinatesGenerator(Boost.Python.instance):

    ##
    # \brief 
    #
    class VolumeConstraintList(Boost.Python.instance):

        ##
        # \brief 
        # \return 
        #
        def __len__() -> int: pass

        ##
        # \brief 
        # \param idx 
        # \return 
        #
        def __getitem__(idx: int) -> VolumeConstraint: pass

        ##
        # \brief 
        # \param idx 
        #
        def __delitem__(idx: int) -> None: pass

    ##
    # \brief 
    #
    class VolumeConstraint(Boost.Python.instance):

        ##
        # \brief Initializes the \e %VolumeConstraint instance.
        # \param self The \e %VolumeConstraint instance to initialize.
        # \param pt1_idx 
        # \param pt2_idx 
        # \param pt3_idx 
        # \param pt4_idx 
        # \param lb 
        # \param ub 
        # 
        def __init__(pt1_idx: int, pt2_idx: int, pt3_idx: int, pt4_idx: int, lb: float, ub: float) -> None: pass

        ##
        # \brief Initializes the \e %VolumeConstraint instance.
        # \param self The \e %VolumeConstraint instance to initialize.
        # \param constr 
        # 
        def __init__(constr: VolumeConstraint) -> None: pass

        ##
        # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
        # \param self The \e %VolumeConstraint instance this method is called upon.
        # 
        # Different Python \e %VolumeConstraint instances may reference the same underlying C++ class instance. The commonly used Python expression
        # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %VolumeConstraint instances \e a and \e b reference different C++ objects. 
        # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
        # <tt>a.getObjectID() != b.getObjectID()</tt>.
        # 
        # \return The numeric ID of the internally referenced C++ class instance.
        # 
        def getObjectID() -> int: pass

        ##
        # \brief 
        # \param constr 
        # \return 
        #
        def assign(constr: VolumeConstraint) -> VolumeConstraint: pass

        ##
        # \brief 
        # \return 
        #
        def getPoint1Index() -> int: pass

        ##
        # \brief 
        # \return 
        #
        def getPoint2Index() -> int: pass

        ##
        # \brief 
        # \return 
        #
        def getPoint3Index() -> int: pass

        ##
        # \brief 
        # \return 
        #
        def getPoint4Index() -> int: pass

        ##
        # \brief 
        # \return 
        #
        def getLowerBound() -> float: pass

        ##
        # \brief 
        # \return 
        #
        def getUpperBound() -> float: pass

        objectID = property(getObjectID)

        point1Index = property(getPoint1Index)

        point2Index = property(getPoint2Index)

        point3Index = property(getPoint3Index)

        point4Index = property(getPoint4Index)

        lowerBound = property(getLowerBound)

        upperBound = property(getUpperBound)

    ##
    # \brief 
    #
    class DistanceConstraintList(Boost.Python.instance):

        ##
        # \brief 
        # \return 
        #
        def __len__() -> int: pass

        ##
        # \brief 
        # \param idx 
        # \return 
        #
        def __getitem__(idx: int) -> DistanceConstraint: pass

        ##
        # \brief 
        # \param idx 
        #
        def __delitem__(idx: int) -> None: pass

    ##
    # \brief 
    #
    class DistanceConstraint(Boost.Python.instance):

        ##
        # \brief Initializes the \e %DistanceConstraint instance.
        # \param self The \e %DistanceConstraint instance to initialize.
        # \param pt1_idx 
        # \param pt2_idx 
        # \param lb 
        # \param ub 
        # 
        def __init__(pt1_idx: int, pt2_idx: int, lb: float, ub: float) -> None: pass

        ##
        # \brief Initializes the \e %DistanceConstraint instance.
        # \param self The \e %DistanceConstraint instance to initialize.
        # \param constr 
        # 
        def __init__(constr: DistanceConstraint) -> None: pass

        ##
        # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
        # \param self The \e %DistanceConstraint instance this method is called upon.
        # 
        # Different Python \e %DistanceConstraint instances may reference the same underlying C++ class instance. The commonly used Python expression
        # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %DistanceConstraint instances \e a and \e b reference different C++ objects. 
        # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
        # <tt>a.getObjectID() != b.getObjectID()</tt>.
        # 
        # \return The numeric ID of the internally referenced C++ class instance.
        # 
        def getObjectID() -> int: pass

        ##
        # \brief 
        # \param constr 
        # \return 
        #
        def assign(constr: DistanceConstraint) -> DistanceConstraint: pass

        ##
        # \brief 
        # \return 
        #
        def getPoint1Index() -> int: pass

        ##
        # \brief 
        # \return 
        #
        def getPoint2Index() -> int: pass

        ##
        # \brief 
        # \return 
        #
        def getLowerBound() -> float: pass

        ##
        # \brief 
        # \return 
        #
        def getUpperBound() -> float: pass

        objectID = property(getObjectID)

        point1Index = property(getPoint1Index)

        point2Index = property(getPoint2Index)

        lowerBound = property(getLowerBound)

        upperBound = property(getUpperBound)

    ##
    # \brief 
    #
    COORDS_DIM = 3

    ##
    # \brief 
    #
    DEF_NUM_CYCLES = 50

    ##
    # \brief 
    #
    DEF_CYCLE_STEP_COUNT_FACTOR = 1.0

    ##
    # \brief 
    #
    DEF_START_LEARNING_RATE = 1.0

    ##
    # \brief 
    #
    DEF_LEARNING_RATE_DECREMENT = 0.019

    ##
    # \brief Initializes the \e %DG3DCoordinatesGenerator instance.
    # \param self The \e %DG3DCoordinatesGenerator instance to initialize.
    # 
    def __init__() -> None: pass

    ##
    # \brief Initializes the \e %DG3DCoordinatesGenerator instance.
    # \param self The \e %DG3DCoordinatesGenerator instance to initialize.
    # \param gen 
    # 
    def __init__(gen: DG3DCoordinatesGenerator) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %DG3DCoordinatesGenerator instance this method is called upon.
    # 
    # Different Python \e %DG3DCoordinatesGenerator instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %DG3DCoordinatesGenerator instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    # 
    # \return The numeric ID of the internally referenced C++ class instance.
    # 
    def getObjectID() -> int: pass

    ##
    # \brief 
    # \param gen 
    # \return 
    #
    def assign(gen: DG3DCoordinatesGenerator) -> DG3DCoordinatesGenerator: pass

    ##
    # \brief 
    #
    def clearDistanceConstraints() -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getNumDistanceConstraints() -> int: pass

    ##
    # \brief 
    # \param idx 
    # \return 
    #
    def getDistanceConstraint(idx: int) -> DistanceConstraint: pass

    ##
    # \brief 
    # \param pt1_idx 
    # \param pt2_idx 
    # \param lb 
    # \param ub 
    #
    def addDistanceConstraint(pt1_idx: int, pt2_idx: int, lb: float, ub: float) -> None: pass

    ##
    # \brief 
    # \param idx 
    #
    def removeDistanceConstraint(idx: int) -> None: pass

    ##
    # \brief 
    # \param num_cycles 
    #
    def setNumCycles(num_cycles: int) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getNumCycles() -> int: pass

    ##
    # \brief 
    # \param fact 
    #
    def setCycleStepCountFactor(fact: float) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getCycleStepCountFactor() -> float: pass

    ##
    # \brief 
    # \param rate 
    #
    def setStartLearningRate(rate: float) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getStartLearningRate() -> float: pass

    ##
    # \brief 
    # \param decr 
    #
    def setLearningRateDecrement(decr: float) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getLearningRateDecrement() -> float: pass

    ##
    # \brief 
    # \param seed 
    #
    def setRandomSeed(seed: int) -> None: pass

    ##
    # \brief 
    # \param num_points 
    # \param coords 
    #
    def generate(num_points: int, coords: CDPL.Math.Vector3DArray) -> None: pass

    ##
    # \brief 
    # \param coords 
    # \return 
    #
    def getDistanceError(coords: CDPL.Math.Vector3DArray) -> float: pass

    ##
    # \brief 
    #
    def clearVolumeConstraints() -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getNumVolumeConstraints() -> int: pass

    ##
    # \brief 
    # \param idx 
    # \return 
    #
    def getVolumeConstraint(idx: int) -> VolumeConstraint: pass

    ##
    # \brief 
    # \param pt1_idx 
    # \param pt2_idx 
    # \param pt3_idx 
    # \param pt4_idx 
    # \param lb 
    # \param ub 
    #
    def addVolumeConstraint(pt1_idx: int, pt2_idx: int, pt3_idx: int, pt4_idx: int, lb: float, ub: float) -> None: pass

    ##
    # \brief 
    # \param idx 
    #
    def removeVolumeConstraint(idx: int) -> None: pass

    ##
    # \brief 
    # \param coords 
    # \return 
    #
    def getVolumeError(coords: CDPL.Math.Vector3DArray) -> float: pass

    objectID = property(getObjectID)

    numCycles = property(getNumCycles, setNumCycles)

    cycleStepCountFactor = property(getCycleStepCountFactor, setCycleStepCountFactor)

    startLearningRate = property(getStartLearningRate, setStartLearningRate)

    learningRateDecrement = property(getLearningRateDecrement, setLearningRateDecrement)

    numDistanceConstraints = property(getNumDistanceConstraints)

    ##
    # \brief FIXME!
    # \brief 
    #
    distanceConstraints = property(getDistanceConstraints)

    numVolumeConstraints = property(getNumVolumeConstraints)

    ##
    # \brief FIXME!
    # \brief 
    #
    volumeConstraints = property(getVolumeConstraints)
