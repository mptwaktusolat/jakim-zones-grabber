# JAKIM ZONES GRABBER

This is the source of truth for the [Waktu Solat API](https://api.waktusolat.app/locations) service.

## How to use

Run the [jakim_parser.py](/jakim_parser.py) script. It will scrape the E-Solat website, find the zone dropdown, and store the results in the [new.json](/new.json) file.

Then it will compare the new zones to the existing zones (`old.json`) by their **`jakimCode`**. If changes are detected, it will output to the console. Example:

```
--- ZONE CHANGES DETECTED ---

NEW ZONES ADDED:
  + PHG07 - Pahang (Zon Khas Daerah Rompin, (Mukim Rompin, Mukim Endau, Mukim Pontian))
```

Using VS Code, select both `old.json` & `new.json` and choose **Compare Selected**. Then, verify the changes manually and commit the file.

> [!NOTE]
> Remember to also update the `zones.json` file in [app_waktu_solat_malaysia](https://github.com/mptwaktusolat/app_waktu_solat_malaysia/blob/master/assets/json/zones.json)