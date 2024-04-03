#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from fpdf import FPDF
from Convert_Numbers_to_Japanese import *

# 生成100个随机数
random_numbers = [random.randint(1, 100) for _ in range(100)]
# 保存转化后的字符
dic ={
    'number': 0,
    "kanji": ''
    "hiragana": '',
    "romaji": '',
}
# 保存转化后的随机数
out_text =[]
# 转化数字为平假名、罗马字符、汉字
for number in random_numbers:
    dic['number']=number
    dic['romaji'] = Convert(number,'romaji')
    dic['hiragana'] = Convert(number,'hiragana')
    dic['kanji'] = Convert(number,'kanji')
    out_text.append(dic)
    
# 创建PDF文档
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# 设置字体和字号
pdf.set_font("Arial", size=12)

# 将随机数写入PDF文件
for number in random_numbers:
    pdf.cell(0, 10, str(number), ln=True, align='C')

# 保存PDF文件
pdf_file_name = "random_numbers.pdf"
pdf.output(pdf_file_name)

print(f"PDF文件已生成: {pdf_file_name}")



