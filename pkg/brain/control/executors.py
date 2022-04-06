import time

import rospy

from control.utils import listify
from control.lifecycle import call_finalizers


class Action(object):
    condition = None
    rate = None
    repeat = True

    def __init__(self, condition=None, rate=None, repeat=True):
        # x or self.x - preserve attributes if they were set for the class
        self.condition = condition or self.condition
        self.rate = rate or self.rate
        self.repeat = repeat if repeat is not None else self.repeat

        self.started = False
        self._start = None

    @property
    def is_repeated(self):
        return self.repeat

    @property
    def start(self):
        # return future if has not started, else start
        return time.time() + 100 if not self.started else self._start

    def _do(self):
        self.started = True
        if self._start is None:
            self._start = time.time()
        self.do()

    def do(self):
        pass


def is_possible(condition=None):
    return not rospy.is_shutdown() and condition() if condition is not None else True


def execute(*actions):
    actions = listify(actions)
    for action in actions:
        if not action.is_repeated:
            if is_possible(action.condition):
                action._do()
            continue
        try:
            while is_possible(action.condition):
                action._do()
                if action.rate is not None:
                    action.rate.sleep()
        except KeyboardInterrupt:
            call_finalizers()
            raise SystemExit
