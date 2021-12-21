class Observer:
    def update(self) -> None:
        raise NotImplementedError


class Subject:
    def register_observer(self, observer: Observer) -> None:
        raise NotImplementedError

    def remove_observer(self, observer: Observer) -> None:
        raise NotImplementedError

    def notify_observers(self) -> None:
        raise NotImplementedError


class DisplayElement:
    def display(self) -> None:
        raise NotImplementedError


class WeatherData(Subject):
    def __init__(self):
        self._observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._temperature = 0.0
        self._humidity = 0.0
        self._weather_data = weather_data
        self._weather_data.register_observer(self)

    def display(self) -> None:
        print(f"Current conditions: {self._temperature}°C, {self._humidity}%")

    def update(self) -> None:
        self._temperature = self._weather_data.temperature
        self._humidity = self._weather_data.humidity
        self.display()


class AvgTempDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._temperature = []
        self._weather_data = weather_data
        self._weather_data.register_observer(self)

    def display(self) -> None:
        print(f"Average temperature: {sum(self._temperature) / len(self._temperature)}°C")

    def update(self) -> None:
        self._temperature.append(self._weather_data.temperature)
        self.display()


weather_data = WeatherData()
current_display = CurrentConditionsDisplay(weather_data)
forecast_display = AvgTempDisplay(weather_data)

weather_data.set_measurements(23.0, 68.1, 1018.0)
weather_data.set_measurements(24.2, 70.4, 1019.2)
weather_data.set_measurements(25.8, 71.2, 1018.4)
