def merge_and_average_dicts(dict1, dict2):
    merged_dict = {}
    
    # Get the common keys from both dictionaries
    common_keys = set(dict1.keys()).intersection(set(dict2.keys()))
    
    # Merge the unique keys from dict1
    for key in set(dict1.keys()).difference(common_keys):
        merged_dict[key] = dict1[key]
    
    # Merge the unique keys from dict2
    for key in set(dict2.keys()).difference(common_keys):
        merged_dict[key] = dict2[key]
    
    # Calculate average (ceil) for common keys
    for key in common_keys:
        average = math.ceil((dict1[key] + dict2[key]) / 2)
        merged_dict[key] = average
    
    return merged_dict
