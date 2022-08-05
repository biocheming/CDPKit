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
class AtomArray3DCoordinatesFunctor(Boost.Python.instance):

    ##
    # \brief Initializes the \e %AtomArray3DCoordinatesFunctor instance.
    # \param func 
    #
    def __init__(func: AtomArray3DCoordinatesFunctor) -> None: pass

    ##
    # \brief Initializes the \e %AtomArray3DCoordinatesFunctor instance.
    # \param coords 
    # \param molgraph 
    #
    def __init__(coords: CDPL.Math.Vector3DArray, molgraph: MolecularGraph) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    #
    # Different Python \e %AtomArray3DCoordinatesFunctor instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %AtomArray3DCoordinatesFunctor instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID() -> int: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %AtomArray3DCoordinatesFunctor instance \a func.
    # \param func The \e %AtomArray3DCoordinatesFunctor instance to copy.
    # \return The assignment target \a self.
    #
    def assign(func: AtomArray3DCoordinatesFunctor) -> AtomArray3DCoordinatesFunctor: pass

    ##
    # \brief 
    # \param atom 
    # \return 
    #
    def __call__(atom: Atom) -> CDPL.Math.Vector3D: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)
