class ChocolateBoiler:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ChocolateBoiler, cls).__new__(cls)
        return cls._instance


boiler_0 = ChocolateBoiler()
boiler_1 = ChocolateBoiler()

print(f"#0: {boiler_0}")
print(f"#1: {boiler_1}")
print(f"Are they the same object? {boiler_0 is boiler_1}")


# Implementation using variable - instantiated on module import:
class ChocolateBoiler:
    pass


chocolate_boiler = ChocolateBoiler()
print(f"Are they the same object? {chocolate_boiler is chocolate_boiler}")


# Implementation using function - using 'attr':
def get_chocolate_boiler() -> ChocolateBoiler:
    if not hasattr(get_chocolate_boiler, "instance"):
        setattr(get_chocolate_boiler, "instance", ChocolateBoiler())
    return getattr(get_chocolate_boiler, "instance")


print(f"Are they the same object? {get_chocolate_boiler() is get_chocolate_boiler()}")

# Implementation using function - using variable:
_chocolate_boiler = None


def get_chocolate_boiler() -> ChocolateBoiler:
    global _chocolate_boiler

    if not _chocolate_boiler:
        _chocolate_boiler = ChocolateBoiler()

    return _chocolate_boiler


print(f"Are they the same object? {get_chocolate_boiler() is get_chocolate_boiler()}")
