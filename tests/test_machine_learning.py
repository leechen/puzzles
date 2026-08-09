import pandas as pd
import pytest

from python.machineLearning import rank_churn_risk


def test_rank_churn_risk_returns_sorted_top_customers(churn_data):
    original = churn_data.copy(deep=True)

    result = rank_churn_risk(churn_data, top_n=10, random_state=7)

    assert len(result) == 10
    assert result["prob_churn"].between(0, 1).all()
    assert result["prob_churn"].is_monotonic_decreasing
    pd.testing.assert_frame_equal(churn_data, original)


def test_rank_churn_risk_is_deterministic(churn_data):
    first = rank_churn_risk(churn_data, top_n=5, random_state=11)
    second = rank_churn_risk(churn_data, top_n=5, random_state=11)
    pd.testing.assert_frame_equal(first, second)


def test_rank_churn_risk_returns_all_rows_when_top_n_is_larger(churn_data):
    assert len(rank_churn_risk(churn_data, top_n=100)) == len(churn_data)


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda frame: frame.drop(columns=["age"]), "Missing required columns: age"),
        (lambda frame: frame.assign(churn=0), "churn must contain both binary classes"),
    ],
)
def test_rank_churn_risk_validates_data(churn_data, mutation, message):
    with pytest.raises(ValueError, match=message):
        rank_churn_risk(mutation(churn_data))


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"top_n": 0}, "top_n must be greater than zero"),
        ({"test_size": 0}, "test_size must be between zero and one"),
        ({"test_size": 1}, "test_size must be between zero and one"),
    ],
)
def test_rank_churn_risk_validates_options(churn_data, kwargs, message):
    with pytest.raises(ValueError, match=message):
        rank_churn_risk(churn_data, **kwargs)
