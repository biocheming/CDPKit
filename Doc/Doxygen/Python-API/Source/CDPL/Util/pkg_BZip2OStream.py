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
class BZip2OStream(CDPL.Base.OStream):

    ##
    # \brief Initializes the \e %BZip2OStream instance.
    # \param self The \e %BZip2OStream instance to initialize.
    #
    def __init__(self: object) -> None: pass

    ##
    # \brief Initializes the \e %BZip2OStream instance.
    # \param self The \e %BZip2OStream instance to initialize.
    # \param os 
    #
    def __init__(self: object, os: CDPL.Base.OStream) -> None: pass

    ##
    # \brief 
    # \param self The \e %BZip2OStream instance this method is called upon.
    #
    def flush(self: BZip2OStream) -> None: pass

    ##
    # \brief 
    # \param self The \e %BZip2OStream instance this method is called upon.
    # \param string 
    #
    def write(self: BZip2OStream, string: object) -> None: pass

    ##
    # \brief 
    # \param self The \e %BZip2OStream instance this method is called upon.
    # \param iterable 
    #
    def writelines(self: BZip2OStream, iterable: object) -> None: pass

    ##
    # \brief 
    # \param self The \e %BZip2OStream instance this method is called upon.
    # \return 
    #
    def tellw(self: BZip2OStream) -> int: pass

    ##
    # \brief 
    # \param self The \e %BZip2OStream instance this method is called upon.
    # \param offs 
    # \param whence 
    #
    def seekw(self: BZip2OStream, offs: int, whence: int = 0) -> None: pass

    ##
    # \brief 
    # \param self The \e %BZip2OStream instance this method is called upon.
    #
    def close(self: BZip2OStream) -> None: pass

    ##
    # \brief 
    # \param self The \e %BZip2OStream instance this method is called upon.
    # \param os 
    #
    def open(self: BZip2OStream, os: CDPL.Base.OStream) -> None: pass

    ##
    # \brief FIXME!
    #
    closed = property(getClosed)

    ##
    # \brief FIXME!
    #
    softspace = property(getSoftspace, setSoftspace)

    ##
    # \brief FIXME!
    #
    mode = property(getMode)

    ##
    # \brief FIXME!
    #
    modeFlags = property(getModeFlags)
