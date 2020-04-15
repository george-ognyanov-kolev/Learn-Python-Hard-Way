print("Marry and a little lamb.")
print("Its fleece was white as {}.".format("snow"))
print("And everywhere marry went")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "s"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# The end key of print function will set the string that needs to be appended when printing is done. 
# By default the end key is set by newline character. 
# So after finishing printing all the variables, a newline character is appended.

print(end1 + end2 + end3 + end4 + end5 + end6, end=" ")
print(end7 + end8 + end9 + end10 + end11 + end12)