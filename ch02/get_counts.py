def get_counts(sequence):
    """
    Count the occurrences of each unique element in a sequence.

    Parameters:
    sequence (iterable): A sequence of elements (e.g., list, tuple, string).

    Returns:
    dict: A dictionary with unique elements as keys and their counts as values.

    Examples:
    >>> get_counts(["apple", "banana", "apple", "orange"])
    {'apple': 2, 'banana': 1, 'orange': 1}

    >>> get_counts("hello")
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
