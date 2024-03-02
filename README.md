# mypackage
This library was created as an example/practice of how to publish your own Python package.

# How to
... import 'myModule' from the 'mypackage' package by: 
from mypackage import myModule
... this will allow any user to us the package function top_n, which will return, in descending order, the top 'n' values of an array.

"""This function is to return the top n items in an array in descending order

    Args:
        items (array): list or array-like object
        n (int): number of items we would want to return

    Return:
        array: display the top n items in desc. order

    Egs:
        >>> top_n([2,6,7,9,4], 3)
        -output: [9,7,6]
        >>> top_n([1,2,3,4,5,6], 5)
        -output: [6,5,4,3,2]
    """