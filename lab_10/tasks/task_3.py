import filecmp
import pathlib
from typing import Union
from lab_10.tasks.task_2 import get_city_data
import datetime as dt

import pandas as pd
import re


API_URL = 'https://www.metaweather.com/api/'


def concat_data(
        path: Union[str, pathlib.Path],
):
    #parts = str(path).rpartition('/')
    #print(parts[0])
    #print(parts[2])

    regex = r'(\S+)(?:/)([0-9]+)(?:_)([0-9]+)(?:_)([0-9]+$)'
    match = re.search(regex, path)

    dir = match.group(1)
    woeid = int(match.group(2))
    year = int(match.group(3))
    month = int(match.group(4))

    dir_path, file_paths = get_city_data(woeid, year, month, path=dir)
    dir_pathed = pathlib.Path(dir_path)

    N = len(file_paths)
    sum_date = [None] *N

    for jj in range(N):
        data = pd.read_csv(dir_pathed / file_paths[jj])
        
        meteo_date = data['applicable_date'].tolist()
        update_date = data['created'].tolist()
        created_date = [None]*len(update_date)
        
        for ii in range(len(meteo_date)):
            meteo_date[ii] = meteo_date[ii][:10]
            created_date[ii] = dt.datetime.strptime(update_date[ii], '%Y-%m-%dT%H:%M:%S.%fZ')
            created_date[ii] = created_date[ii].strftime("%Y-%m-%dT%H:%M")
            update_date[ii] = update_date[ii][:10]

        data["tmp2"] = meteo_date
        data["tmp"] = update_date
        data["created"] = created_date
        data.rename(columns={'the_temp': 'temp'}, inplace=True)

        data = data.loc[data['tmp'] == data['tmp2']]

        data = data[['created',
'min_temp',
'temp',
'max_temp',
'air_pressure',
'humidity',
'visibility',
'wind_direction_compass',
'wind_direction',
'wind_speed']].copy()

        data.sort_values(by=['created'], inplace=True)
        sum_date[jj]=data#[::-1]

    result = pd.concat(sum_date)
    result.to_csv(str(path)+".csv", sep=',', index=False)

if __name__ == '__main__':
    concat_data('weather_data/523920_2017_03')
    assert filecmp.cmp(
        'expected_523920_2017_03.csv',
        'weather_data/523920_2017_03.csv'
    )