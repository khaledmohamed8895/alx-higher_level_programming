#!/usr/bin/python3
"""Student Class"""


class Student:
    """class Student that defines a student by"""

    def __init__(self, first_name, last_name, age):
        """constractor

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): number of age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json

        Args:
            attrs (_type_, optional): _description_. Defaults to None.

        Returns:
            dictionary: data structure
        """
        if attrs is None:
            return self.__dict__
        dictionary = dict()
        for element in attrs:
            for key in self.__dict__:
                if element == key:
                    dictionary[element] = self.__dict__[key]
        return dictionary

    def reload_from_json(self, json):
        """_summary_

        Args:
            json (_type_): _description_
        """
        for element in self.__dict__:
            for key in json:
                if element == key:
                    self.__dict__[key] = json[key]
