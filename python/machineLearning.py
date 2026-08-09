"""Train a logistic regression model and rank customers by churn risk."""

from typing import Final

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


FEATURE_COLUMNS: Final = ["age", "tenure", "monthly_spend"]
REQUIRED_COLUMNS: Final = ["customer_id", *FEATURE_COLUMNS, "churn"]


def rank_churn_risk(
    data: pd.DataFrame,
    top_n: int = 10,
    test_size: float = 0.3,
    random_state: int = 42,
) -> pd.DataFrame:
    """Return the customers with the highest modeled churn probabilities.

    A train/test split is used to keep model training representative of the
    original exercise. The fitted model then ranks all supplied customers.
    The input DataFrame is never modified.
    """
    missing = [column for column in REQUIRED_COLUMNS if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    if top_n <= 0:
        raise ValueError("top_n must be greater than zero")
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between zero and one")

    churn_values = set(data["churn"].dropna().unique())
    if churn_values != {0, 1}:
        raise ValueError("churn must contain both binary classes 0 and 1")

    features = data[FEATURE_COLUMNS]
    labels = data["churn"]
    train_features, _, train_labels, _ = train_test_split(
        features,
        labels,
        test_size=test_size,
        random_state=random_state,
        stratify=labels,
    )

    scaler = StandardScaler()
    scaled_train_features = scaler.fit_transform(train_features)
    model = LogisticRegression(random_state=random_state)
    model.fit(scaled_train_features, train_labels)

    churn_class_index = list(model.classes_).index(1)
    ranked = data.copy(deep=True)
    ranked["prob_churn"] = model.predict_proba(scaler.transform(features))[
        :, churn_class_index
    ]
    return (
        ranked.sort_values("prob_churn", ascending=False, kind="stable")
        .head(top_n)
        .reset_index(drop=True)
    )
