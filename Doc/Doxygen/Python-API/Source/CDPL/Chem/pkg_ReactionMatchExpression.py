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
class ReactionMatchExpression(Boost.Python.instance):

    ##
    # \brief Initializes the \e %ReactionMatchExpression instance.
    #
    def __init__() -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    #
    # Different Python \e %ReactionMatchExpression instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %ReactionMatchExpression instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    #
    # \return The numeric ID of the internally referenced C++ class instance.
    #
    def getObjectID() -> int: pass

    ##
    # \brief 
    # \param query_rxn 
    # \param target_rxn 
    # \param aux_data 
    # \return 
    #
    def matches(query_rxn: Reaction, target_rxn: Reaction, aux_data: CDPL.Base.Variant) -> bool: pass

    ##
    # \brief 
    # \param query_rxn 
    # \param target_rxn 
    # \param mapping 
    # \param aux_data 
    # \return 
    #
    def mappingMatches(query_rxn: Reaction, target_rxn: Reaction, mapping: AtomBondMapping, aux_data: CDPL.Base.Variant) -> bool: pass

    ##
    # \brief 
    # \return 
    #
    def requiresAtomBondMapping() -> bool: pass

    ##
    # \brief 
    #
    objectID = property(getObjectID)
