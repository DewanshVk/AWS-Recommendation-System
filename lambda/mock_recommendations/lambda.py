def lambda_handler(event, context):
    print("Input event:", event)

    user_id = event.get("userId")  # Get userId from input
    
    if not user_id:
        return {
            "userId": None,
            "recommendations": [],
            "error": "Missing userId in event"
        }

    recommendations = [
        "home workout",
        "fitness bands",
        "gym accessories",
        "pre workout",
        "muscle gain"
    ]

    return {
        "userId": user_id,
        "recommendations": recommendations
    }
