from datetime import datetime, timezone

def transform_animal_data(all_animals):
  """Transforms the 'friends' and 'born_at' fields in the animal data."""

  for animal_id, details in all_animals.items():
    if details.get('friends'):
      details['friends'] = details['friends'].split(',')
    else:
      details['friends'] = []

    born_at = details.get('born_at')
    if born_at:
      dt = datetime.fromtimestamp(born_at / 1000, tz=timezone.utc)
      details['born_at'] = dt.isoformat()