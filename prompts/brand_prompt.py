def build(data: dict) -> str:
    clarifications = []

    if data.get("voice"):
        clarifications.append(f"- Tone of voice: {data.get('voice')}")

    if data.get("visual_style"):
        clarifications.append(f"- Visual direction: {data.get('visual_style')}")

    clarifications_block = (
        "\nCLARIFICATIONS\n" + "\n".join(clarifications)
        if clarifications else ""
    )

    return f"""
ROLE
You are a brand communication expert.

CONTEXT
Brand: {data.get('brand_name')}
Brand description: {data.get('brand_description')}
Store type: {data.get('store_type')}
Location: {data.get('location') or 'Not specified'}
Brand vibe: {data.get('brand_vibe')}
Primary color: {data.get('primary_color')}

OBJECTIVE
Create brand-forward promotional content focused on identity and presence.

TONE & STYLE
- Calm, confident, and trustworthy
- Brand-led, not salesy
- No emojis or buzzwords

OUTPUT REQUIREMENTS
1) Brand-led headline
2) Short brand narrative (3–4 lines)
3) Soft call-to-action
4) Suggested on-image text (minimal)
5) Visual direction for a clean brand graphic

CONSTRAINTS
- Avoid discounts unless explicitly stated
- Do not sound like an advertisement
{clarifications_block}
""".strip()
