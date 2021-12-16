import re
def searchRegex(string):
   try:
      match = re.findall('[a-z]+_[a-z]+', string)
      return match
   except:
      return ''


def decor(func):
    def capsule(*args):
        for item in args:
            if (searchRegex(item) == []):
                raise Exception("element does not have the proper format")

        func(*args)
    return capsule

@decor
def myFunc(*args):
    print("parameters are ok!")
    return

myFunc("a_b", "cC_d")