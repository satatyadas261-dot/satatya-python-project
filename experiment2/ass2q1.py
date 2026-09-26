from sklearn.datasets import load_wine
import pandas as pd
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target
print("--- First 5 rows ---")
print(df.head())
print("\n--- Dataset info ---")
print(df.info())
print("\n--- Summary statistics ---")
print(df.describe())
print("\n--- Missing values ---")
print(df.isnull().sum())
print("\n--- Target distribution ---")
print(df['target'].value_counts())
print("\n--- Correlation matrix ---")
print(df.corr(numeric_only=True).round(2))
