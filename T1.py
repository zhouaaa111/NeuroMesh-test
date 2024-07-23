def min_sub(source, target):
    source_len, target_len = len(source), len(target)
    i, j = 0, 0
    count = 0

    while j < target_len:
        count += 1
        i = 0
        start_target_index = j

        while i < source_len and j < target_len:
            if source[i] == target[j]:
                j += 1
            i += 1

        if start_target_index == j:
            return -1

    return count


if __name__ == "__main__":
    source = input("source: ")
    target = input("target: ")
    result = min_sub(source, target)
    print(f"output: {result}")
