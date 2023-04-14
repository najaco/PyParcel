import struct


class Char(str):
    """
    Represents the strict type for a char.
    """

    FORMAT: str = "=c"
    STANDARD_SIZE: int = 1

    def __init__(self, c: str = "\0"):
        if len(c) != 1:
            raise Exception("Char may only take arguments of length 1")
        super(str, Char).__init__(c)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self.encode('ascii'))

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0].decode('ascii'),
            data[self.STANDARD_SIZE:],
        )


class UnsignedChar(int):
    """
    Represents the strict type for an unsigned char.
    """

    FORMAT: str = "=B"
    STANDARD_SIZE: int = 1

    def __init__(self, c: int = 0):
        # Check range of unsigned char
        super(int, UnsignedChar).__init__(c)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self)

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0],
            data[self.STANDARD_SIZE:],
        )


class SignedChar(int):
    """
    Represents the strict type for a signed char.
    """

    FORMAT: str = "=b"
    STANDARD_SIZE: int = 1

    def __init__(self, c: int = 0):
        # Check range of Signed Char
        super(int, SignedChar).__init__(c)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self)

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0],
            data[self.STANDARD_SIZE:],
        )


class Short(int):
    """
    Represents the strict type for a short.
    """

    FORMAT: str = "=h"
    STANDARD_SIZE: int = 2

    def __init__(self, n: int = 0):
        if not -32768 <= n <= 32767:
            raise Exception("Short must be between -32768 and 32767")
        super(int, Short).__init__(n)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self)

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0],
            data[self.STANDARD_SIZE:],
        )


class UnsignedShort(int):
    """
    Represents the strict type for an unsigned short.
    """

    FORMAT: str = "=H"
    STANDARD_SIZE: int = 2

    def __init__(self, n: int = 0):
        if not 0 <= n <= 65535:
            raise Exception("Short must be between 0 and 65535")
        super(int, UnsignedShort).__init__(n)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self)

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0],
            data[self.STANDARD_SIZE:],
        )


class Int(int):
    """
    Represents the strict type for an integer.
    """

    FORMAT: str = "=i"
    STANDARD_SIZE: int = 4

    def __init__(self, n: int = 0):
        if not -2147483648 <= n <= 2147483647:
            raise Exception("Short must be between -2147483648 and 2147483647")
        super(int, Int).__init__(n)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self)

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0],
            data[self.STANDARD_SIZE:],
        )


class UnsignedInt(int):
    """
    Represents the strict type for an unsigned integer.
    """

    FORMAT: str = "=I"
    STANDARD_SIZE: int = 4

    def __init__(self, n: int = 0):
        if not 0 <= n <= 4294967295:
            raise Exception("Unsigned Integer must be between 0 and 4294967295")
        super(int, UnsignedInt).__init__(n)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self)

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0],
            data[self.STANDARD_SIZE:],
        )


class Long(int):
    """
    Represents the strict type for an long.
    """

    FORMAT: str = "=l"
    STANDARD_SIZE: int = 4

    def __init__(self, n: int = 0):
        if not -2147483648 <= n <= 2147483647:
            raise Exception("Long must be between -2147483648 and 2147483647")
        super(int, Long).__init__(n)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self)

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0],
            data[self.STANDARD_SIZE:],
        )


class UnsignedLong(int):
    """
    Represents the strict type for an unsigned long.
    """

    FORMAT: str = "=L"
    STANDARD_SIZE: int = 4

    def __init__(self, n: int = 0):
        if not 0 <= n <= 4294967295:
            raise Exception("UnsignedLong must be between 0 and 4294967295")
        super(int, UnsignedLong).__init__(n)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self)

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0],
            data[self.STANDARD_SIZE:],
        )


class LongLong(int):
    """
    Represents the strict type for a long long.
    """

    FORMAT: str = "=q"
    STANDARD_SIZE: int = 8

    def __init__(self, n: int = 0):
        if not -9223372036854775808 <= n <= 9223372036854775807:
            raise Exception("LongLong must be between 0 and 9223372036854775807")
        super(int, LongLong).__init__(n)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self)

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0],
            data[self.STANDARD_SIZE:],
        )


class UnsignedLongLong(int):
    """
    Represents the strict type for an unsigned long long.
    """

    FORMAT: str = "=Q"
    STANDARD_SIZE: int = 8

    def __init__(self, n: int = 0):
        if not 0 <= n <= 18446744073709551615:
            raise Exception(
                "UnsignedLongLong must be between 0 and 18446744073709551615"
            )
        super(int, UnsignedLongLong).__init__(n)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self)

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0],
            data[self.STANDARD_SIZE:],
        )


class Float(float):
    """
    Represents the strict type for a float.
    """

    FORMAT: str = "=f"
    STANDARD_SIZE: int = 4

    def __init__(self, n: int = 0):
        super(float, Float).__init__(n)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self)

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0],
            data[self.STANDARD_SIZE:],
        )


class Double(float):
    """
    Represents the strict type for a double.
    """

    FORMAT: str = "=d"
    STANDARD_SIZE: int = 8

    def __init__(self, n: int = 0):
        super(float, Double).__init__(n)

    def __pack__(self) -> bytes:
        return struct.pack(self.FORMAT, self)

    def __unpack__(self, data: bytes) -> (float, bytes):
        return (
            struct.unpack(self.FORMAT, data[: self.STANDARD_SIZE])[0],
            data[self.STANDARD_SIZE:],
        )
