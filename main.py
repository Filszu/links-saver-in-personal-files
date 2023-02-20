

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
spacerLenght = 20
recordVisibleLength = 100
print(f"LINKS","-"*spacerLenght,"DESC")
# print()

def getStringDiffSpacer(str1, str2):

    dif = recordVisibleLength-len(str1)-len(str2)
    

    return dif


for url, desc in records:

    showUrl = url[:30]+"..." if len(url) > 20 else url

    print(f"{showUrl} | {desc}")
    print(getStringDiffSpacer(showUrl,desc))


