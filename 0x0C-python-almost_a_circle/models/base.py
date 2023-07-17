#!/usr/bin/python3
""" module doc """
import json


class Base:
    """ class doc """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__+".json"
        with open(filename, 'w', encoding="utf-8") as f:
            list = []
            for ele in list_objs:
                list.append(ele.to_dictionary())
            json.dump(json.loads(cls.to_json_string(list)), f)

    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__+".json"
        with open(filename, encoding="utf-8") as f:
            newlist = []
            dict = cls.from_json_string(json.dumps(json.load(f)))
            for ele in dict:
                if cls.__name__ == "Square":
                    del ele["height"]
                    ele["size"] = ele["width"]
                    del ele["width"]
                newlist.append(cls.create(**ele))
            return newlist
