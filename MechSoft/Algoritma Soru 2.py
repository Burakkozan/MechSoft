"""
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution"""

      
    #iki kümedeki alt kümeyi bulmak
    
def enuzuniçerik(string1, string2):
    answer = ""
    a=0
    results = 0
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""        
    sub_len = len(answer) 
    for i in range(len(string2)):
        if string2[i:i+sub_len] == answer: 
            results += 1
    return (sub_len*results ,"is the solution")
           
print (enuzuniçerik("acldm1labcdhsnd", "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"))