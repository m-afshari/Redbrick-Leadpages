import requests
from concurrent.futures import ThreadPoolExecutor
import time
from config import GET_ANIMAL_DETAILS_MAX_RETRIES, GET_HEALTHY_RESPONSE_CODE, POST_BATCH_SIZE, POST_MAX_RETRIES

def get_animal_details(animal_id, details_base_url):
    """Fetches details for a single animal by ID with retry logic."""
    max_retries = GET_ANIMAL_DETAILS_MAX_RETRIES
    retries = 0

    while retries < max_retries:
        try:
            url = details_base_url.format(animal_id)
            response = requests.get(url, timeout=1)

            if response.status_code == GET_HEALTHY_RESPONSE_CODE:
                return response.json()
            else:
                print(f"Error fetching details for ID {animal_id}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching details for ID {animal_id}: {e}")

        retries += 1

    print(f"Max retries reached for ID {animal_id}. Skipping...")
    return None

def fetch_animals_from_api(base_url, details_base_url):
    """Fetches animal data from the API with pagination and error handling."""
    page = 1
    all_animals = {}
    has_more_pages = True

    while has_more_pages:
        try:
            response = requests.get(base_url, params={'page': page}, timeout=1)

            if response.status_code == GET_HEALTHY_RESPONSE_CODE:
                data = response.json()
                animals = data.get('items', [])

                if not animals:
                    continue
                elif data.get('page', 0) == data.get('total_pages', -1):
                    has_more_pages = False

                with ThreadPoolExecutor() as executor:
                    animal_details_futures = [executor.submit(get_animal_details, animal['id'], details_base_url) for animal in animals]
                    for animal, future in zip(animals, animal_details_futures):
                        details = future.result()
                        if details:
                            all_animals[animal['id']] = details

                page += 1
            else:
                print(f"Encountered {response.status_code} error on page {page}. Retrying...")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page}: {e}")

    return all_animals

def post_animals_in_batches(all_animals, home_url):
    """POSTs animal data to the API in batches with retry logic."""
    batch_size = POST_BATCH_SIZE
    max_retries = POST_MAX_RETRIES
    for i in range(0, len(all_animals), batch_size):
        batch = list(all_animals.values())[i:i + batch_size]
        retries = 0
        while retries < max_retries:
            try:
                response = requests.post(home_url, json=batch)
                response.raise_for_status()
                print(f"Successfully POSTed batch {i // batch_size + 1}")
                break
            except requests.exceptions.RequestException as e:
                print(f"Error POSTing batch {i // batch_size + 1}, retrying... Attempt {retries + 1}: {e}")
                retries += 1
                time.sleep(1)

        if retries == max_retries:
            print(f"Max retries reached for batch {i // batch_size + 1}. Skipping...")