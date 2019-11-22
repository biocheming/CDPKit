/* -*- mode: c++; c-basic-offset: 4; tab-width: 4; indent-tabs-mode: t -*- */

/* 
 * TorsionDriverImpl.cpp 
 *
 * This file is part of the Chemical Data Processing Toolkit
 *
 * Copyright (C) 2003-2010 Thomas A. Seidel <thomas.seidel@univie.ac.at>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; see the file COPYING. If not, write to
 * the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 */


#include "StaticInit.hpp"

#include <boost/thread.hpp>

#include "FallbackTorsionLibrary.hpp"
#include "TorsionLibraryDataReader.hpp"


using namespace CDPL;


namespace
{

    const char* FALLBACK_TORSION_RULES = 
		" <library name=\"FallbackRules\">"
		"  <category name=\"GG\" atomType1=\"*\" atomType2=\"*\">"
		"   <rule pattern=\"[*,#1:1]~[CX4:2]-[n:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"3.07\"/>"
        "     <angle value=\"60.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"3.55\"/>"
        "     <angle value=\"120.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"3.12\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"3.54\"/>"
        "     <angle value=\"-60.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"3.65\"/>"
        "     <angle value=\"-120.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"3.1\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX3:2]-[n:3]~[*:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"20.00\" tolerance2=\"90.00\" score=\"15.81\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"90.00\" score=\"16.32\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX4:2]-[CX4:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-60.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"20.32\"/>"
        "     <angle value=\"60.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"20.33\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"20.6\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX3:2]-[CX3:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"30.57\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"30.57\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX3:2]-[cX3:3]~[*:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"20.00\" tolerance2=\"90.00\" score=\"13.83\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"90.00\" score=\"13.79\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*:1]~[cX3:2]-[cX3:3]~[*:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"10.00\" tolerance2=\"90.00\" score=\"7.96\"/>"
        "     <angle value=\"180.0\" tolerance1=\"10.00\" tolerance2=\"90.00\" score=\"7.93\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX4:2]-[NX4:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-60.0\" tolerance1=\"20.00\" tolerance2=\"60.00\" score=\"14.81\"/>"
        "     <angle value=\"60.0\" tolerance1=\"20.00\" tolerance2=\"60.00\" score=\"14.76\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"14.57\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX4:2]-[NX3:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"60.0\" tolerance1=\"20.00\" tolerance2=\"60.00\" score=\"6.17\"/>"
        "     <angle value=\"-60.0\" tolerance1=\"20.00\" tolerance2=\"60.00\" score=\"6.27\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"60.00\" score=\"6.01\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX3:2]-[NX3:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"30.00\" tolerance2=\"40.00\" score=\"27.02\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"40.00\" score=\"26.99\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*:1]~[cX3:2]-[NX3:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"30.00\" tolerance2=\"90.00\" score=\"13.75\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"90.00\" score=\"14.01\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX3:2]-[NX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-90.0\" tolerance1=\"30.00\" tolerance2=\"40.00\" score=\"0.1\"/>"
        "     <angle value=\"0.0\" tolerance1=\"20.00\" tolerance2=\"40.00\" score=\"40.12\"/>"
        "     <angle value=\"90.0\" tolerance1=\"30.00\" tolerance2=\"40.00\" score=\"0.13\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"40.00\" score=\"40.84\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*:1]~[cX3:2]-[NX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"20.00\" tolerance2=\"90.00\" score=\"14.13\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"90.00\" score=\"15.33\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX3:2]-[nX3:3]~[*:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"30.00\" tolerance2=\"90.00\" score=\"15.81\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"90.00\" score=\"16.32\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX4:2]-[OX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-60.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"12.91\"/>"
        "     <angle value=\"60.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"12.93\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"13.29\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX3:2]-[OX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"35.54\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"34.44\"/>"
        "     <angle value=\"60.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"0.06\"/>"
        "     <angle value=\"-60.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"0.07\"/>"
        "     <angle value=\"120.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"0.09\"/>"
        "     <angle value=\"-120.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"0.07\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*:1]~[cX3:2]-[OX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-90.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"2.43\"/>"
        "     <angle value=\"0.0\" tolerance1=\"15.00\" tolerance2=\"30.00\" score=\"20.47\"/>"
        "     <angle value=\"90.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"2.39\"/>"
        "     <angle value=\"180.0\" tolerance1=\"15.00\" tolerance2=\"30.00\" score=\"20.85\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX4:2]-[SX4:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-60.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"12.72\"/>"
        "     <angle value=\"60.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"12.77\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"12.79\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX4:2]-[SX3:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-60.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"12.55\"/>"
        "     <angle value=\"60.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"12.59\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"13.26\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX3:2]-[SX3:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-120.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"5.53\"/>"
        "     <angle value=\"-60.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"3.61\"/>"
        "     <angle value=\"60.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"4.09\"/>"
        "     <angle value=\"120.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"3.97\"/>"
        "     <angle value=\"0.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"4.09\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"5.29\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX4:2]-[SX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"60.0\" tolerance1=\"30.00\" tolerance2=\"40.00\" score=\"12.79\"/>"
        "     <angle value=\"-60.0\" tolerance1=\"30.00\" tolerance2=\"40.00\" score=\"12.79\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"40.00\" score=\"12.54\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX3:2]-[SX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"10.00\" tolerance2=\"90.00\" score=\"16.95\"/>"
        "     <angle value=\"180.0\" tolerance1=\"10.00\" tolerance2=\"90.00\" score=\"17.62\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*:1]~[cX3:2]-[SX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"10.13\"/>"
        "     <angle value=\"90.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"3.39\"/>"
        "     <angle value=\"-90.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"3.64\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"10.71\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[CX4:2]-[P:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-60.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"10.33\"/>"
        "     <angle value=\"60.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"10.33\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"10.42\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[NX4:2]-[NX4:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"60.0\" tolerance1=\"20.00\" tolerance2=\"20.00\" score=\"0.0\"/>"
        "     <angle value=\"-60.0\" tolerance1=\"20.00\" tolerance2=\"20.00\" score=\"0.0\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"20.00\" score=\"33.33\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[NX4:2]-[NX3:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-60.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"5.56\"/>"
        "     <angle value=\"60.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"5.56\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"13.89\"/>"
        "     <angle value=\"120.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"5.56\"/>"
        "     <angle value=\"-120.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"5.56\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[NX3:2]-[NX3:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"5.93\"/>"
        "     <angle value=\"90.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"3.59\"/>"
        "     <angle value=\"-90.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"3.4\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"6.89\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[NX3:2]-[NX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"25.32\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"29.6\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[NX3:2]-[nX3:3]~[*:4]\">"
		"    <torsions>"
        "     <angle value=\"-90.0\" tolerance1=\"40.00\" tolerance2=\"60.00\" score=\"4.87\"/>"
        "     <angle value=\"0.0\" tolerance1=\"10.00\" tolerance2=\"20.00\" score=\"3.62\"/>"
        "     <angle value=\"90.0\" tolerance1=\"40.00\" tolerance2=\"60.00\" score=\"4.56\"/>"
        "     <angle value=\"180.0\" tolerance1=\"10.00\" tolerance2=\"20.00\" score=\"3.54\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[NX2:2]-[NX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"180.0\" tolerance1=\"40.00\" tolerance2=\"60.00\" score=\"71.33\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*:1]~[nX3:2]-[nX3:3]~[*:4]\">"
		"    <torsions>"
        "     <angle value=\"90.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"19.32\"/>"
        "     <angle value=\"-90.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"19.32\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[NX3:2]-[OX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-110.0\" tolerance1=\"30.00\" tolerance2=\"50.00\" score=\"4.24\"/>"
        "     <angle value=\"0.0\" tolerance1=\"10.00\" tolerance2=\"20.00\" score=\"18.53\"/>"
        "     <angle value=\"110.0\" tolerance1=\"30.00\" tolerance2=\"50.00\" score=\"3.71\"/>"
        "     <angle value=\"180.0\" tolerance1=\"10.00\" tolerance2=\"20.00\" score=\"16.26\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[NX2:2]-[OX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"180.0\" tolerance1=\"15.00\" tolerance2=\"20.00\" score=\"49.69\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*:1]~[nX3:2]-[OX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-90.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"17.83\"/>"
        "     <angle value=\"90.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"17.83\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[N,n:2]-[S:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"1.93\"/>"
        "     <angle value=\"90.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"2.08\"/>"
        "     <angle value=\"-90.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"2.07\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"8.16\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[NX2:2]-[SX4:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"1.78\"/>"
        "     <angle value=\"90.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"2.08\"/>"
        "     <angle value=\"-90.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"2.69\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"45.00\" score=\"8.02\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[NX2:2]-[SX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"10.00\" tolerance2=\"20.00\" score=\"41.82\"/>"
        "     <angle value=\"180.0\" tolerance1=\"10.00\" tolerance2=\"20.00\" score=\"31.36\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[N,n:2]-[P:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"60.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"4.79\"/>"
        "     <angle value=\"-60.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"4.69\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"5.3\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[OX2:2]-[SX4:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"60.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"3.07\"/>"
        "     <angle value=\"-60.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"3.4\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"9.87\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[OX2:2]-[SX3:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"10.00\" tolerance2=\"10.00\" score=\"0.0\"/>"
        "     <angle value=\"70.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"1.28\"/>"
        "     <angle value=\"-70.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"8.97\"/>"
        "     <angle value=\"180.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"6.41\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[OX2:2]-[SX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"90.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"5.00\"/>"
        "     <angle value=\"-90.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"15.00\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[OX2:2]-[P:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-60.0\" tolerance1=\"40.00\" tolerance2=\"60.00\" score=\"4.61\"/>"
        "     <angle value=\"60.0\" tolerance1=\"40.00\" tolerance2=\"60.00\" score=\"4.54\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"7.5\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[SX4:2]-[SX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-50.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"2.56\"/>"
        "     <angle value=\"50.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"3.42\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"40.00\" score=\"5.98\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[SX3:2]-[SX3:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"0.0\" tolerance1=\"10.00\" tolerance2=\"10.00\" score=\"50.0\"/>"
        "     <angle value=\"90.0\" tolerance1=\"10.00\" tolerance2=\"10.00\" score=\"0.0\"/>"
        "     <angle value=\"-90.0\" tolerance1=\"10.00\" tolerance2=\"10.00\" score=\"0.0\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[SX2:2]-[SX2:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"90.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"17.38\"/>"
        "     <angle value=\"-90.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"20.2\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[S:2]-[P:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-120.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"0.94\"/>"
        "     <angle value=\"-60.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"5.77\"/>"
        "     <angle value=\"60.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"5.77\"/>"
        "     <angle value=\"120.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"0.81\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"30.00\" score=\"12.62\"/>"
        "     <angle value=\"0.0\" tolerance1=\"20.00\" tolerance2=\"30.00\" score=\"1.88\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[P:2]-[P:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-60.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"4.44\"/>"
        "     <angle value=\"60.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"4.81\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"14.94\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1:1]~[*^3:2]-[*^3:3]~[*,#1:4]\">"
		"    <torsions>"
        "     <angle value=\"-60.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"18.06\"/>"
        "     <angle value=\"60.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"18.06\"/>"
        "     <angle value=\"180.0\" tolerance1=\"30.00\" tolerance2=\"60.00\" score=\"18.41\"/>"
		"    </torsions>"
		"   </rule>"
		"   <rule pattern=\"[*,#1]~[*:2]-[*:3]~[*,#1:4]\">"
        "    <torsions>"
        "      <angle value=\"0.0\" tolerance1=\"0.0\" tolerance2=\"0.0\" score=\"0.0\"/>"
        "      <angle value=\"30.0\" tolerance1=\"0.0\" tolerance2=\"0.0\" score=\"0.0\"/>"
        "      <angle value=\"60.0\" tolerance1=\"0.0\" tolerance2=\"0.0\" score=\"0.0\"/>"
        "      <angle value=\"90.0\" tolerance1=\"0.0\" tolerance2=\"0.0\" score=\"0.0\"/>"
        "      <angle value=\"120.0\" tolerance1=\"0.0\" tolerance2=\"0.0\" score=\"0.0\"/>"
        "      <angle value=\"150.0\" tolerance1=\"0.0\" tolerance2=\"0.0\" score=\"0.0\"/>"
        "      <angle value=\"180.0\" tolerance1=\"0.0\" tolerance2=\"0.0\" score=\"0.0\"/>"
        "      <angle value=\"210.0\" tolerance1=\"0.0\" tolerance2=\"0.0\" score=\"0.0\"/>"
        "      <angle value=\"240.0\" tolerance1=\"0.0\" tolerance2=\"0.0\" score=\"0.0\"/>"
        "      <angle value=\"270.0\" tolerance1=\"0.0\" tolerance2=\"0.0\" score=\"0.0\"/>"
        "      <angle value=\"300.0\" tolerance1=\"0.0\" tolerance2=\"0.0\" score=\"0.0\"/>"
        "      <angle value=\"330.0\" tolerance1=\"0.0\" tolerance2=\"0.0\" score=\"0.0\"/>"
        "    </torsions>"
		"   </rule>"
		"  </category>"
		" </library>";

    boost::once_flag initFallbackTorLibFlag = BOOST_ONCE_INIT;

    ConfGen::TorsionLibrary::SharedPointer fallbackTorLib;

    void initFallbackTorLib()
    {
		fallbackTorLib.reset(new ConfGen::TorsionLibrary());

		ConfGen::TorsionLibraryDataReader().read(FALLBACK_TORSION_RULES, *fallbackTorLib);
    }
}


const ConfGen::TorsionLibrary::SharedPointer& ConfGen::getFallbackTorsionLibrary()
{
    boost::call_once(&initFallbackTorLib, initFallbackTorLibFlag);

    return fallbackTorLib;
}
