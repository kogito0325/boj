#include <iostream>
#include <cstring>
using namespace std;


void CountLoveCharacter(char name[], int love[4]) {
    for (int i = 0; name[i] != 0; i++) {
        if (name[i] == 'L') {
            love[0]++;
            continue;
        }
        if (name[i] == 'O') {
            love[1]++;
            continue;
        }
        if (name[i] == 'V') {
            love[2]++;
            continue;
        }
        if (name[i] == 'E') {
            love[3]++;
            continue;
        }
    }
}

int main(void) {
    char name[21], team[21], answer[21];
    int n;
    int love[4] = {0}; // ���� �̸��� �ִ� 'L','O','V' ,'E' ����
    cin >> name;
    cin >> n;
    CountLoveCharacter(name, love); // 'L','O','V','E' ī��Ʈ ����
    int max = -1;
    while (n--) {
        cin >> team;
        int love2[4] = {0}; // �� �̸��� �ִ� 'L','O','V' ,'E' ����
        CountLoveCharacter(team, love2); // 'L','O','V','E' ī��Ʈ ����
        love2[0] += love[0];  // ���ο� ���̸��� �ִ� 'L'�� �� ���� 
        love2[1] += love[1];  // ���ο� ���̸��� �ִ� 'O'�� �� ���� 
        love2[2] += love[2];  // ���ο� ���̸��� �ִ� 'V'�� �� ���� 
        love2[3] += love[3];  // ���ο� ���̸��� �ִ� 'E'�� �� ���� 
        int percentage = 1; // ��ȯ�̰� ���� ����
        for (int i = 0; i < 3; i++) {
            for (int j = i + 1; j < 4; j++) {
                percentage *= (love2[i] + love2[j]);
            }
        }
        percentage %= 100;
        if (percentage > max) { // Ȯ���� ���� ������ max �� ����
            max = percentage;
            strcpy(answer, team); // answer�� �ش� �� �̸� ����
        } else if (percentage == max) { // Ȯ�� ���� ������ ���� ������ ��
            if (strcmp(answer, team) > 0) {
                strcpy(answer, team); // ���� ������ �տ� ���� ���̸� ����
            }
        }
    }
    cout << answer;

    return 0;
}