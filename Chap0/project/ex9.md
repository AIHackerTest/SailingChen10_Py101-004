```
PS C:\Users\Administrator\Desktop> py -3 ex9.py
Here are the days:  Mon Tue Wed Thu Fri Sat Sun
Here are the months:  Jan
Feb
Mar
Apr
May
Jun
Jul
Aug

There's something going on here.
With the three double-quotes.
We'll beb able to type as much as we like.
```

```
PS C:\Users\Administrator\Desktop> cat ex9.py
# coding=utf-8

# Here's some new strange stuff, remember type is exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print ("Here are the days: ", days)
print ("Here are the months: ", months)

print ("""
There's something going on here.
With the three double-quotes.
We'll beb able to type as much as we like.
""")
PS C:\Users\Administrator\Desktop>
```
