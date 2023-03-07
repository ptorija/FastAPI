from pydantic import BaseModel
from typing import Optional


class UsuarioMongo(BaseModel):
    name: str
    reviewerId: str
    reviewerUrl: str
    reviewerNumberOfReviews: int
    isLocalGuide: bool
    numReviewsEnBD: int
