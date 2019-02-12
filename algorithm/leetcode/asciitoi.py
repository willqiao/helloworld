import nose

class Solution:
    def findFirstSignOrDigit(self, str): 
      for i in range(str.__len__()):
        if (str[i].isdigit() == False and str[i] != " " and str[i] != "+" and str[i] != "-"):
            return -1
        if (str[i] == " "):
            continue
        if (str[i]== "+" or str[i] == "-"):
            if i + 1 < str.__len__():
                if(str[i+1].isdigit()):
                    return i
                else:
                    return -1
            else:
                return -1
        if (str[i].isdigit()):
            return i

        

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        index = self.findFirstSignOrDigit(str)
        print(index)
        if index==-1 or index== None:
            return 0
        value = str[index]
        for i in range(index+1, str.__len__()):
            if (str[i].isdigit()) :
                value += str[i]
            else:
                break
 
        finalValue = int(value)
        maxValue = 2**31 -1
        minValue = -2**31
        if finalValue > 2**31 -1:
            return maxValue
        if finalValue < minValue:
            return minValue
        
        return finalValue

print(" ".isdigit())
print(Solution().myAtoi("  -33f 3"))