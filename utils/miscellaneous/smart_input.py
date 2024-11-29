from view.base import BaseView
from utils.exceptions.InadequateArgumentsException import InadequateArgumentsException
def smart_input(*args, **kwargs) -> dict[str, any]:
    # in the kwargs:
    # key = name of the argument
    # value = if not None, refers to the typecast function of that type, None otherwise
    for i, key in enumerate(kwargs.keys()):
        cast_func = kwargs[key]
        if (i >= len(args)):
            key_name = key.replace('_', ' ')
            
            print(f"{key_name}: ")
            arg_prompt = BaseView.get_argument_prompt(key)
            if arg_prompt:
                print(f"({arg_prompt})")
            arg = input()
            if not arg and cast_func:
                raise InadequateArgumentsException(f"{key_name} can not be null!")
            if cast_func:
                arg = cast_func(arg)
            kwargs[key] = arg
        else:
            arg = args[i]
            if cast_func:
                arg = cast_func(arg)
            kwargs[key] = arg
    return kwargs