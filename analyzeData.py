import pandas as pd
import numpy as np
import re
import datetime as date
#   list of valid car models
#   car_models = [ "Toyota Camry", "Honda Civic", "Ford F-150"]



#   loads rental car data csv
df = pd.read_csv("messy_rental_data_updated.csv")

#   replace customer name as INV
ndf = df.replace("???", "INV")

ndf = ndf.replace(np.nan,"INV")
#

def validatePhoneNumber():
    ndf["Phone_Number"] = ndf["Phone_Number"].astype(str)

    def check_number(num):
        if num.isdigit() and len(num) == 10:  # Valid 10-digit number
            return num
        return "0"  # Replace invalid numbers with 0
    ndf["Phone_Number"] = ndf["Phone_Number"].apply(check_number)

#   replace invalid emails with INV
ndf = ndf.replace("not_an_email", "INV")

#   convert dates to str
ndf['Rental_End_Date'] = ndf['Rental_End_Date'].astype(str)

ndf = ndf.replace(to_replace='00/00/0000', value='INV', regex=True)

# for date in ndf['Rental_End_Date']:
#     if isinstance(date, str):
#         if "00/" in date:
#             date = "INV"


validatePhoneNumber()
print(ndf)

# validatePhoneNumber()
# for index, name in df['Customer_Name'].items():
#     if not isinstance(name, str):
#         print(f"Row {index}: Bad Name (Not String): {name}")
#         df.loc[index, 'Customer_Name'] = "Unknown"
    #     elif name.strip() == "": #Check if name is just whitespace
    #         print(f"Row {index}: Bad Name (Just whitespace): {name}")
    #         df.loc[index, 'customer_name'] = "Unknown"

    # def validate():
    #     def validateName(name):
    #         for name in df['Customer_Name']:
    #             if not isinstance(name, str):
    #                 return False
    #             #   check if name is only letters or whitespace
    #             if not re.match('^[a-zZ-A\\s]+$', name):
    #                 return False
    #             if len(name) < 2 or len(name) > 50:
    #                 return False

#   convert altered dataframe to new csv file
ndf.to_csv("fixed_rental_data.csv", index=False , encoding = "utf-8")

#   read new csv file
newdf = pd.read_csv("fixed_rental_data.csv")
# print(newdf)