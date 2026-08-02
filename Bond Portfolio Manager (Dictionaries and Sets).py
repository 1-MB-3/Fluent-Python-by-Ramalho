bonds = {

    "UST_10Y": {
        "issuer": 'US Treasury',
        "maturity": 10,
        "coupon": 4.25,
        "face_value": 1000.0
    },

    "DBR_5Y": {
        "issuer": 'German Bund',
        "maturity": 5,
        "coupon": 2.50,
        "face_value": 1000.0
    },

    "UKT_30Y": {
        "issuer": 'UK Gilt',
        "maturity": 30,
        "coupon": 4.75,
        "face_value": 1000.0
    }

}

bonds["JGB_2Y"] = {
    
    "issuer": 'Japan Govt',
    "maturity": 2,
    "coupon": 0.10,
    "face_value": 1000.0

}

print(bonds.get("UST_2Y", "Bond not found"))

low_yield = {"DBR_5Y", "JGB_2Y"}

high_yield = {"UST_10Y", "UKT_30Y"}

print(low_yield & high_yield)

print(low_yield | high_yield)

for bond_id, details in bonds.items():

    print(f"{bond_id} | {details['issuer']} | {details['maturity']}Y | {details['coupon']}%")
