def top_counts(count_dict, n=10):
    """
    Get the top `n` elements with the highest counts from a dictionary.

    Parameters:
    count_dict (dict): A dictionary with elements as keys and their counts as values.
    n (int): The number of top elements to return (default is 10).

    Returns:
    list: A list of tuples (count, key) for the top `n` elements, sorted by count.

    Example:
    >>> counts = {'a': 5, 'b': 2, 'c': 8}
    >>> top_counts(counts, n=2)
    [(5, 'a'), (8, 'c')]
    """
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
