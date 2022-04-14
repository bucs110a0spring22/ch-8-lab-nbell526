class StringUtility:
    def __init__(self, string):
        self.stringhold = string

    def __str__(self):
        return self.stringhold

    def vowels(self):
        sWithVowels = "aAeEiIoOuU"
        count = 0
        for eachChar in self.stringhold:
            if eachChar in sWithVowels:
                count += 1
        if count >= 5:
            return "many"
        else:
            return str(count)

    def bothEnds(self):
        if (len(self.stringhold) <= 2):
            return ''
        return self.stringhold[0] + self.stringhold[1] + self.stringhold[
            -2] + self.stringhold[-1]

    def fixStart(self):
        if (len(self.stringhold) <= 1):
            return self.stringhold
        firstchar = self.stringhold[0]
        newstring = self.stringhold[0]
        for i in range(1, len(self.stringhold)):
            if self.stringhold[i] == firstchar:
                newstring = newstring + '*'
            else:
                newstring = newstring + self.stringhold[i]
        return newstring

    def asciiSum(self):
        count = 0
        for eachChar in self.stringhold:
            asciiCharValue = ord(eachChar)
            count += asciiCharValue
        return count

    def cipher(self):
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase = uppercase.lower()
        returnstring = ''
        for char in self.stringhold:
            if char in uppercase:
                indexupper = uppercase.find(char)
                resultingupperindex = indexupper + len(self.stringhold)
                while resultingupperindex >= 26:
                    resultingupperindex -= 26
                returnstring = returnstring + uppercase[resultingupperindex]
            elif char in lowercase:
                indexlower = lowercase.find(char)
                resultinglowerindex = indexlower + len(self.stringhold)
                while resultinglowerindex >= 26:
                    resultinglowerindex -= 26
                returnstring = returnstring + lowercase[resultinglowerindex]
            else:
                returnstring = returnstring + char

        return returnstring
