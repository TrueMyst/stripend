Stripend | Documentation
=========================

``0`` Overview
------------------
``Stripend`` is Python module that includes utility methods for making your code shorter, more flexible, and smarter.

.. warning::
   This module requires Python 3.6 or above to work properly.


``1`` Installation
------------------

You may use pip or a similar tool to install latest versions of stripend
from the PyPi. To Install the Module -

-  Install the Stable Version:

.. code-block:: bash

   # Linux/macOS
   $ python3 -m pip install -U stripend

   # Windows
   $ python -3 -m pip install -U stripend

-  Install the Beta Version:

.. code-block:: bash

   $ pip install git+https://github.com/TrueMyst/stripend.git

``2`` Usage
-----------

To import the Module, you can do like this -

.. code-block:: python

   >>> import stripend

``2.1`` Examples
~~~~~~~~~~~~~~~~

.. code-block:: python

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

``3`` Available Functions
-------------------------

The following functions are currently available:

================= ======================= ===============
\                 **Available Functions** 
================= ======================= ===============
swap_keys_values  merge_dicts             string_is_empty
any_char_matches  has_unique_elements     method_source
merge_list        find_key_by_value       flatten_list
repeated_value    reverse_text            check_prefix
most_common_items -                       -
================= ======================= ===============

``4`` License
-------------

``stripend`` was created by TrueMyst. It is licensed under the terms of
the MIT license.

``5`` Documentation
-------------------
.. toctree::
   :maxdepth: 2
   :caption: Table of Contents 🧾

   ./stripend

``6`` Misc
---------- 

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
