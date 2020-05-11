# _*_ coding:utf-8 _*_
# @Time 2020/5/10 9:45 下午

from PyPDF2 import PdfFileReader, PdfFileWriter

class PDF4Split(object):

    # PDF文件分割
    def split_pdf(self, pdf_file, out_detail):

        with open(pdf_file, 'rb') as fp_read_file:
            pdf_input = PdfFileReader(fp_read_file)  # 将要分割的PDF内容格式化
            page_count = pdf_input.getNumPages()  # 获取PDF页数
            print(page_count)  # 打印页数

            with open(out_detail, 'r', True, 'utf-8') as fp:
                txt = fp.readlines()
                for detail in txt:  # 打开分割标准文件
                    pages = detail.strip()  # 空格分组
                    #  write_file, write_ext = os.path.splitext(write_file)  # 用于返回文件名和扩展名元组
                    pdf_file = f'{pages}.pdf'
                    # liststr=list(map(int, pages.split('-')))
                    # print(type(liststr))
                    start_page, end_page = list(map(int, pages.split('-')))  # 将字符串数组转换成整形数组
                    start_page -= 1
                    try:
                        print(f'开始分割{start_page}页-{end_page}页，保存为{pdf_file}......')
                        pdf_output = PdfFileWriter()  # 实例一个 PDF文件编写器
                        for i in range(start_page, end_page):
                            pdf_output.addPage(pdf_input.getPage(i))
                        with open(pdf_file, 'wb') as sub_fp:
                            pdf_output.write(sub_fp)
                        print(f'完成分割{start_page}页-{end_page}页，保存为{pdf_file}!')
                    except IndexError:
                        print(f'分割页数超过了PDF的页数')


if __name__ == "__main__":
    PDF4Split().split_pdf('../xxtest/pdf4tranfor/cq2019.pdf', '../xxtest/pdf4tranfor/config.txt')