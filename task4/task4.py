import sys
def min_moves_to_equal_elements(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves
def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as file:
            nums = [int(line.strip()) for line in file if line.strip()] 
        if not nums:
            sys.exit(1)
        moves = min_moves_to_equal_elements(nums)
        print(moves)
    except FileNotFoundError:
        sys.exit(1)
    except ValueError:
        sys.exit(1)
if __name__ == "__main__":
    main()
