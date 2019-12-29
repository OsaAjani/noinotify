#!/usr/bin/python3
import os
import sys

def help () :
    print("Usage : {} <path/to/directory>".format(sys.argv[0]))
    sys.exit(os.EX_USAGE)


def dir_changes (prev_files = None, current_files = None) :
    changes = []
    
    if prev_files == None or current_files == None :
        return changes
    
    for file in current_files :
        if file not in prev_files :
            changes.append({'file': file, 'change': 'CREATE'});
    
    for file in prev_files :
        if file not in current_files :
            changes.append({'file': file, 'change': 'DELETE'});

    return changes


def close () :
    print('Stop watching.')
    sys.exit(os.EX_OK)


def main (args) :

    if len(args) < 2 :
        help()

    directory = args[1]

    if not os.path.exists(directory) :
        print('Error: File {} does not exist.'.format(directory), file=sys.stderr)
        sys.exit(os.EX_NOTFOUND)

    try:
        prev_files = None
        current_files = None

        while True:
            prev_files = current_files
            current_files = os.listdir(directory)

            changes = dir_changes(prev_files, current_files)

            for change in changes :
                print('Change in file : {} [{}]'.format(change['file'], change['change']))

    except KeyboardInterrupt:
        close()

if __name__ == "__main__":
    main(sys.argv)
