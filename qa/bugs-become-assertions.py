def can_transmute(element):
    '''Can this element be turned into gold?'''

    # Bug #172: make sure the input is actually an element.
    assert is_valid_element(element)

    # Gold is trivial.
    if element is Gold:
        return True

    # Trans-uranic metals and halogens are impossible.
    if (element.atomic_number > Uranium.atomic_number) or \
       (element in Halogens):
        return False

    # Look for a sequence of steps that leads to gold.
    steps = search_transmutations(element, Gold)
    if steps == []:
        return False
    else:
        # Bug #201: must be at least two elements in sequence.
        assert len(steps) >= 2
        return True
