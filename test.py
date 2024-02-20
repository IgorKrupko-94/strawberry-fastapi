my_list = [
    {"key1": "value1"},
    {"k1": "v1", "k2": "v2", "k3": "v3"},
    {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}
]


def remove_duplicates(subsequence: list[dict]) -> list[dict]:
    result_list = []
    for elem in subsequence:
        if elem not in result_list:
            result_list.append(elem)
    return result_list


print(remove_duplicates(my_list))
