def main():
    mediatype = checkMedia(input("File Name: ").strip().casefold())
    print(mediatype)

def checkMedia(str):
    if str.endswith(".jpg") | str.endswith(".jpeg"):
        return "image/jpeg"
    elif str.endswith(".gif"):
        return "image/gif"
    elif str.endswith(".png"):
        return "image/png"
    elif str.endswith(".pdf"):
        return "application/pdf"
    elif str.endswith(".txt"):
        return "text/plain"
    elif str.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()
