import pandas as pd

def get_pink_mosels_sales(file_path):
    df = pd.read_csv(file_path)
    pink = df[df["product"] == "pink morsel"]
    pink["sales"] = pink["quantity"].astype(int) * pink["price"].replace('[\$,]', '', regex=True).astype(float)
    pink = pink.drop(columns=["price", "quantity"])
    return pink

df1 = get_pink_mosels_sales("./data/daily_sales_data_0.csv")
df2 = get_pink_mosels_sales("./data/daily_sales_data_1.csv")
df3 = get_pink_mosels_sales("./data/daily_sales_data_2.csv")

combined = pd.concat([df1, df2, df3], ignore_index=True)

new_order = ["product", "sales", "date", "region"]
combined = combined[new_order]
print(combined.head())

combined[["sales", "date", "region"]].to_csv("./output/pink_mosels_sales.csv", index=False)