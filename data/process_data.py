import pandas as pd

df = pd.read_csv("open_pubs_2020-07.csv")
df_lookup = pd.read_csv("country_lookup.csv")

assert set(df.local_authority.unique()).issubset(
    set(df_lookup.local_authority.unique())
), "Check the country lookup table."
df = pd.merge(df, df_lookup, on="local_authority")

df = df.query("country == 'England'")
df_count = df.groupby("local_authority")["fsa_id"].count().reset_index().rename(columns={"fsa_id": "count"})

df_processed = pd.merge(df, df_count, on="local_authority")
df_processed.to_csv("pubs_in_england.csv", index=False)