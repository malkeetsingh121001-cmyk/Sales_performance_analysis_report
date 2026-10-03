import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# sales_analysis.xlsx
while True:
    user=input("Enter original file name (.xlsx): ")
    if ".xlsx" in user:
        df=pd.read_excel(user)
        print("<--Raw Data-->\n")
        print(f"{df}\n")
        break
    else:
        print("Try again\n")
print("---------------------------------------\n")
# revenue column add
name=["Unit_Price","Quantity"]
for col in name:
    df[col]=df[col].astype(float)
df["Revenue"]=df["Unit_Price"]*df["Quantity"]
print("<--Revenue column added-->\n")
print(f"{df}\n")
print("------------------------------------------\n")
# total revenue
df1=df["Revenue"].sum()
print(f"Total revenue: {df1}\n")
# average order
df2=df["Order_ID"].count()
print(f"Average orders: {df2}\n")
print("--------------------------------------------\n")
df3=df.sort_values("Quantity",ascending=True)
print(f"Highest order: {df["Order_ID"].iloc[-1]},\nRevenue: {df3["Revenue"].iloc[-1]}\n")
print("--------------------------------------------\n")
print(f"Lowest order: {df3["Order_ID"].iloc[1]},\nRevenue: {df["Revenue"].iloc[1]}\n")
print("--------------------------------------------\n")
print(f"Total orders: {len(df3["Order_ID"])}\n")
print("--------------------------------------------\n")
print(f"Total quantity sold: {df3["Quantity"].sum()}")
print("--------------------------------------------\n")
# category analysis
df4=df.groupby("Category")["Revenue"].sum()
df5=df.groupby("City")["Revenue"].sum()
df6=df.groupby("Salesperson")["Revenue"].sum()
print(f"Category wise revenue:\n{df4}\n")
print("--------------------------------------------\n")
print(f"City wise revenue:\n{df5}\n")
print("--------------------------------------------\n")
print(f"Revenue by salesperson:\n{df6}\n")
print("--------------------------------------------\n")
print(f"Top product is:{df3["Product"].iloc[-1]},\nRevenue: {df3["Revenue"].iloc[-1]}")
print("--------------------------------------------\n")
plt.bar(df4.index,df4.values)
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.title("Catergory wise revenue")
plt.show()
print("<--Visualization completed-->\n")
print("-----------------------------------------------\n")
# save
df.reset_index(drop=True).to_csv("processed_sales_data.csv")
print("File saved with the name processed_sales_data.csv\n")