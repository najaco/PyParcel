from typing import Generic, List, TypeVar, Tuple, Any
import struct

T = TypeVar("T")
INT_MAX = (1 << 31) - 1
INT_MIN = -1 << 31
ENCODING = "utf-8"


def raise_(ex):
    raise ex

class Architecture:

    def __init__(self, sint:int = 4, sbool: int = 1, sfloat: int = 4, str_length: int = 4):
        self._data = {}
        self._data[int] = sint
        self._data[bool] = sbool
        self._data[float] = sfloat
        self._data["str_length"] = str_length

    def __getitem__(self, key: Any) -> int:
        if key not in self._data:
            raise IndexError

        return self._data[key]

class ConfigManager:
    def __init__(self, size_config: Architecture = Architecture()):
        self._size_config = size_config

    @property
    def Architecture(self) -> Architecture:
        return self._size_config

    @Architecture.setter
    def Architecture(self, size_config: Architecture) -> None:
        self._size_config = size_config

config_manager: ConfigManager = ConfigManager()

def configure(architecture: Architecture) -> None:
    config_manager.SizeConfig = architecture

X86_ARCHITECTURE: Architecture = Architecture()  

# find a way to set default size for int
pack_dict = {
    int: (
        lambda obj: struct.pack("i", obj)
    ),  # if INT_MIN <= obj <= INT_MAX else pack("q", obj)),
    bool: (lambda obj: struct.pack("?", obj)),
    float: (lambda obj: struct.pack("f", obj)),
    bytes: (lambda obj: struct.pack("i{}s".format(len(obj)), len(obj), obj)),
    str: (
        lambda obj: struct.pack("i{}s".format(len(obj)), len(obj), obj.encode(ENCODING))
    ),
    list: (lambda obj: b"".join([pack(x) for x in vars(obj)])),
    set: (lambda obj: raise_(NotImplementedError)),
    dict: (lambda obj: raise_(NotImplementedError)),
    tuple: (lambda obj: pack(*obj)),
}

unpack_dict = {
    int: (
        lambda _, data: (
            struct.unpack("i", data[: config_manager.SizeConfig[int]])[0],
            data[config_manager.SizeConfig[int] :],
        )
    ),
    bool: (
        lambda _, data: (
            struct.unpack("?", data[: config_manager.SizeConfig[bool]])[0],
            data[config_manager.SizeConfig[bool] :],
        )
    ),
    float: (
        lambda _, data: (
            struct.unpack("f", data[: config_manager.SizeConfig[float]])[0],
            data[config_manager.SizeConfig[float] :],
        )
    ),
    bytes: (lambda _, data: unpack_bytes(data)),
    str: (lambda _, data: unpack_string(data)),
    list: (lambda obj, _: raise_(NotImplementedError)),
    set: (lambda obj, _: raise_(NotImplementedError)),
    dict: (lambda obj, _: raise_(NotImplementedError)),
    tuple: (lambda obj, data: unpack_tuple(data, obj)),
}


def unpack_string(data: bytes) -> (str, bytes):
    result, data = unpack_bytes(data)
    return result.decode(ENCODING), data


def unpack_bytes(data: bytes) -> (bytes, bytes):
    length = struct.unpack("i", data[: config_manager.SizeConfig["str_length"]])[0]
    data = data[config_manager.SizeConfig["str_length"] :]
    return struct.unpack("{}s".format(length), data[:length])[0], data[length:]


def unpack_tuple(data: bytes, t: Tuple[Any]) -> (Tuple[Any], bytes):
    unpacked_objs = []
    for obj in t:
        (result, data) = _unpack(data, obj)
        unpacked_objs.append(result)
    return tuple(unpacked_objs), data


def pack(*objs) -> bytes:
    return b"".join(
        [
            pack_dict.get(
                type(obj),
                lambda o: b"".join([pack(o.__getattribute__(x)) for x in vars(o)]),
            )(obj)
            for obj in objs
        ]
    )


def _unpack(data: bytes, obj: T) -> (T, bytes):
    if type(obj) in unpack_dict:
        return unpack_dict[type(obj)](obj, data)
    else:
        for v in vars(obj):
            (result, data) = _unpack(data, obj.__getattribute__(v))
            obj.__dict__[v] = result
    return obj, data


def unpack(data: bytes, *objs) -> Tuple[Any]:
    if len(objs) == 0:
        raise TypeError("unpack() takes a variable number of objects")
    if len(objs) == 1:
        return _unpack(data, objs[0])[0]
    else:
        unpacked_objs = []
        for obj in objs:
            (result, data) = _unpack(data, obj)
            unpacked_objs.append(result)
        return tuple(unpacked_objs)
