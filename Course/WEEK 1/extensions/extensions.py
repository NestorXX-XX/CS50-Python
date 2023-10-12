x = str(input("Enter: ")).lower().strip()
gif = "image/gif"
jpg = "image/jpeg"
jpeg = "image/jpeg"
png = "image/png"
pdf = "application/pdf"
txt = "text/plain"
zip = "application/zip"
common = "application/octet-stream"

if ".gif" in x:
    print(gif)
elif ".jpg" in x:
    print(jpg)
elif ".jpeg" in x:
    print(jpeg)
elif ".png" in x:
    print(png)
elif ".pdf" in x:
    print(pdf)
elif ".txt" in x:
    print(txt)
elif ".zip" in x:
    print(zip)
else:
    print(common)