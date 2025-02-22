import pandas as pd

#   loads rental car data csv
df = pd.read_csv("messy_rental_data.csv")

#   display all data
print(df)

#   check for bad customer name
bad_names = [""]

for index, name in df['Customer_Name'].items():
    if not isinstance(name, str):
        print(f"Row {index}: Bad Name (Not String): {name}")
        df.loc[index, 'Customer_Name'] = "Unknown"
    elif name.strip() == "": #Check if name is just whitespace
        print(f"Row {index}: Bad Name (Just whitespace): {name}")
        df.loc[index, 'customer_name'] = "Unknown"