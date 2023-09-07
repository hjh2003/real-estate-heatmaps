import streamlit as st

# Set Streamlit page configuration
st.set_page_config(layout="wide", page_icon="🌍", initial_sidebar_state="collapsed")

# Page title
st.title("Real Estate Visualization Dashboard")

# Define the HTML file paths for the general map visualizations
html_files = {
    'Homes Sold': 'Maps/General/general_homes_sold_map.html',
    'New Listings': 'Maps/General/general_new_listings_map.html',
    'Off Market in Two Weeks': 'Maps/General/general_off_market_in_two_weeks_map.html',
    'Median Sale Price': 'Maps/General/general_median_sale_price_map.html',
    'Median Days on Market': 'Maps/General/general_median_dom_map.html',
}

# Navigation dropdown for map visualization selection
selected_field = st.selectbox("Select a metric:", list(html_files.keys()))

# Display explanations based on the selected map
if selected_field in html_files:
    explanation = f"This map represents the {selected_field} for different areas. Explore the visualization to gain insights."
else:
    explanation = ""

# Render the selected map visualization
st.title(f"**{selected_field} Map**")
st.markdown(explanation)  # Display the selected explanation
HtmlFile = open(html_files[selected_field], 'r', encoding='utf-8')
source_code = HtmlFile.read()
st.components.v1.html(source_code, height=600)
st.write('---')  # Add a separator between the maps

# Add additional content or features as needed

