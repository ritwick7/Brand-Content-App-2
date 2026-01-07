def build(data: dict) -> str:
    clarifications = []

    if data.get("sales_intent"):
        clarifications.append(f"- Sales intent: {data.get('sales_intent')}")

    if data.get("visual_style"):
        clarifications.append(f"- Preferred visual style: {data.get('visual_style')}")

    clarifications_block = (
        "\nCLARIFICATIONS\n" + "\n".join(clarifications)
        if clarifications else ""
    )

    return f"""
ROLE
You are a senior brand strategist and creative director.

CONTEXT
Brand: {data.get('brand_name')}
Brand description: {data.get('brand_description')}
Product: {data.get('product_name')}
Product description: {data.get('product_description')}
Brand vibe: {data.get('brand_vibe')}
Primary color: {data.get('primary_color')}
Offer / hook: {data.get('offer') or 'None'}

OBJECTIVE
Create brand-safe, platform-agnostic marketing content for a product.

TONE & STYLE
- Confident, clear, and professional
- No hype or buzzwords
- No emojis
- Short sentences preferred

OUTPUT REQUIREMENTS
1) A concise headline
2) A short body copy (3–5 lines)
3) A subtle call-to-action
4) Suggested on-image text (short, bold, minimal)
5) Visual direction for a clean, modern graphic (no people unless necessary)

CONSTRAINTS
- Do not mention AI
- Do not mention platforms
- Avoid marketing clichés
{clarifications_block}
""".strip()
