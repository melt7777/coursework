# python
# Practice formatting datetime stamps.
# Incoming format is from ansible tower.

from datetime import datetime

started = "2021-08-10T23:13:26.820576+00:00"
started_datetime_object = datetime.strptime(started, '%Y-%m-%dT%H:%M:%S.%f%z')
started_out = started_datetime_object.strftime('%Y-%m-%d %H:%M:%S')
print(f'started:  {started_out}')

finished = "2021-08-11T00:02:15.764319+00:00"
finished_datetime_object = datetime.strptime(
    finished, '%Y-%m-%dT%H:%M:%S.%f%z')
finished_out = finished_datetime_object.strftime('%Y-%m-%d %H:%M:%S')
print(f'finished: {finished_out}')

elapsed = finished_datetime_object - started_datetime_object
print(f'hours elapsed: {elapsed}')
