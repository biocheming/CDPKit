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
# \brief Writer for molecule data in any supported format.
# 
class MolecularGraphWriter(MolecularGraphWriterBase):

    ##
    # \brief Initializes the \e %MolecularGraphWriter instance.
    # \param self The \e %MolecularGraphWriter instance to initialize.
    # \param file_name 
    # \param mode 
    # 
    def __init__(file_name: str, mode: OpenMode = CDPL.Base.OpenMode(60)) -> None: pass

    ##
    # \brief Initializes the \e %MolecularGraphWriter instance.
    # \param self The \e %MolecularGraphWriter instance to initialize.
    # \param file_name 
    # \param fmt 
    # \param mode 
    # 
    def __init__(file_name: str, fmt: str, mode: OpenMode = CDPL.Base.OpenMode(60)) -> None: pass

    ##
    # \brief Initializes the \e %MolecularGraphWriter instance.
    # \param self The \e %MolecularGraphWriter instance to initialize.
    # \param file_name 
    # \param fmt 
    # \param mode 
    # 
    def __init__(file_name: str, fmt: CDPL.Base.DataFormat, mode: OpenMode = CDPL.Base.OpenMode12) -> None: pass

    ##
    # \brief Initializes the \e %MolecularGraphWriter instance.
    # \param self The \e %MolecularGraphWriter instance to initialize.
    # \param ios 
    # \param fmt 
    # 
    def __init__(ios: CDPL.Base.IOStream, fmt: str) -> None: pass

    ##
    # \brief Initializes the \e %MolecularGraphWriter instance.
    # \param self The \e %MolecularGraphWriter instance to initialize.
    # \param ios 
    # \param fmt 
    # 
    def __init__(ios: CDPL.Base.IOStream, fmt: CDPL.Base.DataFormat) -> None: pass

    ##
    # \brief 
    # \return 
    #
    def getDataFormat() -> CDPL.Base.DataFormat: pass

    dataFormat = property(getDataFormat)
