from collections import Counter

input = "153517-630395"

def main():
    x = input.split("-")
    print(x)
    lower = int(x[0])
    higher = int(x[1])
    pwlist = []

    counter = lower
    while counter < higher:
        destest = descent(str(counter))
        if destest:
            adjtesting = adjacent(str(counter))
            if adjtesting:
                pwlist.append(str(counter))
                counter = counter + 1
            else:
              counter = counter + 1
        else:
            counter = counter + 1

    print(len(pwlist))
    print(groups(pwlist))


def descent(des):
  bool = False
  initInt = 0

  for str in des:
    if int(str) >= initInt:
      bool = True
      initInt = int(str)
    else:
      return False
  return bool

def adjacent(adj):
  bool = False
  initInt =  "10"

  for str in adj:
    if int(str) == int(initInt):
      return True
    else:
      initInt = str

  return bool

def groups(grp):
  return sum(1 for x in grp if 2 in Counter(x).values())

if __name__== "__main__":
  main()