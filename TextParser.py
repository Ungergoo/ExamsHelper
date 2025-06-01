import pymupdf
from tkinter import *
from random import randrange
#func for extracting bold text and giving random bold texts with PyMuPDF(fitz)
def extract_bold_text(filename):
    n = 0
    bold_blocks = []
    current_bold_block = []
    doc = pymupdf.open(filename)
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    is_bold = "Bold" in span["font"] or span["flags"] & 16
                    if is_bold:
                        current_bold_block.append(span["text"])
                    else:
                        if current_bold_block:
                            bold_blocks.append("".join(current_bold_block))
                            current_bold_block = []
            if current_bold_block:
                bold_blocks.append("".join(current_bold_block))
                current_bold_block = []
    if not bold_blocks:
        return("Не найден жирный текст")
    return(bold_blocks[randrange(len(bold_blocks))])
#func for extracting file name
def fileExtraction():
    FilePath = entry.get()
    if not FilePath:
        print("Пустое имя файла")
        return
    result = extract_bold_text(FilePath)
    labelBielta.config(text=result)
    return(result)
#tkinter stuff
root = Tk()
root.geometry("500x500+700+300")
root.resizable(False, False)
label = Message(root, text="Введите название файла с расширением, или полный путь к файлу (доступные расширения: pdf):", width=300)
label.pack()
entry = Entry()
entry.pack()

btn = Button(root, text="Выдать билет", command=fileExtraction)
btn.pack()
labelBielta = Message(root, text="", width=300)
labelBielta.pack()
root.mainloop()


