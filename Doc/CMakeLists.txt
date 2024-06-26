##
# CMakeLists.txt  
#
# This file is part of the Chemical Data Processing Toolkit
#
# Copyright (C) 2003 Thomas Seidel <thomas.seidel@univie.ac.at>
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
##

if(DOXYGEN_EXECUTABLE)
  add_subdirectory(Doxygen)
endif(DOXYGEN_EXECUTABLE)

if(SPHINX_FOUND)
  add_subdirectory(Sphinx)

  add_custom_target(doc
    ${CMAKE_COMMAND} -E rm -r -f "${CMAKE_CURRENT_BINARY_DIR}/html"
    COMMAND ${CMAKE_COMMAND} -E rename
    "${CMAKE_CURRENT_BINARY_DIR}/Sphinx/html" "${CMAKE_CURRENT_BINARY_DIR}/html"
    COMMENT "-- Generating CDPKit documentation HTML pages...")

  add_dependencies(doc sphinx-doc)
  
  if(DOXYGEN_EXECUTABLE)
    add_custom_command(TARGET doc POST_BUILD
      COMMAND ${CMAKE_COMMAND} -E rm -r
      "${CMAKE_CURRENT_BINARY_DIR}/html/cdpl_api_doc/c++_api_doc"
      COMMAND ${CMAKE_COMMAND} -E rename
      "${CMAKE_CURRENT_BINARY_DIR}/Doxygen/C++-API/html" "${CMAKE_CURRENT_BINARY_DIR}/html/cdpl_api_doc/c++_api_doc")

    add_custom_command(TARGET doc POST_BUILD
      COMMAND ${CMAKE_COMMAND} -E rm -r
      "${CMAKE_CURRENT_BINARY_DIR}/html/cdpl_api_doc/python_api_doc"
      COMMAND ${CMAKE_COMMAND} -E rename
      "${CMAKE_CURRENT_BINARY_DIR}/Doxygen/Python-API/html" "${CMAKE_CURRENT_BINARY_DIR}/html/cdpl_api_doc/python_api_doc")

    add_dependencies(doc c++-api-doc python-api-doc)
  endif(DOXYGEN_EXECUTABLE)

  install(DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/html/" DESTINATION "${CDPKIT_DOC_INSTALL_DIR}"
    COMPONENT Documentation OPTIONAL)
endif(SPHINX_FOUND)
