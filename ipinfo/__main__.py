import argparse
from .ipinfo import *

if __name__ == '__main__':
    desc = "Get information about user's location using IP Address"
    parser = argparse.ArgumentParser(description=desc,formatter_class = argparse.RawTextHelpFormatter)
    parser.add_argument('option',help = options,default = 'a',nargs='?')
    parser.set_defaults(option='a')
    args = parser.parse_args()
    func = functions.get(args.option,get_all)
    print (func())
