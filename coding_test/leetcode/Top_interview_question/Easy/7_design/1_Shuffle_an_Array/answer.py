import time


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

        # Mersenne Twister의 상태 배열 초기화 예시
        self.N = 624  # 상태 배열 크기
        self.F = 0x6C078965  # 상수 f (1812433253)
        current_time_seed = int(time.time())  # 현재 시간을 시드로 변환
        self.MT = self.initialize_mt(current_time_seed)  # 동적 시드 값으로 초기화
        self.index = 0


    def reset(self):
        """
        :rtype: List[int]
        """
        return self.nums


    def shuffle(self):
        """
        :rtype: List[int]
        """
        lsShuffle = self.nums[:]
        for i in range(len(lsShuffle) - 1, 0, -1):
            j = self.extract_number() % (i + 1)
            lsShuffle[i], lsShuffle[j] = lsShuffle[j], lsShuffle[i]

        return lsShuffle


    def initialize_mt(self, seed):
        # 상태 배열 생성
        MT = [0] * self.N
        MT[0] = seed  # 첫 번째 요소는 시드 값으로 설정

        # 나머지 623개의 값 초기화
        for i in range(1, self.N):
            # MT[i]=(f×(MT[i−1]⊕(MT[i−1]>>30))+i)mod2^32
            # ⊕ : 비트 단위 XOR 연산
            # >> 30 : 비트 단위로 30만큼 이동
            MT[i] = (self.F * (MT[i - 1] ^ (MT[i - 1] >> 30)) + i) & 0xffffffff  # 32비트로 제한
        return MT


    # 난수 추출 함수 (비트 변형 과정)
    def extract_number(self):
        if self.index >= self.N:
            self.twist()

        # 상태 배열에서 현재 값 추출
        y = self.MT[self.index]

        # 비트 변형 과정
        y = y ^ (y >> 11)
        y = y ^ ((y << 7) & 0x9D2C5680)
        y = y ^ ((y << 15) & 0xEFC60000)
        y = y ^ (y >> 18)

        self.index = (self.index + 1) % self.N  # 다음 요소로 이동
        return y


    # 상태 갱신 함수 (Twisting)
    def twist(self):
        for i in range(self.N):
            y = (self.MT[i] & 0x80000000) + (self.MT[(i + 1) % self.N] & 0x7fffffff)
            self.MT[i] = self.MT[(i + 397) % self.N] ^ (y >> 1)
            if y % 2 != 0:  # y가 홀수인 경우 상수 XOR
                self.MT[i] = self.MT[i] ^ 0x9908B0DF
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()