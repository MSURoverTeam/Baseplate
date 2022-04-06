import atexit
from copy import copy
from functools import partial, wraps

import rospy

from control.finalizers import COMMON_FINALIZERS

FINALIZERS_CACHE = set()
finalizers = []


def call_finalizers():
    for f, name in finalizers:
        try:
            f()
        except Exception as exc:
            # Global logger object can be already garbage collected, so better to use print
            print("While running finalizer {f_name} caught exception {exc}".format(
                exc=str(exc),
                f_name=name,
            ))


def regiser_finalizer(func):
    if not isinstance(func, partial):
        name = func.__name__
        _wraps = wraps
    else:
        name = func.func.__name__
        _wraps = lambda p: wraps(p.func)

    @_wraps(func)
    def wrapped():
        _name = copy(name)  # to protect from gc at "atexit"
        if _name not in FINALIZERS_CACHE:
            FINALIZERS_CACHE.add(_name)
        else:
            return
        # Global logger object can be already garbage collected, so better to use print
        print('Running "{name}" finalizer'.format(name=_name))
        func()
        print('"{name}" finalizer finished'.format(name=_name))

    finalizers.append((wrapped, name))
    rospy.on_shutdown(wrapped)
    return atexit.register(wrapped)


def setup_finalizers(config):
    for item in config:
        if item not in COMMON_FINALIZERS:
            regiser_finalizer(item)
            return
        name = item

        finalizer_args_obj = config[name]
        if isinstance(finalizer_args_obj, dict):
            finalizer_args, finalizer_kwargs = [], finalizer_args_obj
        elif isinstance(finalizer_args_obj, (tuple, list)):
            finalizer_args, finalizer_kwargs = finalizer_args_obj
        else:
            finalizer_args, finalizer_kwargs = (finalizer_args_obj,), {}

        finalizer_func = partial(COMMON_FINALIZERS[name], *finalizer_args, **finalizer_kwargs)
        regiser_finalizer(finalizer_func)
