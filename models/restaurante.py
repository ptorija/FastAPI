from pydantic import BaseModel


class PlusCode(BaseModel):
    compound_code: str
    global_code: str


class Coordenada(BaseModel):
    lat: float
    lng: float


class Geometry(BaseModel):
    location: Coordenada


class Photo(BaseModel):
    height: int
    width: int
    photo_reference: str
    html_attributions: list[str]


class RestauranteMongo(BaseModel):
    business_status: str
    formatted_address: str
    geometry: Geometry
    icon: str
    icon_background_color: str
    icon_mask_base_uri: str
    name: str
    photos: list[Photo]
    photo_url: str
    place_id: str
    plus_code: PlusCode
    price_level: int
    rating: float
    reference: str
    types: list[str]
    user_ratings_totals: int
