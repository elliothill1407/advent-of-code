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
        
        def getCleanLines(lines):
            digits = {
                'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
            }

            new_lines = []
            for line in lines:
                new_line = ""
                i = 0
                n = len(line)
                
                while i < n:
                    if line[i].isdigit():
                        new_line += line[i]
                        i += 1
                    else:
                        found = False
                        for key, value in digits.items():
                            key_len = len(key)
                            if line[i:i+key_len] == key:
                                new_line += value
                                i += key_len
                                found = True
                                break
                        
                        if not found:
                            i += 1
                
                if new_line != '':
                    new_lines.append(new_line)
            
            return new_lines
        
        file = open('input.txt', 'r')
        lines = file.readlines()
        
        new_lines = getCleanLines(lines)
        
        count = 0
        sum = 0
        for line in new_lines:
            count += 1

            pair = line[0] + line[-1]
            sum += int(pair)
        
        print("Sum: {}".format(sum))
        return sum

solution = Solution()
# sum1 = solution.calibrationValuePartOne()
sum2 = solution.calibrationValuePartTwo()

# print("Sum1 = {}".format(sum1))
print("Sum2 = {}".format(sum2))