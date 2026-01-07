import streamlit as st


def render():
    st.subheader("Product Advertisement")

    data = {}

    data["brand_name"] = st.text_input("Brand Name")
    data["brand_description"] = st.text_input(
        "Brand Description (one line)"
    )

    data["product_name"] = st.text_input("Product Name")
    data["product_description"] = st.text_input(
        "Product Description (one line)"
    )

    data["brand_vibe"] = st.selectbox(
        "Brand Vibe",
        ["", "Minimal", "Bold", "Premium", "Playful"]
    )

    data["primary_color"] = st.text_input(
        "Primary Brand Color (name or hex)"
    )

    data["offer"] = st.text_input(
        "Offer / Hook (optional)"
    )

    # -------------------------------
    # Required fields + messages
    # -------------------------------
    required_fields = {
        "brand_name": "Brand name is required",
        "brand_description": "Brand description is required",
        "product_name": "Product name is required",
        "product_description": "Product description is required",
        "brand_vibe": "Please select a brand vibe",
        "primary_color": "Primary brand color is required",
    }

    return data, required_fields
