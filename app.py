import streamlit as st

from config.categories import CATEGORIES
from categories import product, event, brand
from prompts import product_prompt, event_prompt, brand_prompt
from clarifier import get_clarification_questions


# ---------------------------------
# Page config
# ---------------------------------
st.set_page_config(page_title="Brand Content App", layout="centered")

st.title("Brand Content Generator")
st.write("Choose what you want to create.")

st.divider()


# ---------------------------------
# Session state initialization
# ---------------------------------
if "questions" not in st.session_state:
    st.session_state.questions = []

if "clarified_data" not in st.session_state:
    st.session_state.clarified_data = {}

if "ready_for_prompt" not in st.session_state:
    st.session_state.ready_for_prompt = False

if "prompt_generated" not in st.session_state:
    st.session_state.prompt_generated = False


# ---------------------------------
# Category selection
# ---------------------------------
category_label = st.radio(
    "Content Type",
    list(CATEGORIES.values())
)

category_key = [k for k, v in CATEGORIES.items() if v == category_label][0]

st.divider()


# ---------------------------------
# Render selected form
# ---------------------------------
if category_key == "product":
    data, required_fields = product.render()
elif category_key == "event":
    data, required_fields = event.render()
elif category_key == "brand":
    data, required_fields = brand.render()

st.divider()


# ---------------------------------
# Step 1: Validate + ask clarifications
# ---------------------------------
if st.button("Generate (Preview)"):
    errors = []

    for field, message in required_fields.items():
        value = data.get(field)
        if value is None or value == "":
            errors.append(message)

    if errors:
        for error in errors:
            st.warning(error)

        st.session_state.questions = []
        st.session_state.ready_for_prompt = False
        st.session_state.prompt_generated = False

    else:
        # Store validated base data
        st.session_state.clarified_data = data.copy()

        # Get clarification questions
        st.session_state.questions = get_clarification_questions(
            category_key,
            data
        )

        st.session_state.ready_for_prompt = False
        st.session_state.prompt_generated = False


# ---------------------------------
# Step 2: Clarification questions
# ---------------------------------
if st.session_state.questions:
    st.subheader("Just a couple of quick questions")

    for q in st.session_state.questions:
        answer = st.radio(
            q["question"],
            q["options"],
            key=f"clarify_{q['key']}",
            on_change=lambda: setattr(
                st.session_state, "prompt_generated", False
            )
        )
        st.session_state.clarified_data[q["key"]] = answer

    st.divider()

    if st.button("Generate Final Prompt"):
        st.session_state.ready_for_prompt = True
        st.session_state.prompt_generated = True


# ---------------------------------
# Step 3: Build prompt (explicit only)
# ---------------------------------
if (
    st.session_state.ready_for_prompt
    and st.session_state.prompt_generated
):
    if category_key == "product":
        prompt = product_prompt.build(st.session_state.clarified_data)
    elif category_key == "event":
        prompt = event_prompt.build(st.session_state.clarified_data)
    elif category_key == "brand":
        prompt = brand_prompt.build(st.session_state.clarified_data)

    st.subheader("Generated Prompt")
    st.code(prompt)
