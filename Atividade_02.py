import pandas as pd


arquivo = "POP2025_20260828.xls"

df_uf = pd.read_excel(arquivo, sheet_name=0, header=1)
df_mun = pd.read_excel(arquivo, sheet_name=1, header=1)

# Limpa
df_uf = df_uf.dropna(how='all')
df_mun = df_mun.dropna(how='all')
# Remove colunas vazias com nome Unnamed
df_mun = df_mun.loc[:, ~df_mun.columns.str.contains('^Unnamed')]
df_uf = df_uf.loc[:, ~df_uf.columns.str.contains('^Unnamed')]

print("=== POPULAÇÃO BRASIL E UFs ===")
print(df_uf.head(10))

print("\n=== POPULAÇÃO MUNICÍPIOS (10 primeiros) ===")
print(df_mun.head(10))

print(f"\nTotal de municípios: {len(df_mun)}")

# SC
df_sc = df_mun[df_mun['UF'] == 'SC']
print(f"\n=== SC TEM {len(df_sc)} MUNICÍPIOS ===")
print(df_sc.head(10))