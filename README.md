# Hope 2020 Workshop Registration Checker

## Requirements
- a Twilio account with credit and a phone number
- a Unix environment (Linux, OSX)

## Setup
set the following environment variables:
- `TWILIO_SRC_NUM` - your source phone number (Twilio phone number)
- `TWILIO_DST_NUM` - the number you want to be notified at
- `TWILIO_TOKEN` - your API token for Twilio
- `TWILIO_SID` - your Twilio account SID

By default the program checks every 2 minutes.

## Usage
By default this code is listening for the OSINT class registration (since that's the one I wanted to attend).
If you want to check for a different class, you'll need to change the URL.

The default polling interval is 120 seconds.
For a more aggressive polling interval, change the `120` value in the `main()` function towards the bottom of `hope.py`

```bash
python3 hope.py
```
