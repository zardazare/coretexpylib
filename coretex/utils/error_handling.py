from typing import Any, Callable, TypeVar, Generic, Union, NoReturn, Type, Tuple
from typing_extensions import ParamSpec

import logging


ParamsType = ParamSpec("ParamsType")
ReturnType = TypeVar("ReturnType")
ExceptionType = TypeVar("ExceptionType", bound = BaseException)


class Success(Generic[ReturnType]):

    __match_args__ = ("value",)

    def __init__(self, value: ReturnType) -> None:
        self.value = value

    def unwrap(self) -> ReturnType:
        return self.value


class Error(Generic[ReturnType]):

    __match_args__ = ("exception",)

    def __init__(self, exception: ExceptionType) -> None:
        self.exception = exception

    def unwrap(self) -> NoReturn:
        raise self.exception


class Throws(Generic[ExceptionType]):

    def __init__(self, exceptions: Tuple[Type[ExceptionType], ...]) -> None:
        self.exceptions = exceptions

    def __call__(self, function: Callable[ParamsType, ReturnType]) -> Callable[ParamsType, Union[Success[ReturnType], Error[ExceptionType]]]:
        def inner(*args: Any, **kwargs: Any) -> Union[Success[ReturnType], Error]:
            try:
                result = function(*args, **kwargs)
                return Success(result)
            except KeyboardInterrupt:
                raise
            except BaseException as ex:
                if len(self.exceptions) > 0 and not isinstance(ex, self.exceptions):
                    logging.warning(">> [Coretex] Received unexpected exception")

                return Error(ex)

        # Keep the original function name
        inner.__name__ = function.__name__

        return inner
