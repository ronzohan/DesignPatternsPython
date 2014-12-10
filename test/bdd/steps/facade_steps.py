from lettuce import step
from Facade.facade import Facade
from nose.tools import assert_equal

temp = None


@step(u'Given a city "([^"]*)" on the country "([^"]*)"')
def given_a_city_group1_on_the_country_group2(step, city, country):
    facade = Facade()
    temp = facade.get_forecast('Iligan', 'PH')


@step(u'Then the temperature is "([^"]*)"')
def then_the_temperature_is_group1(step, expected_temp):
    assert_equal(temp, expected_temp)