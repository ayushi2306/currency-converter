import requests

# ----------------------------
# Configuration
# ----------------------------

BASE_URL = "https://open.er-api.com/v6/latest/"


# ----------------------------
# Fetch Exchange Rates
# ----------------------------

def get_exchange_rates(base_currency):
    """
    Fetch live exchange rates from the API.

    Parameters:
        base_currency (str): Currency code (e.g., USD)

    Returns:
        dict: Dictionary containing exchange rates.
        None: If request fails.
    """

    url = BASE_URL + base_currency

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            data = response.json()

            return data

        else:

            print("Server returned:", response.status_code)
            return None

    except requests.exceptions.ConnectionError:

        print("No internet connection.")

        return None

    except requests.exceptions.Timeout:

        print("Request timed out.")

        return None

    except requests.exceptions.RequestException as error:

        print(error)

        return None