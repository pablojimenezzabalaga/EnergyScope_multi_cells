# -*- coding: utf-8 -*-
"""
This file defines a dictionary with global variables to be used in EnergyScope such as fuels, technologies, etc.
"""
import datetime

commons = {}

commons['logfile'] = str(datetime.datetime.now()).replace(':', '-').replace(' ', '_') + '.energyscope.log'

CSV_SEPARATOR = ','
AMPL_SEPARATOR = '\t'

# defining named_space_id
named_space_id = {'AT_BE_BG_CH_CZ_DE_DK_EE_ES_FI_FR_GB_GR_HR_HU_IE_IT_LT_LU_LV_NL_PL_PT_RO_SE_SI_SK': 'eu27',
                  'AT_BE_BG_CH_CZ_DE_DK_EE_ES_FI_FR_GB_GR_HR_HU_IE_IT_LT_LU_LV_NL_NO_PL_PT_RO_SE_SI_SK': 'eu28',
                  'AL_AT_BA_BE_BG_CH_CZ_DE_DK_EE_ES_FI_FR_GB_GR_HR_HU_IE_IT_LT_LU_LV_ME_MK_NL_NO_PL_PT_RO_RS_SE_SI_SK_XK': 'eu34',
                  'BN_BN-IT_BN-YC_CB_CH_LP_OR_PA-NA_PT_SC_SC-AS_SC-CC_SC-CQ_SC-GB_SC-MI_SC-VC_SC-VL_TJ_TJ-BE_TJ-OC': 'BO_SI'}

# defining 2 letter country codes and full country names (ISO3166_alpha2)
eu27_country_code = ['AT', 'BE', 'BG', 'CH', 'CZ',
                     'DE', 'DK', 'EE', 'ES', 'FI',
                     'FR', 'HR', 'HU', 'GR', 'GB',
                     'IE', 'IT', 'LT', 'LU', 'LV',
                     'NL', 'PL', 'PT', 'RO', 'SE',
                     'SI', 'SK']
eu27_full_names = ['Austria', 'Belgium', 'Bulgaria', 'Switzerland', 'Czech Republic',
                   'Germany', 'Denmark', 'Estonia', 'Spain', 'Finland',
                   'France', 'Croatia', 'Hungary', 'Greece', 'United Kingdom',
                   'Ireland', 'Italy', 'Lithuania', 'Luxembourg', 'Latvia',
                   'Netherlands', 'Poland', 'Portugal', 'Romania', 'Sweden',
                   'Slovenia', 'Slovakia']

# defining 2 letter country codes and full country names (ISO3166_alpha2)
eu28_country_code = ['AT', 'BE', 'BG', 'CH', 'CZ',
                     'DE', 'DK', 'EE', 'ES', 'FI',
                     'FR', 'HR', 'HU', 'GR', 'GB',
                     'IE', 'IT', 'LT', 'LU', 'LV',
                     'NL', 'NO', 'PL', 'PT', 'RO', 'SE',
                     'SI', 'SK']
eu28_full_names = ['Austria', 'Belgium', 'Bulgaria', 'Switzerland', 'Czech Republic',
                   'Germany', 'Denmark', 'Estonia', 'Spain', 'Finland',
                   'France', 'Croatia', 'Hungary', 'Greece', 'United Kingdom',
                   'Ireland', 'Italy', 'Lithuania', 'Luxembourg', 'Latvia',
                   'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Sweden',
                   'Slovenia', 'Slovakia']

full_2_code = dict(zip(eu28_full_names, eu28_country_code))
code_2_full = dict(zip(eu28_country_code, eu28_full_names))

# with additional countries
eu34_country_code_eurostat = ['AL', 'AT', 'BA', 'BE', 'BG',
                              'CH', 'CZ', 'DE', 'DK',
                              'EE', 'EL', 'ES', 'FI', 'FR',
                              'HR', 'HU', 'IE', 'IT',
                              'LT', 'LU', 'LV', 'ME', 'MK',
                              'NL', 'NO', 'PL', 'PT',
                              'RO', 'RS', 'SE', 'SI', 'SK',
                              'UK', 'XK']
eu34_country_code_iso3166_alpha2 = ['AL', 'AT', 'BA', 'BE', 'BG',
                                    'CH', 'CZ', 'DE', 'DK',
                                    'EE', 'GR', 'ES', 'FI', 'FR',
                                    'HR', 'HU', 'IE', 'IT',
                                    'LT', 'LU', 'LV', 'ME', 'MK',
                                    'NL', 'NO', 'PL', 'PT',
                                    'RO', 'RS', 'SE', 'SI', 'SK',
                                    'GB', 'XK']
eu34_full_names = ['Albania', 'Austria', 'Bosnia and Herzegovina', 'Belgium', 'Bulgaria',
                   'Switzerland', 'Czech Republic', 'Germany', 'Denmark',
                   'Estonia', 'Greece', 'Spain', 'Finland', 'France',
                   'Croatia', 'Hungary', 'Ireland', 'Italy',
                   'Lithuania', 'Luxembourg', 'Latvia', 'Montenegro', 'North Macedonia',
                   'Netherlands', 'Norway', 'Poland', 'Portugal',
                   'Romania', 'Serbia', 'Sweden', 'Slovenia', 'Slovakia',
                   'United Kingdom', 'Kosovo']

# Defining codes for Bolivia (HASC code)
bo_si_code = ['BN', 'BN-IT', 'BN-YC', 'CB', 'CH', 'LP', 'OR',
           'PA-NA', 'PT', 'SC', 'SC-AS', 'SC-CC', 'SC-CQ',
           'SC-GB', 'SC-MI', 'SC-VC', 'SC-VL', 'TJ', 'TJ-BE',
           'TJ-OC']                                   
bo_si_full_names = ['Beni', 'Sistema It�nez', 'Sistema Yacuma', 'Cochabamba', 'Chuquisaca', 'La Paz', 'Oruro',
                 'Sistema Norte Amaz�nico', 'Potos�', 'Santa Cruz', 'Sistema San Mat�as', 'Sistema Charagua Camiri', 'Sistema Chiquitos',
                 'Sistema Germ�n Busch', 'Sistema Misiones', 'Sistema Valles Cruce�os', 'Sistema San Ignacio de Velasco', 'Tarija', 'Sistema Bermejo',
                 'Sistema Tarija Entre R�os']

# dictionnary for plotting
color_dict = {
    "ELECTRICITY": "dodgerblue",
    "GASOLINE": "gray",
    "DIESEL": "silver",
    "GASOLINE_RE": "Beige",
    "DIESEL_RE": "HoneyDew",
    "LFO": "darkviolet",
    "LFO_RE": "MediumPurple",
    "JET_FUEL": "DarkSlateGray",
    "JET_FUEL_RE": "BurlyWood",
    "GAS": "orange",
    "GAS_RE": "moccasin",
    "WOOD": "peru",
    "ENERGY_CROPS_2": "brown",
    "WET_BIOMASS": "seagreen",
    "BIOMASS_RESIDUES": "darkseagreen",
    "BIOWASTE": "yellowgreen",
    "COAL": "black",
    "URANIUM": "deeppink",
    "WASTE": "olive",
    "H2": "hotpink",
    "H2_RE": "plum",
    "AMMONIA": "slateblue",
    "AMMONIA_RE": "blue",
    "METHANOL": "orchid",
    "METHANOL_RE": "mediumvioletred",
    "CO2_EMISSIONS": "gainsboro",
    "RES_WIND": "limegreen",
    "RES_SOLAR": "yellow",
    "RES_HYDRO": "blue",
    "RES_GEO": "firebrick",
    "CO2_ATM": "dimgray",
    "CO2_INDUSTRY": "darkgrey",
    "CO2_CAPTURED": "lightslategrey",
    "PT_HEAT": "goldenrod",
    "ST_HEAT": "goldenrod",
    "NUCLEAR": "deeppink",
    "CCGT": "darkorange",
    "CCGT_AMMONIA": "slateblue",
    "COAL_US": "black",
    "COAL_IGCC": "dimgray",
    "BIOMASS_TO_POWER": "peru",
    "PV_ROOFTOP": "yellow",
    "PV_UTILITY": "gold",
    "ST_POWER_BLOCK": "goldenrod",
    "PT_POWER_BLOCK": "goldenrod",
    "WIND_ONSHORE": "lawngreen",
    "WIND_OFFSHORE": "green",
    "HYDRO_DAM": "darkslateblue",
    "HYDRO_RIVER": "blue",
    "TIDAL_STREAM": "turquoise",
    "TIDAL_RANGE": "turquoise",
    "WAVE": "paleturquoise",
    "GEOTHERMAL": "firebrick",
    "IND_COGEN_GAS": "orange",
    "IND_COGEN_WOOD": "peru",
    "IND_COGEN_WASTE": "olive",
    "IND_BOILER_GAS": "moccasin",
    "IND_BOILER_WOOD": "goldenrod",
    "IND_BOILER_BIOWASTE": "yellowgreen",
    "IND_BOILER_OIL": "blueviolet",
    "IND_BOILER_COAL": "black",
    "IND_BOILER_WASTE": "olivedrab",
    "IND_DIRECT_ELEC": "royalblue",
    "DHN_HP_ELEC": "blue",
    "DHN_COGEN_GAS": "orange",
    "DHN_COGEN_WOOD": "sandybrown",
    "DHN_COGEN_WASTE": "olive",
    # "DHN_COGEN_WET_BIOMASS" : "seagreen",
    # "DHN_COGEN_BIO_HYDROLYSIS" : "springgreen",
    "DHN_BOILER_GAS": "darkorange",
    "DHN_BOILER_WOOD": "sienna",
    "DHN_BOILER_OIL": "blueviolet",
    "DHN_DEEP_GEO": "firebrick",
    "DHN_SOLAR": "gold",
    "DEC_HP_ELEC": "cornflowerblue",
    "DEC_THHP_GAS": "lightsalmon",
    "DEC_COGEN_GAS": "goldenrod",
    "DEC_COGEN_OIL": "mediumpurple",
    "DEC_ADVCOGEN_GAS": "burlywood",
    "DEC_ADVCOGEN_H2": "hotpink",
    "DEC_BOILER_GAS": "moccasin",
    "DEC_BOILER_WOOD": "peru",
    "DEC_BOILER_OIL": "darkorchid",
    "DEC_SOLAR": "yellow",
    "DEC_DIRECT_ELEC": "deepskyblue",
    "DEC_THHP_GAS_COLD": "lightsalmon",
    "DEC_ELEC_COLD": "cyan",
    "IND_ELEC_COLD": "darkcyan",
    "TRAMWAY_TROLLEY": "dodgerblue",
    "BUS_COACH_DIESEL": "dimgrey",
    "BUS_COACH_HYDIESEL": "gray",
    "BUS_COACH_CNG_STOICH": "orange",
    "BUS_COACH_FC_HYBRIDH2": "hotpink",
    "TRAIN_PUB": "blue",
    "PLANE_SHORT_HAUL": "slategrey",
    "PLANE_H2_SHORT_HAUL": "plum",
    "PLANE_LONG_HAUL": "dimgrey",
    "CAR_GASOLINE": "black",
    "CAR_DIESEL": "lightgray",
    "CAR_NG": "moccasin",
    "CAR_METHANOL": "orchid",
    "CAR_HEV": "salmon",
    "CAR_PHEV": "lightsalmon",
    "CAR_BEV": "deepskyblue",
    "CAR_FUEL_CELL": "magenta",
    "TRAIN_FREIGHT": "royalblue",
    "BOAT_FREIGHT_DIESEL": "dimgrey",
    "BOAT_FREIGHT_NG": "darkorange",
    "BOAT_FREIGHT_METHANOL": "orchid",
    "CARGO_LFO": "dimgrey",
    "CARGO_LNG": "darkorange",
    "CARGO_METHANOL": "orchid",
    "CARGO_AMMONIA": "slateblue",
    "CARGO_FUELCELL_LH2": "plum",
    "CARGO_FUELCELL_AMMONIA": "powderblue",
    "CARGO_RETRO_METHANOL": "orchid",
    "CARGO_RETRO_AMMONIA": "paleturquoise",
    "TRUCK_DIESEL": "darkgrey",
    "TRUCK_FUEL_CELL": "hotpink",
    "TRUCK_ELEC": "dodgerblue",
    "TRUCK_NG": "moccasin",
    "TRUCK_METHANOL": "orchid",
    "EFFICIENCY": "lime",
    "DHN": "orange",
    "GRID": "gold",
    "HVAC_LINE": "dodgerblue",
    "HVDC_SUBSEA": "dodgerblue",
    "GAS_PIPELINE": "orange",
    "GAS_SUBSEA": "orange",
    "H2_RETROFITTED": "plum",
    "H2_NEW": "plum",
    "H2_SUBSEA_RETRO": "plum",
    "H2_SUBSEA_NEW": "plum",
    "PT_COLLECTOR": "goldenrod",
    "ST_COLLECTOR": "goldenrod",
    "H2_ELECTROLYSIS": "violet",
    "H2_NG": "magenta",
    "H2_BIOMASS": "orchid",
    "BIOMASS_TO_METHANE": "orangered",
    "BIOWASTE_TO_METHANE": "orangered",
    "SYN_METHANATION": "moccasin",
    "BIOMETHANATION_WET_BIOMASS": "forestgreen",
    "BIOMETHANATION_BIOWASTE": "forestgreen",
    # "BIO_HYDROLYSIS" : "forestgreen",
    "BIOMASS_TO_GASOLINE": "peru",
    "BIOMASS_TO_DIESEL": "peru",
    "BIOMASS_TO_JET_FUEL": "peru",
    "BIOMASS_TO_LFO": "peru",
    "BIOWASTE_TO_GASOLINE": "yellowgreen",
    "BIOWASTE_TO_DIESEL": "yellowgreen",
    "BIOWASTE_TO_JET_FUEL": "yellowgreen",
    "BIOWASTE_TO_LFO": "yellowgreen",
    "JET_FUEL_TO_DIESEL": "darkslategrey",
    "ATM_CCS": "black",
    "INDUSTRY_CCS": "grey",
    "SYN_METHANOLATION": "mediumpurple",
    "METHANE_TO_METHANOL": "darkmagenta",
    "BIOMASS_TO_METHANOL": "peru",
    "BIOWASTE_TO_METHANOL": "yellowgreen",
    "HABER_BOSCH": "tomato",
    "POWER_TO_GASOLINE": "dodgerblue",
    "POWER_TO_DIESEL": "dodgerblue",
    "POWER_TO_JET_FUEL": "dodgerblue",
    "POWER_TO_LFO": "dodgerblue",
    "H2_TO_GASOLINE": "hotpink",
    "H2_TO_DIESEL": "hotpink",
    "H2_TO_JET_FUEL": "hotpink",
    "H2_TO_LFO": "hotpink",
    "AMMONIA_TO_H2": "rebeccapurple",
    "OIL_TO_HVC": "blueviolet",
    "GAS_TO_HVC": "orange",
    "BIOMASS_TO_HVC": "peru",
    "METHANOL_TO_HVC": "orchid",
    "DAM_STORAGE": "darkslateblue",
    "PHS": "dodgerblue",
    "BATT_LI": "royalblue",
    "BEV_BATT": "deepskyblue",
    "PHEV_BATT": "lightskyblue",
    "TS_DEC_DIRECT_ELEC": "darkgoldenrod",
    "TS_DEC_HP_ELEC": "blue",
    "TS_DEC_THHP_GAS": "orange",
    "TS_DEC_COGEN_GAS": "coral",
    "TS_DEC_COGEN_OIL": "darkviolet",
    "TS_DEC_ADVCOGEN_GAS": "sandybrown",
    "TS_DEC_ADVCOGEN_H2": "plum",
    "TS_DEC_BOILER_GAS": "tan",
    "TS_DEC_BOILER_WOOD": "peru",
    "TS_DEC_BOILER_OIL": "darkviolet",
    "TS_DHN_DAILY": "lightcoral",
    "TS_DHN_SEASONAL": "indianred",
    "TS_HIGH_TEMP": "red",
    "GAS_STORAGE": "orange",
    "H2_STORAGE": "violet",
    "DIESEL_STORAGE": "silver",
    "JET_FUEL_STORAGE": "darkslategrey",
    "GASOLINE_STORAGE": "gray",
    "LFO_STORAGE": "darkviolet",
    "AMMONIA_STORAGE": "slateblue",
    "METHANOL_STORAGE": "orchid",
    "CO2_STORAGE": "lightgray",
    "PT_STORAGE": "goldenrod",
    "ST_STORAGE": "goldenrod",
    "TS_COLD": "cyan",
    "CAES": "orangered",
    "HEAT_HIGH_T": "red",
    "HEAT_LOW_T_HW": "lightpink",
    "HEAT_LOW_T_SH": "indianred",
    "MOBILITY_PASSENGER": "goldenrod",
    "MOBILITY_FREIGHT": "darkgoldenrod",
    "AVIATION_LONG_HAUL": "darkkhaki",
    "SHIPPING": "tan",
    "NON_ENERGY": "darkviolet",
    "PROCESS_COOLING": "darkcyan",
    "SPACE_COOLING": "cyan",
    "HEAT_LOW_T_DECEN": "lightpink",
    "HEAT_LOW_T_DHN": "indianred",
    "MOB_PUBLIC": "gold",
    "MOB_PRIVATE": "goldenrod",
    "AVIATION_SHORT_HAUL": "khaki",
    "MOB_FREIGHT_RAIL": "blanchedalmond",
    "MOB_FREIGHT_ROAD": "darkgoldenrod",
    "MOB_FREIGHT_BOAT": "burlywood",
    "INFRASTRUCTURE": "grey",
    "HVC": "indigo",
    "STORAGE": "chartreuse",
    "END_USES": "lightsteelblue",
    "OTHER": "mediumpurple",
    "OTHER_IMP": "lightgreen",
    "OTHER_LOC": "lightsalmon",
    "OTHER_PROD": "lightgreen",
    "OTHER_CONS": "lightsalmon"
}

# TODO how to differantiate imports from exterior fossil gas or h2 from exchanges with other cells?

plotting_names = {
    "ELECTRICITY": "Electricity",
    "GASOLINE": "Gasoline",
    "DIESEL": "Diesel",
    "GASOLINE_RE": "Re. gasoline",
    "DIESEL_RE": "Re. diesel",
    "LFO": "Oil",
    "LFO_RE": "Re. oil",
    "JET_FUEL": "Jet fuel",
    "JET_FUEL_RE": "Re. jet fuel",
    "GAS": "Methane",
    "GAS_RE": "Re. methane",
    "WOOD": "Woody biomass",
    "ENERGY_CROPS_2": "Energy crops (gen. 2)",
    "WET_BIOMASS": "Wet biomass",
    "BIOMASS_RESIDUES": "Biomass residues",
    "BIOWASTE": "Biowaste",
    "COAL": "Coal",
    "URANIUM": "Uranium",
    "WASTE": "Waste",
    "H2": "Hydrogen",
    "H2_RE": "Re. hydrogen",
    "AMMONIA": "Ammonia",
    "AMMONIA_RE": "Re. ammonia",
    "METHANOL": "Methanol",
    "METHANOL_RE": "Re. methanol",
    "CO2_EMISSIONS": "CO2 emissions",
    "RES_WIND": "Wind",
    "RES_SOLAR": "Solar",
    "RES_HYDRO": "Hydro",
    "RES_GEO": "Geothermal",
    "CO2_ATM": "CO2 atm.",
    "CO2_INDUSTRY": "CO2 industry",
    "CO2_CAPTURED": "CO2 captured",
    "PT_HEAT": "CSP heat",
    "ST_HEAT": "CSP heat",
    "NUCLEAR": "Nuclear",
    "CCGT": "CCGT",
    "CCGT_AMMONIA": "Ammonia CCGT",
    "COAL_US": "Coal",
    "COAL_IGCC": "Coal",
    "BIOMASS_TO_POWER": "Biomass power plant",
    "PV_ROOFTOP": "Rooftop PV",
    "PV_UTILITY": "Utility PV",
    "ST_POWER_BLOCK": "CSP power block",
    "PT_POWER_BLOCK": "CSP power block",
    "PT_COLLECTOR": "CSP collector",
    "ST_COLLECTOR": "CSP collector",
    "WIND_ONSHORE": "Onshore wind",
    "WIND_OFFSHORE": "Offshore wind",
    "HYDRO_DAM": "Hydro dam",
    "HYDRO_RIVER": "Hydro river",
    "TIDAL_STREAM": "Tidal",
    "TIDAL_RANGE": "Tidal",
    "WAVE": "Wave",
    "GEOTHERMAL": "Geothermal",
    "IND_COGEN_GAS": "Ind. cogen gas",
    "IND_COGEN_WOOD": "Ind. cogen wood",
    "IND_COGEN_WASTE": "Ind. cogen waste",
    "IND_BOILER_GAS": "Ind. boiler gas",
    "IND_BOILER_WOOD": "Ind. boiler wood",
    "IND_BOILER_BIOWASTE": "Ind. boiler biowaste",
    "IND_BOILER_OIL": "Ind. boiler oil",
    "IND_BOILER_COAL": "Ind. boiler coal",
    "IND_BOILER_WASTE": "Ind. boiler waste",
    "IND_DIRECT_ELEC": "Ind. boiler elec.",
    "DHN_HP_ELEC": "DHN heat pump",
    "DHN_COGEN_GAS": "DHN cogen gas",
    "DHN_COGEN_WOOD": "DHN cogen wood",
    "DHN_COGEN_WASTE": "DHN cogen waste",
    # "DHN_COGEN_WET_BIOMASS" : "DHN cogen wet biomass",
    # "DHN_COGEN_BIO_HYDROLYSIS" : "DHN cogen wet biomass",
    "DHN_BOILER_GAS": "DHN boiler gas",
    "DHN_BOILER_WOOD": "DHN boiler wood",
    "DHN_BOILER_OIL": "DHN boiler oil",
    "DHN_DEEP_GEO": "DHN deep geothermal",
    "DHN_SOLAR": "DHN solar thermal",
    "DEC_HP_ELEC": "Decen. heat pump",
    "DEC_THHP_GAS": "Decen. gas heat pump",
    "DEC_COGEN_GAS": "Decen. cogen gas",
    "DEC_COGEN_OIL": "Decen. cogen oil",
    "DEC_ADVCOGEN_GAS": "Decen. cogen gas (FC)",
    "DEC_ADVCOGEN_H2": "Decen. cogen H2 (FC)",
    "DEC_BOILER_GAS": "Decen. boiler gas",
    "DEC_BOILER_WOOD": "Decen. boiler wood",
    "DEC_BOILER_OIL": "Decen. boiler oil",
    "DEC_SOLAR": "Decen. solar thermal",
    "DEC_DIRECT_ELEC": "Decen. elec. heater",
    "DEC_THHP_GAS_COLD": "Decen. gas cooler",
    "DEC_ELEC_COLD": "Decen. elec. cooler",
    "IND_ELEC_COLD": "Process cooling",
    "TRAMWAY_TROLLEY": "Tram",
    "BUS_COACH_DIESEL": "Bus diesel",
    "BUS_COACH_HYDIESEL": "Bus hybrid diesel",
    "BUS_COACH_CNG_STOICH": "Bus gas",
    "BUS_COACH_FC_HYBRIDH2": "Bus hydrogen FC",
    "TRAIN_PUB": "Train pub.",
    "PLANE_SHORT_HAUL": "Short-haul plane",
    "PLANE_H2_SHORT_HAUL": "Short-haul H2 plane",
    "PLANE_LONG_HAUL": "Long-haul plane",
    "CAR_GASOLINE": "Car gasoline",
    "CAR_DIESEL": "Car diesel",
    "CAR_NG": "Car gas",
    "CAR_METHANOL": "Car methanol",
    "CAR_HEV": "Car hybrid",
    "CAR_PHEV": "Car plug-in hybrid",
    "CAR_BEV": "Car elec.",
    "CAR_FUEL_CELL": "Car fuel cell",
    "TRAIN_FREIGHT": "Train freight",
    "BOAT_FREIGHT_DIESEL": "Boat freight diesel",
    "BOAT_FREIGHT_NG": "Boat freight gas",
    "BOAT_FREIGHT_METHANOL": "Boat freight methanol",
    "CARGO_LFO": "Oil cargo",
    "CARGO_LNG": "LNG cargo",
    "CARGO_METHANOL": "Methanol cargo",
    "CARGO_AMMONIA": "Ammonia cargo",
    "CARGO_FUELCELL_LH2": "Fuel-cell H2 cargo",
    "CARGO_FUELCELL_AMMONIA": "Fuel-cell ammonia cargo",
    "CARGO_RETRO_METHANOL": "Retro. methanol cargo",
    "CARGO_RETRO_AMMONIA": "Retro. ammonia cargo",
    "TRUCK_DIESEL": "Truck diesel",
    "TRUCK_FUEL_CELL": "Truck fuel cell",
    "TRUCK_ELEC": "Truck elec.",
    "TRUCK_NG": "Truck gas",
    "TRUCK_METHANOL": "Truck methanol",
    "EFFICIENCY": "Efficiency",
    "DHN": "DHN",
    "GRID": "Elec. grid",
    "HVAC_LINE": "Elec. interconnections",
    "HVDC_SUBSEA": "Elec.interconnections subsea",
    "GAS_PIPELINE": "Gas interconnections",
    "GAS_SUBSEA": "Gas interconnections subsea",
    "H2_RETROFITTED": "H2 retrofitted interconnections",
    "H2_NEW": "H2 new interconnections",
    "H2_SUBSEA_RETRO": "H2 retrofitted interconnections subsea",
    "H2_SUBSEA_NEW": "H2 new interconnections subsea",
    "H2_ELECTROLYSIS": "Electrolyser",
    "H2_REG_ELECTROLYSER": "Regeneraive electrolyser",
    "H2_REG_FUELCELL": "Regenerative fuel-cell",
    "H2_NG": "Steam methane reforming",
    "H2_BIOMASS": "Biomass to H2",
    "BIOMASS_TO_METHANE": "Biomass to methane",
    "BIOWASTE_TO_METHANE": "Biowaste to methane",
    "SYN_METHANATION": "H2 methanation",
    "BIOMETHANATION_WET_BIOMASS": "Biomethanation",
    "BIOMETHANATION_BIOWASTE": "Biomethanation (biowaste)",
    "BIOMASS_TO_GASOLINE": "Biomass to gasoline",
    "BIOMASS_TO_DIESEL": "Biomass to diesel",
    "BIOMASS_TO_JET_FUEL": "Biomass to jet fuel",
    "BIOMASS_TO_LFO": "Biomass to oil",
    "BIOWASTE_TO_GASOLINE": "Biowaste to gasoline",
    "BIOWASTE_TO_DIESEL": "Biowaste to diesel",
    "BIOWASTE_TO_JET_FUEL": "Biowaste to jet fuel",
    "BIOWASTE_TO_LFO": "Biowaste to oil",
    "JET_FUEL_TO_DIESEL": "Jet fuel to diesel",
    "ATM_CCS": "Atmospheric CC",
    "INDUSTRY_CCS": "Industrial CC",
    "SYN_METHANOLATION": "H2 methanolation",
    "METHANE_TO_METHANOL": "Methane to methanol",
    "BIOMASS_TO_METHANOL": "Biomass to methanol",
    "BIOWASTE_TO_METHANOL": "Biowaste to methanol",
    "HABER_BOSCH": "Haber-Bosch",
    "POWER_TO_GASOLINE": "Power to gasoline",
    "POWER_TO_DIESEL": "Power to diesel",
    "POWER_TO_JET_FUEL": "Power to jet fuel",
    "POWER_TO_LFO": "Power to oil",
    "H2_TO_GASOLINE": "Hydrogen to gasoline",
    "H2_TO_DIESEL": "Hydrogen to diesel",
    "H2_TO_JET_FUEL": "Hydrogen to jet fuel",
    "H2_TO_LFO": "Hydrogen to oil",
    "AMMONIA_TO_H2": "Ammonia to H2",
    "OIL_TO_HVC": "Oil to HVC",
    "GAS_TO_HVC": "Gas to HVC",
    "BIOMASS_TO_HVC": "Biomass to HVC",
    "METHANOL_TO_HVC": "Methanol to HVC",
    "DAM_STORAGE": "Dam storage",
    "PHS": "PHS",
    "BATT_LI": "Li-ion batt.",
    "BEV_BATT": "BEV batt.",
    "PHEV_BATT": "PHEV batt.",
    "TS_DEC_DIRECT_ELEC": "Decen. thermal storage",
    "TS_DEC_HP_ELEC": "Decen. thermal storage",
    "TS_DEC_THHP_GAS": "Decen. thermal storage",
    "TS_DEC_COGEN_GAS": "Decen. thermal storage",
    "TS_DEC_COGEN_OIL": "Decen. thermal storage",
    "TS_DEC_ADVCOGEN_GAS": "Decen. thermal storage",
    "TS_DEC_ADVCOGEN_H2": "Decen. thermal storage",
    "TS_DEC_BOILER_GAS": "Decen. thermal storage",
    "TS_DEC_BOILER_WOOD": "Decen. thermal storage",
    "TS_DEC_BOILER_OIL": "Decen. thermal storage",
    "TS_DHN_DAILY": "DHN daily storage",
    "TS_DHN_SEASONAL": "DHN seasonal storage",
    "TS_HIGH_TEMP": "High temperature storage",
    "GAS_STORAGE": "Gas storage",
    "H2_STORAGE": "H2 storage",
    "DIESEL_STORAGE": "Diesel storage",
    "JET_FUEL_STORAGE": "Jet fuel storage",
    "GASOLINE_STORAGE": "Gasoline storage",
    "LFO_STORAGE": "Oil storage",
    "AMMONIA_STORAGE": "Ammonia storage",
    "METHANOL_STORAGE": "Methanol storage",
    "CO2_STORAGE": "CO2 storage",
    "PT_STORAGE": "CSP storage",
    "ST_STORAGE": "CSP storage",
    "TS_COLD": "Cold storage",
    "CAES": "CAES",
    "HEAT_HIGH_T": "Heat high temp.",
    "HEAT_LOW_T_HW": "Hot water",
    "HEAT_LOW_T_SH": "Space heating",
    "MOBILITY_PASSENGER": "Passenger mobility",
    "MOBILITY_FREIGHT": "Freight",
    "AVIATION_LONG_HAUL": "Long-haul aviation",
    "SHIPPING": "Shipping",
    "NON_ENERGY": "Non-energy",
    "PROCESS_COOLING": "Process cooling",
    "SPACE_COOLING": "Space cooling",
    "HEAT_LOW_T_DECEN": "Decen. low temp. heat",
    "HEAT_LOW_T_DHN": "DHN low temp. heat",
    "MOB_PUBLIC": "Public mobility",
    "MOB_PRIVATE": "Private mobility",
    "AVIATION_SHORT_HAUL": "Short-haul aviation",
    "MOB_FREIGHT_RAIL": "Rail freight",
    "MOB_FREIGHT_ROAD": "Road freight",
    "MOB_FREIGHT_BOAT": "Boat freight",
    "INFRASTRUCTURE": "Infrastructure",
    "HVC": "HVC",
    "STORAGE": "Storage",
    "END_USES": "End uses",
    "OTHER": "Other",
    "OTHER_IMP": "Other import",
    "OTHER_LOC": "Other local",
    "OTHER_PROD": "Other prod.",
    "OTHER_CONS": "Other cons."
}

color_d_names = {plotting_names[i]: j for i, j in color_dict.items()}
