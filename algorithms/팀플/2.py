import tkinter as tk
from tkinter import messagebox, ttk
import datetime
import json
import os

USER_INFO_FILE = "user_info.json"
RESERVATION_INFO_FILE = "reservation_info.json"
# 임시 데이터베이스로 전화번호와 비밀번호를 저장
users = {}

# 사용자 정보 관련 함수
def save_user_info():
    with open(USER_INFO_FILE, "w") as file:
        json.dump(users, file)

def load_user_info():
    global users
    try:
        with open(USER_INFO_FILE, "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}

# Movie 클래스 정의
class Movie:
    def __init__(self, title, times, age_limit):
        self.title = title
        self.times = times
        self.age_limit = age_limit
        self.seats = {time: [
            'A1', 'A2', 'A3', 'A4', 'A5', 'A6',
            'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 
            'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 
            'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
            'F1', 'F2', 'F3', 'F4', 'F5', 'F6'
        ] for time in times}

# 예매 시스템 클래스 정의
class ReservationSystem:
    def __init__(self, root):
        self.root = root
        self.movies = [
            Movie("범죄도시 4", ["10:00", "11:00", "11:20", "16:00", "19:00", "20:15"], 19),
            Movie("귀멸의 칼날", ["11:00", "14:00", "17:00", "19:07", "20:00"], 15),
            Movie("보라", ["12:00", "15:00", "16:00", "18:20", "20:00", "21:00", "22:00"], 12),
            Movie("영화 4", ["13:30", "14:30", "15:30", "16:00", "17:00", "19:00", "20:30"], 12),
            Movie("영화 5", ["12:00", "13:30", "14:20", "16:00", "19:00", "20:05"], 12)
        ]
        self.ticket_prices = {
            '성인': 18000,
            '청소년': 15000,
            '어린이': 9000
        }
        self.reservations = {}
        self.current_phone_number = ""
        
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)
        
        self.login_frame()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def add_back_button(self, previous_function):
        back_button = ttk.Button(self.main_frame, text="뒤로", command=previous_function)
        back_button.grid(row=0, column=0, sticky='w', pady=10)

    def bind_enter_key(self, function):
        self.root.bind('<Return>', lambda event: function())

    def unbind_enter_key(self):
        self.root.unbind('<Return>')

        def login_frame(self):
            self.clear_frame()
        self.unbind_enter_key()
        ttk.Label(self.main_frame, text="영화 예매 시스템에 오신 것을 환영합니다").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.main_frame, text="전화번호를 입력해 주세요 (예: 010-1234-5678)").grid(row=1, column=0, sticky='w', pady=5)
        self.phone_entry = ttk.Entry(self.main_frame)
        self.phone_entry.grid(row=2, column=0, padx=5, pady=5)

        ttk.Label(self.main_frame, text="비밀번호를 입력하세요:").grid(row=3, column=0, sticky='w', pady=5)
        self.password_entry = ttk.Entry(self.main_frame, show="*")
        self.password_entry.grid(row=4, column=0, padx=5, pady=5)

        login_button = ttk.Button(self.main_frame, text="로그인", command=self.login)
        login_button.grid(row=5, column=0, pady=10)

        register_button = ttk.Button(self.main_frame, text="회원가입", command=self.register)
        register_button.grid(row=6, column=0, pady=10)

        self.bind_enter_key(self.login)


    def register(self):
        def submit_registration():
            phone = phone_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()
            
            if password != confirm_password:
                messagebox.showerror("오류", "비밀번호가 일치하지 않습니다.")
                return
            
            if phone in users:
                messagebox.showerror("오류", "이 전화번호는 이미 가입되어 있습니다.")
            else:
                users[phone] = password
                messagebox.showinfo("성공", "회원가입이 완료되었습니다!")
                register_window.destroy()

        register_window = tk.Toplevel(self.root)
        register_window.title("회원가입")

        tk.Label(register_window, text="전화번호").pack(pady=5)
        phone_entry = tk.Entry(register_window)
        phone_entry.pack(pady=5)

        tk.Label(register_window, text="비밀번호").pack(pady=5)
        password_entry = tk.Entry(register_window, show="*")
        password_entry.pack(pady=5)
        
        tk.Label(register_window, text="비밀번호 재입력").pack(pady=5)
        confirm_password_entry = tk.Entry(register_window, show="*")
        confirm_password_entry.pack(pady=5)

        tk.Button(register_window, text="가입", command=submit_registration).pack(pady=10)

    def login(self):
        phone_number = self.phone_entry.get()
        password = self.password_entry.get()
        
        if phone_number in users and users[phone_number] == password:
            self.current_phone_number = phone_number
            if phone_number not in self.reservations:
                self.reservations[phone_number] = []
            self.main_menu()
        else:
            messagebox.showerror("오류", "전화번호와 비밀번호가 맞지 않습니다.")
    
    def main_menu(self):
        self.clear_frame()
        self.unbind_enter_key()
        ttk.Label(self.main_frame, text=f"{self.current_phone_number}으로 로그인되었습니다.").grid(row=0, column=0, columnspan=2, pady=10)
        
        reserve_button = ttk.Button(self.main_frame, text="1. 영화 예매", command=self.make_reservation)
        reserve_button.grid(row=1, column=0, columnspan=2, pady=10)
        
        view_button = ttk.Button(self.main_frame, text="2. 예매 내역 조회", command=self.view_reservations)
        view_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        logout_button = ttk.Button(self.main_frame, text="3. 로그아웃", command=self.login_frame)
        logout_button.grid(row=3, column=0, columnspan=2, pady=10)

        def make_reservation(self):
        self.clear_frame()
        self.unbind_enter_key()
        self.add_back_button(self.main_menu)
        ttk.Label(self.main_frame, text="영화를 선택하세요:").grid(row=1, column=0, columnspan=2, pady=10)
        
        self.movie_listbox = tk.Listbox(self.main_frame, height=6)
        for movie in self.movies:
            self.movie_listbox.insert(tk.END, f"{movie.title} (연령 제한: {movie.age_limit}세 이상)")
        self.movie_listbox.grid(row=2, column=0, columnspan=2, pady=10)
        
        select_button = ttk.Button(self.main_frame, text="선택", command=self.select_movie)
        select_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.bind_enter_key(self.select_movie)
    
    def select_movie(self):
        try:
            index = self.movie_listbox.curselection()[0]
            self.selected_movie = self.movies[index]
            self.select_num_people()
        except IndexError:
            messagebox.showerror("오류", "영화를 선택하세요.")
    
    def select_num_people(self):
        self.clear_frame()
        self.unbind_enter_key()
       
        self.add_back_button(self.make_reservation)
        ttk.Label(self.main_frame, text=f"{self.selected_movie.title} (연령 제한: {self.selected_movie.age_limit}세 이상)").grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(self.main_frame, text="인원 수를 선택하세요:").grid(row=1, column=0, columnspan=2, pady=10)
        
        ttk.Label(self.main_frame, text="성인:").grid(row=2, column=0, sticky='e', pady=5)
        self.adult_spinbox = tk.Spinbox(self.main_frame, from_=0, to=10, width=5)
        self.adult_spinbox.grid(row=2, column=1, pady=5)
        
        ttk.Label(self.main_frame, text="청소년:").grid(row=3, column=0, sticky='e', pady=5)
        self.teen_spinbox = tk.Spinbox(self.main_frame, from_=0, to=10, width=5)
        self.teen_spinbox.grid(row=3, column=1, pady=5)
        
        ttk.Label(self.main_frame, text="어린이:").grid(row=4, column=0, sticky='e', pady=5)
        self.child_spinbox = tk.Spinbox(self.main_frame, from_=0, to=10, width=5)
        self.child_spinbox.grid(row=4, column=1, pady=5)
        
        next_button = ttk.Button(self.main_frame, text="다음", command=self.select_time)
        next_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.bind_enter_key(self.select_time)
    
    def select_time(self):
        try:
            self.adults = int(self.adult_spinbox.get())
            self.teens = int(self.teen_spinbox.get())
            self.children = int(self.child_spinbox.get())
            total_people = self.adults + self.teens + self.children
            
            if total_people == 0:
                messagebox.showerror("오류", "최소 한 명 이상의 인원을 선택해야 합니다.")
                return
            
            if self.selected_movie.age_limit == 19 and self.teens > 0:
                messagebox.showerror("오류", "이 영화는 청소년 관람 불가입니다.")
                return
            
            if self.selected_movie.age_limit > 15 and self.children > 0:
                messagebox.showerror("오류", f"이 영화는 {self.selected_movie.age_limit}세 이상 관람 가능합니다.")
                return
            
            self.clear_frame()
            self.unbind_enter_key()
            self.add_back_button(self.select_num_people)
            
            ttk.Label(self.main_frame, text=f"{self.selected_movie.title} 상영 시간을 선택하세요:").grid(row=0, column=0, columnspan=2, pady=10)
            
            self.time_listbox = tk.Listbox(self.main_frame, height=6)
            for time in self.selected_movie.times:
                self.time_listbox.insert(tk.END, time)
            self.time_listbox.grid(row=1, column=0, columnspan=2, pady=10)
            
            select_button = ttk.Button(self.main_frame, text="선택", command=self.select_seats)
            select_button.grid(row=2, column=0, columnspan=2, pady=10)
            
            self.bind_enter_key(self.select_seats)
        except ValueError:
            messagebox.showerror("오류", "유효한 인원 수를 입력하세요.")
    
    def select_seats(self):
        try:
            self.selected_time = self.time_listbox.get(self.time_listbox.curselection())
            self.clear_frame()
            self.unbind_enter_key()
            self.add_back_button(self.select_time)
            
            ttk.Label(self.main_frame, text="좌석을 선택하세요:").grid(row=0, column=0, columnspan=6, pady=10)
            
            self.seat_buttons = {}
            for i, seat in enumerate(self.selected_movie.seats[self.selected_time]):
                row, col = divmod(i, 6)
                button = tk.Button(self.main_frame, text=seat, width=5, command=lambda s=seat: self.toggle_seat(s))
                button.grid(row=row + 1, column=col, padx=5, pady=5)
                self.seat_buttons[seat] = button
            
            confirm_button = ttk.Button(self.main_frame, text="확인", command=self.confirm_reservation)
            confirm_button.grid(row=7, column=0, columnspan=6, pady=10)
            
            self.selected_seats = []
        except IndexError:
            messagebox.showerror("오류", "상영 시간을 선택하세요.")
    
    def toggle_seat(self, seat):
        if seat in self.selected_seats:
            self.selected_seats.remove(seat)
            self.seat_buttons[seat].configure(bg='SystemButtonFace')
        else:
            total_people = self.adults + self.teens + self.children
            if len(self.selected_seats) < total_people:
                self.selected_seats.append(seat)
                self.seat_buttons[seat].configure(bg='lightgreen')
            else:
                messagebox.showwarning("경고", "선택한 인원 수 만큼의 좌석을 선택했습니다.")
    
    def confirm_reservation(self):
        total_people = self.adults + self.teens + self.children
        if len(self.selected_seats) != total_people:
            messagebox.showerror("오류", "선택한 인원 수 만큼의 좌석을 선택하세요.")
            return
        
        total_price = (self.adults * self.ticket_prices['성인'] +
                       self.teens * self.ticket_prices['청소년'] +
                       self.children * self.ticket_prices['어린이'])
        
        reservation_details = {
            "movie": self.selected_movie.title,
            "time": self.selected_time,
            "seats": self.selected_seats,
            "total_price": total_price,
            "date": datetime.date.today().isoformat()
        }
        
        self.reservations[self.current_phone_number].append(reservation_details)
        self.selected_movie.seats[self.selected_time] = [seat for seat in self.selected_movie.seats[self.selected_time] if seat not in self.selected_seats]
        
        messagebox.showinfo("성공", f"예매가 완료되었습니다.\n총 가격: {total_price}원")
        self.main_menu()
    
    def view_reservations(self):
        self.clear_frame()
        self.unbind_enter_key()
        self.add_back_button(self.main_menu)
        
        ttk.Label(self.main_frame, text="예매 내역 조회").grid(row=0, column=0, columnspan=2, pady=10)
        
        reservations = self.reservations.get(self.current_phone_number, [])
        
        if not reservations:
            ttk.Label(self.main_frame, text="예매 내역이 없습니다.").grid(row=1, column=0, columnspan=2, pady=10)
        else:
            for i, reservation in enumerate(reservations):
                ttk.Label(self.main_frame, text=f"{i + 1}. {reservation['movie']} - {reservation['time']} - {reservation['seats']} - {reservation['total_price']}원 - {reservation['date']}").grid(row=i + 1, column=0, columnspan=2, pady=5)
        
        close_button = ttk.Button(self.main_frame, text="닫기", command=self.main_menu)
        close_button.grid(row=len(reservations) + 1, column=0, columnspan=2, pady=10)

    if __name__ == "__main__":
    load_user_info()
    
    root = tk.Tk()
    root.title("영화 예매 시스템")
    
    reservation_system = ReservationSystem(root)
    
    def on_closing():
        save_user_info()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
