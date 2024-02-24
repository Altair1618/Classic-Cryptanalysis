import os


dict = {
    "AT": "LA",
    "AH": "LT",
    "AE": "LH",
    "AL": "LE",
    "AI": "XA",
    "AZ": "TI",
    "AY": "HI",
    "AQ": "EI",
    "AU": "LI",
    "AG": "XI",
    "AC": "TG",
    "AK": "HG",
    "AD": "EG",
    "AO": "LG",
    "AS": "XG",
    "AV": "TS",
    "AR": "HS",
    "AM": "ES",
    "AP": "LS",
    "AX": "XS",
    "AB": "TX",
    "AW": "HX",
    "AN": "EX",
    "AF": "LX",
    "TA": "AL",
    "TH": "AT",
    "TE": "AH",
    "TL": "AE",
    "TI": "AZ",
    "TZ": "BT",
    "TY": "HZ",
    "TQ": "EZ",
    "TU": "LZ",
    "TG": "AC",
    "TC": "BZ",
    "TK": "HC",
    "TD": "EC",
    "TO": "LC",
    "TS": "AV",
    "TV": "BC",
    "TR": "HV",
    "TM": "EV",
    "TP": "LV",
    "TX": "AB",
    "TB": "BV",
    "TW": "HB",
    "TN": "EB",
    "TF": "LB",
    "HA": "TL",
    "HT": "TA",
    "HE": "TH",
    "HL": "TE",
    "HI": "AY",
    "HZ": "TY",
    "HY": "WH",
    "HQ": "EY",
    "HU": "LY",
    "HG": "AK",
    "HC": "TK",
    "HK": "WY",
    "HD": "EK",
    "HO": "LK",
    "HS": "AR",
    "HV": "TR",
    "HR": "WK",
    "HM": "ER",
    "HP": "LR",
    "HX": "AW",
    "HB": "TW",
    "HW": "WR",
    "HN": "EW",
    "HF": "LW",
    "EA": "HL",
    "ET": "HA",
    "EH": "HT",
    "EL": "HE",
    "EI": "AQ",
    "EZ": "TQ",
    "EY": "HQ",
    "EQ": "NE",
    "EU": "LQ",
    "EG": "AD",
    "EC": "TD",
    "EK": "HD",
    "ED": "NQ",
    "EO": "LD",
    "ES": "AM",
    "EV": "TM",
    "ER": "HM",
    "EM": "ND",
    "EP": "LM",
    "EX": "AN",
    "EB": "TN",
    "EW": "HN",
    "EN": "NM",
    "EF": "LN",
    "LA": "EL",
    "LT": "EA",
    "LH": "ET",
    "LE": "EH",
    "LI": "AU",
    "LZ": "TU",
    "LY": "HU",
    "LQ": "EU",
    "LU": "FL",
    "LG": "AO",
    "LC": "TO",
    "LK": "HO",
    "LD": "EO",
    "LO": "FU",
    "LS": "AP",
    "LV": "TP",
    "LR": "HP",
    "LM": "EP",
    "LP": "FO",
    "LX": "AF",
    "LB": "TF",
    "LW": "HF",
    "LN": "EF",
    "LF": "FP",
    "IA": "AX",
    "IT": "ZA",
    "IH": "YA",
    "IE": "QA",
    "IL": "UA",
    "IZ": "UI",
    "IY": "UZ",
    "IQ": "UY",
    "IU": "UQ",
    "IG": "AI",
    "IC": "ZG",
    "IK": "YG",
    "ID": "QG",
    "IO": "UG",
    "IS": "AG",
    "IV": "ZS",
    "IR": "YS",
    "IM": "QS",
    "IP": "US",
    "IX": "AS",
    "IB": "ZX",
    "IW": "YX",
    "IN": "QX",
    "IF": "UX",
    "ZA": "IT",
    "ZT": "TB",
    "ZH": "YT",
    "ZE": "QT",
    "ZL": "UT",
    "ZI": "IU",
    "ZY": "IZ",
    "ZQ": "IY",
    "ZU": "IQ",
    "ZG": "IC",
    "ZC": "TZ",
    "ZK": "YC",
    "ZD": "QC",
    "ZO": "UC",
    "ZS": "IV",
    "ZV": "TC",
    "ZR": "YV",
    "ZM": "QV",
    "ZP": "UV",
    "ZX": "IB",
    "ZB": "TV",
    "ZW": "YB",
    "ZN": "QB",
    "ZF": "UB",
    "YA": "IH",
    "YT": "ZH",
    "YH": "HW",
    "YE": "QH",
    "YL": "UH",
    "YI": "ZU",
    "YZ": "ZI",
    "YQ": "ZY",
    "YU": "ZQ",
    "YG": "IK",
    "YC": "ZK",
    "YK": "HY",
    "YD": "QK",
    "YO": "UK",
    "YS": "IR",
    "YV": "ZR",
    "YR": "HK",
    "YM": "QR",
    "YP": "UR",
    "YX": "IW",
    "YB": "ZW",
    "YW": "HR",
    "YN": "QW",
    "YF": "UW",
    "QA": "IE",
    "QT": "ZE",
    "QH": "YE",
    "QE": "EN",
    "QL": "UE",
    "QI": "YU",
    "QZ": "YI",
    "QY": "YZ",
    "QU": "YQ",
    "QG": "ID",
    "QC": "ZD",
    "QK": "YD",
    "QD": "EQ",
    "QO": "UD",
    "QS": "IM",
    "QV": "ZM",
    "QR": "YM",
    "QM": "ED",
    "QP": "UM",
    "QX": "IN",
    "QB": "ZN",
    "QW": "YN",
    "QN": "EM",
    "QF": "UN",
    "UA": "IL",
    "UT": "ZL",
    "UH": "YL",
    "UE": "QL",
    "UL": "LF",
    "UI": "QU",
    "UZ": "QI",
    "UY": "QZ",
    "UQ": "QY",
    "UG": "IO",
    "UC": "ZO",
    "UK": "YO",
    "UD": "QO",
    "UO": "LU",
    "US": "IP",
    "UV": "ZP",
    "UR": "YP",
    "UM": "QP",
    "UP": "LO",
    "UX": "IF",
    "UB": "ZF",
    "UW": "YF",
    "UN": "QF",
    "UF": "LP",
    "GA": "IX",
    "GT": "CA",
    "GH": "KA",
    "GE": "DA",
    "GL": "OA",
    "GI": "IA",
    "GZ": "CI",
    "GY": "KI",
    "GQ": "DI",
    "GU": "OI",
    "GC": "OG",
    "GK": "OC",
    "GD": "OK",
    "GO": "OD",
    "GS": "IG",
    "GV": "CS",
    "GR": "KS",
    "GM": "DS",
    "GP": "OS",
    "GX": "IS",
    "GB": "CX",
    "GW": "KX",
    "GN": "DX",
    "GF": "OX",
    "CA": "GT",
    "CT": "ZB",
    "CH": "KT",
    "CE": "DT",
    "CL": "OT",
    "CI": "GZ",
    "CZ": "ZT",
    "CY": "KZ",
    "CQ": "DZ",
    "CU": "OZ",
    "CG": "GO",
    "CK": "GC",
    "CD": "GK",
    "CO": "GD",
    "CS": "GV",
    "CV": "ZC",
    "CR": "KV",
    "CM": "DV",
    "CP": "OV",
    "CX": "GB",
    "CB": "ZV",
    "CW": "KB",
    "CN": "DB",
    "CF": "OB",
    "KA": "GH",
    "KT": "CH",
    "KH": "YW",
    "KE": "DH",
    "KL": "OH",
    "KI": "GY",
    "KZ": "CY",
    "KY": "YH",
    "KQ": "DY",
    "KU": "OY",
    "KG": "CO",
    "KC": "CG",
    "KD": "CK",
    "KO": "CD",
    "KS": "GR",
    "KV": "CR",
    "KR": "YK",
    "KM": "DR",
    "KP": "OR",
    "KX": "GW",
    "KB": "CW",
    "KW": "YR",
    "KN": "DW",
    "KF": "OW",
    "DA": "GE",
    "DT": "CE",
    "DH": "KE",
    "DE": "QN",
    "DL": "OE",
    "DI": "GQ",
    "DZ": "CQ",
    "DY": "KQ",
    "DQ": "QE",
    "DU": "OQ",
    "DG": "KO",
    "DC": "KG",
    "DK": "KC",
    "DO": "KD",
    "DS": "GM",
    "DV": "CM",
    "DR": "KM",
    "DM": "QD",
    "DP": "OM",
    "DX": "GN",
    "DB": "CN",
    "DW": "KN",
    "DN": "QM",
    "DF": "ON",
    "OA": "GL",
    "OT": "CL",
    "OH": "KL",
    "OE": "DL",
    "OL": "UF",
    "OI": "GU",
    "OZ": "CU",
    "OY": "KU",
    "OQ": "DU",
    "OU": "UL",
    "OG": "DO",
    "OC": "DG",
    "OK": "DC",
    "OD": "DK",
    "OS": "GP",
    "OV": "CP",
    "OR": "KP",
    "OM": "DP",
    "OP": "UO",
    "OX": "GF",
    "OB": "CF",
    "OW": "KF",
    "ON": "DF",
    "OF": "UP",
    "SA": "GX",
    "ST": "VA",
    "SH": "RA",
    "SE": "MA",
    "SL": "PA",
    "SI": "GA",
    "SZ": "VI",
    "SY": "RI",
    "SQ": "MI",
    "SU": "PI",
    "SG": "GI",
    "SC": "VG",
    "SK": "RG",
    "SD": "MG",
    "SO": "PG",
    "SV": "PS",
    "SR": "PV",
    "SM": "PR",
    "SP": "PM",
    "SX": "GS",
    "SB": "VX",
    "SW": "RX",
    "SN": "MX",
    "SF": "PX",
    "VA": "ST",
    "VT": "CB",
    "VH": "RT",
    "VE": "MT",
    "VL": "PT",
    "VI": "SZ",
    "VZ": "CT",
    "VY": "RZ",
    "VQ": "MZ",
    "VU": "PZ",
    "VG": "SC",
    "VC": "CZ",
    "VK": "RC",
    "VD": "MC",
    "VO": "PC",
    "VS": "SP",
    "VR": "SV",
    "VM": "SR",
    "VP": "SM",
    "VX": "SB",
    "VB": "CV",
    "VW": "RB",
    "VN": "MB",
    "VF": "PB",
    "RA": "SH",
    "RT": "VH",
    "RH": "KW",
    "RE": "MH",
    "RL": "PH",
    "RI": "SY",
    "RZ": "VY",
    "RY": "KH",
    "RQ": "MY",
    "RU": "PY",
    "RG": "SK",
    "RC": "VK",
    "RK": "KY",
    "RD": "MK",
    "RO": "PK",
    "RS": "VP",
    "RV": "VS",
    "RM": "VR",
    "RP": "VM",
    "RX": "SW",
    "RB": "VW",
    "RW": "KR",
    "RN": "MW",
    "RF": "PW",
    "MA": "SE",
    "MT": "VE",
    "MH": "RE",
    "ME": "DN",
    "ML": "PE",
    "MI": "SQ",
    "MZ": "VQ",
    "MY": "RQ",
    "MQ": "DE",
    "MU": "PQ",
    "MG": "SD",
    "MC": "VD",
    "MK": "RD",
    "MD": "DQ",
    "MO": "PD",
    "MS": "RP",
    "MV": "RS",
    "MR": "RV",
    "MP": "RM",
    "MX": "SN",
    "MB": "VN",
    "MW": "RN",
    "MN": "DM",
    "MF": "PN",
    "PA": "SL",
    "PT": "VL",
    "PH": "RL",
    "PE": "ML",
    "PL": "OF",
    "PI": "SU",
    "PZ": "VU",
    "PY": "RU",
    "PQ": "MU",
    "PU": "OL",
    "PG": "SO",
    "PC": "VO",
    "PK": "RO",
    "PD": "MO",
    "PO": "OU",
    "PS": "MP",
    "PV": "MS",
    "PR": "MV",
    "PM": "MR",
    "PX": "SF",
    "PB": "VF",
    "PW": "RF",
    "PN": "MF",
    "PF": "OP",
    "XA": "SX",
    "XT": "BA",
    "XH": "WA",
    "XE": "NA",
    "XL": "FA",
    "XI": "SA",
    "XZ": "BI",
    "XY": "WI",
    "XQ": "NI",
    "XU": "FI",
    "XG": "SI",
    "XC": "BG",
    "XK": "WG",
    "XD": "NG",
    "XO": "FG",
    "XS": "SG",
    "XV": "BS",
    "XR": "WS",
    "XM": "NS",
    "XP": "FS",
    "XB": "FX",
    "XW": "FB",
    "XN": "FW",
    "XF": "FN",
    "BA": "XT",
    "BT": "VB",
    "BH": "WT",
    "BE": "NT",
    "BL": "FT",
    "BI": "XZ",
    "BZ": "VT",
    "BY": "WZ",
    "BQ": "NZ",
    "BU": "FZ",
    "BG": "XC",
    "BC": "VZ",
    "BK": "WC",
    "BD": "NC",
    "BO": "FC",
    "BS": "XV",
    "BV": "VC",
    "BR": "WV",
    "BM": "NV",
    "BP": "FV",
    "BX": "XF",
    "BW": "XB",
    "BN": "XW",
    "BF": "XN",
    "WA": "XH",
    "WT": "BH",
    "WH": "RW",
    "WE": "NH",
    "WL": "FH",
    "WI": "XY",
    "WZ": "BY",
    "WY": "RH",
    "WQ": "NY",
    "WU": "FY",
    "WG": "XK",
    "WC": "BK",
    "WK": "RY",
    "WD": "NK",
    "WO": "FK",
    "WS": "XR",
    "WV": "BR",
    "WR": "RK",
    "WM": "NR",
    "WP": "FR",
    "WX": "BF",
    "WB": "BX",
    "WN": "BW",
    "WF": "BN",
    "NA": "XE",
    "NT": "BE",
    "NH": "WE",
    "NE": "MN",
    "NL": "FE",
    "NI": "XQ",
    "NZ": "BQ",
    "NY": "WQ",
    "NQ": "ME",
    "NU": "FQ",
    "NG": "XD",
    "NC": "BD",
    "NK": "WD",
    "ND": "MQ",
    "NO": "FD",
    "NS": "XM",
    "NV": "BM",
    "NR": "WM",
    "NM": "MD",
    "NP": "FM",
    "NX": "WF",
    "NB": "WX",
    "NW": "WB",
    "NF": "WN",
    "FA": "XL",
    "FT": "BL",
    "FH": "WL",
    "FE": "NL",
    "FL": "PF",
    "FI": "XU",
    "FZ": "BU",
    "FY": "WU",
    "FQ": "NU",
    "FU": "PL",
    "FG": "XO",
    "FC": "BO",
    "FK": "WO",
    "FD": "NO",
    "FO": "PU",
    "FS": "XP",
    "FV": "BP",
    "FR": "WP",
    "FM": "NP",
    "FP": "PO",
    "FX": "NF",
    "FB": "NX",
    "FW": "NB",
    "FN": "NW",
}

def main():
    s = ""

    with open(os.path.join(os.path.dirname(__file__), "playfair_raw.txt"), "r") as file:
        content = file.read()

        i = 0
        # for i in range(0, len(content), 2):
        while i < len(content):
            if content[i] == "\n":
                s += "\n"
                i += 1
            
            if content[i:i + 2] in dict:
                s += dict[content[i:i + 2]]
            elif content[i + 1] + content[i] in dict:
                s += dict[content[i + 1] + content[i]][::-1]
            else:
                # s += content[i:i + 2]
                s += "__"
            
            i += 2

    with open(os.path.join(os.path.dirname(__file__), "substituted.txt"), "w") as file:
        file.write(s)


if __name__ == "__main__":
    main()
