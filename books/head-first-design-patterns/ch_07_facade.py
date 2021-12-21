from unittest.mock import Mock


class HomeTheaterFacade:
    def __init__(self, amplifier, tuner, projector, lights, screen, player, popper):
        self._amplifier = amplifier
        self._tuner = tuner
        self._projector = projector
        self._lights = lights
        self._screen = screen
        self._player = player
        self._popper = popper

    # Wrap complex behavior into single method:
    def watch_movie(self, movie):
        self._popper.on()
        self._popper.pop()

        self._lights.dim(10)

        self._screen.down()

        self._projector.on()

        self._amplifier.on()
        self._amplifier.set_volume(20)

        self._player.on()
        self._player.play(movie)


home_theater = HomeTheaterFacade(*([Mock()] * 7))
home_theater.watch_movie("Joker")
