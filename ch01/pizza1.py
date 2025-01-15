import tkinter as tk
from tkinter import messagebox

# 주문 제출 함수
def submit_order():
    pizza_type = pizza_var.get()
    slices = slices_var.get()
    toppings = []
    if cheese_var.get():
        toppings.append("치즈 추가")
    if pepperoni_var.get():
        toppings.append("페퍼로니 추가")
    if mushrooms_var.get():
        toppings.append("버섯 추가")

    order_summary = f"피자 종류: {pizza_type}\n조각 수: {slices}조각\n추가 토핑: {', '.join(toppings) if toppings else '없음'}"
    messagebox.showinfo("주문 확인", order_summary)

# 창 설정
root = tk.Tk()
root.title("피자 주문 프로그램")
root.geometry("400x300")

# 피자 종류 선택
tk.Label(root, text="피자 종류 선택").pack(anchor="w", padx=10, pady=5)
pizza_var = tk.StringVar(value="마가리타")
pizza_options = ["마가리타", "페퍼로니", "하와이안", "콤비네이션"]
for option in pizza_options:
    tk.Radiobutton(root, text=option, variable=pizza_var, value=option).pack(anchor="w", padx=20)

# 조각 수 선택
tk.Label(root, text="조각 수 선택").pack(anchor="w", padx=10, pady=5)
slices_var = tk.IntVar(value=1)
tk.Spinbox(root, from_=1, to=12, textvariable=slices_var, width=5).pack(anchor="w", padx=20, pady=5)

# 추가 토핑 선택
tk.Label(root, text="추가 토핑").pack(anchor="w", padx=10, pady=5)
cheese_var = tk.BooleanVar()
pepperoni_var = tk.BooleanVar()
mushrooms_var = tk.BooleanVar()
tk.Checkbutton(root, text="치즈 추가", variable=cheese_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="페퍼로니 추가", variable=pepperoni_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="버섯 추가", variable=mushrooms_var).pack(anchor="w", padx=20)

# 주문 제출 버튼
tk.Button(root, text="주문 제출", command=submit_order).pack(pady=20)

# 메인 루프 실행
root.mainloop()
