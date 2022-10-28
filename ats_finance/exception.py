class NotAValidSource(Exception):
    """Exception raised for an invalid source arg"""

    def __init__(self, message: str = "Not a valid source argument.") -> None:
        super().__init__(message)


class NotAValidTicker(Exception):
    """Exception raised for an invalid ticker arg"""

    def __init__(self, message: str = "Not a valid ticker argument.") -> None:
        super().__init__(message)


class MissingRequestArgument(Exception):
    """Exception raised when missing a request argument"""

    def __init__(self, message: str = "Not a valid request argument.") -> None:
        super().__init__(message)


class MissingPolygonApiKey(Exception):
    """Exception raised when missing a request argument"""

    def __init__(self, message: str = "Missing polygon api key.") -> None:
        super().__init__(message)


class NotAValidIntervalType(Exception):
    """Exception raised for an invalid interval_type"""

    def __init__(self, message: str = "Not a valid interval_type argument.") -> None:
        super().__init__(message)
