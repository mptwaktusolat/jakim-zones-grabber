# JAKIM ZONES GRABBER

This is the source of truth for [MPT-Server](https://mpt-server.vercel.app) API service.

## How to use

Go to [E-Solat JAKIM](https://www.e-solat.gov.my/) website, inspect the zones dropdown element and copy the HTML element (`<select id="inputzone" class="form-control shadow">`). Paste in the [data.html](/data.html) file.

Run the [jakim_parser.py](/jakim_parser.py) script. It will generate a new [new.json](/new.json) file.

Using VS Code, select both `old.json` & `new.json` and select **compare selected**. Then, verify the changes manually and save the file.

Commit the changes and push to GitHub.
