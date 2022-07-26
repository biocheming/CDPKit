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
class Vector2FArray(Boost.Python.instance):

    ##
    # \brief Initializes the \e %Vector2FArray instance.
    # \param self The \e %Vector2FArray instance to initialize.
    #
    def __init__(self: object) -> None: pass

    ##
    # \brief Initializes the \e %Vector2FArray instance.
    # \param self The \e %Vector2FArray instance to initialize.
    # \param array 
    #
    def __init__(self: object, array: Vector2FArray) -> None: pass

    ##
    # \brief Initializes the \e %Vector2FArray instance.
    # \param arg1 The \e %Vector2FArray instance to initialize.
    # \param a 
    #
    def __init__(arg1: object, a: object) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %Vector2FArray instance this method is called upon.
    #
    # Different Python \e %Vector2FArray instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %Vector2FArray instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: Vector2FArray) -> int: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \return 
    #
    def getSize(self: Vector2FArray) -> int: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \return 
    #
    def isEmpty(self: Vector2FArray) -> bool: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param num_elem 
    # \param value 
    #
    def resize(self: Vector2FArray, num_elem: int, value: Vector2F) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param num_elem 
    #
    def reserve(self: Vector2FArray, num_elem: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \return 
    #
    def getCapacity(self: Vector2FArray) -> int: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    #
    def clear(self: Vector2FArray) -> None: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %Vector2FArray instance \a array.
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param array The \e %Vector2FArray instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: Vector2FArray, array: Vector2FArray) -> Vector2FArray: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %Vector2FArray instance \a num_elem.
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param num_elem The \e %Vector2FArray instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: Vector2FArray, num_elem: int, value: Vector2F) -> None: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %Vector2FArray instance \a a.
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param a The \e %Vector2FArray instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: Vector2FArray, a: object) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param value 
    #
    def addElement(self: Vector2FArray, value: Vector2F) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param values 
    #
    def addElements(self: Vector2FArray, values: Vector2FArray) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param idx 
    # \param value 
    #
    def insertElement(self: Vector2FArray, idx: int, value: Vector2F) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param idx 
    # \param num_elem 
    # \param value 
    #
    def insertElements(self: Vector2FArray, idx: int, num_elem: int, value: Vector2F) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param index 
    # \param values 
    #
    def insertElements(self: Vector2FArray, index: int, values: Vector2FArray) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    #
    def popLastElement(self: Vector2FArray) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param idx 
    #
    def removeElement(self: Vector2FArray, idx: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param begin_idx 
    # \param end_idx 
    #
    def removeElements(self: Vector2FArray, begin_idx: int, end_idx: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \return 
    #
    def getFirstElement(self: Vector2FArray) -> Vector2F: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \return 
    #
    def getLastElement(self: Vector2FArray) -> Vector2F: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param idx 
    # \return 
    #
    def getElement(self: Vector2FArray, idx: int) -> Vector2F: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param idx 
    # \param value 
    #
    def setElement(self: Vector2FArray, idx: int, value: Vector2F) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param as_vec 
    # \return 
    #
    def toArray(self: Vector2FArray, as_vec: bool) -> object: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param idx 
    #
    def __delitem__(self: Vector2FArray, idx: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param idx 
    # \return 
    #
    def __getitem__(self: Vector2FArray, idx: int) -> Vector2F: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \return 
    #
    def __len__(self: Vector2FArray) -> int: pass

    ##
    # \brief 
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param index 
    # \param value 
    #
    def __setitem__(self: Vector2FArray, index: int, value: Vector2F) -> None: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == array</tt>.
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param array The \e %Vector2FArray instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __eq__(self: Vector2FArray, array: object) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != array</tt>.
    # \param self The \e %Vector2FArray instance this method is called upon.
    # \param array The \e %Vector2FArray instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __ne__(self: Vector2FArray, array: object) -> bool: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief 
    #
    size = property(getSize)
