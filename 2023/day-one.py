class Solution:
    def calibrationValue(self):
        # Using readlines()
        file = open('input.txt', 'r')
        lines = file.readlines()
        
        count = 0
        sum = 0
        # Strips the newline character
        for line in lines:
            count += 1
            numbers = [ x for x in line if x.isdigit() ]
            pair = (int(numbers[0]) * 10) + int(numbers[-1])
            sum += pair
            # print("Line {}: {} -> {} = {}".format(count, line.strip(), numbers, pair))
            # print(" -> Current sum = {}".format(sum))
        
        print("Sum: {}".format(sum))

solution = Solution()
solution.calibrationValue()
