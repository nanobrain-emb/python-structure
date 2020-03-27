
def main(args):
  print("Hello World, NanoBrain!")

  return

if __name__ == '__main__':
  import sys, os
  sys.path.append(os.getcwd() + '/lib/')
  sys.exit(main(sys.argv))