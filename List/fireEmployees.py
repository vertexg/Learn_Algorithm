def fireEmployees(employees,unemployed):
    hashmap = set(unemployed)
    results = []
    # 連想配列にない要素を追加
    for i in employees:
        if i not in hashmap:
             results.append(i)

    return results
