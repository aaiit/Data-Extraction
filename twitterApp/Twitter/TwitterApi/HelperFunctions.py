def my_reduce(x, y: list):
    '''
    :param x: object to investigate
    :param y: list of successive attributes; can exist in a dictionary, list or object.
    '''
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
        attr = my_reduce(x[y[0]], y[1:])
    else:
        attr = my_reduce(getattr(x, y[0]), y[1:])
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
