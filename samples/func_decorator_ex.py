import datetime

datetime_now = datetime.datetime.now()
before_10s = datetime_now + datetime.timedelta(0, -10)
after_10s = datetime_now + datetime.timedelta(0, 10)
after_20s = datetime_now + datetime.timedelta(0, 20)


def duration_decorator(first_datetime, second_datetime):
    def real_decorator(function_to_decorate):
        def wrapper(*args, **kwargs):
            if not isinstance(first_datetime, datetime.datetime) or not isinstance(second_datetime, datetime.datetime):
                raise TypeError("duration_decorator's args must be datetime type")
            now = datetime.datetime.now()
            if first_datetime <= now <= second_datetime or first_datetime >= now >= second_datetime:
                print("in time!")
            function_to_decorate(*args, **kwargs)
        return wrapper
    return real_decorator


@duration_decorator(before_10s, after_10s)
def say_something(message):
    print(message)


say_something("hello world")
