import pandas as pd
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import Descriptors

df=pd.read_csv(r'C:\Users\E\AppData\Local\Temp\tox21.csv')
target="NR-AR"

df_clean=df[["smiles",target]].dropna()

def calculate_mol(smiles):
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    properties={
        "mol_weight":Descriptors.MolWt(mol),
        "LogP":Descriptors.MolLogP(mol),
        "NumHDonors":Descriptors.NumHDonors(mol),
        "NumHAcceptors":Descriptors.NumHAcceptors(mol),
        "NumRotatableBonds":Descriptors.NumRotatableBonds(mol),
        "NumAromaticRings":Descriptors.NumAromaticRings(mol)


    }
    return properties

property_list=[]

for smiles in df_clean["smiles"]:
    molecules=calculate_mol(smiles)
    if molecules is not None:
        property_list.append(molecules)
    else:
        property_list.append({k:None for k in ["mol_weight", "LogP", "NumHDonors", "NumHAcceptors", "NumRotatableBonds", "NumAromaticRings"]})

property_df=pd.DataFrame(property_list)
print(property_df.head())

"""
print(df_clean.head())
print(f"Rows:{len(df_clean)}")
print(f"Columns:{len(df_clean.columns)}")
print(f"Not Toxic:{len(df_clean)-df_clean[target].sum()}")
print(df_clean.columns.tolist())
"""
