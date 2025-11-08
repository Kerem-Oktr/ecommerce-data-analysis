import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
dataset_1 = "customer_details.csv"
dataset_2 = "basket_details.csv"
dFrame_1 = pd.read_csv(dataset_1)
dFrame_2 = pd.read_csv(dataset_2)
df_3 = pd.merge(dFrame_1,dFrame_2, on="customer_id", how="outer")
df_3["sex"] = df_3["sex"].fillna("Unknown")
df_3["customer_age"] = df_3["customer_age"].fillna("Unknown")
df_3["tenure"] = df_3["tenure"].fillna("Unknown")
df_3["product_id"] = df_3["product_id"].fillna("Unknown")
df_3["basket_date"] = df_3["basket_date"].fillna("Unknown")
df_3["basket_count"] = df_3["basket_count"].fillna("Unknown")
satisPerformansi = df_3["product_id"].value_counts()
if 'Unknown' in satisPerformansi.index:
    satisPerformansi = satisPerformansi.drop('Unknown')
    print("Not: 'Unknown' kategorisi (varsa) grafikten çıkarıldı.")
en_iyi_35_urun = satisPerformansi.head(35)
adf = df_3.copy()
adf = adf[adf['basket_date'] != 'Unknown']
adf['basket_date'] = pd.to_datetime(adf['basket_date'])
adf['basket_count'] = pd.to_numeric(adf['basket_count'], errors='coerce')
adf['basket_count'] = adf['basket_count'].fillna(0)
adf = adf.set_index('basket_date') 
gunluk_hacim = adf['basket_count'].resample('D').sum()
plt.figure(figsize=(18, 8))
plt.plot(gunluk_hacim.index, gunluk_hacim.values, linestyle='-', marker='o', markersize=3) 
plt.title('Daily Sales Volume Over Time (Total Product Quantity)')
plt.xlabel('Date')
plt.ylabel('Total Product Quantity')
plt.grid(True)
plt.tight_layout()
plt.show()
#Showing Daily Sales Volume Over Time
plt.bar(en_iyi_35_urun.index.astype(str),en_iyi_35_urun.values)
plt.xlabel("Product ID")
plt.ylabel("Count of sold product")
plt.xticks(rotation=90)
#Showing Sales Perfromance
plt.show()
