from random import shuffle

inputFile = open("greetings.tsv", "r")
outputFile = open("index.html", "w")

outputFile.write("<html>\n")
outputFile.write("<head>\n<link rel=\"stylesheet\" href=\"style.css\">\n</head>")
outputFile.write("<body>\n<div id=\"wrapper\">");

line = inputFile.readline()
adjectives = []

while True:
    line = inputFile.readline()
    if not line:
        break

    outputFile.write("\t<div class=\"box\">\n")
    line = line.split("\t")

    for i in range(len(line)):
        entry = line[i]    
        
        if i == 0 :
            continue
        if i == 3 :
            adjectives.append(entry)
            continue
        if i == 1 :
            outputFile.write("\t\t<p class=\"name\">\n")
        if i == 2 :
            outputFile.write("\t\t<p class=\"message\">\n")

        outputFile.write("\t\t\t" + entry);
        outputFile.write("\n\t\t</p>\n")

    outputFile.write("\t</div>\n")

outputFile.write("<div class=\"describe\">\n<div class=\"name\">How others described you</div><div class=\"message\">");

dictionary = {}

for line in adjectives:
    line = line.split(",")
    for adjective in line:
        adjective = adjective.replace("\n", "")
        adjective = adjective.replace(" ", "")
        adjective = adjective.lower()
        if adjective in dictionary:
            count = dictionary[adjective] + 1
        else:
            count = 0
            
        dictionary[adjective] = count

toSort = []
for key in dictionary:
    count = dictionary[key] + 1

    toSort.append(str(count) + ": " + key);

toSort.sort(reverse=True)

for adjective in toSort:
    count = int(adjective.split(": ")[0]);
    size = (18 + (count * 5))
    outputFile.write("<div style=\"font-size: " + str(size) + "\">" + adjective + "</div>");
        
outputFile.write("</div></div>");
    
outputFile.write("\n</div>\n</body>\n</html>");

inputFile.close()
outputFile.close()
