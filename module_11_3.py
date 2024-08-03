import inspect

class Introspection:
   # @staticmethod
    def introspection_info(obj):
        obj_type = str(type(obj))
        attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
        methods = [method for method in dir(obj) if callable(getattr(obj, method))]
        module = inspect.getmodule(obj).__name__ if inspect.ismodule(obj) else None

        result = {
            'type': obj_type,
            'attributes': attributes,
            'methods': methods,
            'module': module
        }
        return result


number_info = Introspection.introspection_info(42)
print(number_info)

str_1 = 'aaaaaa'
str_info = Introspection.introspection_info(str_1)
print(str_info)

self_class = Introspection
self_info = Introspection.introspection_info(self_class)
print(self_info)