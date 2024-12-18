import customtkinter as ctk
from PIL import ImageTk, Image

class loginWindow(ctk.CTk):
    
    
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('system')
        ctk.set_default_color_theme('green')
        
        # Login Authentication
        def login_auth(user_id, user_pass):
            pass
        
        def register(name, email, user_id, user_pass):
            pass

        self.geometry("900x700")
        self.title("Login Page")
        
        self.resizable(width=False, height=False)
        
        # Create Background
        img_bg = ImageTk.PhotoImage(Image.open("./financial_program/assets/img_bg.jpg"))
        login_bg = ctk.CTkLabel(self, text="", image=img_bg)
        login_bg.pack()

        # Create Frame for Input Field
        frame_login = ctk.CTkFrame(self, 
                           height=500, 
                           width=400,
                           fg_color='#3E5879')
        frame_login.place(relx =0.5, rely =0.5, anchor='center')

        # Create Frame Title
        title = ctk.CTkLabel(frame_login, 
                             bg_color='transparent', 
                             text='WELCOME!! \n\nPLEASE LOGIN TO YOUR ACCOUNT', 
                             font=('Century Schoolbook', 18, 'bold'), 
                             text_color='#F5EFE7')
        title.place(x=25, y=70)

        # Create Username Entry
        user_field = ctk.CTkEntry(frame_login,
                                width=300, 
                                height=45, 
                                placeholder_text='Username',
                                font=('Century SchoolBook', 13, 'bold'),
                                text_color='#213555',
                                corner_radius=20,
                                placeholder_text_color='#213555',
                                fg_color='#D8C4B6')
        user_field.place(x=50, y=150)
        
if __name__ == '__main__':
    app = loginWindow()
    app.mainloop()