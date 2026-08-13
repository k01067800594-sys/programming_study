// 부모 클래스(Employee)
// 모든 직원이 공통적으로 가지는 정보와 기능을 작성
class Employee {

    // 직원 이름
    String name;

    // 기본급
    int basePay;

    // 생성자
    Employee(String name, int basePay) {
        this.name = name;
        this.basePay = basePay;
    }

    // 일반 직원의 급여는 기본급
    int getPay() {
        return basePay;
    }

    // 일반 직원 정보 출력
    void printInfo() {
        System.out.println("직원 이름: " + name + ", 급여: " + getPay());
    }
}


// 자식 클래스(ContractEmployee)
// Employee를 상속받음
class ContractEmployee extends Employee {

    // 계약직 수당
    int bonus;

    // 생성자
    ContractEmployee(String name, int basePay, int bonus) {

        // 부모 생성자 호출
        super(name, basePay);

        // 수당 초기화
        this.bonus = bonus;
    }

    // 계약직 급여 계산(기본급 + 수당)
    @Override
    int getPay() {
        return basePay + bonus;
    }

    // 계약직 정보 출력
    @Override
    void printInfo() {
        System.out.println("계약 직원 이름: " + name + ", 급여: " + getPay());
    }
}


// 실행 클래스
public class GenericMain {

    public static void main(String[] args) {

        // 부모 타입 배열 생성(다형성)
        Employee[] emp = new Employee[2];

        // 일반 직원 객체 생성
        emp[0] = new Employee("이순신", 3100000);

        // 계약 직원 객체 생성
        emp[1] = new ContractEmployee("홍길동", 2000000, 300000);

        // 전체 급여 합계 저장 변수
        int total = 0;

        // 배열에 저장된 모든 직원 정보 출력
        for (Employee e : emp) {

            // 직원 정보 출력
            e.printInfo();

            // 급여 합계 계산
            total += e.getPay();
        }

        // 전체 급여 합계 출력
        System.out.println("전체 직원 급여 합계: " + total);
    }
}