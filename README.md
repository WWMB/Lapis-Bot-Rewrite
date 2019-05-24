# Lapis Bot Rewrite
* By InValidFire

## Purpose
You won't really have a use for this unless you're on my Discord server, as its prime function is to aid us over there.

### Current features
* Scheduled Event Announcements (WIP)
  * Send announcements at a specific time (Done)
  * Allow for custom event messages (Done)
  * Command for adding/removing events from Discord (WIP)
  * Command to reload the events.cfg file without a reboot (WIP)

### Planned features
* Server activity tracking
* Allow players to set their own time zone, and others to query it.

### Contributing
If you're feeling kind and you see a bug or issue that you can fix, feel free to make modifications and submit a pull request!

### Focus of this branch
* Obtaining functional saving and loading of the data files for the bot while using discord.py's task system, all the while fixing and improving old code.
* The file setup.py may be changed with this branch, as saveload.py and setup.py are closely related.
* Once these are achieved, it will be merged back into the master branch.
