from api_utils import fetch_animals_from_api, post_animals_in_batches
from data_transformer import transform_animal_data
import config

# Step 1:
all_animals = fetch_animals_from_api(config.API_BASE_URL, config.API_DETAILS_BASE_URL) 
# Output the collected animals
print(f"\nCollected details for {len(all_animals)} animals:")

#Step 2:
transform_animal_data(all_animals)

#Step 3:
post_animals_in_batches(all_animals, config.API_HOME_URL)