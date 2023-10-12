def main():
    list = []
    while True:
        try:
            list.append(input())
        except EOFError:
            break
    list.sort()
    list_dict = list_to_dict(list)
    for i, j in list_dict.items():
        print(f"{j} {i.upper()}")


def list_to_dict(list):
    list_dict = {}
    for item in list:
        if item in list_dict:
            list_dict[item] += 1
        else:
            list_dict[item] = 1
    return list_dict


main()