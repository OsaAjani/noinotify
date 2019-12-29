# noinotify
```usage: noinotify.py [-h] [--dir DIR] [--on ON] [--command COMMAND]

optional arguments:
  -h, --help         show this help message and exit
  --dir DIR          Directory to watch
  --on ON            Events type to react on, seperated by comma, no spaces.
                     Types : ALL,CREATE,DELETE
  --command COMMAND  Command to run on event type detection. Use flags ::file
                     and ::change to get filepath and change type event.
```
