# integif
A quick GIF maker for Slack/Raspberry Pi. This software was originally written for an integrate.ai hackathon.

# Dependencies:
- `slackclient` python library
- `ffmpeg`
- webcam drivers for your system
- API key for your Slack

# Usage:
- Create the appropriate application and bot in your Slack following [this guide](https://get.slack.help/hc/en-us/articles/115005265703-Create-a-bot-for-your-work) 
- Give the bot user the following permissions:
-- Confirm user’s identity
-- Add a bot user with the username @integif.ai
-- Access user’s public channels
-- Access content in user’s private channels
-- Send messages as integif.ai
-- Upload and modify files as user
-- Add link previews to messages
- Invite the bot to your channel or open a private message
- Type in `Video`

There is a delay of about 3 seconds before the webcam starts capturing. The gif will be generated and uploaded in 20 seconds.

The software works best on a Raspberry Pi with a USB webcam. Place it in a fun place at your work to quickly make shareable gifs!

