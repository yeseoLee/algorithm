#include<stdio.h>
#include<stdlib.h>
#define SWAP(a,b) {int t; t=a; a=b; b=t;}
void bubbleSort(int* ar, int n);
void printArray(int* ar, int n);

int main() {
	int n, i;
	int* ar;
	scanf("%d", &n); //�迭�� ����
	ar = (int*)malloc(sizeof(int) * n); //���̰� n�� �迭 �����Ҵ�
	for (i = 0; i < n; i++) {
		scanf("%d", (ar+i)); 
	}
	bubbleSort(ar, n); //����
	printArray(ar, n); //���
	return 0;
}
void bubbleSort(int* ar, int n) {
	int i,j;
	for (i = 0; i < n - 1; i++) { 
		for (j = 0; j < n - 1 - i; j++) { 
			if (ar[j] >= ar[j+1]) { 
				SWAP(ar[j], ar[j + 1]);
				//������ �� ���� ���ϸ� ū ���� ��� �ڷ� ���� -> �������� ����
			}
		}
	}
}
void printArray(int* ar, int n) {
	int i;
	for (i = 0; i < n; i++) {
		printf("%d\n",ar[i]);
	}
}