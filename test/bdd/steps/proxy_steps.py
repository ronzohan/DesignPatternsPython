from lettuce import step
from Proxy.proxy import Proxy
from nose.tools import assert_equal


@step(u'Given I instatiated multiple proxy')
def given_i_instatiated_multiple_proxy(step):
    for row in step.hashes:
        row = Proxy()


@step(u'Then the proxy class will have "([^"]*)" reference count')
def then_the_proxy_class_will_have_group1_reference_count(step, ref_count):
    proxy1 = Proxy()
    proxy2 = Proxy()
    proxy3 = Proxy()

    assert_equal(Proxy().__class__.reference_count, int(ref_count))


@step(u'Given I instatiated a proxy')
def given_i_instatiated_a_proxy(step):
    proxy1 = Proxy()


@step(u'And I delete that instance')
def and_i_delete_that_instance(step):
    proxy1 = Proxy()
    del proxy1


@step(u'Then the proxy class will now have "([^"]*)" reference count')
def then_the_proxy_class_will_have_group1_reference_cont(step, ref_count):
    proxy1 = Proxy()
    del proxy1

    assert_equal(Proxy().__class__.reference_count, int(ref_count))



