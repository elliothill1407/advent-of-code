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
        
        # read lines from the file
        with open("input.txt", 'r') as file:
            lines = file.readlines()

        total_sum = 0

        for line in lines:
            line = line.strip()
            first_digit = None
            last_digit = None
            i = 0

            while i < len(line):
                if line[i].isnumeric():
                    if first_digit is None:
                        first_digit = line[i]
                    else:
                        last_digit = line[i]
                else:
                    for word, digit in digits.items():
                        # check if the current substring matches a word or digit
                        if line[i:i+len(word)] == word:
                            if first_digit is None:
                                first_digit = digit
                            last_digit = digit
                            i += len(word) - 1  # move index forward by the length of the word - 1
                            break
                i += 1

            if first_digit is not None and last_digit is not None:
                # form the two-digit number and add to total sum
                calibration_value = int(f"{first_digit}{last_digit}")
                total_sum += calibration_value

        print(f"Sum: {total_sum}")
        return total_sum

solution = Solution()
sum2 = solution.calibrationValuePartTwo()
print("Sum2 = {}".format(sum2))