import pymupdf
from tkinter import *
from random import randrange
#func for extracting bold text and giving random bold texts with PyMuPDF(fitz)
def extract_bold_text(filename):
    n = 0
    doc = pymupdf.open(filename)
    bold_text = []
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    if "Bold" in span["font"] or span["flags"] & 16:
                        bold_text.append(span["text"])
    for i in bold_text:
        n+=1
    randomBilet = bold_text[randrange(n)]
    return randomBilet
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


