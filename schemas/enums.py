from base_enums import RichEnum

class UnitEnum(RichEnum):
    NEWTON = ("NEWTON", "N")
    KILOGRAM = ("KILOGRAM", "kg")
    METER_PER_SECOND = ("METER_PER_SECOND ", "m/s")
    GRAMM_PER_MILLILITRE = ("GRAMM_PER_MILLILITRE", "g/ml")

class ChemicalClassEnum(RichEnum):
    pass

class StructureEnum(RichEnum):
    # organic
    LINEAR = ("LINEAR", "Linear")
    BRANCHED = ("BRANCHED", "Branched")
    CYCLIC = ("CYCLIC", "Cyclic")
    POLYCYCLIC = ("POLYCYCLIC", "Polycyclic")

    # crystals
    TRICLINIC_PEDIAL = ("TRICLINIC_PEDIAL", "Triclinic pedial")
    TRICLINIC_PINACOIDAL = ("TRICLINIC_PINACOIDAL", "Triclinic pinacoidal")

    MONOCLINIC_SPHENOIDAL = ("MONOCLINIC_SPHENOIDAL", "Monoclinic sphenoidal")
    MONOCLINIC_DOMATIC = ("MONOCLINIC_DOMATIC", "Monoclinic domatic")
    MONOCLINIC_PRISMATIC = ("MONOCLINIC_PRISMATIC", "Monoclinic prismatic")

    RHOMBIC_DISPHENOIDAL = ("RHOMBIC_DISPHENOIDAL", "Rhombic disphenoidal")
    RHOMBIC_PYRAMIDAL = ("RHOMBIC_PYRAMIDAL", "Rhombic pyramidal")
    RHOMBIC_DIPYRAMIDAL = ("RHOMBIC_DIPYRAMIDAL", "Rhombic dipyramidal")

    TETRAGONAL_PYRAMIDAL = ("TETRAGONAL_PYRAMIDAL", "Tetragonal pyramidal")
    TETRAGONAL_DISPHENOIDAL = ("TETRAGONAL_DISPHENOIDAL", "Tetragonal disphenoidal")
    TETRAGONAL_DIPYRAMIDAL = ("TETRAGONAL_DIPYRAMIDAL", "Tetragonal dipyramidal")
    TETRAGONAL_TRAPEZOHEDRAL = ("TETRAGONAL_TRAPEZOHEDRAL", "Tetragonal trapezohedral")
    TETRAGONAL_SCALENOHEDRAL = ("TETRAGONAL_SCALENOHEDRAL", "Tetragonal scalenohedral")
    DITETRAGONAL_PYRAMIDAL = ("DITETRAGONAL_PYRAMIDAL", "Ditetragonal pyramidal")
    DITETRAGONAL_DIPYRAMIDAL = ("DITETRAGONAL_DIPYRAMIDAL", "Ditetragonal dipyramidal")

    HEXAGONAL_PYRAMIDAL = ("HEXAGONAL_PYRAMIDAL", "Hexagonal pyramidal")
    HEXAGONAL_DIPYRAMIDAL = ("HEXAGONAL_DIPYRAMIDAL", "Hexagonal dipyramidal")
    HEXAGONAL_TRAPEZOHEDRAL = ("HEXAGONAL_TRAPEZOHEDRAL", "Hexagonal trapezohedral")
    
    HEXAGONAL_TRIGONAL_PYRAMIDAL = ("HEXAGONAL_TRIGONAL_PYRAMIDAL", "Trigonal pyramidal")
    HEXAGONAL_TRIGONAL_DIPYRAMIDAL = ("HEXAGONAL_TRIGONAL_DIPYRAMIDAL", "Trigonal dipyramidal")
    HEXAGONAL_TRIGONAL_RHOMBOHERDAL = ("HEXAGONAL_TRIGONAL_RHOMBOHERDAL", "Trigonal rhombohedral")
    HEXAGONAL_DITRIGONAL_PYRAMIDAL = ("HEXAGONAL_DITRIGONAL_PYRAMIDAL", "Ditrigonal pyramidal")
    HEXAGONAL_DITRIGONAL_SCALENOHEDRAL = ("HEXAGONAL_DITRIGONAL_SCALENOHEDRAL", "Hexagonal scalenohedral")
    HEXAGONAL_DITRIGONAL_DIPYRAMIDAL = ("HEXAGONAL_DITRIGONAL_DIPYRAMIDAL", "Ditrigonal dipyramidal")
    
    DIHEXAGONAL_PYRAMIDAL = ("DIHEXAGONAL_PYRAMIDAL", "Dihexagonal pyramidal")
    DIHEXAGONAL_DIPYRAMIDAL = ("DIHEXAGONAL_DIPYRAMIDAL", "Dihexagonal dipyramidal")

    CUBIC_TETARTOIDAL = ("CUBIC_TETARTOIDAL", "Cubic tetartoidal")
    CUBIC_DIPLOIDAL = ("CUBIC_DIPLOIDAL", "Cubic diploidal")
    CUBIC_GYROIDAL = ("CUBIC_GYROIDAL", "Cubic gyroidal")
    CUBIC_HEXTETRAHEDRAL = ("CUBIC_HEXTETRAHEDRAL", "Cubic hextetrahedral")
    CUBIC_HEXOCTAHEDRAL = ("CUBIC_HEXOCTAHEDRAL", "Cubic hexoctahedral")

class HStatementEnum(RichEnum):
    """
    Enum for GHS Hazard Statements (H-Statements).
    Each member's value is a tuple: (code, description).
    """
    # H2xx: Physical Hazards
    H200 = ("H200", "H200 - Unstable explosives")
    H201 = ("H201", "H201 - Explosive; mass explosion hazard")
    H202 = ("H202", "H202 - Explosive, severe projection hazard")
    H203 = ("H203", "H203 - Explosive; fire, blast or projection hazard")
    H204 = ("H204", "H204 - Fire or projection hazard")
    H205 = ("H205", "H205 - May mass explode in fire")
    H206 = ("H206", "H206 - Fire, blast or projection hazard; increased risk of explosion if desensitising agent is reduced")
    H207 = ("H207", "H207 - Fire or projection hazard; increased risk of explosion if desensitising agent is reduced")
    H208 = ("H208", "H208 - Fire hazard; increased risk of explosion if desensitising agent is reduced")
    H220 = ("H220", "H220 - Extremely flammable gas")
    H221 = ("H221", "H221 - Flammable gas")
    H222 = ("H222", "H222 - Extremely flammable aerosol")
    H223 = ("H223", "H223 - Flammable aerosol")
    H224 = ("H224", "H224 - Extremely flammable liquid and vapour")
    H225 = ("H225", "H225 - Highly flammable liquid and vapour")
    H226 = ("H226", "H226 - Flammable liquid and vapour")
    H228 = ("H228", "H228 - Flammable solid")
    H229 = ("H229", "H229 - Pressurised container: May burst if heated")
    H230 = ("H230", "H230 - May react explosively even in the absence of air")
    H231 = ("H231", "H231 - May react explosively even in the absence of air at elevated pressure and/or temperature")
    H232 = ("H232", "H232 - May ignite spontaneously if exposed to air")
    H240 = ("H240", "H240 - Heating may cause an explosion")
    H241 = ("H241", "H241 - Heating may cause a fire or explosion")
    H242 = ("H242", "H242 - Heating may cause a fire")
    H250 = ("H250", "H250 - Catches fire spontaneously if exposed to air")
    H251 = ("H251", "H251 - Self-heating: may catch fire")
    H252 = ("H252", "H252 - Self-heating in large quantities; may catch fire")
    H260 = ("H260", "H260 - In contact with water releases flammable gases which may ignite spontaneously")
    H261 = ("H261", "H261 - In contact with water releases flammable gases")
    H270 = ("H270", "H270 - May cause or intensify fire; oxidiser")
    H271 = ("H271", "H271 - May cause fire or explosion; strong oxidiser")
    H272 = ("H272", "H272 - May intensify fire; oxidiser")
    H280 = ("H280", "H280 - Contains gas under pressure; may explode if heated")
    H281 = ("H281", "H281 - Contains refrigerated gas; may cause cryogenic burns or injury")
    H290 = ("H290", "H290 - May be corrosive to metals")

    # H3xx: Health Hazards
    H300 = ("H300", "H300 - Fatal if swallowed")
    H301 = ("H301", "H301 - Toxic if swallowed")
    H302 = ("H302", "H302 - Harmful if swallowed")
    H304 = ("H304", "H304 - May be fatal if swallowed and enters airways")
    H310 = ("H310", "H310 - Fatal in contact with skin")
    H311 = ("H311", "H311 - Toxic in contact with skin")
    H312 = ("H312", "H312 - Harmful in contact with skin")
    H314 = ("H314", "H314 - Causes severe skin burns and eye damage")
    H315 = ("H315", "H315 - Causes skin irritation")
    H317 = ("H317", "H317 - May cause an allergic skin reaction")
    H318 = ("H318", "H318 - Causes serious eye damage")
    H319 = ("H319", "H319 - Causes serious eye irritation")
    H330 = ("H330", "H330 - Fatal if inhaled")
    H331 = ("H331", "H331 - Toxic if inhaled")
    H332 = ("H332", "H332 - Harmful if inhaled")
    H334 = ("H334", "H334 - May cause allergy or asthma symptoms or breathing difficulties if inhaled")
    H335 = ("H335", "H335 - May cause respiratory irritation")
    H336 = ("H336", "H336 - May cause drowsiness or dizziness")
    H340 = ("H340", "H340 - May cause genetic defects <state route of exposure if it is conclusively proven that no other routes of exposure cause the hazard >")
    H341 = ("H341", "H341 - Suspected of causing genetic defects <state route of exposure if it is conclusively proven that no other routes of exposure cause the hazard>")
    H350 = ("H350", "H350 - May cause cancer <state route of exposure if it is conclusively proven that no other routes of exposure cause the hazard>")
    H350i = ("H350i", "H350i - May cause cancer by inhalation")
    H351 = ("H351", "H351 - Suspected of causing cancer <state route of exposure if it is conclusively proven that no other routes of exposure cause the hazard>")
    H360 = ("H360", "H360 - May damage fertility or the unborn child <state specific effect if known > <state route of exposure if it is conclusively proven that no other routes of exposure cause the hazard>")
    H360F = ("H360F", "H360F - May damage fertility")
    H360D = ("H360D", "H360D - May damage the unborn child")
    H360FD = ("H360FD", "H360FD - May damage fertility. May damage the unborn child")
    H360Fd = ("H360Fd", "H360Fd - May damage fertility. Suspected of damaging the unborn child")
    H360Df = ("H360Df", "H360Df - May damage the unborn child. Suspected of damaging fertility")
    H361 = ("H361", "H361 - Suspected of damaging fertility or the unborn child <state specific effect if known> <state route of exposure if it is conclusively proven that no other routes of exposure cause the hazard>")
    H361f = ("H361f", "H361f - Suspected of damaging fertility")
    H361d = ("H361d", "H361d - Suspected of damaging the unborn child")
    H361fd = ("H361fd", "H361fd - Suspected of damaging fertility. Suspected of damaging the unborn child")
    H362 = ("H362", "H362 - May cause harm to breast-fed children")
    H370 = ("H370", "H370 - Causes damage to organs <or state all organs affected, if known> <state route of exposure if it is conclusively proven that no other routes of exposure cause the hazard>")
    H371 = ("H371", "H371 - May cause damage to organs <or state all organs affected, if known> <state route of exposure if it is conclusively proven that no other routes of exposure cause the hazard>")
    H372 = ("H372", "H372 - Causes damage to organs <or state all organs affected, if known> through prolonged or repeated exposure <state route of exposure if it is conclusively proven that no other routes of exposure cause the hazard>")
    H373 = ("H373", "H373 - May cause damage to organs <or state all organs affected, if known> through prolonged or repeated exposure <state route of exposure if it is conclusively proven that no other routes of exposure cause the hazard>")

    # H3xx Combinations
    H300_PLUS_H310 = ("H300 + H310", "H300 + H310 - Fatal if swallowed or in contact with skin")
    H300_PLUS_H330 = ("H300 + H330", "H300 + H330 - Fatal if swallowed or if inhaled")
    H310_PLUS_H330 = ("H310 + H330", "H310 + H330 - Fatal in contact with skin or if inhaled")
    H300_PLUS_H310_PLUS_H330 = ("H300 + H310 + H330", "H300 + H310 + H330 - Fatal if swallowed, in contact with skin or if inhaled")
    H301_PLUS_H311 = ("H301 + H311", "H301 + H311 - Toxic if swallowed or in contact with skin")
    H301_PLUS_H331 = ("H301 + H331", "H301 + H331 - Toxic if swallowed or if inhaled")
    H311_PLUS_H331 = ("H311 + H331", "H311 + H331 - Toxic in contact with skin or if inhaled")
    H301_PLUS_H311_PLUS_H331 = ("H301 + H311 + H331", "H301 + H311 + H331 - Toxic if swallowed, in contact with skin or if inhaled")
    H302_PLUS_H312 = ("H302 + H312", "H302 + H312 - Harmful if swallowed or in contact with skin")
    H302_PLUS_H332 = ("H302 + H332", "H302 + H332 - Harmful if swallowed or if inhaled")
    H312_PLUS_H332 = ("H312 + H332", "H312 + H332 - Harmful in contact with skin or if inhaled")
    H302_PLUS_H312_PLUS_H332 = ("H302 + H312 + H332", "H302 + H312 + H332 - Harmful if swallowed, in contact with skin or if inhaled")

    # H4xx: Environmental Hazards
    H400 = ("H400", "H400 - Very toxic to aquatic life")
    H410 = ("H410", "H410 - Very toxic to aquatic life with long lasting effects")
    H411 = ("H411", "H411 - Toxic to aquatic life with long lasting effects")
    H412 = ("H412", "H412 - Harmful to aquatic life with long lasting effects")
    H413 = ("H413", "H413 - May cause long lasting harmful effects to aquatic life")
    H420 = ("H420", "H420 - Harms public health and the environment by destroying ozone in the upper atmosphere")

class EUHStatementEnum(RichEnum):
    """
    Enum for supplemental EU Hazard Statements (EUH-Statements).
    Each member's value is a tuple: (code, description).
    """
    EUH014 = ("EUH 014", "EUH 014 – Reacts violently with water.")
    EUH018 = ("EUH 018", "EUH 018 – In use may form flammable/explosive vapour- air mixture.")
    EUH019 = ("EUH 019", "EUH 019 – May form explosive peroxides.")
    EUH029 = ("EUH 029", "EUH 029 – Contact with water liberates toxic gas.")
    EUH031 = ("EUH 031", "EUH 031 – Contact with acids liberates toxic gas.")
    EUH032 = ("EUH 032", "EUH 032 – Contact with acids liberates very toxic gas.")
    EUH044 = ("EUH 044", "EUH 044 – Risk of explosion if heated under confinement.")
    EUH066 = ("EUH 066", "EUH 066 – Repeated exposure may cause skin dryness or cracking.")
    EUH070 = ("EUH 070", "EUH 070 – Toxic by eye contact.")
    EUH071 = ("EUH 071", "EUH 071 – Corrosive to the respiratory tract.")

    EUH201_201A = ("EUH 201/201A", "EUH 201/201A – Contains lead. Should not be used on surfaces liable to be chewed or sucked by children. Warning! Contains lead.")
    EUH202 = ("EUH 202", "EUH 202 – Cyanoacrylate. Danger. Bonds skin and eyes in seconds. Keep out of the reach of children.")
    EUH203 = ("EUH 203", "EUH 203 – Contains chromium (VI). May produce an allergic reaction.")
    EUH204 = ("EUH 204", "EUH 204 – Contains isocyanates. May produce an allergic reaction.")
    EUH205 = ("EUH 205", "EUH 205 – Contains epoxy constituents. May produce an allergic reaction.")
    EUH206 = ("EUH 206", "EUH 206 – Warning! Do not use together with other products. May release dangerous gases (chlorine).")
    EUH207 = ("EUH 207", "EUH 207 – Warning! Contains cadmium. Dangerous fumes are formed during use. See information supplied by the manufacturer. Comply with the safety instructions.")
    EUH208 = ("EUH 208", "EUH 208 – Contains <name of sensitising substance>. May produce an allergic reaction.")
    EUH209_209A = ("EUH 209/209A", "EUH 209/209A – Can become highly flammable in use. Can become flammable in use.")
    EUH210 = ("EUH 210", "EUH 210 – Safety data sheet available on request.")
    EUH211 = ("EUH 211", "EUH 211 – Warning! Hazardous respirable droplets may be formed when sprayed. Do not breathe spray or mist.")
    EUH212 = ("EUH 212", "EUH 212 – Warning! Hazardous respirable dust may be formed when used. Do not breathe dust.")

    EUH380 = ("EUH 380", "EUH 380 – May cause endocrine disruption in humans.")
    EUH381 = ("EUH 381", "EUH 381 – Suspected of causing endocrine disruption in humans.")
    
    EUH401 = ("EUH 401", "EUH 401 – To avoid risks to human health and the environment, comply with the instructions for use.")
    EUH430 = ("EUH 430", "EUH 430 – May cause endocrine disruption in the environment.")
    EUH431 = ("EUH 431", "EUH 431 – Suspected of causing endocrine disruption in the environment.")
    EUH440 = ("EUH 440", "EUH 440 – Accumulates in the environment and living organisms including in humans.")
    EUH441 = ("EUH 441", "EUH 441 – Strongly accumulates in the environment and living organisms including in humans.")
    EUH450 = ("EUH 450", "EUH 450 – Can cause long-lasting and diffuse contamination of water resources.")
    EUH451 = ("EUH 451", "EUH 451 – Can cause very long-lasting and diffuse contamination of water resources.")

class StateOfMatterEnum(RichEnum):
    SOLID = ("SOLID", "Solid")
    LIQUID = ("LIQUID", "Liquid")
    GAS = ("GAS", "Gas")
    PLASMA = ("PLASMA", "Plasma")