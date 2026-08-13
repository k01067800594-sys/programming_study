public class ps {
    public static void main(String[] args) {
                // 1. 비밀번호를 저장할 문자열 배열 선언
                String[] passwords = {"pass2026", "java", "Admin123"};

                // 9. 길이 조건을 통과한 비밀번호 개수를 카운트할 변수 선언
                int validCount = 0;

                // 2. 향상된 for문(Enhanced For Loop)을 사용하여 배열의 비밀번호를 하나씩 처리
                for (String password : passwords) {
                    // 3. 비밀번호 출력
                    System.out.println("비밀번호: " + password);

                    // 4. length() 메서드로 비밀번호 길이 구하기
                    int length = password.length();
                    System.out.println("비밀번호 길이: " + length);

                    // 5. 비밀번호 길이가 6자 이상인지 조건 검사
                    if (length >= 6) {
                        System.out.println("길이 조건 통과");
                        validCount++; // 통과한 개수 1 증가
                    } else {
                        System.out.println("길이 조건 미통과");
                    }

                    // 6. toUpperCase() 메서드로 대문자 변환 후 출력
                    System.out.println("대문자 변환: " + password.toUpperCase());

                    // 7. toLowerCase() 메서드로 소문자 변환 후 출력
                    System.out.println("소문자 변환: " + password.toLowerCase());

                    // 8. charAt(0)을 사용하여 첫 번째 문자 출력
                    System.out.println("첫 번째 문자: " + password.charAt(0));

                    // 출력 형식 맞춤을 위한 줄바꿈
                    System.out.println();
                }

                // 9. 최종적으로 길이 조건을 통과한 비밀번호 개수 출력
                System.out.println("길이 조건을 통과한 비밀번호 수: " + validCount);
            }
        }
