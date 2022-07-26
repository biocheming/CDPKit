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
class DGConstraintGeneratorSettings(Boost.Python.instance):

    ##
    # \brief FIXME!
    #
    DEFAULT = _UNKNOWN_VALUE_

    ##
    # \brief Initializes the \e %DGConstraintGeneratorSettings instance.
    # \param self The \e %DGConstraintGeneratorSettings instance to initialize.
    #
    def __init__(self: object) -> None: pass

    ##
    # \brief Initializes the \e %DGConstraintGeneratorSettings instance.
    # \param self The \e %DGConstraintGeneratorSettings instance to initialize.
    # \param settings 
    #
    def __init__(self: object, settings: DGConstraintGeneratorSettings) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %DGConstraintGeneratorSettings instance this method is called upon.
    #
    # Different Python \e %DGConstraintGeneratorSettings instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %DGConstraintGeneratorSettings instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: DGConstraintGeneratorSettings) -> int: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %DGConstraintGeneratorSettings instance \a settings.
    # \param self The \e %DGConstraintGeneratorSettings instance this method is called upon.
    # \param settings The \e %DGConstraintGeneratorSettings instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: DGConstraintGeneratorSettings, settings: DGConstraintGeneratorSettings) -> DGConstraintGeneratorSettings: pass

    ##
    # \brief 
    # \param self The \e %DGConstraintGeneratorSettings instance this method is called upon.
    # \param exclude 
    #
    def excludeHydrogens(self: DGConstraintGeneratorSettings, exclude: bool) -> None: pass

    ##
    # \brief 
    # \param self The \e %DGConstraintGeneratorSettings instance this method is called upon.
    # \return 
    #
    def excludeHydrogens(self: DGConstraintGeneratorSettings) -> bool: pass

    ##
    # \brief 
    # \param self The \e %DGConstraintGeneratorSettings instance this method is called upon.
    # \param regard 
    #
    def regardAtomConfiguration(self: DGConstraintGeneratorSettings, regard: bool) -> None: pass

    ##
    # \brief 
    # \param self The \e %DGConstraintGeneratorSettings instance this method is called upon.
    # \return 
    #
    def regardAtomConfiguration(self: DGConstraintGeneratorSettings) -> bool: pass

    ##
    # \brief 
    # \param self The \e %DGConstraintGeneratorSettings instance this method is called upon.
    # \param regard 
    #
    def regardBondConfiguration(self: DGConstraintGeneratorSettings, regard: bool) -> None: pass

    ##
    # \brief 
    # \param self The \e %DGConstraintGeneratorSettings instance this method is called upon.
    # \return 
    #
    def regardBondConfiguration(self: DGConstraintGeneratorSettings) -> bool: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief FIXME!
    #
    exclHydrogens = property(getExclHydrogens, setExclHydrogens)

    ##
    # \brief FIXME!
    #
    regardAtomConfig = property(getRegardAtomConfig, setRegardAtomConfig)

    ##
    # \brief FIXME!
    #
    regardBondConfig = property(getRegardBondConfig, setRegardBondConfig)
