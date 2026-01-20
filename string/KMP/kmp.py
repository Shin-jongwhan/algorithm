def build_lps(sPattern):
    # LPS(Longest Proper Prefix which is also Suffix) 배열 생성
    # lsLps[i] = sPattern[0:i+1]에서 prefix==suffix가 되는 최대 길이
    nM = len(sPattern)
    lsLps = [0] * nM

    nLen = 0          # 현재까지 일치한 prefix 길이
    nI = 1            # lsLps[0]은 항상 0이므로 1부터 시작

    while nI < nM:
        if sPattern[nI] == sPattern[nLen]:
            nLen += 1
            lsLps[nI] = nLen
            nI += 1
        else:
            if nLen != 0:
                # 이전에 알던 lps로 "패턴만" 당겨서 다시 비교
                nLen = lsLps[nLen - 1]
            else:
                lsLps[nI] = 0
                nI += 1

    return lsLps


def kmp_search(sText, sPattern, lsLps=None):
    # sText에서 sPattern이 등장하는 시작 인덱스들을 리스트로 반환
    # lsLps를 미리 만들어 전달하면 재사용 가능
    if sPattern == "":
        # 빈 패턴은 정의가 애매하지만, 여기서는 "모든 위치"로 처리
        return list(range(0, len(sText) + 1))

    if lsLps is None:
        lsLps = build_lps(sPattern)

    lsFound_idx = []
    nN = len(sText)
    nM = len(sPattern)

    nI = 0  # text index
    nJ = 0  # pattern index

    while nI < nN:
        if sText[nI] == sPattern[nJ]:
            nI += 1
            nJ += 1

            if nJ == nM:
                # 패턴 하나를 끝까지 매칭
                lsFound_idx.append(nI - nM)
                # 다음 가능한 매칭을 위해 패턴 인덱스만 점프
                nJ = lsLps[nJ - 1]
        else:
            if nJ != 0:
                # 텍스트 인덱스는 유지, 패턴 인덱스만 lps로 점프
                nJ = lsLps[nJ - 1]
            else:
                # 패턴의 첫 글자부터도 불일치면 텍스트를 한 칸 진행
                nI += 1

    return lsFound_idx


# 사용 예시
sText = "ababcabcabababd"
sPattern = "ababd"
lsLps = build_lps(sPattern)
lsIdx = kmp_search(sText, sPattern, lsLps)
print(lsLps)
print(lsIdx)