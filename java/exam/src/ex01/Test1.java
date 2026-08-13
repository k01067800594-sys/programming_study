public class Test1 {

    public static void main(String[] args) {

        // 비밀번호를 저장한 문자열 배열
        String[] passwords = {"pass2026", "java", "Admin123"};

        // 최종 통과한 비밀번호 개수
        int count = 0;

        // 향상된 for문을 사용하여 배열의 모든 비밀번호 검사
        for (String pw : passwords) {

            // 현재 비밀번호 출력
            System.out.println("비밀번호: " + pw);

            // length()를 사용하여 길이 출력
            System.out.println("비밀번호 길이: " + pw.length());

            // 길이가 5자를 초과하는지 검사
            if (pw.length() > 5) {
                System.out.println("길이 조건 통과");
            } else {
                System.out.println("길이 조건 미통과");
            }

            // contains()를 사용하여 "pass" 포함 여부 검사
            if (pw.contains("pass")) {
                System.out.println("문자열 조건 통과");
            } else {
                System.out.println("문자열 조건 미통과");
            }

            // 대문자로 변환
            System.out.println("대문자 변환: " + pw.toUpperCase());

            // 소문자로 변환
            System.out.println("소문자 변환: " + pw.toLowerCase());

            // 첫 번째 문자 출력
            System.out.println("첫 번째 문자: " + pw.charAt(0));

            // 마지막 문자 출력
            System.out.println("마지막 문자: " + pw.charAt(pw.length() - 1));

            // 숫자가 포함되어 있는지 검사
            boolean hasNumber = false;

            // 문자열을 한 글자씩 검사
            for (int i = 0; i < pw.length(); i++) {

                // Character.isDigit() 사용
                if (Character.isDigit(pw.charAt(i))) {
                    hasNumber = true;
                    break;
                }
            }

            // 숫자 포함 여부 출력
            if (hasNumber) {
                System.out.println("숫자 포함");
            } else {
                System.out.println("숫자 미포함");
            }

            // 최종 통과 조건
            // 길이가 5자 초과이고 숫자가 하나 이상 포함
            if (pw.length() > 5 && hasNumber) {
                count++;
            }

            // 보기 좋게 한 줄 띄우기
            System.out.println();
        }

        // 최종 통과한 비밀번호 개수 출력
        System.out.println("최종 통과 비밀번호 수: " + count);
    }
}