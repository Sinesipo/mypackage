from mypackage import myFunction
def test_top_n():
     """Return the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object containing numerical values.
        n (int): number of top items to return.

    Returns:
        array: top n items, in descending order.

    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    """
    assert myFunction.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'incorrect'
    assert myFunction.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert myFunction.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'
