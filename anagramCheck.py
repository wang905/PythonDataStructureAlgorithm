def anagram_solution(s1, s2):
    l2 = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2<len(l2) and not found:
            if s1[pos1] == l2[pos2]:
                found = True
            else:
                pos2 += 1
        
        if found:
            l2[pos2] = None
        else:
            still_ok = False
        
        pos1 += pos1

    return still_ok

print(anagram_solution('abcd', 'dcbadd'))
