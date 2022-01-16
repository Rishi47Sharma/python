def pig_latin(text):
  say = " "
  # Separate the text into words
  words = text.split()
  new_word=[]
  for word in words:
    # Create the pig latin word and add it to the list
    latin_word=word[1:]+word[:1]+"ay"
    new_word.append(latin_word)
    # Turn the list back into a phrase
  latin = say.join(new_word)
  return latin
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
