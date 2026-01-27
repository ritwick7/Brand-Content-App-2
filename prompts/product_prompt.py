def build(data: dict) -> str:
    """
    Build a premium IMAGE GENERATION PROMPT
    using explicit, strong user inputs from product.py
    """

    # -----------------------------
    # Core inputs
    # -----------------------------
    brand_name = data.get("brand_name", "").strip()
    brand_description = data.get("brand_description", "").strip()
    product_name = data.get("product_name", "").strip()
    product_description = data.get("product_description", "").strip()

    product_category = data.get("product_category", "").strip()
    product_category_detail = data.get("product_category_detail", "").strip()

    product_role = data.get("product_role", "").strip()
    visual_style = data.get("visual_style", "").strip()
    composition_preset = data.get("composition_preset", "").strip()
    platform = data.get("platform", "Instagram feed (1:1)").strip()
    goal = data.get("goal", "").strip()
    creative_notes = data.get("creative_notes", "").strip()

    # Negative preferences
    no_people = data.get("no_people", False)
    no_text = data.get("no_text", False)
    no_logos = data.get("no_logos", False)
    no_exaggeration = data.get("no_exaggeration", False)

    # -----------------------------
    # Product role interpretation
    # -----------------------------
    if "Hero" in product_role:
        role_text = (
            "the primary hero subject of the image, "
            "clearly dominant and commanding immediate attention"
        )
    elif "Supporting" in product_role:
        role_text = (
            "a supporting element within a broader scene, "
            "integrated naturally without overpowering the composition"
        )
    else:
        role_text = (
            "a conceptual or abstract representation rather than a literal depiction, "
            "symbolizing the product’s value and purpose"
        )

    # -----------------------------
    # Composition interpretation
    # -----------------------------
    if "Studio" in composition_preset:
        composition_text = (
            "a studio-style hero composition with controlled lighting, "
            "clean surfaces, and a refined, editorial feel"
        )
    elif "Lifestyle" in composition_preset:
        composition_text = (
            "a lifestyle editorial composition set in a realistic environment, "
            "with natural lighting and an aspirational yet believable mood"
        )
    else:
        composition_text = (
            "a minimal abstract composition using shapes, gradients, or symbolic "
            "visual elements to communicate the idea rather than a literal scene"
        )

    # -----------------------------
    # Platform interpretation
    # -----------------------------
    if "story" in platform.lower():
        platform_text = "Instagram story format (9:16)"
    elif "website" in platform.lower() or "banner" in platform.lower():
        platform_text = "a wide-format website banner layout"
    else:
        platform_text = "Instagram feed format (square 1:1)"

    # -----------------------------
    # Main prompt assembly
    # -----------------------------
    prompt = f"""
Create a high-quality {platform_text} image for a {visual_style.lower()} product advertisement by the brand {brand_name}.

Brand context:
{brand_description}

Product context:
The product being promoted is {product_name}, categorized under {product_category}
{f"({product_category_detail})" if product_category_detail else ""}.
{product_description}

The goal of this image is {goal}.

Product role and focus:
The product should be presented as {role_text}.

Scene and composition:
Use {composition_text}, following visual patterns commonly seen in category-leading brands within this product category.
The composition should feel intentional, premium, and uncluttered, with clear subject hierarchy and thoughtful use of negative space.

Visual style and mood:
The overall aesthetic should feel {visual_style.lower()}, refined, and confident.
Lighting should be deliberate and well-balanced, with textures and materials that reinforce quality, credibility, and professionalism.

Color and visual language:
Use a restrained, tasteful color palette aligned with the brand identity.
Avoid overpowering colors or visual noise.

Technical and platform constraints:
Ensure the image is high resolution, professionally styled, and suitable for direct marketing use without further edits.
""".strip()

    # -----------------------------
    # Optional creative notes
    # -----------------------------
    if creative_notes:
        prompt += f"\n\nAdditional creative direction:\n{creative_notes}"

    # -----------------------------
    # Negative prompt
    # -----------------------------
    negatives = [
        "low-quality or amateur rendering",
        "cluttered or unbalanced compositions",
        "flat or harsh lighting",
        "exaggerated or unrealistic visual effects",
        "cartoonish or gimmicky styles",
        "watermarks or stock-photo artifacts",
    ]

    if no_people:
        negatives.append("people or human figures")
    if no_text:
        negatives.append("visible text or typography")
    if no_logos:
        negatives.append("logos or branding marks embedded in the image")
    if no_exaggeration:
        negatives.append("overly stylized or surreal elements")

    negative_prompt = "Avoid " + ", ".join(negatives) + "."

    # -----------------------------
    # Final output
    # -----------------------------
    return f"""
IMAGE GENERATION PROMPT
----------------------
{prompt}

NEGATIVE PROMPT
---------------
{negative_prompt}
""".strip()
