#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector <int> minimi(9);
void sum100();

int main() {
	for (int i = 0; i < 9; i++)
		cin >> minimi[i];
	
	sum100();	// �ϰ������� Ű�� ���� 100�� �Ǵ� ����
	sort(minimi.begin(), minimi.end());  // ��������

	for (int i = 2; i < 9; i++)  // index 0,1�� ������ -> ������
		cout << minimi[i] << "\n";
}


void sum100() {
	int sum9= 0; // sum��ȩ������ Ű ��
	for (int i = 0; i < 9; i++)
		sum9 += minimi[i];

	for(int i=0; i<8; i++)
		for (int j = i + 1; j < 9; j++) {
			if (sum9 - (minimi[i] + minimi[j]) == 100) {
				minimi[i] = 0;
				minimi[j] = 0;
				return;
			}
		}
}