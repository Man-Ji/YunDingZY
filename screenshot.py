import cv2
import numpy as np
import pyautogui
import pytesseract
from PIL import Image

def screen_Save():
    # 定义矩形区域的位置和大小
    rectangles = [
        (483, 1040, 152, 27),  # (左上角x坐标, 左上角y坐标, 宽度, 高度)
        (684, 1040, 152, 27),
        (885, 1040, 152, 27),
        (1086, 1040, 152, 27),
        (1287, 1040, 152, 27)
    ]

    # 遍历每个矩形区域
    #region = (474, 923, 1000, 147)
    #screenshot = pyautogui.screenshot()
    for i, rect in enumerate(rectangles):
        # 获取矩形区域的截图
        screenshot = pyautogui.screenshot(region=rect)
        screenshot.save(f'{i}screenshot.png')
        #img = np.array(screenshot)
        #region_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        #region_img = img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]

        # 将截取的图像转换为 PIL.Image 对象
        #screenshot = cv2.imread(f'hero/{i}screenshot.png')
        #pil_img = Image.fromarray(screenshot)

        # 提取文字
        #extracted_text = pytesseract.image_to_string(region_img, lang='chi_sim', config='-psm 6')
        #extracted_text = pytesseract.image_to_string(pil_img, lang='chi_sim')
        # 保存图片
        #save_path = f'hero/{extracted_text.strip()}.png'
        #cv2.imwrite(save_path, region_img)
        #pil_img.save(save_path)
        # 显示截图（可选）
        #region_img.show()

if __name__ == '__main__':
    #while True:
        screen_Save()

