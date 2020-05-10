# _*_ coding:utf-8 _*_
# @Time 2020/5/10 9:45 下午

from PyPDF2 import PdfFileReader, PdfFileWriter


# PDF文件分割
def split_pdf(read_file, out_detail):
    try:
        fp_read_file = open(read_file, 'rb')
        pdf_input = PdfFileReader(fp_read_file)  # 将要分割的PDF内容格式话
        page_count = pdf_input.getNumPages()  # 获取PDF页数
        print(page_count)  # 打印页数

        with open(out_detail, 'r', True, 'utf-8')as fp:
            # print(fp)
            txt = fp.readlines()
            # print(txt)
            for detail in txt:  # 打开分割标准文件
                # print(type(detail))
                pages = detail.strip()  # 空格分组
                #  write_file, write_ext = os.path.splitext(write_file)  # 用于返回文件名和扩展名元组
                pdf_file = f'img/{pages}.pdf'
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
        # fp.close()
    except Exception as e:
        print(e)
    finally:
        fp_read_file.close()


split_pdf('cq2019.pdf', 'config.txt')