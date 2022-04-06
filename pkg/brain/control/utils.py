LIST_T = (tuple, list)


def listify(args):
    if not isinstance(args, LIST_T):
        args = [args]
    elif len(args) == 1 and isinstance(args[0], LIST_T):
        args = args[0]
    return args
