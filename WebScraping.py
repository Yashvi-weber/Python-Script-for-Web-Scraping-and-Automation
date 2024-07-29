import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Choose the Right Website
url = "https://www.amazon.in/Spice-Organiser-Mounted-Hanging-Seasoning/dp/B09DS6HT6B/?_encoding=UTF8&pd_rd_w=xzHfc&content-id=amzn1.sym.c47020cc-0a08-4653-b3aa-1c306df3c44f&pf_rd_p=c47020cc-0a08-4653-b3aa-1c306df3c44f&pf_rd_r=J6BAEJ5XXEAN2PJ53F8E&pd_rd_wg=W1avt&pd_rd_r=b4e6c2ba-45cc-4a50-a91d-cee8e2b83467&ref_=pd_hp_d_btf_a2i_ohl_gw_cml"  # Replace with your chosen website

# Step 2: Use Web Scraping Libraries
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Data Processing
# Extract relevant data from the website
data = [] #empty list 

print(soup.find_all('div'))
for item in soup.find_all('div'):
    title = item.text.strip()
    data.append({'title': title})

# Create a Pandas DataFrame to store the data
df = pd.DataFrame(data)

# Check if the DataFrame is not empty
if not df.empty:
    # Clean and organize the data
    df['title'] = df['title'].str.strip()
    print(df)
else:
    print("No data found.")
