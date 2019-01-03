from contextlib import contextmanager


@contextmanager
def auto_commit():
    try:
        yield
        print("yield 后")
    except Exception as e:
        print("except")
        raise e


with auto_commit():
    1/0
    print('begin')
