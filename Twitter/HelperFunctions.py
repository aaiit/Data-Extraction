import datetime
from copy import deepcopy


def my_reduce(x, yy: list):
    '''
    :param x: object to investigate
    :param y: list of successive attributes; can exist in a dictionary, list or object.
    '''
    y=deepcopy(yy)
    if len(y) == 0:
        return x
    if isinstance(x, list):
        attr = []
        for i in range(len(x)):
            try:
                attr.append(my_reduce(x[i], y))
            except Exception:
                continue
        if attr==[]:
            raise ValueError()
    elif isinstance(x, dict):
        attr = my_reduce(x[y.pop(0)], y)
    else:
        attr = my_reduce(getattr(x, y.pop(0)), y)
    return attr


def get_attr(obj, attrs):
    '''
    :param obj: starting object.
    :param attrs: string of words separated by periods.
    '''
    try:
        res = my_reduce(obj, [key for key in attrs.strip().split('.')])
        res = [(True, res)]
    except Exception:
        # Raised if the field doesn't exist.
        res = [(False, None)]
    return res



def check_date_format(date_string):
    format = "YYYY-MM-DD"
    try:
        datetime.datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False
