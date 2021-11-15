import tkinter as tk
import main as m

def ytdGui():
    def downloader():
        print(url.get())
        print(rute.get())
        root.destroy()

    root = tk.Tk()
    root.title('ytDownloader')
    root.minsize(400, 100)
    root.maxsize(400, 100)
    
    url = tk.StringVar()
    rute = tk.StringVar()
    
    label_url = tk.Label(root, text="URL:").grid(pady=5, row=0, column=0)
    label_rute = tk.Label(root, text="Ruta:").grid(pady=5, row=1, column=0)

    insert_url = tk.Entry(root, width=40,textvariable=url).grid(padx=5, row=0, column=1)
    insert_rute = tk.Entry(root, width=40,textvariable=rute).grid(padx=5, row=1, column=1)

    button_download = tk.Button(root, text="Descargar",command=downloader, width=50).grid(
        padx=10, pady=10, row=2, column=0, columnspan=2)


    root.mainloop()

if __name__ == "__main__":
    ytdGui()