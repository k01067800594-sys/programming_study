package ex01;
//제너릭(Generic): 자료형을 미리 딱 정하지 않고, 사용할 때 정하게 해 주는 문법
//                       하나의 클래스를 여러 자료형에 재사용할 수 있게 해 주는 문법
//                       보통 <> 기호를 사용

class Box<T> {
    private T data;

    // 값 저장 메서드
    public void setData(T data) {
        this.data = data;
    }

    // 값 반환 메서드
    public T getData() {
        return data;
    }
}

public class GenericMain {//클래스
    public static void main(String[] args) {// 메인메서드(시작)
        // 문자열
        Box<String> nameBox = new Box<>();
        nameBox.setData("홍길동");

        //정수
        Box<Integer> scoreBox = new Box<>();
        scoreBox.setData(90);

        //실수
        Box<Double> doubleBox = new Box<>();
        doubleBox.setData(150.5);

        //참 거짓 (불리언)
        Box<Boolean> passBox = new Box<>();
        passBox.setData(true);

        printBox(nameBox);
        printBox(scoreBox);
        printBox(doubleBox);
        printBox(passBox);
    }//메인메서드 끝

    //보조메서드는 메인메서드안에 넣으면 안됨(메서드안에 메서드 안됨)
    public static <T> void printBox(Box<T> box) // 보조메서드(실행함)
    {
        System.out.println(box.getData());
    }
} //클래스 끝

//<래퍼클래스>
//래퍼 클래스는 int, double, boolean 같은 기본형 값을 객체처럼
// 사용할 수 있게 감싸 주는 클래스
//ArrayList 같은 컬렉션에는 기본형 자료형을 직접 넣을 수 없기 때문이다
//ArrayList는 객체를 담는 상자
// 래퍼 클래스는 메서드를 사용할 수 있다

//기본형       래퍼 클래스
//byte           Byte
//short          Short
//int            Integer
//long           Long
//float           Float
//double          Double
//char           Character
//boolean         Boolean
