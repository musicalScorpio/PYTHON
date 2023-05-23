path = "excerpt.txt"
with open(path,"r") as f:
  lst = [line.strip() for line in f if line.strip()]
print(lst)

#Opening a csv file