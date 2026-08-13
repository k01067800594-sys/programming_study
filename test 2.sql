-- 1.속성명과 데이터 
alter table 주문 rename column 배송도시 to 배송도시코드;
alter table 주문 modify 배송도시코드 varchar(256);

-- 2. 인덱스 생성과 삭제
create index idx_order_data on 주문(주문일);
alter table 주문 drop index idx_order_data;

create view vw_order as
select 고객번호,
	count(*) as 주문건수,
    sum(주문가격) as 총주문금액
from 주문
group by 고객번호;
select * from vw_order;

-- 4.
select 고객번호, 주문건수, 총주문금액
from vw_order
where 총주문금액 >=50000;