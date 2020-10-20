"""
A simple hello world
"""


def hello(name):
    """
    Simple function that prints "Hello X" for 
    an input `name`. 

    Parameters
    ----------
        name : str
            The name of the person.

    Returns
    -------
        greeting: str
            The message - Hello `name`.
    """
    if type(name) != str:
        raise ValueError("Name should be a string")
    greeting = "Hello " + name
    return greeting


class ChatBot(object):
    """
    Simple class that acts as a bot.
    
    Parameters
    —————————-
    name : str
            The name of the person.
    """

    def __init__(self, name):
        self.name = name
        if type(name) != str:
            raise ValueError("Name should be a string")

    def hello(self):
        """
        Simple function that prints Hello `name`
        an input `name`. 

        Returns
        ——————-
        str
            The message - Hello `name`.
        """
        return "Hello " + self.name

    def goodbye(self):
        """
        Simple function that prints Bye `name`
        an input `name`. 

        Returns
        ——————-
        str
            The message - Bye `name`.
        """
        return "Bye " + self.name
