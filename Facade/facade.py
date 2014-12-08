from parser import Parser
from cache import Cache
from weather import WeatherProvider, Converter, Weather


class Facade(object):
    def get_forecast(self, city, country):
        cache = Cache('myfile')

        cache_result = cache.load()

        if cache_result:
            return cache_result

        else:
            weather_provider = WeatherProvider()
            weather_data = weather_provider.get_weather_data(city, country)

            parser = Parser()
            parsed_data = parser.parse_weather_data(weather_data)

            weather = Weather(parsed_data)
            converter = Converter()
            temperature_celcius = converter.from_kelvin_to_celcius(weather.
                                                                   temperature)

            cache.save(temperature_celcius)
            return temperature_celcius


if __name__ == '__main__':
    facade = Facade()
    print facade.get_forecast('London', 'UK')
