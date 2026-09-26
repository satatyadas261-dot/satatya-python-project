from sklearn.datasets import load_wine
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df.boxplot(figsize=(14, 8))
plt.title('Boxplots for Wine Dataset Features')
plt.ylabel('Values')
plt.tight_layout()
plt.savefig('wine_boxplots.png')
plt.close()
print('Boxplot saved as wine_boxplots.png')
