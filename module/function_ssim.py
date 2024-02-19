# ssim的相关方法
import cv2
import numpy

from module import function_normal


def _image_to_numpy(image_file):
    """将图片转换为numpy图片对象"""
    image_numpy = cv2.imdecode(numpy.fromfile(image_file, dtype=numpy.uint8), -1)
    image_numpy = cv2.resize(image_numpy, (8, 8))

    try:
        image_numpy = cv2.cvtColor(image_numpy, cv2.COLOR_BGR2GRAY)
    except cv2.error:
        pass

    return image_numpy


def calc_images_ssim(image_1, image_2):
    """计算两张图片的ssim相似度"""
    function_normal.print_function_info()
    image_numpy1 = _image_to_numpy(image_1)
    image_numpy2 = _image_to_numpy(image_2)

    # 计算均值、方差和协方差
    mean1, mean2 = numpy.mean(image_numpy1), numpy.mean(image_numpy2)
    var1, var2 = numpy.var(image_numpy1), numpy.var(image_numpy2)
    covar = numpy.cov(image_numpy1.flatten(), image_numpy2.flatten())[0][1]

    # 设置常数
    c1 = (0.01 * 255) ** 2
    c2 = (0.03 * 255) ** 2

    # 计算SSIM
    numerator = (2 * mean1 * mean2 + c1) * (2 * covar + c2)
    denominator = (mean1 ** 2 + mean2 ** 2 + c1) * (var1 + var2 + c2)
    ssim = numerator / denominator

    return ssim
