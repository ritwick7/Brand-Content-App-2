import streamlit as st # type: ignore

def render():
    st.subheader("Event Announcement")

    data = {}
    data["event_name"] = st.text_input("Event Name")
    data["event_type"] = st.text_input("Event Type (Live Music, Standup, etc.)")
    data["event_description"] = st.text_input("One-line Event Description")
    data["performer"] = st.text_input("Performer / Speaker Name")
    data["date"] = st.text_input("Date")
    data["time"] = st.text_input("Time")
    data["venue"] = st.text_input("Venue / Location")
    data["brand_vibe"] = st.selectbox(
        "Brand Vibe",
        ["", "Minimal", "Bold", "Premium", "Playful"]
    )
    data["primary_color"] = st.text_input("Primary Brand Color")

    required_fields = {
        "event_name": "Event name is required",
        "event_type": "Event type is required",
        "event_description": "Event description is required",
        "performer": "Performer name is required",
        "date": "Event date is required",
        "time": "Event time is required",
        "venue": "Venue is required",
        "brand_vibe": "Please select a brand vibe",
        "primary_color": "Primary brand color is required"
    }

    return data, required_fields
