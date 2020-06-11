def hanoi(panes, src, buffer, dst):
    if panes == 1:
        print(f'Move {src} == {1} ==> {dst}')
    else:
        # 将n-1个移到中间
        hanoi(panes - 1,src,dst,buffer)
        # 将最后一个移到目标位置
        print(f'Move {src} == {panes} ==> {dst}')
        # 将n-1个移到目标位置
        hanoi(panes - 1,buffer,src,dst)

if __name__ == '__main__':
    hanoi(4, 'A', 'B', 'C')