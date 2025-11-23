def main():
    try:
        isbn_input = input("请输入ISBN号码: ").strip()
        
        # 检查输入长度
        if len(isbn_input) != 13:
            print(f"错误：ISBN号码必须是13位字符，当前输入了{len(isbn_input)}位")
            return
        
        a = list(isbn_input)
        A = [-1] * 13
        
        # 处理输入数据（添加边界检查）
        for i in range(min(13, len(a))):  # 确保不越界
            if a[i] != '-':
                try:
                    A[i] = int(a[i])
                except ValueError:
                    print(f"错误：第{i+1}位字符'{a[i]}'不是有效数字")
                    return
        
        # 计算校验和
        j = 0
        total_sum = 0
        for i in range(12):  # 只处理前12位
            if A[i] != -1:
                j += 1
                total_sum += A[i] * j
        
        checksum = total_sum % 11
        
        # 验证和修正（添加边界检查）
        if A[12] != -1:  # 确保第13位存在
            if checksum == A[12]:
                print("Right")
            elif checksum == 10 and a[12] == 'X':
                print("Right")
            else:
                if checksum != 10:
                    a[12] = str(checksum)
                else:
                    a[12] = 'X'
                print('修正后的ISBN:', ''.join(a))
        else:
            print("错误：缺少校验位（第13位）")
            
    except Exception as e:
        print(f"程序出错: {e}")

if __name__ == "__main__":
    main()