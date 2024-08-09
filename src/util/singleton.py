from typing import Dict, Type


class SingletonMeta(type):
    """Singleton metaclass para ser usada em classes que devem ter apenas uma instância"""

    _instances: Dict[Type, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
