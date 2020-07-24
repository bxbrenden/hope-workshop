# Hope 2020 Workshop Registration Checker

## Success Story
HOPE 2020 is the first online-only edition of the Hackers on Planet Earth convention.
I wanted to make sure I woke up in time to register for their hands-on workshops.
Registration was set to begin at 6AM Pacific on July 24th, 2020.
So, a couple of days earlier I wrote this Python + Selenium WebDriver script to check the registration status for workshops.

The script worked and notified me when registration opened. **However**, registration was broken for most users when it initially opened.
People were reporting in the official Matrix chat that their event ticket codes, which were supposed to be their ticket to register, were not working.
Everyone was getting an `Invalid Registration` error.
All of a sudden, the moderators shut down registration again so they could debug their code.

At this point I had signed up for zero workshops and was bummed.
I started up my listener program again since it was now proven to work, and after the mods finished their troubleshooting an hour or two later, I was able to sign up for 6 classes!
I **for sure** would have missed out if I hadn't automated this.

## Requirements
- a Twilio account with credit and a phone number
- a Unix environment (Linux, OSX)
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) must be in your $PATH

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
