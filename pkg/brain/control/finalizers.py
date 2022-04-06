from geometry_msgs.msg import Twist

COMMON_FINALIZERS = {}


def register(func):
    COMMON_FINALIZERS[func.__name__] = func
    return func


@register
def full_stop(publisher):
    stop = Twist()
    stop.linear.x = stop.linear.y = stop.linear.z = 0
    stop.angular.x = stop.angular.y = stop.angular.z = 0
    publisher.publish(stop)
