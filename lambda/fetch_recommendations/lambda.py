def lambda_handler(event, context):
    print("EVENT:", event)

    user_id = event.get("userId")

    if not user_id:
        return {
            "userId": None,
            "recommendations": [],
            "error": "Missing userId in event"
        }

    recommendations = [
        "home workout",
        "fitness bands",
        "gym accessories"
    ]

    return {
        "userId": user_id,
        "recommendations": recommendations
    }
