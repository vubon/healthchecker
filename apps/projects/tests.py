from datetime import datetime

# from django.test import TestCase

# Create your tests here.
import json

data = ["11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45",
        "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45",
        "17:00", "17:15", "17:30", "17:45", "18:00", "18:15"]


def get_list_hours_for_interval(start_time, end_time):
    if datetime.now().hour >= 23:
        start_time = "18:00"
    start = hour_to_integer(start_time)
    end = hour_to_integer(end_time)

    hours = list()
    for minutes in range(start, end + 1, 15):
        hours.append(integer_to_hour(minutes))

    # print(json.dumps(hours))

    new_list = []
    for item in data:
        hour, minute = item.split(":")
        if not (12 <= int(hour) < 18):
            new_list.append(item)

    print(len(new_list))
    print(new_list)


def hour_to_integer(hour: str = '00:00') -> int:
    """
    :param hour:
    :return:
    """
    split = hour.split(":")
    total_minutes = int(split[0]) * 60 + int(split[1])
    return total_minutes


def integer_to_hour(total_minutes: int = 0) -> str:
    """
    :param total_minutes:
    :return:
    """
    hours = int(total_minutes / 60)
    minutes = total_minutes - 60 * hours

    str_hours = "0" + str(hours) if hours < 10 else str(hours)
    str_minutes = "0" + str(minutes) if minutes < 10 else str(minutes)

    return str_hours + ":" + str_minutes


if __name__ == '__main__':
    get_list_hours_for_interval("08:00", "22:00")
