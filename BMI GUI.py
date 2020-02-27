"""BMI Calculator with GUI"""


# import tkinter with from
from tkinter import *

# make class for tk App
class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        #create header font and label fonts
        self.headerFont = ("Calibri", "18", "bold underline")
        self.lblFont = ("Arial", "11", "italic")

        #set app title and create label as title to calculator (spanning all col)
        self.title("BMI Calc")
        Label(self, text = "Body Mass Index Calculator",
              font = self.headerFont).grid(columnspan = 3)

        #add weight lbls/entry boxes
        #add height
        #add BMI output
        #add reset, exit, and calculate buttons
        self.addWeight()
        self.addHeight()
        self.addBMI()
        self.addButtons()


    def addWeight(self):
        """ add weight elements"""
        #add "weight" label and "lbs." label on left and right sides, rspctvly
        Label(self, text = "Weight",
              font = self.lblFont).grid(row = 1, column = 0)
        Label(self, text = "lbs.",
              font = self.lblFont).grid(row = 1, column = 2)

        #add entry box for weight in between two labels
        self.txtWeight = Entry(self, relief = SUNKEN)
        self.txtWeight.grid(row = 1, column = 1)
        self.txtWeight.insert(0, "0")


    def addHeight(self):
        """add height elements"""
        #add "height" label and "ft." on left and right sides
        #add "in." on right side of next row
        Label(self, text = "Height",
              font = self.lblFont).grid(row = 2, column = 0, rowspan = 2)
        Label(self, text = "ft.",
              font = self.lblFont).grid(row = 2, column = 2)
        Label(self, text = "in.",
              font = self.lblFont).grid(row = 3, column = 2)
        
        #add entry boxes: one for ft. and one for in. on next row
        self.txtHeightFT = Entry(self, relief = "sunken")
        self.txtHeightFT.grid(row = 2, column = 1)
        self.txtHeightFT.insert(0, "0")

        self.txtHeightIN = Entry(self, relief = "sunken")
        self.txtHeightIN.grid(row = 3, column = 1)
        self.txtHeightIN.insert(0, "0")


    def addBMI(self):
        """add BMI Elements"""
        #add BMI label and output label
        #add Status label and ouput label
        Label(self, text = """
----RESULTS----""",
              font = self.headerFont).grid(row = 4, columnspan = 3)
        Label(self, text = "BMI:",
              font = self.lblFont).grid(row = 5, column = 0)
        Label(self, text = "Status:",
              font = self.lblFont).grid(row = 6, column = 0)


        #add readonly text boxes
        self.lblBMI = Label(self, bg = "#C6E2FF", anchor = "w", relief = "flat")
        self.lblBMI.grid(row = 5, column = 1, sticky = "we")

        self.lblStatus = Label(self, bg = "#C6E2FF", anchor = "w", relief = "flat")
        self.lblStatus.grid(row = 6, column = 1, sticky = "we")


    def calculate(self):
        """ calculate BMI from height and weight """

        #set "Status" variable to "" for if loop
        status = ""
        
        #get entries from both height boxes and weight entry box
        heightFT = int(self.txtHeightFT.get())
        heightIN = int(self.txtHeightIN.get())
        weight = int(self.txtWeight.get())

        #convert feet to inches and add together
        heightTot = (heightFT * 12) + heightIN

        #calculate BMI
        BMI = (weight/(heightTot ** 2)) * 703

        #set BMI to lblBMI
        self.lblBMI["text"] = "%.2f" % BMI

        #determine the "status"/classification for BMI
        if BMI <= 18.5:
            status = "Underweight"
        elif BMI <= 25:
            status = "Average"
        elif BMI <= 30:
            status = "Overweight"
        elif BMI > 30:
            status = "Obese"
        else:
            status = "Something went wrong..."

        self.lblStatus["text"] = "{}".format(status)


    def addButtons(self):
        """ add buttons at bottom """
        #add calculate button
        self.btnCalc = Button(self, text = "Calculate!")
        self.btnCalc.grid(row = 7, column = 0)
        self.btnCalc["command"] = self.calculate

        #add Reset button
        self.btnReset = Button(self, text = "Reset")
        self.btnReset.grid(row = 7, column = 1)
        self.btnReset["command"] = self.reset

        #add exit button
        self.btnExit = Button(self, text = "Exit")
        self.btnExit.grid(row = 7, column = 2)
        self.btnExit["command"] = self.close


    def reset(self):
        """ method to reset height and weight to 0 """
        #delete entry boxes and insert 0
        self.txtHeightFT.delete(0, END)
        self.txtHeightFT.insert(0, "0")

        self.txtHeightIN.delete(0, END)
        self.txtHeightIN.insert(0, "0")

        self.txtWeight.delete(0, END)
        self.txtWeight.insert(0, "0")

        #clear BMI and status boxes
        self.lblBMI["text"] = ""
        self.lblStatus["text"] = ""


    def close(self):
        """add exit button"""
        #destroy yourself
        self.destroy()

        
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
