restartFromSeed(path='seed')

database(
    thermoLibraries = [ 'NH3', 'BurkeH2O2', 'NitrogenCurran', 'primaryNS','thermo_Oct102024','CHON_G4', 'NitrogenCurran', 'NOx2018', 'Klippenstein_Glarborg2016', 'thermo_DFT_CCSDTF12_BAC', 'primaryThermoLibrary', 'JetSurF2.0', 'CBS_QB3_1dHR', 'BurcatNS', 'CurranPentane'],
    reactionLibraries = [ 'NCN2025','2025_Klippenstein', 'Doner2024','HydrazinePDep', 'primaryNitrogenLibrary','primaryNitrogenLibrary/LowT','Think_fixed', 'Nox2020', 'NOx2018', 'Knyazev_Korobeinichev2010','Wang2024','Nitrogen_Dean_and_Bozzelli'],
    seedMechanisms =  ['primaryH2O2','MyNewLibrary' ],
    kineticsDepositories = ['training'],
    kineticsFamilies = [
    '1+2_Cycloaddition',
    #    '1,2-Birad_to_alkene',
    '1,2_Insertion_CO',
    '1,2_Insertion_carbene',
    '1,2_shiftS',
    '1,3_Insertion_CO2',
    '1,3_Insertion_ROR',
    '1,3_Insertion_RSR',
    '1,4_Cyclic_birad_scission',
    '1,4_Linear_birad_scission',
    '2+2_cycloaddition',
    'Birad_recombination',
    'CO_Disproportionation',
    'Birad_R_Recombination',
    'Cyclic_Ether_Formation',
    'Cyclic_Thioether_Formation',
    'Diels_alder_addition',
    'Diels_alder_addition_Aromatic',
    'Disproportionation',
    'HO2_Elimination_from_PeroxyRadical',
    'H_Abstraction',
    'Intra_Retro_Diels_alder_bicyclic',
    'Intra_Disproportionation',
    'Intra_R_Add_Endocyclic',
    'Intra_R_Add_Exocyclic',
    'R_Addition_COm',
    'R_Addition_MultipleBond',
    'R_Recombination',
    'intra_H_migration',
    'intra_NO2_ONO_conversion',
    'intra_OH_migration',
    'intra_substitutionCS_cyclization',
    'intra_substitutionCS_isomerization',
    'intra_substitutionS_cyclization',
    'intra_substitutionS_isomerization',
    '1,3_sigmatropic_rearrangement',
    'Singlet_Carbene_Intra_Disproportionation',
    'Singlet_Val6_to_triplet',
    'Intra_5_membered_conjugated_C=C_C=C_addition',
    'Intra_Diels_alder_monocyclic',
    'Concerted_Intra_Diels_alder_monocyclic_1,2_shiftH',
    'Intra_2+2_cycloaddition_Cd',
    'Intra_ene_reaction',
    'Cyclopentadiene_scission',
    '6_membered_central_C-C_shift',
    'Intra_R_Add_Exo_scission',
    '1,2_shiftC',
    '1,2_NH3_elimination',
    '1,3_NH3_elimination',
    'Retroene',
    'Ketoenol',
    ],
    kineticsEstimator = 'rate rules',
    transportLibraries=['PrimaryTransportLibrary', 'OneDMinN2', 'NOx2018', 'GRI-Mech', 'NIST_Fluorine']
)


# List of species
species(
    label='NH3',
    structure=SMILES("N"),
)
species(
    label='N2',
    structure=SMILES("N#N"),
)
species(
   label='O2',
   structure=SMILES("[O][O]"),
)
species(
    label='H2',
    structure=SMILES("[H][H]"),
)
species(
    label='H',
    structure=SMILES("[H]"),
)
species(label='N', structure=SMILES("[N]"))
species(label='NH', structure=SMILES("[NH]"))
species(label='NH2', structure=SMILES("[NH2]"))
species(label='NNH', structure=SMILES("[N]=N"))
species(label='N2H2', structure=SMILES("N=N"))
species(label='H2NN', structure=SMILES("[NH2+]=[N-]"))
species(label='N2H3', structure=SMILES("[NH]N"))
species(label='N2H4', structure=SMILES("NN"))
species(label='NO', structure=SMILES("[N]=O"))
species(label='HNO', structure=SMILES("N=O"))
species(label='HON', structure=SMILES("O[N]"))
species(label='H2NO', structure=SMILES("N[O]"))
species(label='HNOH', structure=SMILES("[NH]O"))
species(label='NH2OH', structure=SMILES("NO"))
species(label='N2O', structure=SMILES("[N-]=[N+]=O"))
species(label='NO2', structure=SMILES("O=[N+][O-]"))
species(label='HONO', structure=SMILES("ON=O"))
species(label='HNO2', structure=SMILES("O=[NH+][O-]"))
species(label='NO3', structure=SMILES("[O-][N+](=O)[O]"))
species(label='HONO2', structure=SMILES("[O-][N+](=O)O"))

species(label="CH4", structure=SMILES("C"))
species(label="CH3", structure=SMILES("[CH3]"))     
species(label="CH3O", structure=SMILES("C[O]"))    
species(label="CH3O2", structure=SMILES("CO[O]"))    
species(label="CH3O2H", structure=SMILES("COO"))     
species(label="CH2O", structure=SMILES("C=O"))        
species(label="HCO", structure=SMILES("[CH]=O"))   
species(label="CO", structure=SMILES("[C-]#[O+]"))   
species(label="CO2", structure=SMILES("O=C=O"))   
species(label="COHO", structure=SMILES("[O]C=O"))   

species(label='CH3NH2', structure=SMILES("CN"))
species(label='CH3NO2', structure=SMILES("C[N+](=O)[O-]"))
#species(label='CH2NH', structure=SMILES("C=N"))
#species(label='CH2NO2', structure=SMILES("[CH2][N+](=O)[O-]"))
#species(label='H2CN', structure=SMILES("[CH2][N]"))
species(label='HCN', structure=SMILES("C#N"))
species(label='C2H6', structure=SMILES("CC"))
species(label='NCN', structure=SMILES("[N]=C=[N]"))
#species(label='HCNH', structure=SMILES("[CH]=N"))
species(label='CH3NH', structure=SMILES("C[NH]"))
species(label='CHNH2', structure=SMILES("[C]N"))




species(
    label='Ar',
    reactive=False,
    structure=SMILES("[Ar]"),
)





# NH3=0.7, CH4=0.3, Phi=0.7
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.7,'CH4':0.3,'H2':0.0,'O2':1.607,'N2':6.043,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)
# NH3=0.7, CH4=0.3, Phi=1.5
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.7,'CH4':0.3,'H2':0.0,'O2':0.75,'N2':2.82,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)
# NH3=0.6, CH4=0.4, Phi=0.7
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.6,'CH4':0.4,'H2':0.0,'O2':1.786,'N2':6.714,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)
# NH3=0.6, CH4=0.4, Phi=1.5
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.6,'CH4':0.4,'H2':0.0,'O2':0.833,'N2':3.132,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)
# NH3=0.4, CH4=0.6, Phi=0.7
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.4,'CH4':0.6,'H2':0.0,'O2':2.14,'N2':8.05,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)
# NH3=0.4, CH4=0.6, Phi=1.5
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.4,'CH4':0.6,'H2':0.0,'O2':1.0,'N2':3.76,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)
# NH3=0.2, CH4=0.8, Phi=0.7
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.2,'CH4':0.8,'H2':0.0,'O2':2.5,'N2':9.4,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)

# NH3=0.2, CH4=0.8, Phi=1.5
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.2,'CH4':0.8,'H2':0.0,'O2':1.167,'N2':4.38,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)

# The following two conditions are depressurized to 1 bar:
# NH3=0.6, CH4=0.4, Phi=2.0
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.6,'CH4':0.4,'H2':0.0,'O2':0.625,'N2':2.35,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)
# NH3=0.5, CH4=0.5, Phi=0.5
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.5,'CH4':0.5,'H2':0.0,'O2':2.75,'N2':10.34,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)


# The following condition is depressurized to 5 bar:
# NH3=0.95, CH4=0.05, Phi=0.7
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(5.0,'bar')],
    initialMoleFractions={'NH3':0.95,'CH4':0.05,'H2':0.0,'O2':0.406,'N2':1.526,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)

# The following condition is depressurized to 5 bar:
# NH3=0.95, CH4=0.05, Phi=0.5
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(5.0,'bar')],
    initialMoleFractions={'NH3':0.95,'CH4':0.05,'H2':0.0,'O2':1.626,'N2':6.115,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)
# NH3=0.005, CH4=0.005, Ar=97.625, Phi=1.0
simpleReactor(
     temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.005,'CH4':0.005,'H2':0.0,'O2':0.01375,'N2':0.0,'Ar':97.625},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)
# NH3=0.000351, CH4=0.005032, Phi=1.0 
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.000351,'CH4':0.005032,'H2':0.0,'O2':0.005383,'N2':0.005036,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)


# NH3=0, CH4=1, Phi=1.0 
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.000351,'CH4':0.005032,'H2':0.0,'O2':0.005383,'N2':0.005036,'Ar':0.0},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)

# Pure CH4, Phi = 1.0
simpleReactor(
    temperature=[(700,'K'), (1800,'K')],
    pressure=[(1.0,'bar'), (1.0,'bar')],
    initialMoleFractions={
        'CH4': 0.0950,
        'O2':  0.190,
        'N2':  0.715,
        'NH3': 0.0,
        'H2':  0.0,
        'Ar':  0.0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)

# Pure CH4, Phi = 2.0 (fuel-rich)
simpleReactor(
    temperature=[(700,'K'), (1800,'K')],
    pressure=[(1.0,'bar'), (1.0,'bar')],
    initialMoleFractions={
        'CH4': 0.1736,
        'O2':  0.1736,
        'N2':  0.6528,
        'NH3': 0.0,
        'H2':  0.0,
        'Ar':  0.0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)

#
simpleReactor(
    temperature=[(700,'K'),(1800,'K')],
    pressure=[(1.0,'bar'),(1.0,'bar')],
    initialMoleFractions={'NH3':0.005,'CH4':0.005,'H2':0.0,'O2':0.006875,'N2':0,'Ar':0.983125},
    terminationRateRatio=0.01, terminationTime=(10,'s'),
)

#############################################

# Reaction systems
# NH3 + 0.75 O2 <=> 0.5 N2 + 1.5 H2O
#1_Reactor for neat ammonia phi=0.25
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'O2': 3.0, 'N2':11.28, 'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)

# Reaction systems
# NH3 + 0.75 O2 <=> 0.5 N2 + 1.5 H2O
#2_Reactor for neat ammonia phi=0.5
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'O2': 1.5, 'N2':5.64, 'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)
#3_Reactor for neat ammonia phi=1.0
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'O2':0.75, 'N2':2.82,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)
#4_Reactor for neat ammonia phi=1.5
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'O2':0.5, 'N2':1.88,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)

# Reaction systems
# NH3 + 0.75 O2 <=> 0.5 N2 + 1.5 H2O
#5_Reactor for neat ammonia phi=2
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'O2': 0.375, 'N2':1.41, 'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)
#6_Reactor for ammonia with hydrogen phi=0.25
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':0.1, 'O2':3.2, 'N2':12.0,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)
#7_Reactor for ammonia with hydrogen phi=0.5
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':0.1, 'O2':1.6, 'N2':6.0,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)
#8_Reactor for ammonia with hydrogen phi=1.0
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':0.1, 'O2':0.80, 'N2':3.0,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)
#9_Reactor for ammonia with hydrogen phi=1.5
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':0.1, 'O2':0.53, 'N2':2.0,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)

#10_Reactor for ammonia with hydrogen phi=2
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':0.1, 'O2':0.4, 'N2':1.5,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)

#11_Reactor for ammonia with hydrogen phi=0.25
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':0.5, 'O2':3.2, 'N2':12.0,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)
#12_Reactor for ammonia with hydrogen phi=0.5
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':0.5, 'O2':1.6, 'N2':6.0,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)
#13_Reactor for ammonia with hydrogen phi=1.0
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':0.5, 'O2':0.80, 'N2':3.0,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)
#14_Reactor for ammonia with hydrogen phi=1.5
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':0.5, 'O2':0.53, 'N2':2.0,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)

#15_Reactor for ammonia with hydrogen phi=2
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':0.5, 'O2':0.4, 'N2':1.5,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)


#16_Reactor for ammonia with hydrogen phi=0.25
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':1, 'O2':3.2, 'N2':12.0,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)
#17_Reactor for ammonia with hydrogen phi=0.5
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':1, 'O2':1.6, 'N2':6.0,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)
#18_Reactor for ammonia with hydrogen phi=1.0
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':1, 'O2':0.80, 'N2':3.0,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)
#19_Reactor for ammonia with hydrogen phi=1.5
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':1, 'O2':0.53, 'N2':2.0,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)

#20_Reactor for ammonia with hydrogen phi=2
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1, 'H2':1, 'O2':0.4, 'N2':1.5,  'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)

#21_pure NH3 pyrolysis
simpleReactor(
    temperature=[(700,'K'),(1900,'K')],
    pressure=[(1.0,'bar'),(10.0,'bar')],
    initialMoleFractions={
         'NH3':1,'Ar':0,
    },
    terminationRateRatio=0.01,
    terminationTime=(10,'s'),
)

# pute H2 combustion - stoichiometric
# #22_pure H2 combustion - stoichiometric
# simpleReactor(
#     temperature=[(700,'K'),(1900,'K')],
#     pressure=[(1.0,'bar'),(10.0,'bar')],
#     initialMoleFractions={
#          'H2':1,'O2':0.5,'N2':2.0,'Ar':0,
#     },
#     terminationRateRatio=0.01,
#     terminationTime=(10,'s'),
# )

# #23_pure H2 combustion - rich
# simpleReactor(
#     temperature=[(700,'K'),(1900,'K')],
#     pressure=[(1.0,'bar'),(10.0,'bar')],
#     initialMoleFractions={
#          'H2':1,'O2':0.1,'N2':0.4,'Ar':0,
#     },
#     terminationRateRatio=0.01,
#     terminationTime=(10,'s'),
# )

# #24_pure H2 combustion - lean
# simpleReactor(
#     temperature=[(700,'K'),(1900,'K')],
#     pressure=[(1.0,'bar'),(10.0,'bar')],
#     initialMoleFractions={
#          'H2':1,'O2':2.0,'N2':8.0,'Ar':0,
#     },
#     terminationRateRatio=0.01,
#     terminationTime=(10,'s'),
# )

simulator(
    atol=1e-12,
    rtol=1e-6,
)

model(
    toleranceKeepInEdge=0.001,
    toleranceMoveToCore=0.1,
    toleranceInterruptSimulation=0.1,
    maximumEdgeSpecies=50000,
    filterReactions=True,

)

options(
    units='si',
    generateOutputHTML=False,
    generatePlots=False,
    saveEdgeSpecies=False,
    saveSimulationProfiles=False,
)

pressureDependence(
        method='modified strong collision',
        maximumGrainSize=(0.5,'kcal/mol'),
        minimumNumberOfGrains=250,
        temperatures=(500,2000,'K',6),
        pressures=(0.1,50,'bar',7),
        interpolation=('PDepArrhenius', 6, 4),
	#interpolation=('Chebyshev', 6, 4),
        maximumAtoms=16,
)



generatedSpeciesConstraints(
    allowed=['input species','seed mechanisms','reaction libraries'],
    maximumCarbonAtoms=2,
    maximumOxygenAtoms=2,
    maximumNitrogenAtoms=3,
    maximumSiliconAtoms=0,
    maximumSulfurAtoms=0,
    maximumHeavyAtoms=5,
    maximumRadicalElectrons=2,
    maximumSingletCarbenes=0,
    maximumCarbeneRadicals=0,
    allowSingletO2=True,
)
