from lettuce import step, world
from Observer.subject import Subject
from nose.tools import assert_equal
from Observer.observer import USATimeObserver


@step(u'Given a subject')
def given_a_observer_group1(step):
    world.subject = Subject()


@step(u'And a USA time observer "([^"]*)" registers to subject')
def and_observer_group1_registers_to_subject(step, name):
    world.observer = USATimeObserver(name)
    world.subject.register_observer(world.observer)


@step(u'Then subject will have "([^"]*)" observer')
def then_subject_will_have_group1_observer(step, count):
    assert_equal(len(world.subject.observers), int(count))
