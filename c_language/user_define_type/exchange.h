//헤더파일:공통적으로 참조할 내용 선언
//#pragma once //이 파일을 중복 읽힘 방지
#ifndef EXCHANGE_H //정의되지 않으면
#define EXCHANGE_H //지금부터 EXCHANGE_H 만듦

// 1. 환율 설정 (1달러당 원화 가격)
#define RATE  1450.5 //기호상수 1450.5->RATE

// 2. 함수 선언
double won (double usd); // 달러를 원화로 변환
double doll (double krw); // 원화를 달러로 변환
#endif