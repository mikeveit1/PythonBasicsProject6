def full_name(first_names):
    full_names = []
    for name in first_names:
        if name[0] == 'M':
            full_names.append(name + " " + "Miller")
    return full_names
