def filter_dict(**kwargs):
  """a function that filters the dict"""
  if kwargs:
    clean_data = {}
    for key, value in kwargs.items():
      if isinstance(value, int, float)
      clean_data[key] = value
      