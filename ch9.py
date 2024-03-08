"""9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""

name = input("Enter file:")
handle = open(name)
counts = dict()
# find the sender
for line in handle:
    if line.startswith("From "): ######'From ' not 'From' else it will count words like(From: , Fromat,....)
        words = line.split()
        sender = words[1]
        counts[sender] = counts.get(sender, 0) + 1
# max loop
bigcount = None
bigsender = None
for sender, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigsender = sender
print(bigsender, bigcount)

