import java.sql.*;
import java.sql.DriverManager;
import java.util.Scanner;

public class Login {
    public static void main(String[] args) {
        String url="jdbc:mysql://localhost:3306/movie_db";
        // MySQL 사용자 계정
        String user = "root";
        // MySQL 비밀번호
        String password ="sql12345";
        Scanner scanner = new Scanner(System.in);
        try{
            Connection conn = DriverManager.getConnection(url, user, password);
            System.out.println("[영화관 회원 로그인]");
            System.out.println("아이디:");
            String inputId =scanner.nextLine();
            System.out.println("비밀번호:");
            String inputPass=scanner.nextLine();

            String sql =
                    "SELECT m_id, user_id, m_name, m_role " +
                            "FROM member " +
                            "WHERE user_id = ? AND user_password = ?";

            System.out.println("\n 실행할 sql문");
            System.out.println(sql);

            // 문장을 sql에 전달
            PreparedStatement pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, inputId);
            pstmt.setString(2, inputPass);

            // sql문장을 실행->결과 받기
            ResultSet rs = pstmt.executeQuery();
            if(rs.next())
            {
                //sql 결과 -> 자바 변수
                String memberName = rs.getString("m_name");
                String memberRole = rs.getString("m_role");

                System.out.println("\n 로그인 성공");
                System.out.println(memberName + "님 환영합니다");
                System.out.println("회원권한:"+memberRole);
            } else{
                System.out.println("아이디나 비밀번호가 일치하지 않습니다");
            }
            rs.close();
            pstmt.close();
            conn.close();
        }
        catch(Exception e){
            System.out.println("데이터베이스 오류가 발생했습니다");
            System.out.println(e.getMessage());
        }
        finally{
            scanner.close();
        }
    }
}