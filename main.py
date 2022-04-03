import re
s = """
-----------------
1/1/2022
-----------------
$60.0

$40.0

$165.0


-----------------
3/3/2022
-----------------
$60.0
"""
x = input("enter date in format xx/xx/xxxx")
s = s.partition(f"{x}")[2]  # separate  the list of price at that day
s = s.replace(f'{"-"*17}', "", 1)  # remove the -- after date
try:
    s = s[:s.index("-")]  # get only prices of that day if not the last day
except ValueError as e:
    pass
sales = [str(i+"$") for i in re.findall(r'\d+.\d+', s)]  # return  the vales as list in $
print(sales)
