

with open("data.txt", "r") as file:

    records = []

    for line in file:
        # Split the line into two parts, separated by a space
        parts = line.strip().split(" ",1)

        # print(f"parts {parts} parts len {len(parts)}")


        if len(parts) == 1:
            link, desc = parts[0], None
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

print(f"LINKS",getStringDiffSpacer("LINKS","LINKS","*"),"LINKS\n")
# print("***",getStringDiffSpacer("***","***"),"***")
# print()


for url, desc in records:

    showUrl = url[:30]+"..." if len(url) > 20 else url

    # print(f"{showUrl}",getStringDiffSpacer(showUrl,desc),desc)
    print(desc,getStringDiffSpacer(showUrl,desc),showUrl)


