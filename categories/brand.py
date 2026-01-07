import streamlit as st # type: ignore

def render():
    st.subheader("Store / Brand Advertisement")

    data = {}
    data["brand_name"] = st.text_input("Brand Name")
    data["brand_description"] = st.text_input("Brand Description (one line)")
    data["store_type"] = st.text_input("Store Type (Coffee shop, Clothing store, etc.)")
    data["location"] = st.text_input("Location (optional)")
    data["brand_vibe"] = st.selectbox(
        "Brand Vibe",
        ["", "Minimal", "Bold", "Premium", "Playful"]
    )
    data["primary_color"] = st.text_input("Primary Brand Color")

    required_fields = {
        "brand_name": "Brand name is required",
        "brand_description": "Brand description is required",
        "store_type": "Store type is required",
        "brand_vibe": "Please select a brand vibe",
        "primary_color": "Primary brand color is required"
    }

    return data, required_fields
