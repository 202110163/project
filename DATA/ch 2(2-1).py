def main():
    A = [10, 20, 30]
    B = A[:]  # A 리스트를 복사하여 B에 할당
    
    print("배열 복사 결과:")
    for i in range(len(A)):
        print(f"A[{i}] = {A[i]}\tB[{i}] = {B[i]}")

if __name__ == "__main__":
    main()
