import datetime


class DurationDecorator(object):
    def __init__(self, first_datetime, second_datetime):
        if not isinstance(first_datetime, datetime.datetime) or not isinstance(second_datetime, datetime.datetime):
            raise TypeError("DurationDecorator's args must be datetime type")
        self.first_datetime = first_datetime
        self.second_datetime = second_datetime

    def __call__(self, func_to_decorate, *args, **kwargs):
        def decorated_func(*args, **kwargs):
            now = datetime.datetime.now()
            if self.first_datetime <= now <= self.second_datetime or self.first_datetime >= now >= self.second_datetime:
                print("in time!")
            return func_to_decorate(*args, **kwargs)
        return decorated_func


# prepare datetime arguments
datetime_now = datetime.datetime.now()
before_10s = datetime_now + datetime.timedelta(0, -10)
after_10s = datetime_now + datetime.timedelta(0, 10)
after_20s = datetime_now + datetime.timedelta(0, 20)


@DurationDecorator(before_10s, after_10s)
def say_something(message):
    print(message)


say_something("hello world")
