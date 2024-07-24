import cv2  
import numpy as np  


def check(posx, posy, H, W): # 会true的时候继续走，false的时候停止 即抬起来
    for i in range(-1, 2):  
        for j in range(-1, 2):  
            new_x = posx + i  
            new_y = posy + j    
            if new_x >= 0 and new_x < H and new_y >= 0 and new_y < W:    
                if binary_array[new_x, new_y] == 1:  
                    return True  
    return False 

def point(posx, posy, H, W):   
    for i in range(-1, 2):  
        for j in range(-1, 2):  
            new_x = posx + i  
            new_y = posy + j    
            if new_x >= 0 and new_x < H and new_y >= 0 and new_y < W:    
                if binary_array[new_x, new_y] == 1:  
                    binary_array[new_x, new_y] = 0
                    return [new_x, new_y, 0]
    return [-1, 0, 0]
          

Point_np = []

for i in range(2, 3):  # 假设要处理文件名1.png到5.png的情况  
    # 读取输入图片    0 是黑色 255是白色
    image = cv2.imread(f'out/{i}.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    H, W = image.shape
    binary_array = (image == 255).astype(np.uint8)  
    
    # 找到一个点 开始找下一个点
    for i in range(H):
        for j in range(W):
            if(binary_array[i][j]):
                Point_np.append([float(i)/1000, float(j)/1000, 0])
                binary_array[i][j] = 0
                point_tmp = point(i, j, H, W)
                while(point_tmp[0] != -1):
                    x_tmp = point_tmp[0]
                    y_tmp = point_tmp[1]
                    Point_np.append([float(x_tmp)/1000, float(y_tmp)/1000, 0])
                    binary_array[x_tmp][y_tmp] = 0
                    point_tmp = point(x_tmp, y_tmp, H, W)       
                else:
                    Point_np.append(point_tmp)
            else:
                continue
print(Point_np)