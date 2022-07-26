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
class Slice(Boost.Python.instance):

    ##
    # \brief Initializes the \e %Slice instance.
    # \param self The \e %Slice instance to initialize.
    #
    def __init__(self: object) -> None: pass

    ##
    # \brief Initializes the \e %Slice instance.
    # \param self The \e %Slice instance to initialize.
    # \param s 
    #
    def __init__(self: object, s: ast.Slice) -> None: pass

    ##
    # \brief Initializes the \e %Slice instance.
    # \param self The \e %Slice instance to initialize.
    # \param start 
    # \param stride 
    # \param size 
    #
    def __init__(self: object, start: int, stride: int, size: int) -> None: pass

    ##
    # \brief 
    # \param self The \e %Slice instance this method is called upon.
    # \return 
    #
    def getStart(self: Slice) -> int: pass

    ##
    # \brief 
    # \param self The \e %Slice instance this method is called upon.
    # \return 
    #
    def getStride(self: Slice) -> int: pass

    ##
    # \brief 
    # \param self The \e %Slice instance this method is called upon.
    # \return 
    #
    def getSize(self: Slice) -> int: pass

    ##
    # \brief 
    # \param self The \e %Slice instance this method is called upon.
    # \return 
    #
    def isEmpty(self: Slice) -> bool: pass

    ##
    # \brief 
    # \param self The \e %Slice instance this method is called upon.
    # \param i 
    # \return 
    #
    def getIndex(self: Slice, i: int) -> int: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %Slice instance \a s.
    # \param self The \e %Slice instance this method is called upon.
    # \param s The \e %Slice instance to copy.
    # \return The assignment target \a self.
    #
    def assign(self: Slice, s: ast.Slice) -> ast.Slice: pass

    ##
    # \brief 
    # \param self The \e %Slice instance this method is called upon.
    # \param s 
    #
    def swap(self: Slice, s: ast.Slice) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %Slice instance this method is called upon.
    #
    # Different Python \e %Slice instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %Slice instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID(self: Slice) -> int: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self == s</tt>.
    # \param self The \e %Slice instance this method is called upon.
    # \param s The \e %Slice instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __eq__(self: Slice, s: ast.Slice) -> bool: pass

    ##
    # \brief Returns the result of the comparison operation <tt>self != s</tt>.
    # \param self The \e %Slice instance this method is called upon.
    # \param s The \e %Slice instance to be compared with.
    # \return The result of the comparison operation.
    #
    def __ne__(self: Slice, s: ast.Slice) -> bool: pass

    ##
    # \brief 
    # \param self The \e %Slice instance this method is called upon.
    # \param i 
    # \return 
    #
    def __call__(self: Slice, i: int) -> int: pass

    ##
    # \brief 
    # \param self The \e %Slice instance this method is called upon.
    # \param i 
    # \return 
    #
    def __getitem__(self: Slice, i: int) -> int: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)

    ##
    # \brief 
    #
    start = property(getStart)

    ##
    # \brief 
    #
    stride = property(getStride)

    ##
    # \brief 
    #
    size = property(getSize)