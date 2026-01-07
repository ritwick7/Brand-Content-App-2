def get_clarification_questions(category: str, data: dict):
    """
    Returns a list of clarification questions.
    Each question is a dict with:
    - key
    - question
    - options
    """

    questions = []

    # ---------- PRODUCT ----------
    if category == "product":
        if not data.get("offer"):
            questions.append({
                "key": "sales_intent",
                "question": "Should this feel more sales-focused or brand-led?",
                "options": ["Sales-focused", "Brand-led"]
            })

        if len(questions) < 2:
            questions.append({
                "key": "visual_style",
                "question": "Which visual style fits better?",
                "options": ["Product close-up", "Lifestyle / abstract"]
            })

    # ---------- EVENT ----------
    if category == "event":
        questions.append({
            "key": "urgency",
            "question": "How urgent should this feel?",
            "options": ["High urgency", "Calm announcement"]
        })

        if len(questions) < 2:
            questions.append({
                "key": "visual_focus",
                "question": "What should the poster focus on?",
                "options": ["Performer", "Event details"]
            })

    # ---------- BRAND ----------
    if category == "brand":
        questions.append({
            "key": "voice",
            "question": "What tone should the message have?",
            "options": ["Confident", "Friendly"]
        })

        if len(questions) < 2:
            questions.append({
                "key": "visual_style",
                "question": "Preferred visual direction?",
                "options": ["Abstract brand graphic", "Product / space imagery"]
            })

    return questions[:2]
