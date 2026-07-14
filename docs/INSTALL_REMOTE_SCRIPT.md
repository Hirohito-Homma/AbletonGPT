# Install the AbletonGPT Remote Script

## Where to copy the Remote Script

Copy the Remote Script package directory into your Ableton Live User Library:

- macOS: ~/Music/Ableton/User\ Library/Remote\ Scripts/

The folder to copy is:

- remote_script/AbletonGPT/

## How to enable it in Live

1. Open Ableton Live 12.
2. Open Preferences > Library.
3. Make sure the User Library path is available.
4. Restart Live if the Remote Script does not appear immediately.
5. In Live, open the preferences for the control surface and select "AbletonGPT".

## How to verify it loaded

1. Start Ableton Live.
2. Confirm the Remote Script folder is present in the User Library.
3. Check the Live log or console output for:
   - "AbletonGPT loaded"
4. Optionally connect to localhost:8765 with a JSON message such as:
   - {"command": "play"}

If the Remote Script is imported outside of Ableton, the placeholder classes remain available and no Live modules are required.
