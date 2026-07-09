package ex01;

interface Login{
    void login();
    void logout();
}

interface Print{
    void printinfo();
}

class Student implements Login, Print{
    public void login(){
        System.out.println("학생 계정으로 로그인");
    }

    @Override
    public void logout() {
        System.out.println("학생 계정으로 로그아웃");
    }
    @Override
    public void printinfo(){
        System.out.println("학생 정보를 출력합니다");
    }
}

class Teacher implements Login, Print{
    public void login(){
        System.out.println("교사 계정으로 로그인");
    }

    @Override
    public void logout() {
        System.out.println("교사 계정으로 로그아웃");
    }
    @Override
    public void printinfo(){
        System.out.println("교사 정보를 출력합니다");
    }
}


public class interfaceMain {
    public static void main(String[] args) {
        Login s = new Student();
        s.login();
        s.logout();

        Print p = new Student();
        p.printinfo();

        Login t = new Teacher();
        t.login();
        t.logout();

        Print p2 = new Student();
        p2.printinfo();
    }
}
