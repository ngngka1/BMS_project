from utils.exceptions.InadequateArgumentsException import InadequateArgumentsException
def smart_input(*args, kwargs) -> dict[str, any]: # this is not wrong fyi, kwargs is intentional
    for i, key in enumerate(kwargs.keys()):
        if (i >= len(args)):
            key_name = key.replace('_', ' ')
            arg = input(f"Input {key_name}: ")
            if not arg:
                raise InadequateArgumentsException(f"{key_name} can not be null!")
            kwargs[key] = arg
        else:
            kwargs[key] = args[i]
    return kwargs