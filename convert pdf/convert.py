import fitz  # PyMuPDF
from PIL import Image
import io

# PDF 文件路径
pdf_path = '/Users/dongdongd/Desktop/智能化办公系统的构建及应用.pdf'  # 替换为您的 PDF 文件路径

# 打开 PDF 文件
pdf = fitz.open(pdf_path)

# 遍历每一页
for page_num in range(len(pdf)):
    # 获取页面
    page = pdf.load_page(page_num)

    # 将页面转换为图片（Pixmap）
    pix = page.get_pixmap()

    # 将图片转换为字节
    img_data = pix.tobytes("png")

    # 使用 Pillow 创建一个 Image 对象
    image = Image.open(io.BytesIO(img_data))

    # 将图片保存为 JPEG 格式
    image.save(f"page_{page_num + 1}.jpg")

# 关闭 PDF 文件
pdf.close()
