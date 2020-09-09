import pytest
from pysumtypes import (
    sumtype, SumTypeAttributeNotFound, SumTypeInitError)
from dataclasses import dataclass


@dataclass
class Success:
    data: str


@dataclass
class Failure:
    error_code: int
    error_message: str


@sumtype
class Response:
    success: Success
    failure: Failure


@dataclass
class Whut:
    x: str


class NoInit:
    x: int


@sumtype
class BadResponse:
    success: Success
    failure: Failure
    oops: Failure


def test_sumtype_correct():
    s = Response(Success('it worked'))
    f = Response(Failure(401, error_message='oh no'))
    assert s.match(Success)
    assert f.match(Failure)
    assert s.data == 'it worked'
    assert f.error_code == 401


def test_eq_override():
    sr = Response(Success(data='it worked'))
    s = Success('it worked')
    no = Success('uh oh')
    assert sr.match(Success)
    assert sr == s
    assert not sr.match(Failure)
    assert sr != no


def test_sumtype_bad_init():
    with pytest.raises(SumTypeInitError):
        Response(Whut('it worked'))
    with pytest.raises(SumTypeInitError):
        Response(NoInit())
    with pytest.raises(SumTypeInitError):
        BadResponse(Success("Wow"))


def test_sumtype_bad_access():
    s = Response(Success('it worked'))
    with pytest.raises(SumTypeAttributeNotFound):
        s.error_code


def test_sumtype_unwrap():
    s = Response(Success('it worked'))
    s = s.unwrap()
    assert (type(s)) == Success
