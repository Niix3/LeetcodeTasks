#
# Complete the function/method so that it takes a PascalCase string and
# returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.
def to_underscore(string):
    result = ""
    string = str(string)
    for index,char in enumerate(string):
        if char.istitle() and index !=0 :
            result += "_"
        result += char.lower()
    return result
print(to_underscore('1'))