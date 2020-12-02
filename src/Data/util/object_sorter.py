def object_sorter(objects):
    objects = sorted(objects, key=lambda k: k.id)
    return objects