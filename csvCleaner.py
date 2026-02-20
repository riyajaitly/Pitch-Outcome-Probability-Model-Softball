import pandas as pd


df = pd.read_csv("Tritons_Pitches_2025.csv")


model_cols = [
    "pitchOutcome",
    "Vel",
    "PXNorm",
    "PZNorm",
    "x",
    "y",
    "pitchType",
    "count",
    "outs",
    "inn",
    "batterHand",
    "pitcherHand",
    "batter",
    "pitcher",
    "battingTeam",
    "pitchingTeam",
    "pitchOutcome",
    "Vel",
    "PXNorm",
    "PZNorm",
    "pitchType",
    "count"
]


df_clean = df.replace("", pd.NA)
df_clean = df_clean[model_cols]
df_clean = df_clean.dropna()
df_clean = df_clean.reset_index(drop=True)


df_clean.to_csv("Tritons_Pitches_2025_cleaned.csv", index=False)