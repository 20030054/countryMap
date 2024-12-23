import streamlit as st
import pydeck as pdk
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import st_folium

def main():
    st.title("Country Map Viewer")
    st.write("Enter a country name to see its map.")

    # Input for country name
    country_name = st.text_input("Country Name:", "")

    if country_name:
        # Get the latitude and longitude of the country using geopy
        geolocator = Nominatim(user_agent="country_map_app")
        try:
            location = geolocator.geocode(country_name)
            if location:
                st.success(f"Showing map for: {country_name}")

                # Create a map centered around the country
                country_map = folium.Map(location=[location.latitude, location.longitude], zoom_start=5)

                # Add a marker for the country's location
                folium.Marker(
                    [location.latitude, location.longitude],
                    popup=f"{country_name}",
                    tooltip="Click for more info"
                ).add_to(country_map)

                # Display the map using streamlit-folium
                st_folium(country_map, width=700, height=500)
            else:
                st.error("Could not find the country. Please check the name and try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
