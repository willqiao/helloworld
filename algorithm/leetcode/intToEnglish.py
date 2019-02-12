class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        stack = []
        result = ""
        
        value = str(num)
        r = len(value) % 3
        if r != 0:
            stack.append(value[:r])
        index = r
        while index+3 <= len(value):
            stack.append(value[index:index+3])
            index=index+3
        
        
        print(stack)
        
        result = self.digitstoWords(stack.pop())
        if len(stack) > 0:
            temp = self.digitstoWords(stack.pop())
            if temp != "":
                result = temp + " Thousand " + result
        
        if len(stack) > 0:
            temp = self.digitstoWords(stack.pop())
            if temp != "":
                result = temp + " Million " + result
        
        if len(stack) > 0:
            temp = self.digitstoWords(stack.pop())
            if temp != "":
                result = temp + " Billion " + result
        
        result = result.replace("  ", " ")
        
        while result[len(result)-1] == " ":
            result = result[:len(result)-1]
            
        return result
            
    
    def digitstoWords(self, mystr):
        myresult = ""
        while len(mystr) > 0 and mystr[0] == "0":
            mystr = mystr[1:]
        
        if len(mystr) == 3:
            return self.digitstoWords(mystr[0]) + " Hundred " + self.digitstoWords(mystr[1:])
        
        if len(mystr) == 2:
            if int(mystr) < 20:
                if mystr == "10":
                    return "Ten"
                if mystr == "11":
                    return "Eleven"
                if mystr == "12":
                    return "Twelve"
                if mystr == "13":
                    return "Thirteen"
                if mystr == "14":
                    return "Fourteen"
                if mystr == "15":
                    return "Fifteen"
                if mystr == "16":
                    return "Sixteen"
                if mystr == "17":
                    return "Seventeen"
                if mystr == "18":
                    return "Eighteen"
                if mystr == "19":
                    return "Nineteen"
            else:
                if mystr[0] == "2":
                    return "Twenty " + self.digitstoWords(mystr[1])
                if mystr[0] == "3":
                    return "Thirty " + self.digitstoWords(mystr[1])
                if mystr[0] == "4":
                    return "Forty " + self.digitstoWords(mystr[1])
                if mystr[0] == "5":
                    return "Fifty " + self.digitstoWords(mystr[1])
                if mystr[0] == "6":
                    return "Sixty " + self.digitstoWords(mystr[1])
                if mystr[0] == "7":
                    return "Seventy " + self.digitstoWords(mystr[1])
                if mystr[0] == "8":
                    return "Eighty " + self.digitstoWords(mystr[1])
                if mystr[0] == "9":
                    return "Ninety " + self.digitstoWords(mystr[1])
                
                
        if len(mystr) == 1:
            if mystr == "1":
                return "One"
            if mystr == "2":
                return "Two"
            if mystr == "3":
                return "Three"
            if mystr == "4":
                return "Four"
            if mystr == "5":
                return "Five"
            if mystr == "6":
                return "Six"
            if mystr == "7":
                return "Seven"
            if mystr == "8":
                return "Eight"
            if mystr == "9":
                return "Nine"
        if len(mystr) == 0:
            myresult = ""
        
        return myresult
        
# print(Solution().digitstoWords("360"))
# print(Solution().numberToWords(1230567891))
print(Solution().numberToWords(0))