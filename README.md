# Py Sum Types

[![Build Status](https://api.travis-ci.org/danpozmanter/PySumTypes.svg?branch=main&status=unknown)](https://travis-ci.org/danpozmanter/PySumTypes) [![PyPi Package](https://img.shields.io/pypi/v/PySumtypes.svg)](https://pypi.org/project/PySumTypes/)

**Simple syntax to declare, match, compare, and unwrap sum types for Python**

`Sum Types`, aka `Discriminated Unions` are a kind of `Algebraic Data Type` (`ADT`) found in strongly typed functional languages (among other places).

```fsharp
type Success = {Data: string}
type Failure = {ErrorCode: int; ErrorMessage: string}
type Response =
    | Succeeded of Success
    | Failed of Failure

let example(a: int) =
    if (a > 0) then
        Response.Succeeded <| {Data="Data!"}
    else
        Response.Failed <| { ErrorCode=401; ErrorMessage="Nope"}

let response = example(22)

match response with
    | Response.Succeeded s -> printf "%s\n" s.Data
    | Response.Failed f -> printf "%s\n" f.ErrorMessage
```

### Definition & Useage

So how might we do this in Python?

#### Definition

```python

@dataclass
class Success:
    data: str
    count: int

@dataclass
class Failure:
    error_code: int
    error_message: str

@sumtype
class Response:
    success: Success
    failure: Failure
```

#### Useage

```python
def example(a:int) -> Response:
    if a > 0:
        return Response(Failure(error_code=403, error_message='Not Today'))
    return Response(Success('Wow such data', count=500))

response = example(22)

if response.match(Success):
    print('Look at this data {}'.format(response.data))
    actual_instance = response.unwrap()
    actual_instance.count += 1000
else:
    print('Oh what have we done sweet corgi buns!!! Error: {}'.format(response.error_message))
    if response == Failure(403, 'Not Today'):
        print('Not today!!!')
```

#### Exceptions

```python
x = example(22)
print('Look at this data {}'.format(x.data))
# raises a SumTypeAttributeNotFound exception
```

```python
@dataclass
class Failcess:
    error_message: str
    error_code: int

@sumtype
class TooManyTypes:
    success: Success
    hurray: Success
    fail: Failure
    oops: Failure

def example(a) -> TooManyTypes:
    return TooManyTypes(Success('Wow such data', 500))
    # raises a SumTypeInitError exception
    # Sum Types should have unique types
```
