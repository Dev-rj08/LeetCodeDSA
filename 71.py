# 71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        l1 = path.split("/")
        l2 = []
        
        for i in l1:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if len(l2) > 0:
                    l2.pop()
            else:
                l2.append(i)
        
        str1 = "/" + "/".join(l2)
        return str1
