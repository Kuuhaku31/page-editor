# from PIL 导入 Image
from PIL import Image


def concat_images(img_path1, img_path2, output_path):
    # 打开两张图片
    img1 = Image.open(img_path1)
    img2 = Image.open(img_path2)

    # 计算新图片的尺寸
    new_width = img1.width + img2.width
    new_height = max(img1.height, img2.height)

    # 创建新图片
    new_img = Image.new("RGB", (new_width, new_height), (255, 255, 255))

    # 粘贴两张图片
    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (img1.width, 0))

    # 保存新图片
    new_img.save(output_path)
    print(f"拼接完成，已保存到 {output_path}")


if __name__ == "__main__":
    # 示例用法：请将 img1.jpg 和 img2.jpg 替换为你的图片路径
    root_path = "D:/repositories/page-editor/imgs"
    concat_images(f"{root_path}/001.jpg", f"{root_path}/000.jpg", f"{root_path}/output.jpg")
