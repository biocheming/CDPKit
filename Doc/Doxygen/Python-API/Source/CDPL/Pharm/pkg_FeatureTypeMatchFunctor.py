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
# \brief FeatureTypeMatchFunctor.
# 
class FeatureTypeMatchFunctor(Boost.Python.instance):

    ##
    # \brief Initializes the \e %FeatureTypeMatchFunctor instance.
    # \param self The \e %FeatureTypeMatchFunctor instance to initialize.
    # \param func 
    # 
    def __init__(func: FeatureTypeMatchFunctor) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %FeatureTypeMatchFunctor instance this method is called upon.
    # 
    # Different Python \e %FeatureTypeMatchFunctor instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %FeatureTypeMatchFunctor instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    # 
    # \return The numeric ID of the internally referenced C++ class instance.
    # 
    def getObjectID() -> int: pass

    ##
    # \brief Replaces the current state of \a self with a copy of the state of the \e %FeatureTypeMatchFunctor instance \a func.
    # \param self The \e %FeatureTypeMatchFunctor instance this method is called upon.
    # \param func The \e %FeatureTypeMatchFunctor instance to copy.
    # \return \a self
    # 
    def assign(func: FeatureTypeMatchFunctor) -> FeatureTypeMatchFunctor: pass

    ##
    # \brief Checks if <em>ftr1</em> and <em>ftr2</em> have the same feature type.
    # 
    # \param ftr1 The first feature.
    # \param ftr2 The second feature.
    # 
    # \return <tt>True</tt> if the feature types are equal, and <tt>False</tt> otherwise. 
    # 
    # \see Pharm.getType(const Feature&)
    # 
    def __call__(ftr1: Feature, ftr2: Feature) -> bool: pass

    objectID = property(getObjectID)
