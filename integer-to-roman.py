class Solution(object):
    RomanSymbols = (
            ('M', 1000),
            ('D', 500),
            ('C', 100),
            ('L', 50),
            ('X', 10),
            ('V', 5),
            ('I', 1))
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        i = 0
        while num > 0:
            if num >= Solution.RomanSymbols[i][1]:
                if i % 2 == 0:
                    k, num = divmod(num, Solution.RomanSymbols[i][1])
                    if k == 4 and i > 0:
                        result.append(Solution.RomanSymbols[i][0])
                        result.append(Solution.RomanSymbols[i - 1][0])
                    else:
                        result.append(Solution.RomanSymbols[i][0] * k)
                else:
                    if num >= Solution.RomanSymbols[i + 1][1] * 9:
                        num -= Solution.RomanSymbols[i + 1][1] * 9
                        result.append(Solution.RomanSymbols[i + 1][0])
                        result.append(Solution.RomanSymbols[i - 1][0])
                    else:
                        num -= Solution.RomanSymbols[i][1]
                        result.append(Solution.RomanSymbols[i][0])
            i += 1
        return ''.join(result)
    def intToRoman1(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        i = 0
        while num > 0:
            if num >= Solution.RomanSymbols[i][1]:
                if i % 2 == 0:
                    k, num = divmod(num, Solution.RomanSymbols[i][1])
                    if k == 4 and i > 0:
                        result.append(Solution.RomanSymbols[i][0])
                        result.append(Solution.RomanSymbols[i - 1][0])
                    else:
                        result.append(Solution.RomanSymbols[i][0] * k)
                else:
                    num -= Solution.RomanSymbols[i][1]
                    result.append(Solution.RomanSymbols[i][0])
            elif i in (0,2,4) and num >= Solution.RomanSymbols[i + 2][1] * 9:
                num -= Solution.RomanSymbols[i + 2][1] * 9
                result.append(Solution.RomanSymbols[i + 2][0])
                result.append(Solution.RomanSymbols[i][0])
            else:
                i += 1
        return ''.join(result)


testCases = [
        [0, ''],
        [1, 'I'],
        [2, 'II'],
        [3, 'III'],
        [4, 'IV'],
        [5, 'V'],
        [6, 'VI'],
        [7, 'VII'],
        [8, 'VIII'],
        [9, 'IX'],
        [10, 'X'],
        [11, 'XI'],
        [12, 'XII'],
        [13, 'XIII'],
        [14, 'XIV'],
        [15, 'XV'],
        [16, 'XVI'],
        [17, 'XVII'],
        [18, 'XVIII'],
        [19, 'XIX'],
        [20, 'XX'],
        [21, 'XXI'],
        [22, 'XXII'],
        [23, 'XXIII'],
        [24, 'XXIV'],
        [25, 'XXV'],
        [26, 'XXVI'],
        [27, 'XXVII'],
        [28, 'XXVIII'],
        [29, 'XXIX'],
        [30, 'XXX'],
        [31, 'XXXI'],
        [32, 'XXXII'],
        [33, 'XXXIII'],
        [34, 'XXXIV'],
        [35, 'XXXV'],
        [36, 'XXXVI'],
        [37, 'XXXVII'],
        [38, 'XXXVIII'],
        [39, 'XXXIX'],
        [40, 'XL'],
        [41, 'XLI'],
        [42, 'XLII'],
        [43, 'XLIII'],
        [44, 'XLIV'],
        [45, 'XLV'],
        [46, 'XLVI'],
        [47, 'XLVII'],
        [48, 'XLVIII'],
        [49, 'XLIX'],
        [50, 'L'],
        [51, 'LI'],
        [52, 'LII'],
        [53, 'LIII'],
        [54, 'LIV'],
        [55, 'LV'],
        [56, 'LVI'],
        [57, 'LVII'],
        [58, 'LVIII'],
        [59, 'LIX'],
        [60, 'LX'],
        [61, 'LXI'],
        [62, 'LXII'],
        [63, 'LXIII'],
        [64, 'LXIV'],
        [65, 'LXV'],
        [66, 'LXVI'],
        [67, 'LXVII'],
        [68, 'LXVIII'],
        [69, 'LXIX'],
        [70, 'LXX'],
        [71, 'LXXI'],
        [72, 'LXXII'],
        [73, 'LXXIII'],
        [74, 'LXXIV'],
        [75, 'LXXV'],
        [76, 'LXXVI'],
        [77, 'LXXVII'],
        [78, 'LXXVIII'],
        [79, 'LXXIX'],
        [80, 'LXXX'],
        [81, 'LXXXI'],
        [82, 'LXXXII'],
        [83, 'LXXXIII'],
        [84, 'LXXXIV'],
        [85, 'LXXXV'],
        [86, 'LXXXVI'],
        [87, 'LXXXVII'],
        [88, 'LXXXVIII'],
        [89, 'LXXXIX'],
        [90, 'XC'],
        [91, 'XCI'],
        [92, 'XCII'],
        [93, 'XCIII'],
        [94, 'XCIV'],
        [95, 'XCV'],
        [96, 'XCVI'],
        [97, 'XCVII'],
        [98, 'XCVIII'],
        [99, 'XCIX'],
        [100, 'C'],
        [207, 'CCVII'],
        [501, 'DI'],
        [530, 'DXXX'],
        [550, 'DL'],
        [707, 'DCCVII'],
        [890, 'DCCCXC'],
        [900, 'CM'],
        [1066, 'MLXVI'],
        [1500, 'MD'],
        [1800, 'MDCCC'],
        [1954, 'MCMLIV'],
        [1990, 'MCMXC'],
        [2014, 'MMXIV'],
        [3999, 'MMMCMXCIX'],
        [4000, 'MMMM'],
        ]
s = Solution()
for tc in testCases:
    result = s.intToRoman(*tc[:-1])
    passed = result == tc[-1]
    if not passed:
        print(tc, result, passed)

