from datetime import timedelta

from ywit_event_countdown.countdown import get_time_difference


def main():
    time_left = get_time_difference()
    days = time_left // timedelta(days=1)
    hours = time_left // timedelta(hours=1) % 24
    minutes = time_left // timedelta(minutes=1) % 60
    if minutes < 0:
        print(
            "The event has already happened. Watch https://netapp.ywit.io for"
            " next year's announcement."
        )
    else:
        print(
            f"There are {days} days, {hours} hours, and {minutes} minutes left"
            " until the next NetApp YWIT event!"
        )


if __name__ == "__main__":
    main()
