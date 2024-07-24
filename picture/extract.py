import cv2  
import numpy as np  

for i in range(1, 5):  # 假设要处理文件名1.png到5.png的情况  
    # 读取输入图片  
    image = cv2.imread(f'pic/{i}.png')  

    # 将图片转为灰度图并使用Canny边缘检测算法获取图像边缘  
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    edges = cv2.Canny(gray_image, 100, 200)  

    # 执行闭运算来处理图像边缘，进一步细化边缘线  
    # kernel = np.ones((3, 3), np.uint8)  
    # edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)  
    # edges = cv2.dilate(edges, kernel, iterations=1)  
    # edges = cv2.erode(edges, kernel, iterations=1)  

    # 保存细化后的图片  
    output_image_path = f'out/{i}.png'  
    
    edges_resized = cv2.resize(edges, (300, 300), interpolation=cv2.INTER_AREA)  # 这个地方大小得统一
    cv2.imwrite(output_image_path, edges_resized)  

    print(f"处理完毕：{output_image_path}")