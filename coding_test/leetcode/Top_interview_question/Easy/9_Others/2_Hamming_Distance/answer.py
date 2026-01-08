class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = bin(x)[2:]
        by = bin(y)[2:]

        if len(bx) > len(by) : 
            by = '{0:0{1}d}'.format(int(by), len(bx))
        else : 
            bx = '{0:0{1}d}'.format(int(bx), len(by))

        hm = 0
        for i in range(0, len(bx)) : 
            print(bx[i], by[i])
            if bx[i] != by[i] :
                hm += 1
                
        return hm