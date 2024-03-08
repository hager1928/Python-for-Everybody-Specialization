"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)  # .split()
count = dict()
# sp = handle.read().rstrip().split()
for line in handle:
    if line.startswith("From "):
        sp = line.split()
        fh = sp[5]
        hour = fh.split(":")[0]
        count[hour] = count.get(hour, 0) + 1
'''sort = sorted(count.items())
for hour, count in sort:

    print(hour, count)'''
    
print(sorted([(hour,count) for hour ,count in count.items()]))
