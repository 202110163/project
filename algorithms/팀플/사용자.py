#이 코드는 사용자로부터 전화번호와 비밀번호를 입력 받아 회원가입과 로그인을 처리하는 gui 에플리케이션
#기능(회원가입) 1. 회원가입 창을 열고, 사용자로부터 전화번호와 비밀번호를 입력받음
#              2. 비밀번호가 일치하는지 확인
#              3. 미이 등록된 전화번호인지 확인, 그렇지 않으면 새로운 사용자 정보를 저장
#   (로그인)   1. 메인 창에서 전화번호와 비밀번호를 입력받아 확인
#              2. 일치한 경우 로그인 성공 메시지를 생성 그렇지 않으면 오류 메시지를 생성 

#tkinter(표준라이브러리), messaebox(팝업창)
import tkinter as tk
from tkinter import messagebox
#사용자의 전화번호와 비밀번호를 저장하기 위한 데이터 장소
users = {}
#회원가입 함수
def register():
    #가입 버튼을 누를 시 호출되는 함수
    def submit_registration():
        phone = phone_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        
        if password != confirm_password:
            messagebox.showerror("오류", "비밀번호를 다시 입력해 주세요.")
            return
        
        if phone in users:
            messagebox.showerror("오류", "이 전화번호는 이미 가입되어 있습니다.")
        else:
            users[phone] = password
            messagebox.showinfo("Success", "회원가입이 완료되었습니다!")
            register_window.destroy()
    #회원가입 창 제작
    register_window = tk.Toplevel(root)
    register_window.title("회원가입")
    #사용자 정보(전화번호)
    tk.Label(register_window, text="전화번호").pack()
    phone_entry = tk.Entry(register_window)
    phone_entry.pack()
    #사용자 정보(비밀번호)
    tk.Label(register_window, text="비밀번호").pack()
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack()
    #사용자 정보(비밀번호 재입력)
    tk.Label(register_window, text="비밀번호 재입력").pack()
    confirm_password_entry = tk.Entry(register_window, show="*")
    confirm_password_entry.pack()
    #가입 버튼 
    tk.Button(register_window, text="가입", command=submit_registration).pack()
#로그인 함수
def login():
    phone = phone_entry.get()
    password = password_entry.get()
    #입력한 정보 참/거짓 판별 
    if phone in users and users[phone] == password:
        messagebox.showinfo("성공", "로그인이 완료되었습니다!")
    else:
        messagebox.showerror("오류", "전화번호()와 비밀번호가 맞지 않습니다.")
#메인 에플리케이션 창 생성
root = tk.Tk()
#메인 창의 제목을 설정
root.title("로그인")
#메인 창에 전화번호 버튼 배치
tk.Label(root, text="전화번호").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()
#메인 창에 비밀번호 버튼 배치
tk.Label(root, text="비밀번호").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="로그인", command=login).pack()

tk.Button(root, text="회원가입", command=register).pack()
#사용자가 창을 닫을 때까지 계속 실행 
root.mainloop()
