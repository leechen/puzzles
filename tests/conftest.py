from dataclasses import dataclass
from typing import Optional

import pandas as pd
import pytest


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


@pytest.fixture
def bst() -> TreeNode:
    return TreeNode(
        6,
        left=TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
        right=TreeNode(8, TreeNode(7), TreeNode(9)),
    )


@pytest.fixture
def churn_data() -> pd.DataFrame:
    rows = []
    for customer_id in range(1, 31):
        churn = int(customer_id % 3 == 0 or customer_id % 7 == 0)
        rows.append(
            {
                "customer_id": customer_id,
                "age": 20 + customer_id,
                "tenure": 36 - customer_id,
                "monthly_spend": 35.0 + customer_id * 4.5,
                "churn": churn,
            }
        )
    return pd.DataFrame(rows)
