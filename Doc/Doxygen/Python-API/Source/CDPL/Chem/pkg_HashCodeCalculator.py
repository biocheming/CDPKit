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
# \brief HashCodeCalculator.
# 
# \see [\ref MHASH]
# 
class HashCodeCalculator(Boost.Python.instance):

    ##
    # \brief The default functor for the generation of atom hash seeds.
    # 
    class DefAtomHashSeedFunctor(Boost.Python.instance):

        ##
        # \brief Initializes the \e %DefAtomHashSeedFunctor instance.
        # \param self The \e %DefAtomHashSeedFunctor instance to initialize.
        # \param calc 
        # \param flags 
        # 
        def __init__(calc: HashCodeCalculator, flags: int = 159) -> None: pass

        ##
        # \brief Generates an initial hash code value (seed) for the specified atom.
        # 
        # The generated hash seed depends on the set of considered atomic properties that has been specified in the constructor.
        # 
        # \param atom The atom for which to generate the initial hash code.
        # 
        # \return The generated atom hash seed.
        # 
        def __call__(atom: Atom) -> int: pass

    ##
    # \brief The default functor for the generation of bond hash seeds.
    # 
    class DefBondHashSeedFunctor(Boost.Python.instance):

        ##
        # \brief Constructs the bond hash seed functor object for the specified set of bond properties.
        # 
        # The <em>flags</em> argument is an OR combination of the constants defined in namespace Chem.BondPropertyFlag. Supported property flags are:
        #  - Chem.BondPropertyFlag.ORDER
        #  - Chem.BondPropertyFlag.TOPOLOGY
        #  - Chem.BondPropertyFlag.AROMATICITY
        #  - and Chem.BondPropertyFlag.CIP_CONFIGURATION
        # 
        # \param flags Specifies the set of considered bond properties.
        # 
        def __init__(flags: int = 15) -> None: pass

        ##
        # \brief Generates an initial hash code value (seed) for the specified bond.
        # 
        # The generated hash seed depends on the set of considered bond properties that has been specified in the constructor.
        # 
        # \param bond The bond for which to generate the initial hash code.
        # 
        # \return The generated bond hash seed.
        # 
        def __call__(bond: Bond) -> int: pass

    ##
    # \brief Specifies the default set of atomic properties considered in the generation of initial atom hash codes by HashCodeCalculator.DefAtomHashSeedFunction.
    # 
    DEF_ATOM_PROPERTY_FLAGS = 159

    ##
    # \brief Specifies the default set of bond properties considered in the generation of initial bond hash codes by HashCodeCalculator.DefBondHashSeedFunction.
    # 
    DEF_BOND_PROPERTY_FLAGS = 15

    ##
    # \brief Constructs the <tt>HashCodeCalculator</tt> instance.
    # 
    def __init__() -> None: pass

    ##
    # \brief Constructs the <tt>HashCodeCalculator</tt> instance and calculates the hash code of the molecular graph <em>molgraph</em>.
    # 
    # The calculated hash code can be retrieved by a call to getResult().
    # 
    # \param molgraph The molecular graph for which the hash code has to be calculated.
    # 
    def __init__(molgraph: MolecularGraph) -> None: pass

    ##
    # \brief Returns the numeric identifier (ID) of the wrapped C++ class instance.
    # \param self The \e %HashCodeCalculator instance this method is called upon.
    # 
    # Different Python \e %HashCodeCalculator instances may reference the same underlying C++ class instance. The commonly used Python expression
    # <tt>a is not b</tt> thus cannot tell reliably whether the two \e %HashCodeCalculator instances \e a and \e b reference different C++ objects. 
    # The numeric identifier returned by this method allows to correctly implement such an identity test via the simple expression
    # <tt>a.getObjectID() != b.getObjectID()</tt>.
    # 
    # \return The numeric ID of the internally referenced C++ class instance.
    # 
    def getObjectID() -> int: pass

    ##
    # \brief Allows to specify a custom function for the generation of initial atom hash codes.
    # 
    # \param func A HashCodeCalculator.AtomHashSeedFunction instance that wraps the target function.
    # 
    # \note By default, atom hash seeds are generated by HashCodeCalculator.DefAtomHashSeedFunctor.
    # 
    def setAtomHashSeedFunction(func: SizeTypeAtomFunctor) -> None: pass

    ##
    # \brief Allows to specify a custom function for the generation of initial bond hash codes.
    # 
    # \param func A HashCodeCalculator.BondHashSeedFunction instance that wraps the target function.
    # 
    # \note By default, bond hash seeds are generated by HashCodeCalculator.DefBondHashSeedFunctor.
    # 
    def setBondHashSeedFunction(func: UInt64BondFunctor) -> None: pass

    ##
    # \brief Allows to specify whether or not global stereochemical features shall have an influence on the calculated hash codes.
    # 
    # When global stereochemical features are considered, the hash code of a molecular graph will not only depend on basic atom and bond properties but also on additional stereochemical characteristics like the relative spatial arrangement of substituents. The mutual spatial arrangement of substituents may be the only feature that allows the differentiation of stereoisomers with a plane of symmetry. Diastereoisomers like <em>cis-1,4-Cyclohexanediol</em> and <em>trans-1,4-Cyclohexanediol</em> are typical examples for such corner cases.
    # 
    # \param include If <tt>True</tt>, global stereochemical features will be considered and get ignored otherwise.
    # 
    # \note By default, global stereochemical features are included in the hash code calculation.
    # 
    def includeGlobalStereoFeatures(include: bool) -> None: pass

    ##
    # \brief Tells whether or not global stereochemical features influence the calculated hash codes.
    # 
    # \return <tt>True</tt> if global stereochemical features of a molecular graph are considered, and <tt>False</tt> otherwise. 
    # 
    # \see includeGlobalStereoFeatures()
    # 
    def globalStereoFeaturesIncluded() -> bool: pass

    ##
    # \brief Calculates the hash code of the molecular graph <em>molgraph</em>.
    # 
    # \param molgraph The molecular graph for which to calculate the hash code.
    # 
    # \return The hash code of the molecular graph <em>molgraph</em>.
    # 
    def calculate(molgraph: MolecularGraph) -> int: pass

    ##
    # \brief Returns the result of the last hash code calculation.
    # 
    # \return The result of the last hash code calculation, or zero if a calculation has not yet been performed.
    # 
    def getResult() -> int: pass

    ##
    # \brief 
    # \param molgraph 
    # \return 
    #
    def __call__(molgraph: MolecularGraph) -> int: pass

    objectID = property(getObjectID)

    result = property(getResult)

    ##
    # \brief FIXME!
    # \brief 
    #
    globalStereoFeatures = property(getGlobalStereoFeatures, setGlobalStereoFeatures)
