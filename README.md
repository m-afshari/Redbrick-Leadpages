# Redbrick | Leadpages

## Animal Data Processing and Transfer

This Python project fetches animal data from a paginated API, transforms specific fields, and then POSTs the data in batches to another API endpoint. It's designed to be modular and resilient to network errors.

### Key Features

*   **Configuration:** API endpoint URLs and 'GET' and 'POST' configurations are stored in a `config.py` file for easy customization.

### Getting Started

1.  **Prerequisites:**
    *   Python 3.x
    *   `requests` library (`pip install requests`)

1.  **Execution:**
    *   Run the `main.py` script.

### Code Structure

*   `api_utils.py`: Contains functions for interacting with the API.
*   `data_transformer.py`: Contains functions for transforming the animal data.
*   `config.py`: Stores API endpoint URLs and 'GET' and 'POST' configurations.
*   `main.py`: The main script that orchestrates the data fetching, transformation, and POSTing.

### Support

Feel free to raise an issue or email me @ afshari.mehdi@gmail.com
