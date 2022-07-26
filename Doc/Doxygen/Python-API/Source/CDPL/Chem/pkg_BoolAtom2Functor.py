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
class BoolAtom2Functor(Boost.Python.instance):

    ##
    # \brief Initializes the \e %BoolAtom2Functor instance.
    # \param self The \e %BoolAtom2Functor instance to initialize.
    #
    def __init__(self: object) -> None: pass

    ##
    # \brief Initializes the \e %BoolAtom2Functor instance.
    # \param self The \e %BoolAtom2Functor instance to initialize.
    # \param func 
    #
    def __init__(self: object, func: CDPL.ForceField.InteractionFilterFunction2) -> None: pass

    ##
    # \brief Initializes the \e %BoolAtom2Functor instance.
    # \param arg1 The \e %BoolAtom2Functor instance to initialize.
    # \param callable 
    #
    def __init__(arg1: object, callable: object) -> None: pass

    ##
    # \brief 
    # \param self The \e %BoolAtom2Functor instance this method is called upon.
    # \param arg1 
    # \param arg2 
    # \return 
    #
    def __call__(self: InteractionFilterFunction2, arg1: Atom, arg2: Atom) -> bool: pass

    ##
    # \brief 
    # \param self The \e %BoolAtom2Functor instance this method is called upon.
    # \return 
    #
    def __bool__(self: InteractionFilterFunction2) -> bool: pass

    ##
    # \brief 
    # \param self The \e %BoolAtom2Functor instance this method is called upon.
    # \return 
    #
    def __nonzero__(self: InteractionFilterFunction2) -> bool: pass
