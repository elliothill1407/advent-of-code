class Solution:
    def calibrationValuePartOne(self):
        file = open('input.txt', 'r')
        lines = file.readlines()
        
        count = 0
        sum = 0
        
        for line in lines:
            count += 1
            
            numbers = [ x for x in line if x.isdigit() ]
            pair = numbers[0] + numbers[-1]
            sum += int(pair)
        
        print("Sum: {}".format(sum))
        return sum

    def calibrationValuePartTwo(self):
        
        digits = {
                'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
            }
        
        file = open('input.txt', 'r')
        lines = file.readlines()
        
        count = 0
        sum = 0
        
        for line in lines:
            count += 1
            
            for word, digit in digits.items():
                line = line.replace(word, digit)
            
            numbers = [ x for x in line if x.isdigit() ]
            pair = numbers[0] + numbers[-1]
            sum += int(pair)
        
        print("Sum: {}".format(sum))
        return sum

solution = Solution()
sum2 = solution.calibrationValuePartTwo()
print("Sum2 = {}".format(sum2))