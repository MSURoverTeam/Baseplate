import threading

import rospy

from control.utils import listify


def interruptable_join(thread):
    while True:
        thread.join(600)
        if not thread.isAlive():
            break


def launch_spinner_thread(is_daemon=True):

    def _listen():
        thread = threading.current_thread()

        rospy.loginfo("Spinning from thread {thread_info}".format(
            thread_info={"name": thread.getName(), "id": thread.ident}
        ))
        rospy.spin()

    thread = threading.Thread(target=_listen, name='spinner_thread')
    thread.setDaemon(is_daemon)
    thread.start()

    return thread


def chain_callbacks(*callbacks, **kwargs):
    suppress_exceptions = kwargs.pop('suppress_exceptions', False)
    callbacks = listify(callbacks)

    def _callback(msg):
        for callback in callbacks:
            try:
                callback(msg)
            except Exception as e:
                if suppress_exceptions:
                    rospy.logerr("Exception in callback {callback_info}: {exc_info}".format(
                        callback_info=str(callback),
                        exc_info=str(e),
                    ))
                    continue
                raise

    return _callback
