def my(name,**data):
  print(name)
  for i,j in data.items():
   print(i,j)

my('navin',age = 25,city = 'mumbai')