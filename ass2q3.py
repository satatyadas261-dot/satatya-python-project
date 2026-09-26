import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
corr = df.corr()
mask = np.eye(len(corr), dtype=bool)
flat_corr = corr.where(~mask).stack().sort_values(ascending=False)
pair = None
for (feature1, feature2), value in flat_corr.items():
    if value > 0:
        pair = (feature1, feature2, value)
        break
plt.figure(figsize=(12, 9))
sns.heatmap(corr, annot=False, cmap='coolwarm', fmt='.2f')
plt.title('Wine Dataset Correlation Heatmap')
plt.tight_layout()
plt.savefig('wine_correlation_heatmap.png')
plt.close()

print('Strongest positive correlation pair:')
print(pair[0], 'and', pair[1], 'with correlation =', round(pair[2], 4))
print('Heatmap saved as wine_correlation_heatmap.png')
