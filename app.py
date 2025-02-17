
import streamlit as st  # Import Streamlit library for web app creation
import pandas as pd     # Import pandas for handling data in DataFrame format
import random           # Import random for selecting random products

# Define the file path to your CSV file (adjust the path as necessary)
file_path = 'sample-data.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Strip any extra spaces from column names to avoid issues with mismatched names
df.columns = df.columns.str.strip()

# Set the title of the Streamlit app
st.title("Product Recommendations System")

# Add a brief description for the user
st.write("Select a product to get recommendations for related items")

# Print the column names to the console for debugging purposes
# This can be helpful if you're unsure of the columns in your DataFrame
print(df.columns)

# Convert the 'id' column to a list and use it for the dropdown menu options
product_ids = df['id'].tolist()

# Create a dropdown menu for selecting a product ID
# The user selects a product from this list
selected_product_id = st.selectbox("Select a product ID", product_ids)

# Fetch the details of the selected product by filtering the DataFrame for that 'id'
# iloc[0] gets the first row of the resulting filtered DataFrame (since there's only one match)
selected_product = df[df['id'] == selected_product_id].iloc[0]  

# Extract the product description for the selected product
product_description = selected_product['description']

# Display the selected product's description in the Streamlit app
st.write(f"**Description:** {product_description}")

# Filter out the selected product from the DataFrame to avoid recommending the same product
other_products = df[df['id'] != int(selected_product_id)]

# Randomly select 3 other products from the remaining products as recommendations
random_related_products = other_products.sample(3)

# If there are any related products, display them in the app
if not random_related_products.empty:
    st.write("### You may also like")
    for index, row in random_related_products.iterrows():
        # For each related product, show its description
        st.write(f"- {row['description']}")
else:
    # If there are no related products, display a fallback message
    st.write("No recommendations found")
