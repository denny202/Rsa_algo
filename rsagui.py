import tkinter as tk
import customtkinter as ctk
from mrsa import RSA_Algo

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#class inherits ctk and the rsa class
class Guiapp(ctk.CTk,RSA_Algo):
    
    cypher=1
    
#Constructor 
    def __init__(self):
        super().__init__()
        

        # configure window
        self.title("RSA Algorithms")
        self.geometry("400x240")
        
        #create p label and place 
        self.pl = ctk.CTkLabel(self,text = "Enter p  ")
        self.pl.place(relx=0.4, rely=0.1, anchor=tk.CENTER)


        #create input textbox area and place 
        self.ptxt= ctk.CTkTextbox(self, height = 5,width = 50)
        self.ptxt.place(relx=0.4, rely=0.22, anchor=tk.CENTER)

        # #create q label 
        self.ql = ctk.CTkLabel(self,text = "Enter q  ")
        self.ql.place(relx=0.6, rely=0.1, anchor=tk.CENTER)
       
        #create input textbox area and place 
        self.qtxt= ctk.CTkTextbox(self,height = 5,width = 50)
        self.qtxt.place(relx=0.6, rely=0.22, anchor=tk.CENTER)
        
        #label text above buttons
        self.ml = ctk.CTkLabel(self,text = "Enter Text to encrypt o decrypt ")
        self.ml.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        #Input textbox for message or ciphertext to encrypt and decrypt
        self.mtext= ctk.CTkTextbox(self,height = 5,width = 120)
        self.mtext.place(relx=0.5, rely=0.47, anchor=tk.CENTER)

        # # Create button and pass function to perform the encryption
        self.button = ctk.CTkButton(self, text="Encrypt", command=self.display_result_encryption)
        self.button.place(relx=0.3, rely=0.62, anchor=tk.CENTER)
        
        # # Create button and pass function to perform the decryption
        self.button = ctk.CTkButton(self, text="Decrypt", command=self.display_result_decryption)
        self.button.place(relx=0.7, rely=0.62, anchor=tk.CENTER)
        
        # #Create label where rsesult will be showing
        self.ll=ctk.CTkLabel(self,text="Result : ")
        self.ll.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    

    def display_result_encryption(self):
        inputp = self.ptxt.get("1.0", "end-1c")
        inputq = self.qtxt.get("1.0", "end-1c")
        inputm = self.mtext.get("1.0", "end-1c")
        global en
        en=RSA_Algo(int(inputp),int(inputq),int(inputm))
        cypher=en.encrypt()
        cypher=str(cypher)
        
        self.ll.configure(text="Result : "+cypher)
        

    def display_result_decryption(self,):
        inputp = self.ptxt.get("1.0", "end-1c")
        inputq = self.qtxt.get("1.0", "end-1c")
        inputm = self.mtext.get("1.0", "end-1c")
        message=en.decrypt()
        message=str(message)
        
        self.ll.configure(text="Result : "+message)


#Main Function        
if __name__ == "__main__":
    
    rsapp=Guiapp()
    rsapp.mainloop()

