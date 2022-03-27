import re, inspect, itertools

from typing import Union
from collections import Counter


def swap_keys_values(_dict: dict):
    """Swaps the Keys and Values in Dictionary.

    Parameters
    ----------
    _dict : dict
        The dictionary that needs to be reversed.

    Returns
    -------
    swapped_dict : dict
        Returns the Swapped/Reversed Dictionary.
    """
    swapped_dict = {value: key for key, value in _dict.items()}

    return swapped_dict


def merge_dicts(*_dicts: dict):
    """Merges numerous dictionaries into just one.

    Parameters
    ----------
    _dicts : dict
        The list of dictionaries which should be merged.

    Returns
    -------
    merge_dicts : dict
        Returns the Merged Dictionary.
    """
    return {key: value for d in _dicts for key, value in d.items()}


def string_is_empty(string: str):
    """Checks to see whether the string is empty.

    Parameters
    ----------
    string : str
        The string that needs to be checked.

    Returns
    -------
    is_empty : str
        Checks the length of the string and
        Returns `True` if the string is empty, else `False`.
    """

    is_empty = bool(len(string) <= 0)

    return is_empty


def any_char_matches(substring: str, mainString: str):
    """Scans the string for any matches a certain pattern.

    Parameters
    ----------
    substring : str
        The string that is used to find matches from `mainString`.

    mainString : str
        The `mainstring` which contains the original string.

    Returns
    -------
    is_matching : bool
        Returns `True` if the `substring` matches with the `mainSting` else `False`.
    """
    is_matching = bool(re.search(substring, mainString))

    return is_matching


def has_unique_elements(_list: Union[list, tuple]):
    """Determines whether or not the items of a list are unique.

    Parameters
    ----------
    _list : Union[list, tuple]
        The list that must be checked.

    Returns
    -------
    is_unique : bool
        Returns `True` if the items of the lists are unique, else `False`.
    """
    is_unique = len(set(_list)) == len(_list)

    return is_unique


def method_source(method):
    """Returns the Source Code of an object/method.

    Parameters
    ----------
    method : function
        The method or function that will be used to retrieve the source code.

    Returns
    -------
    source_code : str
        The source code of the method.
    """
    source_code = "".join(inspect.getsourcelines(method)[0])

    return source_code


def merge_list(*_list: list):
    """Combines multiple lists into a new one.

    Parameters
    ----------
    *_list : list
        It contains all of the lists inside it.

    Returns
    -------
    merged_list : list
        Returns the Merged list.
    """
    merged_list = []

    for list in _list:
        merged_list.extend(iter(list))

    return merged_list


def find_key_by_value(_dict: dict, value: str):
    """Finds the Key by using the value in the dictionary.

    Parameters
    ----------
    _dict : dict
        The dictionary, which contains the keys and values.

    value : str
        The dictionary's value, which will be used to find the key.

    Returns
    -------
    dict_key : str
        Returns the Dictionary's Key based on the Value.
    """
    dict_key = list(_dict.keys())[list(_dict.values()).index(value)]

    return dict_key


def flatten_list(_list: list):
    """Flattens a nested list properly.

    Parameters
    ----------
    _list : list
        Contains the list with nested lists within it.

    Returns
    -------
    flattened_list : list
        Returns the flattened list.
    """
    flatten_list = itertools.chain(*_list)

    return flatten_list


def repeated_value(content: Union[str, list, tuple]):
    """Finds the most frequently common value.

    Parameters
    ----------
    content : Union[list, tuple]
        Contains the list/string/tuple's value.

    Returns
    -------
    repeated_value : str
        Returns the Repeated Value.
    """
    if type(content) == str:
        return max(set(list(content)), key=content.count)

    repeated_value = max(set(content), key=content.count)

    return repeated_value


def reverse_text(_char: str):
    """Returns the text in reverse order.

    Parameters
    ----------
    _char : str
        The original/raw string.

    Returns
    -------
    reversed_str : str
        Returns the reversed string.
    """
    return _char[::-1]


def check_prefix(prefix: Union[str, tuple, list], content: str):
    """Determines whether or not the prefix matches the content.

    Parameters
    ----------
    prefix : Union[str, tuple, list]
        The affix that appears at the beginning of a sentence.

    content : str
        The string that contains the content.

    Returns
    -------
    starts_with_prefix : bool
        _description_
    """
    starts_with_prefix = bool(content.startswith(tuple(prefix)))

    return starts_with_prefix


def most_common_items(content: Union[str, list, tuple]):
    """Finds the top three most commonly given values.

    Parameters
    ----------
    content : Union[str, list, tuple]
        The `content` is composed of the items/values.

    Returns
    -------
    common_elements : list
        Returns a list containing the three most common values.
    """
    common_elements = Counter(content).most_common(3)

    return common_elements
