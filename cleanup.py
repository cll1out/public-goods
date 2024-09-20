# VARIABLES
inputFile = "input.css"
outputFile = "output.conf"


# METRICS
linesProcessed = 0
linesRemoved = 0
linesUncommented = 0



# Open our files
print("Opening Files...")
input = open(inputFile,"r")
output = open(outputFile, "w")


# iterate thru to copy lines
print("Processing lines...")
## Handle /* */ comment blocks
inCommentBlock = False
## For each line in input file
for line in input:

    # Metrics
    linesProcessed += 1


    # If we are in a comment block
    if inCommentBlock:
        # If the comment line ends, release flag
        if "*/" in line:
            inCommentBlock = False

        linesRemoved += 1
        continue


    # If the line is an "insertion" command
    if line[0:4] == "//++":
        linesUncommented += 1
        output.writelines(line[4:])
        continue


    # If line is a single line comment
    if line[0:2] == "//":
        linesRemoved += 1
        continue


    # If line is a start of a comment block ...
    if line[0:2] == "/*":

        # ... And not ending in the same line
        if "*/" not in line:
            inCommentBlock = True

        linesRemoved += 1
        continue

    # If we get this far, the line is to be copied over.
    output.writelines(line)


print("Closing files...")
input.close()
output.close()

print("Complete!\n")
print(f"{linesProcessed} lines processed.")
print(f"{linesRemoved} lines removed.")
print(f"{linesUncommented} lines uncommented with '\\\\++'.")