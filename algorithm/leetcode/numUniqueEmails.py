class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        resultset = set()
        for email in emails:
            atIndex = email.index("@")
            newLocal = ""
            for c in email[:atIndex]:
                if c == "+":
                    break
                if c != ".":
                    newLocal = newLocal + c
            
            resultset.add(newLocal + email[atIndex:])
        return len(resultset)


print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))      