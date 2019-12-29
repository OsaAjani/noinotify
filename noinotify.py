#!/usr/bin/python3
import os
import sys
import argparse


def help (message) :
    print(message)
    sys.exit(os.EX_USAGE)


def execute_command (command, change) :
    command = command.replace('::file', change['file'])
    command = command.replace('::change', change['change'])

    os.system(command)


def dir_changes (dirpath = None, prev_files = None, current_files = None) :
    changes = []
    
    if not dirpath or prev_files == None or current_files == None :
        return changes
    
    for file in current_files :
        if file not in prev_files :
            changes.append({'file': os.path.join(dirpath, file), 'change': 'CREATE'});
    
    for file in prev_files :
        if file not in current_files :
            changes.append({'file': os.path.join(dirpath, file), 'change': 'DELETE'});

    return changes


def close () :
    print('Stop watching.')
    sys.exit(os.EX_OK)


def get_args () :
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help = 'Directory to watch', type = str)
    parser.add_argument('--on', help = 'Events type to react on, seperated by comma, no spaces. Types : ALL,CREATE,DELETE', type = str)
    parser.add_argument('--command', help = 'Command to run on event type detection. Use flags ::file and ::change to get filepath and change type event.', type = str)

    args = parser.parse_args(sys.argv[1:])

    if args.dir == None or args.on == None or args.command == None :
        help(parser.format_help());

    return args


def main () :    
    args = get_args()

    directory = os.path.abspath(args.dir)
    command = args.command
    on_events = args.on.split(',')

    if not os.path.exists(directory) :
        print('Error: File {} does not exist.'.format(directory), file=sys.stderr)
        sys.exit(os.EX_OSFILE)

    try:
        prev_files = None
        current_files = None

        while True:
            prev_files = current_files
            current_files = os.listdir(directory)
            
            changes = dir_changes(directory, prev_files, current_files)

            for change in changes :
                if change['change'] in on_events or 'ALL' in on_events :
                    execute_command(command, change)

    except KeyboardInterrupt:
        close()


if __name__ == "__main__":
    main()
