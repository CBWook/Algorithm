def solution(progresses, speeds):
    answer = []
    front = 0
    while front < len(progresses):
        for i in range(front, len(progresses)):
            progresses[i] += speeds[i]

        if progresses[front] >= 100:
            cnt = 0
            while front < len(progresses) and progresses[front] >= 100:
                front += 1
                cnt += 1
            answer.append(cnt)

    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))