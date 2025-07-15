import sys
def circular_path(n, m):
    path = []
    current = 1
    while True:
        path.append(str(current))
        next_pos = (current + m - 1) % n or n
        if next_pos == 1:
            break
        current = next_pos
    return ''.join(path)
if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    print(circular_path(n, m))
