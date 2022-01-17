def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  new_list=[]
  for student in list2:
    new_list.append(student)
  list1.reverse()
  for student in list1:
    new_list.append(student)  
  # Followed by the elements of list1 in reverse order
  return new_list
  
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
