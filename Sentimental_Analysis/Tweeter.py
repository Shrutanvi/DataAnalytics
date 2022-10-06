

import re
with open("/Users/shrutanvidatar/MSSEM1/Data_Analytics_with_Python/Sentimental_Analysis/tesla.txt","r", encoding='unicode-escape') as tesla:
    tesla_data = tesla.read()


tesla_data.replace('ofâ\x80¦', "of")
print(tesla_data)
