# from PIL 导入 Image
import os

from PIL import Image


def 获取文件列表(path) -> list[str]:
    """
    获取指定目录下的所有文件列表
    :param path: 目录路径
    :return: 文件名列表
    """

    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


def 分组(文件列表, 单张编号):
    """
    编号从 0 开始
    """
    print("开始分组")

    分好的组列表 = []

    p = 0
    状态 = "开始新的分组"
    while True:

        if p >= len(文件列表):
            break

        elif p in 单张编号:
            状态 = "开始新的分组"
            分好的组列表.append([文件列表[p]])
            p += 1
            continue

        elif 状态 == "开始新的分组":
            分好的组列表.append([文件列表[p]])
            状态 = "分组中"
            p += 1
            continue

        elif 状态 == "分组中":
            分好的组列表[-1].append(文件列表[p])
            p += 1
            continue

    return 分好的组列表


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


测试数据列表 = ["aaaa", "bbbb", "cccc", "dddd", "e", "f", "g"]
测试数据编号 = [0, 1, 4]

if __name__ == "__main__":

    root_path = "D:/repositories/page-editor/img"

    # concat_images(f"{root_path}/001.jpg", f"{root_path}/000.jpg", f"{root_path}/output.jpg")

    # file_list = 获取文件列表(root_path)
    # print(file_list)

    # 分好的组列表 = 分组(测试数据列表, 测试数据编号)
    # print("测试数据列表:", 测试数据列表)
    # print("测试数据编号:", 测试数据编号)
    # print("分好的组列表:", 分好的组列表)
