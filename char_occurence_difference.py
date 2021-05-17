"""
Oh! That’s the difference!
Create a func,on difference which takes a string S and character K. Find the difference between
first occurrence of K and last occurrence of K in string S. Convert the input to lower case before
processing.
Check for following condi,ons :
1. If K not occurred in S, return “K not found in S”.
2. If K occurred only once in S, return “Difference can’t be calculated”.
3. If K occurs more than once, return count of difference.
Sample I/O:
• Input: S= ‘talentpy', K=‘a’ => output: “Difference can’t be calculated”,
• Input: S=“science”, K=‘c’ => output: 3.
"""
def char_occurence_difference(string,char):
    string = string.lower()
    count_occurence = string.count(char)
    if count_occurence == 0 :
        return 'K not found in S'
    elif count_occurence ==1:
        return 'Difference can’t be calculated'
    else:
        #last occurence - first occurence - index offset
        return string.rfind(char) - string.find(char) - 1
        


print(char_occurence_difference("science",'c'))
