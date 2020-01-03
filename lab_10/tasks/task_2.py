import pathlib
from typing import Optional, Union, List
from urllib.parse import urljoin
import requests
import csv
import os.path


API_URL = 'https://www.metaweather.com/api/'


def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.
) -> (str, List[str]):
    files=[]
    days = 31+1
    emptyPath = False
    
    direct = str(woeid) + "_" + str(year) + "_" + f"{month:02d}"

    if path is None:
        path0 = pathlib.Path.cwd()
        emptyPath = True
    elif not os.path.isabs(path):
        path0 = pathlib.Path.cwd() / path

    path0 = path0 / direct

    if emptyPath:
        path1 = path0
    else:
        path1 = path + "/" + direct

    path0.mkdir(parents=True, exist_ok=True)

    for day in range(1, days):
        location_url = urljoin(API_URL, f'location/{woeid}/{year}/{month}/{day}')
        try:
            response = requests.get(location_url, timeout=5)
        except requests.exceptions.Timeout:
            print(f'Request for: {location_url} took to long!')
        else:
            print(response.url)
            data = response.json()
            if len(data) == 0:
                break
            else:
                file_name = f'{year}-{month}-{day}.csv'
                files.append(file_name)
                with open(path0 / file_name, 'w') as _file:
                    writer = csv.DictWriter(_file, delimiter=',', quotechar='"', fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
    
    return (str(path1), files)


if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = 'weather_data/523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    print(dir_path)
    print(expected_path)
    assert expected_path == dir_path

    expected_path = 'weather_data/523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    #errors