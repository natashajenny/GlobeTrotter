from app import api
from flask_restplus import fields

location_types = api.model('location_types',{
    "romance": fields.Boolean(),
    "nature": fields.Boolean(),
    "wildlife": fields.Boolean(),
    "shopping": fields.Boolean(),
    "historical": fields.Boolean(),
    "cultural": fields.Boolean(),
    "family": fields.Boolean(),
    "beaches": fields.Boolean(),
    "food": fields.Boolean()
})

location_coordinate = api.model('location_coordinate',{
    "latitude": fields.Float(),
    "longitude": fields.Float()
})

location = api.model('location',{
    "location_types": fields.Nested(location_types),
    "venue_name": fields.String(),
    "coordinate": fields.Nested(location_coordinate),
    "pictures": fields.List(fields.String()),
    "location_id": fields.String()
})

locations = api.model('locations',{
    "city": fields.String(),
    "locations": fields.List(fields.Nested(location))
})
