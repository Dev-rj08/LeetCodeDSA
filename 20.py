class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            if "{}" in s:
                s=s.replace("{}","")
            elif "[]" in s:
                s=s.replace("[]","")
            elif "()" in s:
                s=s.replace("()","")
            else:
                if bool(s) == True:
                    return False
                else:
                    return True