#%%
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

df = pd.read_csv("GDPlist.csv")
df['Country']= df['Country'].map(lambda x:x.lstrip('�'))
df['Continent'].unique()

# %%
df['GDP (millions of US$)'].describe()

# %%
print (stats.ttest_1samp(df['GDP (millions of US$)'] ,9.6089))

# %%
print("Do pvalue < 0.01 –>, chấp nhận giả thuyết đối")
print("Trung bình GDP của các quốc gia trên thế giới không phải là 500 tỉ usd/năm")
#%%
df_Asia = df.groupby(df['Continent'] == 'Asia').mean()
df_Asia

# %%
df_Eu = df.groupby(df['Continent'] == 'Europe').mean()
df_Eu

# %%
print (stats.ttest_ind(df_Asia, df_Eu,equal_var=False))
print("Chúng ta nhìn thấy rằng: pvalue > 5% nên không đủ cơ sở để bác bỏ giả thuyết không \n Kết luận: Không đủ căn cứ để kết luận rằng GDP trung bình ở các quốc gia ở châu Âu cao hơn châu Á")
# %%
df_NA = df.groupby(df['Continent'] == 'North America').mean()
df_NA
#%%
df_Eu = df.groupby(df['Continent'] == 'Europe').mean()
df_Eu

# %%
print (stats.ttest_ind(df_NA, df_Eu,equal_var=False))
print("Chúng ta nhìn thấy rằng: pvalue > 5% nên không đủ cơ sở để bác bỏ giả thuyết không \n Kết luận: Không đủ căn cứ để kết luận rằng GDP trung bình ở các quốc gia ở châu Âu cao hơn châu Á")

# %%
