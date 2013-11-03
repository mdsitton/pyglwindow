
import argparse

def command_line_args():
    parser = argparse.ArgumentParser(description='Welcome!')

    parser.add_argument('-f', '--fullscreen', type=bool, help='Fullscreen Mode')
    parser.add_argument('-x', '--width', type=int, help='Horizontal resolution')
    parser.add_argument('-y', '--height', type=int, help='Vertical resolution')
    parser.add_argument('-g', '--game', type=str, help='Game import to launch')

    args = vars(parser.parse_args())

    return args

if __name__ == "__main__":
    args = command_line_args()
    
    importSet = False

    # Process the command line arguments and remove any that have not been used
    delItems = []
    for item in args:
        if args[item] is None:
            delItems.append(item)
            
    
    if args['game']:
        if args['game'][:8] == 'src.game':
            importSet = True
        delItems.append('game')
    
    if importSet == True:
        lunchbox = __import__(args['game'], fromlist=[args['game']])
        Main = getattr(lunchbox, 'Main')
    else:
        from src.game.main import Main

    # You cant delete an item when iterating on it so we delete it afterwards
    for item in delItems:
        del args[item]

    Main(**args)
