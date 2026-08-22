def flatten_dictionary(d: dict, parent_key: str = "", sep: str = ".") -> dict:
    """Recursively flattens a nested dictionary into dot-separated keys with string values."""
    flat_dict = {}
    for key, value in d.items():
        new_key = f"{parent_key}{key}"
        if isinstance(value, dict):
            flat_dict.update(flatten_dictionary(value, f"{new_key}{sep}", sep=sep))
        else:
            flat_dict[new_key] = str(value)
    return flat_dict