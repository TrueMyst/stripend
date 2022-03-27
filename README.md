# stripend 0.1.2

<p align = "center"><img width="750" height="350" src="https://i.imgur.com/O0r8lYo.png"></p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python module that includes utility methods for making your code shorter, more flexible, and smarter.

## Tables of Contents
* `0` [Updates](#0-updates)
* `1` [Installation](#1-installation)
* `2` [Usage](#2-usage)
    * `2.1` [Examples](#21-examples)
* `3` [Modules](#3-available-functions)
* `4` [Feedback](#4-feedback)
* `5` [License](#5-license)

## `0` Updates
- New features: 
    - The function names have been changed to Snake Case.
    - Changed `MostCommon()` function to `most_common_items()`

- Bug Fixes 



## `1` Installation 
You may use pip or a similar tool to install latest versions of stripend from the PyPi. To Install the Module - 

- Install the Stable Version: 
```bash
# Linux/macOS
$ python3 -m pip install -U stripend

# Windows
$ py -3 -m pip install -U stripend
```
- Install the Beta Version:
```cmd
pip install git+https://github.com/TrueMyst/stripend.git
```
## `2` Usage 
To import the Module, you can do like this - 
```py
>>> import stripend
```
### `2.1` Examples
```py
>>> import stripend

# Use "HasUniqueElements" to check whether a list has any unique items.
>>> random_list = ["Banana", "Apple", "Orange", "Cherry", "Blueberry"]

>>> print(stripend.has_unique_elements(random_list))
>>> True 

# Use "Flattenlist()" to flatten a nested list.
>>> nested_list = [["Banana", "Apple"], ["Orange"], ["Cherry", "Blueberry"]]

>>> print(stripend.flatten_list(nested_list))
>>> ["Banana", "Apple", "Orange", "Cherry", "Blueberry"]

>>> xyz = {"Say" : "1", "Hello" : "2", "World" : "3"}

>>> print(stripend.find_key_by_value(xyz, "2"))
>>> 'Hello'
```


## `3` Available Functions

The following functions are currently available:

|                   | **Available Functions** |                 |
| :--------         | :----------------       | :------------   |
| swap_keys_values  | merge_dicts             | string_is_empty |
| any_char_matches  | has_unique_elements     | method_source   |
| merge_list        | find_key_by_value       | flatten_list    |
| repeated_value    | reverse_text            | check_prefix    |
| most_common_items |         -               |       -         |


## `4` Feedback

If you have any feedback, please reach out to us at our [Discord](https://discord.gg/your_link)

## `5` License
`stripend` was created by TrueMyst. It is licensed under the terms of the MIT license.

