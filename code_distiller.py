
from tkinter import *
from tkinter import filedialog,messagebox,simpledialog


class Application:

    def __init__(self,toplevel):
        mainwin = Frame(toplevel)
        mainwin.grid()

        self.labelIn = Label(mainwin,text="Data file: ")
        self.labelIn.grid(column=0,row=0)

        self.entryIn = Entry(mainwin,width=50)
        self.entryIn.grid(column=1,row=0)

        self.labelOut = Label(mainwin,text="LaTeX file: ")
        self.labelOut.grid(column=0,row=1)

        self.entryOut = Entry(mainwin,width=50)
        self.entryOut.grid(column=1,row=1)

        self.buttonIn = Button(mainwin,text="Select data file",width=15,command=self.selectFile)
        self.buttonIn.grid(column=1,row=2)

        self.buttonIn = Button(mainwin,text="Select output file",width=15,command=self.selectOFile)
        self.buttonIn.grid(column=1,row=3)
        
        self.buttonPd = Button(mainwin,text="Prepare data",width=15,fg="red",command=self.prepareData)
        self.buttonPd.grid(column=1,row=4)

        self.buttonSi = Button(mainwin,text="Show info",width=15,command=self.showInfo)
        self.buttonSi.grid(column=1,row=5)



    def selectFile(self):
        infile = filedialog.askopenfilename(title="Select data file",filetypes=[["Comma Separated Values",".csv"]])
        self.entryIn.delete(0, END)
        self.entryIn.insert(END,infile)

    def selectOFile(self):
        outfile = filedialog.asksaveasfilename(title="Select output file",filetypes=[["LaTeX files",".tex"]])
        if ".tex" in outfile:
            pass
        else:
            outfile = outfile+".tex"
            
        self.entryOut.delete(0, END)
        self.entryOut.insert(END,outfile)

    def showInfo(self):
        infotext = """Codesticker Distiller 1.0\n\nconverts specific CSV files into LaTeX source files that can be used to produce stickers with barcode (code128) and labels.\n\n
(C) Lukas Ruzicka, 2017.\n This program is under the GPLv3 license. """
        messagebox.showinfo("Information",infotext)

    def prepareData(self):
        infile = self.entryIn.get()
        outfile = self.entryOut.get()

        try:
            with open(infile,'r') as csvfile:
                data = csvfile.readlines()

            output = []
            page = []

            for line in data:
                row = line.split(",")
                code = row[0]
                item = row[1]
                store = row[2]
                ctype = "code128"

                page.append("\\begin{center}\n")
                page.append("\\begin{pspicture}(40mm,30mm)\n")
                page.append("\\psbarcode{%s}{includetext inkspread=0.5}{%s}\n" % (code,ctype))
                page.append("\\end{pspicture}\n\n")
                page.append("\\vspace{12pt}\n\n")
                page.append("%s\n\n" % (item))
                page.append("%s\n" % (store))
                page.append("\\end{center}\n\n")
                page = "".join(page)
                output.append(page)
                page = []

            output = "".join(output)

            with open(outfile,'w') as texfile:
                c = texfile.write(output)

            message = messagebox.showinfo("Creating LaTex file","The LaTeX file was created successfully!")

        except:
            message = messagebox.showerror("Creating LaTex file","Something went wrong. Maybe wrong data? No file was created!")

root = Tk()
root.title("Codesticker Distiller 1.0")
app = Application(root)

root.mainloop()
#root.destroy()
        
