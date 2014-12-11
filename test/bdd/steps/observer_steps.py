from lettuce import step, world
from Observer.subject import Subject
from nose.tools import assert_equal, assert_in
from Observer.observer import USATimeObserver
from contextlib import contextmanager
from StringIO import StringIO
import sys


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


@step(u'Given a subject, observer "([^"]*)" and "([^"]*)"')
def given_a_subject_observer_group1_and_group2(step, obs1, obs2):
    world.subject = Subject()
    world.obs1 = USATimeObserver(obs1)
    world.obs2 = USATimeObserver(obs2)


@step(u'And observer "([^"]*)" and "([^"]*)" registers to subject')
def and_observer_group1_and_group2_registers_to_subject(step, group1, group2):
    world.subject.register_observer(world.obs1)
    world.subject.register_observer(world.obs2)


@step(u'Then the subject notifies its observer')
def then_the_subject_notifies_its_observer(step):
    message = []
    for row in step.hashes:
        message.append(str(row['message'] + '\n'))

    with open('test.txt') as file:
        for line in file:
            assert_in(line, message)