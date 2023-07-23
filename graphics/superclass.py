class MultipleConstructors:
    """
    A class that enables handling multiple constructors for a class.

    Constructors are defined as pairs of signature lists and corresponding initializer methods.

    Attributes:
        __constructors__: A list containing two sublists: one for constructor signatures and another for corresponding
                          initializer methods.

    Methods:
        __handle__: Handles the initialization of the class based on the provided constructor signature and arguments.
    """

    __constructors__ = [[], []]

    def __handle__(self, **kwargs):
        """
        Handles the initialization of the class based on the provided constructor signature and arguments.

        The method checks the provided keyword arguments against the constructor signatures and calls the corresponding
        initializer method if a match is found.

        Args:
            **kwargs: Keyword arguments passed during class initialization.

        Returns:
            int: Index of the called initializer method in the '__constructors__' list.

        Raises:
            KeyError: If no matching constructor is found for the provided initialization arguments.
        """
        constructor = tuple(kwargs.keys())
        constructor = constructor[0] if len(constructor) == 1 else constructor

        for i, constructor_scheme in enumerate(self.__constructors__[0]):
            if constructor == constructor_scheme:
                data = list(kwargs.values())
                self.__constructors__[1][i](self, *data)
                return i

        raise KeyError(f"\n    No matching constructor for initialization of {constructor}" /
                       "Candidate constructor not viable")
