def reviewEntity(item) -> dict:
    return {
        "oid": str(item["_id"]),
        "placeId": item["placeId"],
        "restaurantName": item["restaurantName"],
        "name": item["name"],
        "text": item["text"],
        "publishedAtDate": item["publishedAtDate"],
        "likesCount": item["likesCount"],
        "reviewId": item["reviewId"],
        "reviewerId": item["reviewerId"],
        "reviewerUrl": item["reviewerUrl"],
        "reviewerNumberOfReviews": item["reviewerNumberOfReviews"],
        "isLocalGuide": item["isLocalGuide"],
        "stars": item["stars"],
        "lastReview": item["lastReview"],
    }


def reviewsEntity(reviews) -> dict:
    return [reviewEntity(item) for item in reviews]