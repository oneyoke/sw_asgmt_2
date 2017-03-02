import sys

def parseCommandLine(argv):
    print 'Inside parser'
    return argv[1] if len(argv) > 1 else ""


if __name__ == "__main__":
    latin = parseCommandLine(sys.argv)
    print(latin)
    print("igpay atinlay")
