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
# \brief Calculates the <em>Hamming Distance</em> [\ref WHAM, \ref CITB] between the bitsets <em>bs1</em> and <em>bs2</em>.
# 
# The <em>Hamming Distance</em> \f$ D_{ab} \f$ is calculated by:
# 
# \[ D_{ab} = N_a + N_b \]
# 
# where \f$ N_a \f$ is the number of bits that are set in the first bitset but not in the second bitset and \f$ N_b \f$ is the number of bits that are set in the second bitset but not in the first one.
# 
# If the specified bitsets <em>bs1</em> and <em>bs2</em> are of different size, missing bits at the end of the smaller bitset are assumed to be zero.
# 
# \param bs1 The first bitset.
# \param bs2 The second bitset.
# 
# \return The calculated distance.
# 
def calcHammingDistance(bs1: CDPL.Util.BitSet, bs2: CDPL.Util.BitSet) -> int: pass

##
# \brief Calculates the <em>Euclidean Distance</em> [\ref CITB] between the bitsets <em>bs1</em> and <em>bs2</em>.
# 
# The <em>Euclidean Distance</em> \f$ D_{ab} \f$ is calculated by:
# 
# \[ D_{ab} = \sqrt{N_a + N_b} \]
# 
# where \f$ N_a \f$ is the number of bits that are set in the first bitset but not in the second bitset and \f$ N_b \f$ is the number of bits that are set in the second bitset but not in the first one.
# 
# If the specified bitsets <em>bs1</em> and <em>bs2</em> are of different size, missing bits at the end of the smaller bitset are assumed to be zero.
# 
# \param bs1 The first bitset.
# \param bs2 The second bitset.
# 
# \return The calculated distance.
# 
def calcEuclideanDistance(bs1: CDPL.Util.BitSet, bs2: CDPL.Util.BitSet) -> float: pass

##
# \brief Calculates the <em>Dice Similarity Measure</em> [\ref GSIM] for the given bitsets <em>bs1</em> and <em>bs2</em>.
# 
# The <em>Dice Similarity Measure</em> \f$ S_{ab} \f$ is calculated by:
# 
# \[ S_{ab} = \frac{2 * N_{ab}}{N_a + N_b + 2 * N_{ab}} \]
# 
# where \f$ N_{ab} \f$ is the number of bits that are set in both bitsets, \f$ N_a \f$ is the number of bits that are only set in the first bitset and \f$ N_b \f$ is the number of bits that are only set in the second bitset.
# 
# If the specified bitsets <em>bs1</em> and <em>bs2</em> are of different size, missing bits at the end of the smaller bitset are assumed to be zero.
# 
# \param bs1 The first bitset.
# \param bs2 The second bitset.
# 
# \return The calculated similarity measure.
# 
def calcDiceSimilarity(bs1: CDPL.Util.BitSet, bs2: CDPL.Util.BitSet) -> float: pass

##
# \brief Calculates the <em>Cosine Similarity Measure</em> [\ref WCOS] for the given bitsets <em>bs1</em> and <em>bs2</em>.
# 
# The <em>Cosine Similarity Measure</em> \f$ S_{ab} \f$ is calculated by:
# 
# \[ S_{ab} = \frac{N_{ab}}{\sqrt{N_a * N_b}} \]
# 
# where \f$ N_{ab} \f$ is the number of bits that are set in both bitsets, \f$ N_a \f$ is the number of bits that are set in the first bitset and \f$ N_b \f$ is the number of bits that are set in the second bitset.
# 
# If the specified bitsets <em>bs1</em> and <em>bs2</em> are of different size, missing bits at the end of the smaller bitset are assumed to be zero.
# 
# \param bs1 The first bitset.
# \param bs2 The second bitset.
# 
# \return The calculated similarity measure.
# 
def calcCosineSimilarity(bs1: CDPL.Util.BitSet, bs2: CDPL.Util.BitSet) -> float: pass

##
# \brief Calculates the <em>Euclidean Similarity Measure</em> [\ref GSIM] for the given bitsets <em>bs1</em> and <em>bs2</em>.
# 
# The <em>Euclidean Similarity Measure</em> \f$ S_{ab} \f$ is calculated by:
# 
# \[ S_{ab} = \sqrt{\frac{N_{ab} + N_{!ab}}{N_a + N_b + N_{ab} + N_{!ab}}} \]
# 
# where \f$ N_{ab} \f$ is the number of bits that are set in both bitsets, \f$ N_a \f$ is the number of bits that are set only in the first bitset, \f$ N_b \f$ is the number of bits that are set only in the second bitset and \f$ N_{!ab} \f$ is the number of bits that are not set in both bitsets.
# 
# If the specified bitsets <em>bs1</em> and <em>bs2</em> are of different size, missing bits at the end of the smaller bitset are assumed to be zero.
# 
# \param bs1 The first bitset.
# \param bs2 The second bitset.
# 
# \return The calculated similarity measure.
# 
def calcEuclideanSimilarity(bs1: CDPL.Util.BitSet, bs2: CDPL.Util.BitSet) -> float: pass

##
# \brief Calculates the <em>Manhattan Similarity Measure</em> [\ref GSIM] for the given bitsets <em>bs1</em> and <em>bs2</em>.
# 
# The <em>Manhattan Similarity Measure</em> \f$ S_{ab} \f$ is calculated by:
# 
# \[ S_{ab} = \frac{N_a + N_b}{N_a + N_b + N_{ab} + N_{!ab}} \]
# 
# where \f$ N_{ab} \f$ is the number of bits that are set in both bitsets, \f$ N_a \f$ is the number of bits that are set only in the first bitset, \f$ N_b \f$ is the number of bits that are set only in the second bitset and \f$ N_{!ab} \f$ is the number of bits that are not set in both bitsets.
# 
# If the specified bitsets <em>bs1</em> and <em>bs2</em> are of different size, missing bits at the end of the smaller bitset are assumed to be zero.
# 
# \param bs1 The first bitset.
# \param bs2 The second bitset.
# 
# \return The calculated similarity measure.
# 
def calcManhattanSimilarity(bs1: CDPL.Util.BitSet, bs2: CDPL.Util.BitSet) -> float: pass

##
# \brief Calculates the <em>Tanimoto Similarity Measure</em> [\ref CITB] for the given bitsets <em>bs1</em> and <em>bs2</em>.
# 
# The <em>Tanimoto Similarity Measure</em> \f$ S_{ab} \f$ is calculated by:
# 
# \[ S_{ab} = \frac{N_{ab}}{N_a + N_b - N_{ab}} \]
# 
# where \f$ N_{ab} \f$ is the number of bits that are set in both bitsets, \f$ N_a \f$ is the number of bits that are set in the first bitset and \f$ N_b \f$ is the number of bits that are set in the second bitset.
# 
# If the specified bitsets <em>bs1</em> and <em>bs2</em> are of different size, missing bits at the end of the smaller bitset are assumed to be zero.
# 
# \param bs1 The first bitset.
# \param bs2 The second bitset.
# 
# \return The calculated similarity measure.
# 
def calcTanimotoSimilarity(bs1: CDPL.Util.BitSet, bs2: CDPL.Util.BitSet) -> float: pass

##
# \brief Calculates the <em>Tversky Similarity Measure</em> [\ref GSIM] for the given bitsets <em>bs1</em> and <em>bs2</em>.
# 
# The <em>Tversky Similarity Measure</em> \f$ S_{ab} \f$ is calculated by:
# 
# \[ S_{ab} = \frac{N_{ab}}{a * N_a + b * N_b + N_{ab}} \]
# 
# where \f$ N_{ab} \f$ is the number of bits that are set in both bitsets, \f$ N_a \f$ is the number of bits that are only set in the first bitset and \f$ N_b \f$ is the number of bits that are only set in the second bitset. \f$ a \f$ and \f$ b \f$ are bitset contribution weighting factors.
# 
# The <em>Tversky Measure</em> is asymmetric. Setting the parameters \f$ a = b = 1.0 \f$ is identical to using the <em>Tanimoto</em> measure.
# 
# If the specified bitsets <em>bs1</em> and <em>bs2</em> are of different size, missing bits at the end of the smaller bitset are assumed to be zero.
# 
# \param bs1 The first bitset.
# \param bs2 The second bitset.
# \param a Weights the contribution of the first bitset.
# \param b Weights the contribution of the second bitset.
# 
# \return The calculated similarity measure.
# 
def calcTverskySimilarity(bs1: CDPL.Util.BitSet, bs2: CDPL.Util.BitSet, a: float, b: float) -> float: pass
