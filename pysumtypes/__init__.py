"""PySumType"""
__version__ = '0.0.1'


class SumTypeInitError(Exception):
    """Sum Type initialization error"""

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f'Sum Type Init Error: {self.message}'


class SumTypeAttributeNotFound(Exception):
    """Attribute not found error"""

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f'Sum Type Attribute Not Found: {self.message}'


def sumtype(cls):
    """sumtype class decorator"""

    class SumTypeWrapper(object):
        def __init__(self, instance):
            """
            Initialize Sum Type

            SumTypeExample(SubType(arg1, arg2))

            :param instance: Initialized class
            :type python_type: Class instance
            :return: Wrapped Sum Type
            :rtype: Wrapped Sum Type that for match/compare/get/unwrap
            :raises SumTypeInitError: Initialization error (with message)
            """
            types = cls.__annotations__.values()
            if type(instance) not in types:
                raise SumTypeInitError(message='sum type - type not found')
            if len(types) != len(set(types)):
                raise SumTypeInitError(
                    message='sum type - subtypes in a sum type must be unique')
            self._instance = instance
            self._active_type = type(self._instance)

        def __eq__(self, obj):
            """
            Compare wrapped type to obj

            :param obj: Object to compare
            :type obj: Any
            :return: Whether wrapped type == obj
            :rtype: bool
            """
            return self._instance == obj

        def __getattr__(self, name):
            """
            Compare wrapped type to obj

            :param name: Name of attribute to get
            :type obj: str
            :return: Value of attribute if found
            :rtype: type of attribute if found
            :raises SumTypeAttributeNotFound: Attribute not found error
            """
            if not hasattr(self._instance, name):
                raise SumTypeAttributeNotFound(message=f'{name} not found')
            return getattr(self._instance, name)

        def match(self, python_type):
            """
            Match against type

            variable.match(ExampleClass)

            :param python_type: Python type to match against
            :type python_type: type
            :return: Whether the wrapped type matches the python type provided
            :rtype: bool
            """
            return self._active_type == python_type

        def unwrap(self):
            """
            Retrieve the wrapped instance
            :return: Wrapped instance
            :rtype: type of wrapped instance
            """
            return self._instance

    return SumTypeWrapper
