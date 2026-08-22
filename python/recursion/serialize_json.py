def serialize(d: dict, parent_key: str = "", sep: str = ".") -> str:
    """Recursively flattens a nested dictionary and formats it into key:value strings."""

    def flatten_dictionary(
        current_dict: dict, current_key: str = "", separator: str = "."
    ) -> dict:
        flat_dict = {}
        for key, value in current_dict.items():
            new_key = f"{current_key}{key}"
            if isinstance(value, dict):
                flat_dict.update(
                    flatten_dictionary(
                        value, f"{new_key}{separator}", separator=separator
                    )
                )
            else:
                flat_dict[new_key] = str(value)
        return flat_dict

    flattened = flatten_dictionary(d, parent_key, sep)
    res = []
    for key, val in flattened.items():
        res.append(f"{key}:{val}")
    return ";".join(res)