class Company {
    String name;

    Company(String name) {
        this.name = name;
    }

    void start() {
        System.out.println(name + "이(가) 출근했습니다.");
    }

    void end() {
        System.out.println(name + "이(가) 퇴근했습니다.");
    }
}

class Devel extends Company {
    Devel(String name) {
        super(name);
    }

    @Override
    void start() {
        super.start();
    }

    void work() {
        System.out.println(name + "님이 프로그램을 개발합니다.");
    }
}

class ab extends Company {
    ab(String name) {
        super(name);
    }

    @Override
    void start() {
        super.start();
    }

    void work() {
        System.out.println(name + "님이 프로그램을 개발합니다.");
    }
}

class abc extends Company {
    abc(String name) {
        super(name);
    }

    @Override
    void start() {
        super.start();
    }

    void work() {
        System.out.println(name + "님이 프로그램을 개발합니다.");
    }
}

public class Abstrect {
    public static void main(String[] args) {

        Devel emp1 = new Devel("이상혁");
        ab emp2 = new ab("류민석");
        abc emp3 = new abc("문현준");

        emp1.start();
        emp1.work();
        emp1.end();

        System.out.println();

        emp2.start();
        emp2.work();
        emp2.end();

        System.out.println();

        emp3.start();
        emp3.work();
        emp3.end();
    }
}