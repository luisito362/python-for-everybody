7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
        X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average
of those values and produce an output as shown below.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when 
you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
count = 0
big = 0
big = float(big)
fname = input("ENTER FILE NAME :")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        a=float(line[20:26])
        big = big+a
        count = count + 1
print('Average spam confidence:',big/count)
