import dropbox

APP_KEY = ""
APP_SECRET = ""
ACCESS_TOKEN = ""

dbx = dropbox.Dropbox(ACCESS_TOKEN)

try:
    result = dbx.files_list_folder("")
    if result.entries:
        print("File Listing Test: Successfully listed files:")
        for entry in result.entries:
            print(entry.path_display)
    else:
        print("File Listing Test: No files found.")

except dropbox.exceptions.ApiError as e:
    print("Dropbox API error:", e)

except dropbox.exceptions.DropboxException as e:
    print("Dropbox error:", e)

except Exception as e:
    print("An error occurred:", e)
