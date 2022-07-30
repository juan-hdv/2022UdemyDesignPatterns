# Singleton metaclass
# Only instanciates once
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = (
                super(Singleton, cls).__call__(*args, **kwargs)
            )
        return cls._instances[cls]

# A singleton class should inherit from that metaclass
class Database1 (metaclass=Singleton):
    def __init__(self):
        print ("Loading")

# A singleton decorator
def singleton(class_):
    instances = {}

    def get_instance (*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance

# A singleton class should use the decotartor
@singleton
class Database1 (metaclass=Singleton):
    def __init__(self):
        print ("Loading")


"""
Write a method is_simgleton which takes a factory method that
returns an object and determines if that object is a singleton object
"""
def is_singleton(factory)-> bool:
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not

    f1 = factory()
    f2 = factory()

    return f1 is f2


