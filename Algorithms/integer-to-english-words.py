class Solution(object):
    NumWords = {
            1 : 'One',
            2 : 'Two',
            3 : 'Three',
            4 : 'Four',
            5 : 'Five',
            6 : 'Six',
            7 : 'Seven',
            8 : 'Eight',
            9 : 'Nine',
            10 : 'Ten',
            11 : 'Eleven',
            12 : 'Twelve',
            13 : 'Thirteen',
            14 : 'Fourteen',
            15 : 'Fifteen',
            16 : 'Sixteen',
            17 : 'Seventeen',
            18 : 'Eighteen',
            19 : 'Nineteen',
            20 : 'Twenty',
            30 : 'Thirty',
            40 : 'Forty',
            50 : 'Fifty',
            60 : 'Sixty',
            70 : 'Seventy',
            80 : 'Eighty',
            90 : 'Ninety'
            }
    Chunks = ('Billion', 'Million', 'Thousand')
    def numberToWords0to999(self, num):
        if num == 0:
            return ''
        if num in Solution.NumWords:
            return Solution.NumWords[num]
        result = []
        hundred, num = divmod(num, 100)
        if hundred > 0 and hundred <= 9 and hundred in Solution.NumWords:
            result.append(Solution.NumWords[hundred])
            result.append('Hundred')
        if num > 0:
            if num in Solution.NumWords:
                result.append(Solution.NumWords[num])
            else:
                decade, num = divmod(num, 10)
                result.append(Solution.NumWords[decade * 10])
                result.append(Solution.NumWords[num])
        return ' '.join(result)
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        result = []
        for i in range(3):
            chunk, num = divmod(num, 1000 ** (3 - i))
            if chunk > 0:
                result.append(self.numberToWords0to999(chunk))
                result.append(Solution.Chunks[i])
        if num > 0:
            result.append(self.numberToWords0to999(num))
        return ' '.join(result)

testCases = [
        [0, 'Zero'],
        [10, 'Ten'],
        [11, 'Eleven'],
        [12, 'Twelve'],
        [13, 'Thirteen'],
        [14, 'Fourteen'],
        [20, 'Twenty'],
        [40, 'Forty'],
        [100, 'One Hundred'],
        [1000, 'One Thousand'],
        [1110, 'One Thousand One Hundred Ten'],
        [1000010, 'One Million Ten'],
        [2100000100, 'Two Billion One Hundred Million One Hundred']
        ]
s = Solution()
for tc in testCases:
    result = s.numberToWords(tc[0])
    if result != tc[1]:
        print(tc[0], result, result == tc[1])

