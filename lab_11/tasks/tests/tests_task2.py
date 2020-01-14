import pytest
from unittest.mock import Mock

from lab_11.tasks.tools.metaweather import (
    get_metaweather
)

if __name__ == '__main__':
	#request.get = Mock()
	#request.get.raise_for_status.side_effect = [Null, requests.exceptions.HTTPError]
	#request.get.raise_for_status = True

	response_mock = Mock()

	response_mock.json.return_value = {
            'Warsaw': 523920,
			'Newark': 2459269,
			'Opole': 12345
        }
	response_mock.raise_for_status = True

	requests.get.side_effect = [response_mock, Timeout]