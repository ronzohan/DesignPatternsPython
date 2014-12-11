from abc import ABCMeta, abstractmethod
import datetime
from _pyio import __metaclass__
from subject import Subject
import time


class Observer(object):
    """Abstract class for observers, provides notify method as
    interface for subjects."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def notify(self, unix_timestamp):
        pass


class USATimeObserver(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, unix_timestamp):
        time = datetime.datetime.fromtimestamp(int(unix_timestamp)) \
            .strftime('%Y-%m-%d %I:%M:%S%p')

        print 'Observer', self.name, 'says:', time


class EUTimeObserver(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, unix_timestamp):
        time = datetime.datetime.fromtimestamp(int(unix_timestamp)) \
            .strftime('%Y-%m-%d %H:%M:%S')

        print 'Observer', self.name, 'says:', time


if __name__ == "__main__":
    subject = Subject()

    print 'Adding usa_time_observer'
    observer1 = USATimeObserver('usa_time_observer')
    subject.register_observer(observer1)
    subject.notify_observers()

    time.sleep(2)
    print 'Adding eu_time_observer'
    observer2 = EUTimeObserver('eu_time_observer')
    subject.register_observer(observer2)
    subject.notify_observers()

    time.sleep(2)
    print 'Removing usa_time_observer'
    subject.unregister_observer(observer1)
    subject.notify_observers()

