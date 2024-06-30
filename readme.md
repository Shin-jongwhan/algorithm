### 240630
## 문자열 매칭 알고리즘
### 요즘 문자열 매칭에 대해서 공부를 하고 있다. 문자열 매칭은 같은 걸 찾는 데에 시간복잡도를 최대한 줄이는 방향으로 해야 한다(효율성을 위해).
### 내가 하고 싶은 건 완벽한 문자열 매칭 이외에도 mismatch, gap을 같이 찾는 것이다. 
### <br/><br/><br/>

## brute-force search
### 그냥 무작위로 막 찾는 거다. 예를 들어 비밀번호 자물쇠가 있는데, 0000, 0001 ... 계속 대입해가면서 모든 경우의 수를 찾는 거다.
### <br/><br/><br/>

## KMP 알고리즘
### 접미사, 접두사의 일치하는 개수를 배열로 미리 계산해서 매칭된 문자열에서 접미사 쪽으로 건너 뛰는 방식이다.
### 이 알고리즘은 가장 많이 사용하는 알고리즘 중 하나도 예제도 많이 있다.
### <br/><br/><br/>

## Rabin-Karp 알고리즘
### 문자열에 hash 값을 계산한다. 그리고 참조 문자열에서 해당 hash값이 찾아진 것이 있으면 matching된 것으로 판단한다.
### 이것도 가장 많이 사용하는 알고리즘 중 하나이다.
### <br/><br/><br/>

## suffix / prefix trie
### 별도로 suffix와 prefix에 대한 정보인 trie를 저장해두고 거기서 문자열 매칭을 찾는다.
#### ![image](https://github.com/Shin-jongwhan/string_matchong_algorithm/assets/62974484/9e453a29-a467-455a-b757-6cf195bdeaaf)
### <br/><br/><br/>

## suffix array with BWT (Burrows-Wheeler Transform)
### BWT output과 prefix trie를 이용하여 미리 참조 문자열에 대해 정보를 만들어두고 사용하는 방법이다.
