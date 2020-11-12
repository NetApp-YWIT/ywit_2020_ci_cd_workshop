"""
This is the main functionality of our package. it implements the logic necessary
to fetch the next event from the server and return it as a time delta for us to use.
"""

from datetime import datetime, timedelta, timezone, tzinfo

import requests


def get_time_difference(from_time: datetime = None) -> timedelta:
    if not from_time:
        from_time = datetime.now()
    if not from_time.tzinfo:
        from_time = from_time.replace(tzinfo=datetime.now().astimezone().tzinfo)

    next_ywit_event = datetime.fromisoformat(_get_event_from_api())
    return next_ywit_event - from_time


def _get_event_from_api() -> str:
    response = requests.get("https://netapp.ywit.io/api/get_next_event")
    return response.json()["next_event"]
