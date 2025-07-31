import webbrowser as wb

def workouto():
    ChromPath="/usr/bin/google-chrome"
    urls=("instagram.com",
          "youtube.com",
          "google.com")
    for url in urls:
        wb.get(ChromPath).open(url)
workouto()