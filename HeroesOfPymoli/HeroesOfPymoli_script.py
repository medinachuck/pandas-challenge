# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

# Display total number of players 
#print(purchase_data.dtypes) 
SN = purchase_data['SN']
Total_Players = pd.DataFrame([len(SN.unique())])
Total_Players.rename(columns={0: "Total Players"})

#number unique items 
items = purchase_data['Item Name']
number_unique_items = pd.Series(len(items.unique()))
#average price 
average_price = pd.Series(purchase_data['Price'].mean()) 
average_price = '$' + round(average_price, 2).astype(str) 
#Number Purchases 




player_purchases = pd.DataFrame(SN.value_counts()).reset_index()
print(player_purchases.head())
#ballers bought more than one thing
ballers = pd.Series().astype(float)
# for i in range(576):
#     if player_purchases['SN'][i] >= 2:
#         ballers = player_purchases['index'][i-1]
#     else: pass 
# ballers

