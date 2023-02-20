#  python main.py filszu.links 
import getFromFile
import browserTools
file = "data.txt"
external = getFromFile.readData()
if external:
    file = external 


with open(file, "r") as file:

    records = []

    for line in file:
        # Split the line into two parts, separated by a space
        parts = line.strip().split(" ",1)

        # print(f"parts {parts} parts len {len(parts)}")


        if len(parts) == 1:
            link, desc = parts[0], ""
            # Otherwise, set the link and description
        else:
            link, desc = parts

        # Create a tuple and append it to the list
        records.append((link, desc))

# Print the list of tuples
# print(records)

recordVisibleLength = 80

def getStringDiffSpacer(str1, str2, spacer="-"):

    dif = recordVisibleLength-len(str1)-len(str2)
    
    # print(dif)

    return spacer*dif

print(f"LINKS",getStringDiffSpacer("LINKS","DESCRIPTION","*"),"DESCRIPTION\n")
# print("***",getStringDiffSpacer("***","***"),"***")
# print()


for url, desc in records:

    showUrl = url[:30]+"..." if len(url) > 20 else url

    print(f"{showUrl}",getStringDiffSpacer(showUrl,desc),desc)
    # print(desc,getStringDiffSpacer(showUrl,desc),showUrl)


re = input("open all links in browser? (y/n)")

if re.lower() == "y":
    for url,d in records:
        print(url)
        browserTools.openUrl(url)
