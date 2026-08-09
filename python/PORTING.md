# C# to Python source mapping

All 70 algorithm sources under `TestLeetCode/<Category>` map one-to-one to
`python/<category>/<snake_case_name>.py`. Category names and filenames are
normalized to Python conventions; the original C# files remain authoritative
historical references and are not modified.

Notable normalized names:

- `Graph/CouseSchedule2.cs` → `graph/course_schedule_2.py`
- `Graph/RottenOrange.cs` → `graph/rotten_orange.py`
- `Tree/LCABst.cs` → `tree/lca_bst.py`
- `TwoPointer/IsValidPalandrom.cs` → `two_pointer/is_valid_palandrom.py`

Public C# solution methods use snake_case in Python. Stateful data structures
retain their familiar class names. Explicitly obsolete implementations
(`ThreeSumOld` and `IsValidBSTSolutionWrong`) are intentionally not ported.
