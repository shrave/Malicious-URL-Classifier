'''def convert_keys_to_string(dictionary):
    """Recursively converts dictionary keys to strings."""
    if not isinstance(dictionary, dict):
        return dictionary
    return dict((str(k), convert_keys_to_string(v))
        for k, v in dictionary.items())
'''
import unicodedata
def convert_keys_to_string(my_dict):
    return {str(k): str(v) for k, v in my_dict.items()}

def average(num_list):
    return float(sum(num_list)) / max(len(num_list), 1)
def unicode_decode(string):
    return unicodedata.normalize('NFKD', string).encode('ascii','ignore')
