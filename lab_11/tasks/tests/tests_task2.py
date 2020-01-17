import pytest
import requests_mock
import requests

from lab_11.tasks.tools.metaweather import (
    get_metaweather,
    get_cities_woeid
)


API_URL = 'https://www.metaweather.com/api/location/search?query=Warszawa'

if __name__ == '__main__':

    with requests_mock.Mocker() as m:

        jay = [{'title': 'Warsaw', 'woeid' : 523920, 'rubbish' : 5}, {'title': 'Newark', 'woeid' : 2459269, 'blah' : 'blah'}]

        m.get('/api/location/search?query=Warszawa', json=[])
        assert get_cities_woeid('Warszawa') == {}

        m.get('/api/location/search?query=War', json=jay)
        assert get_cities_woeid('War') == {'Warsaw': 523920, 'Newark': 2459269}

        m.get('/api/location/search?query=War', exc = requests.exceptions.Timeout)
        try:
            get_cities_woeid('War', 0.1)
        except Exception as exc:
            assert isinstance(exc, requests.exceptions.Timeout)

        m.get('/api/location/search?query=War', status_code = 404)
        try:
            get_cities_woeid('War', 0.1)
        except Exception as exc:
            assert isinstance(exc, requests.exceptions.HTTPError)
        