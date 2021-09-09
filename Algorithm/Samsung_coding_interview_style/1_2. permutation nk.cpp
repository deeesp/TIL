// nPr ����
// n > r 


#include <iostream>

using namespace std;

int arr[] = { 1,2,3,4 };

void swap(int *a, int *b);
void print_arr();
void permutation(int n, int r, int depth);

int main() {
	int r;
	cout << "r�� �Է����ּ���: ";
	cin >> r;
	permutation(sizeof(arr) / sizeof(int), r, 0);
	return 0;
}


void swap(int *a, int *b) {
	int tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}
void print_arr(int size) {
	for (int i = 0; i < size; i++)
		cout << arr[i];
	cout << "\n";
}

void permutation(int n, int r, int depth) {
	// r�� depth�� ũ�Ⱑ �������� ����ϰ� ��ȯ
	// �迭 index�� 0���� depth-1����(r-1����)
	// �� r����ŭ �տ��� ������ �����Ǿ��⿡ ��ȯ
	if (r == depth) {
		print_arr(depth);
		return;
	}

	for (int i = depth; i < n ; i++) {
		swap(&arr[i], &arr[depth]);
		permutation(n, r, depth+1);
		// �ٽ� swap������� �������� ��� ������ �� arr�� ��ȭ ����
		swap(&arr[i], &arr[depth]); 
	}
}