'''def convert_keys_to_string(dictionary):
    """Recursively converts dictionary keys to strings."""
    if not isinstance(dictionary, dict):
        return dictionary
    return dict((str(k), convert_keys_to_string(v))
        for k, v in dictionary.items())
'''
def convert_keys_to_string(my_dict):
    return {str(k): str(v) for k, v in my_dict.items()}
