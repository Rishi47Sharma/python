def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  for Rorys_guests,friends_Rorys in guests1.items():
    for Taylors_guests,friends_Taylors in guests2.items():
      if Taylors_guests == Rorys_guests:
        guests1[Rorys_guests]+=guests2[Taylors_guests]


  return guests1
