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
# \param molgraph 
# \return 
#
def calcTPSA(molgraph: CDPL.Chem.MolecularGraph) -> float: pass

##
# \brief 
# \param molgraph 
# \return 
#
def calcXLogP(molgraph: CDPL.Chem.MolecularGraph) -> float: pass

##
# \brief 
# \param molgraph 
# \return 
#
def calcLogS(molgraph: CDPL.Chem.MolecularGraph) -> float: pass

##
# \brief 
# \param molgraph 
# \return 
#
def buildMolecularFormula(molgraph: CDPL.Chem.MolecularGraph) -> object: pass

##
# \brief 
# \param molgraph 
# \return 
#
def getRuleOfFiveScore(molgraph: CDPL.Chem.MolecularGraph) -> int: pass

##
# \brief 
# \param molgraph 
# \return 
#
def buildMassCompositionString(molgraph: CDPL.Chem.MolecularGraph) -> object: pass

##
# \brief 
# \param arg1 
# \param molgraph 
# \param hist 
#
def buildElementHistogram(arg1: CDPL.Chem.MolecularGraph, molgraph: ElementHistogram, hist: bool) -> None: pass

##
# \brief 
# \param molgraph 
# \param comp 
#
def calcMassComposition(molgraph: CDPL.Chem.MolecularGraph, comp: MassComposition) -> None: pass

##
# \brief 
# \param molgraph 
# \return 
#
def calcCyclomaticNumber(molgraph: CDPL.Chem.MolecularGraph) -> int: pass

##
# \brief 
# \param molgraph 
# \param overwrite 
#
def calcAtomHydrophobicities(molgraph: CDPL.Chem.MolecularGraph, overwrite: bool) -> None: pass

##
# \brief 
# \param molgraph 
# \return 
#
def calcMass(molgraph: CDPL.Chem.MolecularGraph) -> float: pass

##
# \brief 
# \param molgraph 
# \param inc_h_rotors 
# \param inc_amide_bonds 
# \return 
#
def getRotatableBondCount(molgraph: CDPL.Chem.MolecularGraph, inc_h_rotors: bool, inc_amide_bonds: bool) -> int: pass

##
# \brief 
# \param molgraph 
# \return 
#
def getHydrogenBondCount(molgraph: CDPL.Chem.MolecularGraph) -> int: pass

##
# \brief 
# \param molgraph 
# \return 
#
def getChainBondCount(molgraph: CDPL.Chem.MolecularGraph) -> int: pass

##
# \brief 
# \param molgraph 
# \return 
#
def getBondCount(molgraph: CDPL.Chem.MolecularGraph) -> int: pass

##
# \brief 
# \param molgraph 
# \param order 
# \param inc_aro 
# \return 
#
def getBondCount(molgraph: CDPL.Chem.MolecularGraph, order: int, inc_aro: bool = True) -> int: pass

##
# \brief 
# \param molgraph 
# \return 
#
def getChainAtomCount(molgraph: CDPL.Chem.MolecularGraph) -> int: pass

##
# \brief 
# \param molgraph 
# \return 
#
def getHydrogenDonorAtomCount(molgraph: CDPL.Chem.MolecularGraph) -> int: pass

##
# \brief 
# \param molgraph 
# \return 
#
def getHydrogenAcceptorAtomCount(molgraph: CDPL.Chem.MolecularGraph) -> int: pass

##
# \brief 
# \param molgraph 
# \return 
#
def getAtomCount(molgraph: CDPL.Chem.MolecularGraph) -> int: pass

##
# \brief 
# \param molgraph 
# \param type 
# \return 
#
def getAtomCount(molgraph: CDPL.Chem.MolecularGraph, type: int) -> int: pass

##
# \brief 
# \param molgraph 
# \return 
#
def getImplicitHydrogenCount(molgraph: CDPL.Chem.MolecularGraph) -> int: pass

##
# \brief 
# \param molgraph 
# \param flags 
# \return 
#
def getOrdinaryHydrogenCount(molgraph: CDPL.Chem.MolecularGraph, flags: int = 2147483648) -> int: pass

##
# \brief 
# \param molgraph 
# \param flags 
# \return 
#
def getExplicitOrdinaryHydrogenCount(molgraph: CDPL.Chem.MolecularGraph, flags: int = 2147483648) -> int: pass

##
# \brief 
# \param molgraph 
# \return 
#
def getComponentCount(molgraph: CDPL.Chem.MolecularGraph) -> int: pass

##
# \brief 
# \param molgraph 
# \return 
#
def calcMeanPolarizability(molgraph: CDPL.Chem.MolecularGraph) -> float: pass