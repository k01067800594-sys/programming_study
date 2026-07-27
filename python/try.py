# try:
    #  혹시 오류가 있을지도 모르는 수행문
# except:
    # 오류가 발생했을때 실행
# else:
    #  오류가 발생하지 않을때 실행
# finally:
    # 오류 여부 관계없이 항상 수행
try :
    num= int(input("숫자를 입력하세요"))
    res=100/num
except ValueError:
    print("오류!!숫자를 입력하세요")
except ZeroDivisionError:
    print("0으로 나눌수 없음")
except Exception  as e:
    print("오류메시지",e)    
else:
    print("결과는:", res)
finally:
    print("프로그램 종료")
