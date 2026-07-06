#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//구조체:다른 자료형을 모아둔것
struct student
{
	int number;
	char name[10];
	double grade;
};

int main (void) {

	struct student s; //구조체 변수 선언
	printf ("학번을 입력하시오:");
	scanf ("%d", &s.number); //구조체 멤버의 주소 전달

	printf ("이름을 입력하시오:");
	scanf ("%s", s.name);

	printf ("학점을 입력하시오:");
	scanf ("%lf", &s.grade);

	printf ("학번:%d\n", s.number);
	printf ("이름:%s\n", s.name);
	printf ("학점:%.2f", s.grade);


	return 0; //정상종료
}