import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--left", default= 0.5 , help = "left margin (in.)")
parser.add_argument("--right", default = 0.5, help = "right margin (in.)")
parser.add_argument("--file", default = "DATA1.txt", help = "path to input file")
args = parser.parse_args()

assert float(args.left) > 0, "Left margin value must be positive"
assert float(args.right) > 0, "Right margin value must be positive"
assert (float(args.left) + float(args.right)) * 6 < 72, "Margins exceed max page width"

print('01234567890123456789012345678901234567890123456789012345678901234567890123456789')

leftMargin, rightMargin  = [], []

for i in range(int(float(args.left) * 6)):
    leftMargin.append(" ")

for i in range(int(float(args.right) * 6)):
    rightMargin.append(" ")

leftMargin = "".join(leftMargin)
rightMargin = "".join(rightMargin)

with open(args.file, "r") as inFile, open(args.file[:-4] + ".out", "w") as outFile:
     
    wordList = []
    for line in inFile:
        words = line.split(" ")
        for word in words:
            wordList.append(word)
    
    maxLength = 80 - len(leftMargin) - len(rightMargin)
    currLength = 0
    i = 0
    
    outFile.write(leftMargin)
    while (i < len(wordList)):
      if (wordList[i][-1] == "\n"):
          currLength = 0
          outFile.write(wordList[i] + leftMargin)
      elif (wordList[i][-1] == "."):
        if (currLength + len(wordList[i]) + 2 <= maxLength):
            currLength += len(wordList[i]) + 2
            outFile.write(wordList[i] + "  ")
        else:
            outFile.write(rightMargin + "\n" + leftMargin + wordList[i] + "  ")
            currLength = len(wordList[i]) + 2
      else:
        if (currLength + len(wordList[i]) + 1 <= maxLength):
            currLength += len(wordList[i]) + 1
            outFile.write(wordList[i] + " ")
        else:
            outFile.write(rightMargin + "\n" + leftMargin + wordList[i] + " ")
            currLength = len(wordList[i]) + 1
      i += 1
      
with open(args.file[:-4]+".out", 'r') as outFile: 
          for line in outFile:
              print(line)
        