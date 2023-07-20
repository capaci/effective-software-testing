import pytest

from ._01_planning_poker import identify_extremes, Estimate


def test_basic_case():
    estimates: list[Estimate] = [
        Estimate('A', 5),
        Estimate('B', 15),
        Estimate('C', 3),
        Estimate('D', 4),
        Estimate('E', 9),
        Estimate('F', 8),
    ]

    result = identify_extremes(estimates)

    assert len(result) == 2
    assert 'C' in result
    assert 'B' in result


def test_reject_none_input():
    with pytest.raises(ValueError, match='Estimates cannot be None'):
        identify_extremes(None)


def test_reject_empty_list():
    with pytest.raises(ValueError, match='There has to be more than 1 estimate in the list'):
        identify_extremes([])


def test_reject_single_estimate():
    with pytest.raises(ValueError, match='There has to be more than 1 estimate in the list'):
        identify_extremes([Estimate('Eleanor', 1)])
