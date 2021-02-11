import collections

if __name__ == '__main__':
    s = input()
    # y = collections.Counter(sorted(s))
    # print(y)
    # x = collections.Counter(sorted(s)).most_common(3)
    # print(x)
    [print(*c) for c in collections.Counter(sorted(s)).most_common(3)]