from typing import List


class Device:
    @property
    def name(self) -> str:
        return self.__class__.__name__

    def on(self) -> None:
        print(f"{self.name} was turned on")

    def off(self) -> None:
        print(f"{self.name} was turned off")


class Light(Device):
    pass


class Tv(Device):
    pass


class Stereo(Device):
    def __init__(self) -> None:
        self.volume = 0

    def set_cd(self) -> None:
        print(f"{self.name} CD set")

    def set_volume(self, volume: int) -> None:
        print(f"{self.name} Volume set to {volume}")
        self.volume = volume


class Command:
    def execute(self) -> None:
        raise NotImplementedError

    def undo(self) -> None:
        raise NotImplementedError


class NoCommand(Command):
    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass


class MarcoCommand(Command):
    def __init__(self, commands: List[Command]):
        self._commands = commands

    def execute(self) -> None:
        for command in self._commands:
            command.execute()

    def undo(self) -> None:
        for command in self._commands[::-1]:
            command.undo()


class DeviceOnCommand(Command):
    def __init__(self, device: Device) -> None:
        self._device = device

    def execute(self) -> None:
        self._device.on()

    def undo(self) -> None:
        self._device.off()


class DeviceOffCommand(Command):
    def __init__(self, device: Device) -> None:
        self._device = device

    def execute(self) -> None:
        self._device.off()

    def undo(self) -> None:
        self._device.on()


class StereoVolumeUpCommand(Command):
    def __init__(self, stereo: Stereo) -> None:
        self._stereo = stereo

    def execute(self) -> None:
        self._stereo.set_volume(stereo.volume + 1)

    def undo(self) -> None:
        self._stereo.set_volume(stereo.volume - 1)


class RemoteControl:
    def __init__(self):
        self._on_commands = [NoCommand()] * 7
        self._off_commands = [NoCommand()] * 7
        self._undo_commands = []

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_pushed(self, slot: int) -> None:
        self._on_commands[slot].execute()
        self._undo_commands.append(self._on_commands[slot])

    def off_button_pushed(self, slot: int) -> None:
        self._off_commands[slot].execute()
        self._undo_commands.append(self._off_commands[slot])

    def undo_button_pushed(self) -> None:
        if not self._undo_commands:
            return
        self._undo_commands.pop().undo()


light = Light()
tv = Tv()
stereo = Stereo()

light_on_command, light_off_command = DeviceOnCommand(light), DeviceOffCommand(light)
tv_on_command, tv_off_command = DeviceOnCommand(tv), DeviceOffCommand(tv)
stereo_on_command, stereo_off_command = DeviceOnCommand(stereo), DeviceOffCommand(stereo)

volume_up_command = StereoVolumeUpCommand(stereo)

party_on_command = MarcoCommand([light_on_command, tv_on_command, stereo_on_command, volume_up_command])
party_off_command = MarcoCommand([light_on_command, tv_on_command, stereo_off_command])

remote = RemoteControl()
remote.set_command(0, light_on_command, light_off_command)
remote.set_command(1, tv_on_command, tv_off_command)
remote.set_command(2, stereo_on_command, stereo_off_command)
remote.set_command(3, party_on_command, party_off_command)

remote.on_button_pushed(1)
remote.on_button_pushed(3)
remote.undo_button_pushed()
