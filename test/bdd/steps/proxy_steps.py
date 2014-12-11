from lettuce import step, world
from Proxy.proxy import Proxy
from nose.tools import assert_equal
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


@step(u'Given I instatiated multiple proxy')
def given_i_instatiated_multiple_proxy(step):
    message = ''
    for row in step.hashes:
        message += row['message'] + '\n'

    # Capture all output from the console
    with captured_output() as (out, err):
        world.proxy1 = Proxy()
        world.proxy2 = Proxy()
        world.proxy3 = Proxy()
    # The captured print
    output = out.getvalue().strip()
    output += '\n'
    assert_equal(output, str(message))


@step(u'Then I will delete proxy 2 and will output')
def then_i_will_delete_proxy_2_and_will_output(step):
    message = ''
    for row in step.hashes:
        message += row['message'] + '\n'

    # Capture all output from the console
    with captured_output() as (out, err):
        del world.proxy2

    output = out.getvalue().strip() + '\n'
    assert_equal(output, str(message))