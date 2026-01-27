import streamlit as st # type: ignore


def render():
    st.subheader("Product Advertisement")

    data = {}

    # -------------------------------
    # Brand & product basics
    # -------------------------------
    data["brand_name"] = st.text_input("Brand Name")

    data["brand_description"] = st.text_input(
        "Brand Description (one line)"
    )

    data["product_name"] = st.text_input("Product Name")

    data["product_description"] = st.text_input(
        "Product Description (one line)"
    )

    # -------------------------------
    # Product category
    # -------------------------------
    data["product_category"] = st.selectbox(
        "Product Category",
        [
            "",
            "SaaS / Software",
            "Electronics / Tech",
            "Skincare / Beauty",
            "Fashion / Apparel",
            "Food & Beverage",
            "Lifestyle / Home",
            "Other",
        ],
    )

    data["product_category_detail"] = st.text_input(
        "Category Details (optional, e.g. 'AI analytics for contact centers')"
    )

    # -------------------------------
    # Product role in image
    # -------------------------------
    data["product_role"] = st.radio(
        "How should the product appear in the image?",
        ["Hero product", "Supporting element", "Conceptual / abstract"],
    )

    # -------------------------------
    # Visual style
    # -------------------------------
    data["visual_style"] = st.selectbox(
        "Visual Style & Mood",
        [
            "",
            "Premium & luxury",
            "Clean & minimal",
            "Bold & energetic",
            "Friendly & lifestyle",
            "Experimental / artistic",
        ],
    )

    # -------------------------------
    # Composition preset
    # -------------------------------
    data["composition_preset"] = st.selectbox(
        "Image Composition",
        [
            "",
            "Studio hero shot",
            "Lifestyle editorial shot",
            "Minimal abstract composition",
        ],
    )

    # -------------------------------
    # Platform
    # -------------------------------
    data["platform"] = st.selectbox(
        "Platform",
        [
            "Instagram feed (1:1)",
            "Instagram story (9:16)",
            "Website / banner",
        ],
    )

    # -------------------------------
    # Goal & creative direction
    # -------------------------------
    data["goal"] = st.text_input(
        "Goal of this image (e.g. product launch, feature highlight, brand awareness)"
    )

    data["creative_notes"] = st.text_area(
        "Additional Creative Notes (optional)",
        placeholder="Any specific mood, reference, or idea you have in mind…",
    )

    # -------------------------------
    # Negative preferences
    # -------------------------------
    st.markdown("**Things to avoid (optional):**")
    data["no_people"] = st.checkbox("No people")
    data["no_text"] = st.checkbox("No text")
    data["no_logos"] = st.checkbox("No logos")
    data["no_exaggeration"] = st.checkbox("No exaggerated effects")

    # -------------------------------
    # Required fields
    # -------------------------------
    required_fields = {
        "brand_name": "Brand name is required",
        "brand_description": "Brand description is required",
        "product_name": "Product name is required",
        "product_description": "Product description is required",
        "product_category": "Please select a product category",
        "visual_style": "Please select a visual style",
        "composition_preset": "Please select a composition preset",
        "goal": "Please specify the goal of this image",
    }

    return data, required_fields
