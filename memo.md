### 한줄 PS일기

날짜 | 내용
------------ | ------------- 
1. | ```print("hello world") ```
2. | input 보다 sys.stdin.readline()이 빠르다. input쓰면 종종 시간초과난다.
3. | 만약 여러 줄을 입력받고 싶으면 sys.stdin을 이용하자. ^Z를 입력받으면 종료해주기 때문에 임의의 여러 줄을 입력받아야 하는 문제에서 유용하다.
4. | 소수점 반올림은 음수/양수일 때 따져야한다. 그냥 round() 써도되고.
5. | 오름차순 또는 내림차순 등의 정렬에서 정렬 조건이 여러 개일 경우(비교할 아이템의 요소가 복수 개일 경우), 튜플로 그 순서를 내보내주면 된다.  
 || ex. sorted(e, key = lambda x : (x[0], -x[1])) (-를 붙이면, 현재 정렬차순과 반대로 하게 된다.)
 6. | a=[int(sys.stdin.readline())) for i in range(n)] 한 줄에 한개 씩 n줄을 입력받아 리스트에 저장할 때
 || line = [sys.stdin.readline().split() for i in range(n)] 한줄에 여러개 원소를 n줄 입력받기, \n까지 입력되기 때문에 split()으로 잘라준다.
 || p=list(map(int,sys.stdin.readline().split())) 한줄에 여러개의 원소를 입력받아 정수 리스트로 변환
7. | from collections import Counter -> 문자열에서 문자 개수 셀 때, 배열에서 같은 값 개수 셀 때 유용하다. 사용법을 잘 익혀두자.
8. | list = str.split() : 문자열 -> 리스트 ''.join( list ) : 리스트 -> 문자열
|| print('\n'.join([''.join([str(i) for i in row]) for row in arr]))
9. | .format함수 (문자열 포매팅, 자바스크립트 닮았다)
10. | 그리디 알고리즘: 매 순간에 최적해를 찾는다. 다만 부분합이 전체의 최적해라는 보장은 없다.
 || 그리디 알고리즘 의 예시중 하나인 스케쥴링은 빠른종료시간일 때 반례 없는 최적해를 가진다.
11. | 매번 직접 구현하지말고 최대한 라이브러리를 활용하는 습관을 가지자. 특히 math
12. | 2차원 배열 초기화 array = [[0 for col in range(w)] for row in range(h)] 또는 array = [[0]*w for i in range(h)]
|| 예를 들어 w이 2, h이 3이면 [[0,0],[0,0][0,0]]즉 array[w][h]과 같다.
13. | '''3차원 배열은 [layer][row][colunm] 순이다.'''
14. | '''reversed 함수는 단순히 iterator를 반환하고, 슬라이싱 [::-1]은 객체를 반환한다.'''
