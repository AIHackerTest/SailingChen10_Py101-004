```
PS C:\Users\Administrator\Desktop> py -3 ex7.py
Mary had a little lamb.
Its fleece was white as snow.
And everywhere that Mary went.
..........
Cheese
Burger
```

```
PS C:\Users\Administrator\Desktop> cat ex7.py
# coding=utf-8

print ("Mary had a little lamb.")
print ("Its fleece was white as %s." % 'snow')
print ("And everywhere that Mary went.")
print ("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see waht happens
print (end1 + end2 + end3 + end4 + end5 + end6,)
print (end7 + end8 + end9 + end10 + end11 + end12)
PS C:\Users\Administrator\Desktop>
```
