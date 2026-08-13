-- 1.사용자 생성
create user 'user1'@'localhost' identified by 'sql123';

-- 2. 권한 부여와 회수
use test;
GRANT SELECT,INSERT on 주문 to 'user1'@'localhost';
REVOKE INSERT ON 주문 FROM 'user1'@'localhost';
show GRANTS for 'user1'@'localhost';

-- 3. Auto Commit 해제
set autocommit = 0;
-- set autocommit = false;
-- 4. 트랜잭션 시작-> 변경 ->복구지점 설정
START TRANSACTION;
update 주문 set 주문가격 = 20000
where 주문번호='O1001';
select * from 주문;
SAVEPOINT P1;

-- 5. 삭제 이후 p1으로 복구(작업취소)
set sql_safe_updates=0;
delete from 주문 where 주문번호='O1003';
select * from 주문;
rollback to savepoint P1;
select * from 주문;

-- 6. 트렌젝션 죄종확정
commit;

-- 7. 계정 삭제
drop user 'user1'@'localhost';
show grants;