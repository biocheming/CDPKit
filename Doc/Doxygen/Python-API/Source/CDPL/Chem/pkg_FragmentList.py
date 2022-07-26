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
class FragmentList(Boost.Python.instance):

    ##
    # \brief Initializes the \e %FragmentList instance.
    # \param self The \e %FragmentList instance to initialize.
    #
    def __init__(self: object) -> None: pass

    ##
    # \brief Initializes the \e %FragmentList instance.
    # \param self The \e %FragmentList instance to initialize.
    # \param list 
    #
    def __init__(self: object, list: FragmentList) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %FragmentList instance this method is called upon.
    #
    # Different Python \e %FragmentList instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %FragmentList instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: FragmentList) -> int: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \return 
    #
    def getSize(self: FragmentList) -> int: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \return 
    #
    def isEmpty(self: FragmentList) -> bool: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param num_elem 
    # \param value 
    #
    def resize(self: FragmentList, num_elem: int, value: Fragment) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param num_elem 
    #
    def reserve(self: FragmentList, num_elem: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \return 
    #
    def getCapacity(self: FragmentList) -> int: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    #
    def clear(self: FragmentList) -> None: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %FragmentList instance \a array.
    # \param self The \e %FragmentList instance this method is called upon.
    # \param array The \e %FragmentList instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: FragmentList, array: FragmentList) -> FragmentList: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %FragmentList instance \a num_elem.
    # \param self The \e %FragmentList instance this method is called upon.
    # \param num_elem The \e %FragmentList instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: FragmentList, num_elem: int, value: Fragment) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param value 
    #
    def addElement(self: FragmentList, value: Fragment) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param values 
    #
    def addElements(self: FragmentList, values: FragmentList) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param idx 
    # \param value 
    #
    def insertElement(self: FragmentList, idx: int, value: Fragment) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param idx 
    # \param num_elem 
    # \param value 
    #
    def insertElements(self: FragmentList, idx: int, num_elem: int, value: Fragment) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param index 
    # \param values 
    #
    def insertElements(self: FragmentList, index: int, values: FragmentList) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    #
    def popLastElement(self: FragmentList) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param idx 
    #
    def removeElement(self: FragmentList, idx: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param begin_idx 
    # \param end_idx 
    #
    def removeElements(self: FragmentList, begin_idx: int, end_idx: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \return 
    #
    def getFirstElement(self: FragmentList) -> Fragment: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \return 
    #
    def getLastElement(self: FragmentList) -> Fragment: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param idx 
    # \return 
    #
    def getElement(self: FragmentList, idx: int) -> Fragment: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param idx 
    # \param value 
    #
    def setElement(self: FragmentList, idx: int, value: Fragment) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param idx 
    #
    def __delitem__(self: FragmentList, idx: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param idx 
    # \return 
    #
    def __getitem__(self: FragmentList, idx: int) -> Fragment: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \return 
    #
    def __len__(self: FragmentList) -> int: pass

    ##
    # \brief 
    # \param self The \e %FragmentList instance this method is called upon.
    # \param index 
    # \param value 
    #
    def __setitem__(self: FragmentList, index: int, value: Fragment) -> None: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == list</tt>.
    # \param self The \e %FragmentList instance this method is called upon.
    # \param list The \e %FragmentList instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __eq__(self: FragmentList, list: object) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != list</tt>.
    # \param self The \e %FragmentList instance this method is called upon.
    # \param list The \e %FragmentList instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __ne__(self: FragmentList, list: object) -> bool: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief 
    #
    size = property(getSize)