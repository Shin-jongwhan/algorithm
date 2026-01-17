class SamState:
    def __init__(self):
        # 전이(transition): key=문자, value=다음 상태 번호
        self.dicNext = {}
        # suffix link: 가장 가까운 접미 상태로 점프
        self.nLink = -1
        # 이 상태가 대표하는 문자열들 중 가장 긴 문자열 길이
        self.nLen = 0
        # A 문자열 기준으로, 이 상태가 대표하는 문자열 중 "어떤 하나"의 끝 위치(0-based)
        self.nFirstpos = -1
        # A에서 이 상태(=endpos 집합)의 등장 횟수 (오버랩 포함)
        self.nOccur = 0


class SuffixAutomaton:
    def __init__(self):
        self.lsStates = []

        stRoot = SamState()
        stRoot.nLen = 0
        stRoot.nLink = -1
        stRoot.nFirstpos = -1
        stRoot.nOccur = 0
        self.lsStates.append(stRoot)

        self.nLast = 0
        self.bOccur_ready = False

    def extend(self, sCh, nPos):
        nCur = len(self.lsStates)
        stCur = SamState()
        stCur.nLen = self.lsStates[self.nLast].nLen + 1
        stCur.nFirstpos = nPos
        stCur.nOccur = 1
        self.lsStates.append(stCur)

        nP = self.nLast
        while nP != -1 and sCh not in self.lsStates[nP].dicNext:
            self.lsStates[nP].dicNext[sCh] = nCur
            nP = self.lsStates[nP].nLink

        if nP == -1:
            self.lsStates[nCur].nLink = 0
        else:
            nQ = self.lsStates[nP].dicNext[sCh]
            if self.lsStates[nP].nLen + 1 == self.lsStates[nQ].nLen:
                self.lsStates[nCur].nLink = nQ
            else:
                nClone = len(self.lsStates)
                stClone = SamState()
                stClone.dicNext = dict(self.lsStates[nQ].dicNext)
                stClone.nLen = self.lsStates[nP].nLen + 1
                stClone.nLink = self.lsStates[nQ].nLink
                stClone.nFirstpos = self.lsStates[nQ].nFirstpos
                stClone.nOccur = 0
                self.lsStates.append(stClone)

                while nP != -1 and self.lsStates[nP].dicNext.get(sCh) == nQ:
                    self.lsStates[nP].dicNext[sCh] = nClone
                    nP = self.lsStates[nP].nLink

                self.lsStates[nQ].nLink = nClone
                self.lsStates[nCur].nLink = nClone

        self.nLast = nCur
        self.bOccur_ready = False

    def build(self, sText):
        for nPos in range(0, len(sText)):
            self.extend(sText[nPos], nPos)
        self._prepare_occurrence()

    def _prepare_occurrence(self):
        # suffix link 방향으로 등장 횟수 전파: len 큰 상태 -> 작은 상태
        lsOrder = list(range(0, len(self.lsStates)))
        lsOrder.sort(key=lambda nIdx: self.lsStates[nIdx].nLen, reverse=True)

        for nV in lsOrder:
            nLink = self.lsStates[nV].nLink
            if nLink != -1:
                self.lsStates[nLink].nOccur += self.lsStates[nV].nOccur

        self.bOccur_ready = True

    def _kmp_build_lps(self, sPattern):
        lsLps = [0] * len(sPattern)
        nLen = 0
        nI = 1

        while nI < len(sPattern):
            if sPattern[nI] == sPattern[nLen]:
                nLen += 1
                lsLps[nI] = nLen
                nI += 1
            else:
                if nLen != 0:
                    nLen = lsLps[nLen - 1]
                else:
                    lsLps[nI] = 0
                    nI += 1

        return lsLps

    def _kmp_count_overlaps(self, sText, sPattern):
        if len(sPattern) == 0:
            return 0

        lsLps = self._kmp_build_lps(sPattern)
        nCount = 0

        nI = 0
        nJ = 0

        while nI < len(sText):
            if sText[nI] == sPattern[nJ]:
                nI += 1
                nJ += 1

                if nJ == len(sPattern):
                    nCount += 1
                    nJ = lsLps[nJ - 1]
            else:
                if nJ != 0:
                    nJ = lsLps[nJ - 1]
                else:
                    nI += 1

        return nCount

    def contains_substring(self, sPattern, blFind_idx=False):
        # 부분문자열 존재 여부: 시작 상태에서 전이를 따라가며 검사
        # blFind_idx=True면, A 문자열에서의 (start, end) idx도 같이 반환
        nV = 0
        for sCh in sPattern:
            if sCh not in self.lsStates[nV].dicNext:
                if blFind_idx:
                    return False, (-1, -1)
                return False
            nV = self.lsStates[nV].dicNext[sCh]

        if not blFind_idx:
            return True

        nEnd_a = self.lsStates[nV].nFirstpos
        nStart_a = nEnd_a - len(sPattern) + 1
        return True, (nStart_a, nEnd_a)

    def find_lcs(self, sOther, blFind_idx=False):
        # sOther(B)를 SAM(A) 위에서 주행하며 최장 공통 "부분문자열" 찾기
        # blFind_idx=False면: (sLcs, nLen, dicCount)
        # blFind_idx=True면 : (sLcs, nLen, dicIdx, dicCount)

        if not self.bOccur_ready:
            self._prepare_occurrence()

        nV = 0
        nCur_len = 0

        nBest_len = 0
        nBest_end_b = -1
        nBest_state = 0

        for nI in range(0, len(sOther)):
            sCh = sOther[nI]

            if sCh in self.lsStates[nV].dicNext:
                nV = self.lsStates[nV].dicNext[sCh]
                nCur_len += 1
            else:
                while nV != -1 and sCh not in self.lsStates[nV].dicNext:
                    nV = self.lsStates[nV].nLink

                if nV == -1:
                    nV = 0
                    nCur_len = 0
                else:
                    nCur_len = self.lsStates[nV].nLen + 1
                    nV = self.lsStates[nV].dicNext[sCh]

            if nCur_len > nBest_len:
                nBest_len = nCur_len
                nBest_end_b = nI
                nBest_state = nV

        if nBest_len == 0:
            dicCount = {'A': 0, 'B': 0}
            if blFind_idx:
                dicIdx = {'A': (-1, -1), 'B': (-1, -1)}
                return "", 0, dicIdx, dicCount
            return "", 0, dicCount

        nStart_b = nBest_end_b - nBest_len + 1
        nEnd_b = nBest_end_b
        sLcs = sOther[nStart_b:nEnd_b + 1]

        # A에서 등장 횟수 (SAM endpos-count)
        nCount_a = self.lsStates[nBest_state].nOccur
        # B에서 등장 횟수 (KMP로 오버랩 포함 카운트)
        nCount_b = self._kmp_count_overlaps(sOther, sLcs)

        dicCount = {'A': nCount_a, 'B': nCount_b}

        if not blFind_idx:
            return sLcs, nBest_len, dicCount

        # idx가 필요할 때만 계산
        nEnd_a = self.lsStates[nBest_state].nFirstpos
        nStart_a = nEnd_a - nBest_len + 1

        dicIdx = {
            'A': (nStart_a, nEnd_a),
            'B': (nStart_b, nEnd_b),
        }

        return sLcs, nBest_len, dicIdx, dicCount


# 사용 예시
sA = "ababa"
sB = "bababx"

sam = SuffixAutomaton()
sam.build(sA)

# 1) 포함 여부만
print(sam.contains_substring("bab"))

# 2) 포함 여부 + A에서 idx
print(sam.contains_substring("bab", blFind_idx=True))

# 3) LCS + 길이 + count만
print(sam.find_lcs(sB))

# 4) LCS + 길이 + idx(A/B) + count(A/B)
print(sam.find_lcs(sB, blFind_idx=True))