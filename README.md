# JAKIM ZONES GRABBER

This is the source of truth for the [Waktu Solat API](https://api.waktusolat.app/locations) service.

## How to use

Run the [jakim_parser.py](/jakim_parser.py) script. It will scrape the [E-Solat](https://www.e-solat.gov.my/) website, find the zone dropdown, and store the results in the [locations.json](/locations.json) file.

![image](https://github.com/user-attachments/assets/940db694-5b52-4578-b900-3e4859660046)

Then it will compare the new zones to the existing zones (`locations_current.json`) by their **`jakimCode`**. If changes are detected, it will output to the console. Example:

```
--- ZONE CHANGES DETECTED ---

NEW ZONES ADDED:
  + PHG07 - Pahang (Zon Khas Daerah Rompin, (Mukim Rompin, Mukim Endau, Mukim Pontian))
```

View the diff of `new.json` to confirm the changes.

> [!NOTE]
> Remember to also update the `zones.json` file in [app_waktu_solat_malaysia](https://github.com/mptwaktusolat/app_waktu_solat_malaysia/blob/master/assets/json/zones.json)
