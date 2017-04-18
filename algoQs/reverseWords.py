"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

"""

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    results = []
    words = s.split(" ")
    for word in words:
        out = word[::-1]
        results.append(out)
    res = ' '.join(results)
    return res

string = "Let's take LeetCode contest"

print reverseWords(string)