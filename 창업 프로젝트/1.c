#include <stdio.h>
#include <string.h>

void recommend_exercise(char *goal, char *part) {
    if (strcmp(goal, "체중 감량") == 0) {
        if (strcmp(part, "전체") == 0) {
            printf("추천 운동: 유산소 운동 (조깅, 자전거 타기)\n");
        } else if (strcmp(part, "복근") == 0) {
            printf("추천 운동: 플랭크, 크런치\n");
        } else if (strcmp(part, "다리") == 0) {
            printf("추천 운동: 스쿼트, 런지\n");
        }
    } else if (strcmp(goal, "근력 강화") == 0) {
        if (strcmp(part, "팔") == 0) {
            printf("추천 운동: 바벨 컬, 푸쉬업\n");
        } else if (strcmp(part, "가슴") == 0) {
            printf("추천 운동: 벤치 프레스, 덤벨 플라이\n");
        } else if (strcmp(part, "다리") == 0) {
            printf("추천 운동: 레그 프레스, 데드리프트\n");
        }
    } else {
        printf("알 수 없는 목표입니다.\n");
    }
}

int main() {
    char goal[50];
    char part[50];

    printf("운동 목표를 입력하세요 (체중 감량, 근력 강화 등): ");
    scanf("%s", goal);
    
    printf("운동 부위를 입력하세요 (팔, 다리, 복근, 전체 등): ");
    scanf("%s", part);

    recommend_exercise(goal, part);

    return 0;
}
