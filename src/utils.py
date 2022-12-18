import os

def get_env_variable(name):
    """
    Gets the value of an environment variable or raises an exception if it is not set.
    """
    try:
        return os.environ[name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(name)
        raise EnvironmentError(error_msg)
