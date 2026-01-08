def placement_record_router(query: str):
    q = query.lower().strip()

    PLACEMENT_TRIGGERS = [
        "placement record",
        "placement records",
        "placement",
        "placements",
        "placement statistics",
        "niet placement",
        "placement performance"
    ]

    if not any(trigger in q for trigger in PLACEMENT_TRIGGERS):
        return None

    return {
        "final_answer": "Here are the Placement Records",
        "images": [
            "https://niet.co.in/assets/frontend/images/record-group-12.jpg",
            "https://niet.co.in/assets/frontend/images/record-group-122.webp",
            "https://niet.co.in/assets/frontend/images/record-group-123.webp",
            "https://niet.co.in/assets/frontend/images/record-group-124.webp",
            "https://niet.co.in/assets/frontend/images/record-group-13.jpg",
            "https://niet.co.in/assets/frontend/images/record-group-14.jpg",
            "https://niet.co.in/assets/frontend/images/record-group-15.jpg",
            "https://niet.co.in/assets/frontend/images/record-group-16.jpg",
            "https://niet.co.in/assets/frontend/images/record-group-17.jpg",
            "https://niet.co.in/assets/frontend/images/record-group-18.jpg",
            "https://niet.co.in/assets/frontend/images/record-group-19.jpg",
            "https://niet.co.in/assets/frontend/images/record-group-20.jpg",
            "https://niet.co.in/assets/frontend/images/record-group-21.jpg"
        ]
    }
