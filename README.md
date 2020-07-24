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

```bash
python3 hope.py
```
