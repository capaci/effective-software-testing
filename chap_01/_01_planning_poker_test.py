from random import shuffle

from hypothesis import given, strategies as st
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


@given(
    st.lists(
        st.tuples(
            st.text(min_size=1, max_size=2),
            st.integers(2, 99)
        ),
        min_size=2,
        max_size=5,
    ))
def test_many_estimates(estimates):
    """
    Hypothesis will generate a random list of estimates.
    
    With the parameters, we ensure the estimates will always be in the range 2..99
    Then we insert 1 and 100 to ensure the min and max estimates are known.
    """
    estimates_input = [
        Estimate(estimate[0], estimate[1])
        for estimate in 
    estimates]

    estimates_input.append(Estimate('MinDev', 1))
    estimates_input.append(Estimate('MaxDev', 100))

    shuffle(estimates_input)

    result = identify_extremes(estimates_input)


    assert len(result) == 2
    assert 'MinDev' in result
    assert 'MaxDev' in result
