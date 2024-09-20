"""API URLS Configs"""
API_BASE_URL = "http://localhost:3123/animals/v1/animals"
API_DETAILS_BASE_URL = "http://localhost:3123/animals/v1/animals/{}"
API_HOME_URL = "http://localhost:3123/animals/v1/home"

"""FETCH and POST Configs"""
GET_ANIMAL_DETAILS_MAX_RETRIES = 15+1
GET_HEALTHY_RESPONSE_CODE = 200
POST_BATCH_SIZE = 100
POST_MAX_RETRIES = 3

