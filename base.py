import pandas as pd
from matplotlib import pyplot as plt

import seaborn as sns

df = pd.read_csv('data_files/hero_base.csv')
atk_df = df.drop(['STR', 'STR+', 'STR25', 'AGI', 'AGI+', 'AGI25', 'INT', 'INT+', 'INT25', 'T', 'T+',
                  'T25', 'MS', 'AR', 'DMG_MIN', 'DMG_MAX', 'RG', 'BAT', 'VS-D', 'VS-N', 'TR', 'COL', 'HPReg', 'L'], axis=1)
print atk_df

attribute_type_colors = ['#ff0000', '#0000ff', "#00ff00"]

sns.set_style('whitegrid')
# sns.lmplot(x='ATK_S', y='DMG_MAX', data=df, hue='Attribute', fit_reg=False)
# sns.violinplot(x="Attribute", y="AGI+", data=df, palette=attribute_type_colors, inner=None)
# sns.swarmplot(x="Attribute", y="AGI+", data=df, color='k', alpha=0.7)
sns.boxplot(data=atk_df)

plt.plot()
plt.show()

