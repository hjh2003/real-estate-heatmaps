import streamlit as st

# Set Streamlit page configuration
st.set_page_config(layout="wide", page_icon="🌍", initial_sidebar_state="collapsed")

# Page title
st.title("San Francisco Real Estate Visualization")

# Define the HTML file paths for each map visualization

# Define the HTML file paths for each map visualization
html_files = {
    'New Listings': 'Maps/San Francisco/San Francisco_new_listings_map.html',
    'Homes Sold': 'Maps/San Francisco/San Francisco_homes_sold_map.html',
    'Off Market in Two Weeks': 'Maps/San Francisco/San Francisco_off_market_in_two_weeks_map.html',
    'Median Sale Price': 'Maps/San Francisco/San Francisco_median_sale_price_map.html',
    'Median Days on Market': 'Maps/San Francisco/San Francisco_median_dom_map.html',
}

# Navigation dropdown for map visualization selection
selected_field = st.selectbox("Select a metric:", list(html_files.keys()))

# Display explanations based on the selected map
if selected_field == 'New Listings':
    explanation = "This map shows the new listings of residential properties in San Francisco. Explore the areas with the highest new listing activity."
elif selected_field == 'Homes Sold':
    explanation = "This map displays the number of homes sold in different neighborhoods of San Francisco. Observe the areas with the most home sales."
elif selected_field == 'Off Market in Two Weeks':
    explanation = "This map reveals properties that have gone off the market within two weeks of being listed. Identify the neighborhoods with rapid sales."
elif selected_field == 'Median Sale Price':
    explanation = "Explore the median sale price of residential properties in San Francisco. The darker the color, the higher the median sale price."
elif selected_field == 'Median Days on Market':
    explanation = "Discover the median number of days properties stay on the market before being sold. A higher value indicates a longer duration."
else:
    explanation = ""

# Render the selected map visualization
st.title(f"**{selected_field} Map**")
st.markdown(explanation)  # Display the selected explanation
HtmlFile = open(html_files[selected_field], 'r', encoding='utf-8')
source_code = HtmlFile.read()
st.components.v1.html(source_code, height=600)
st.write('---')  # Add a separator between the maps