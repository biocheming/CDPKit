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
class MMFF94HeavyToHydrogenAtomTypeMap(Boost.Python.instance):

    ##
    # \brief 
    #
    class Entry(Boost.Python.instance):

        ##
        # \brief Initializes the \e %Entry instance.
        # \param self The \e %Entry instance to initialize.
        # 
        def __init__() -> None: pass

        ##
        # \brief Initializes the \e %Entry instance.
        # \param self The \e %Entry instance to initialize.
        # \param entry 
        # 
        def __init__(entry: Entry) -> None: pass

        ##
        # \brief Initializes the \e %Entry instance.
        # \param self The \e %Entry instance to initialize.
        # \param parent_type 
        # \param h_atom_type 
        # 
        def __init__(parent_type: str, h_atom_type: str) -> None: pass

        ##
        # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
        # \param self The \e %Entry instance this method is called upon.
        # 
        # Different Python \e %Entry instances may reference the same underlying C++ class instance. The commonly used Python expression
        # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %Entry instances \e a and \e b reference different C++ objects. 
        # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
        # <tt>a.getObjectID() != b.getObjectID()</tt>.
        # 
        # \return The numeric ID of the internally referenced C++ class instance.
        # 
        def getObjectID() -> int: pass

        objectID = property(getObjectID)

        ##
        # \brief FIXME!
        # \brief 
        #
        parentAtomType = property(getParentAtomType)

        ##
        # \brief FIXME!
        # \brief 
        #
        hydrogenAtomType = property(getHydrogenAtomType)

    ##
    # \brief Initializes the \e %MMFF94HeavyToHydrogenAtomTypeMap instance.
    # \param self The \e %MMFF94HeavyToHydrogenAtomTypeMap instance to initialize.
    # 
    def __init__() -> None: pass

    ##
    # \brief Initializes the \e %MMFF94HeavyToHydrogenAtomTypeMap instance.
    # \param self The \e %MMFF94HeavyToHydrogenAtomTypeMap instance to initialize.
    # \param map 
    # 
    def __init__(map: MMFF94HeavyToHydrogenAtomTypeMap) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %MMFF94HeavyToHydrogenAtomTypeMap instance this method is called upon.
    # 
    # Different Python \e %MMFF94HeavyToHydrogenAtomTypeMap instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %MMFF94HeavyToHydrogenAtomTypeMap instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    # 
    # \return The numeric ID of the internally referenced C++ class instance.
    # 
    def getObjectID() -> int: pass

    ##
    # \brief 
    # \param parent_type 
    # \param h_atom_type 
    #
    def addEntry(parent_type: str, h_atom_type: str) -> None: pass

    ##
    # \brief 
    # \param parent_type 
    # \return 
    #
    def removeEntry(parent_type: str) -> bool: pass

    ##
    # \brief 
    # \param parent_type 
    # \return 
    #
    def getEntry(parent_type: str) -> object: pass

    ##
    # \brief 
    #
    def clear() -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getNumEntries() -> int: pass

    ##
    # \brief 
    # \return 
    #
    def getEntries() -> list: pass

    ##
    # \brief 
    # \param is 
    #
    def load(is: CDPL.Base.IStream) -> None: pass

    ##
    # \brief 
    #
    def loadDefaults() -> None: pass

    ##
    # \brief 
    # \param map 
    # \return 
    #
    def assign(map: MMFF94HeavyToHydrogenAtomTypeMap) -> MMFF94HeavyToHydrogenAtomTypeMap: pass

    ##
    # \brief 
    # \param map 
    #
    @staticmethod
    def set(map: MMFF94HeavyToHydrogenAtomTypeMap) -> None: pass

    ##
    # \brief 
    # \param  
    # \return 
    #
    @staticmethod
    def get(: ) -> MMFF94HeavyToHydrogenAtomTypeMap: pass

    objectID = property(getObjectID)

    numEntries = property(getNumEntries)

    entries = property(getEntries)
