import requests
from urllib.parse import urljoin
API_URL = 'https://www.metaweather.com/api/'

def get_cities_woeid(query: str, timeout: float = 5.):
    result = {}
    location_url = urljoin(API_URL, 'location/search')

    try:
        response = requests.get(location_url, params=dict(query=query), timeout=timeout)
        tablica = response.json()
        for elem in tablica:
            result[elem["title"]] = elem["woeid"]
    except requests.exceptions.Timeout:
        print(f'Request for: {location_url} took to long!')
    except requests.exceptions.HTTPError:
        print(f'HTTP Error!')
    except RuntimeError:
        print(f'Runtime error!')
    finally:
        return result


if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
