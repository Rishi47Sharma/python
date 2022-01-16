

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames=[]
i=0
for  item in filenames:
 if item.endswith("hpp"):
   newfilenames.append( item.replace("hpp","h"))
 else:
   newfilenames.append(item)


print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
