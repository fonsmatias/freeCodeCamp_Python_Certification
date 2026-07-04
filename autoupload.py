import subprocess
import os
from datetime import datetime

# 1. Configura la ruta de la carpeta donde está tu archivo .git
CARPETA_REPO = r"C:\Users\matia\Desktop\fCC" 

def automatizar_git():
    try:
        # Cambiamos el directorio de trabajo de Python a la carpeta del repositorio
        os.chdir(CARPETA_REPO)
        
        # Generamos un mensaje de commit automático con la fecha y hora de hoy
        fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M")
        mensaje_commit = f"automatic update fCC proyects - {fecha_hoy}"
        
        print(f"Iniciando subida automática: {fecha_hoy}")
        
        # 2. EJECUTAR LOS COMANDOS DE GIT BASH
        # 2.a. git add .
        subprocess.run(["git", "add", "."], check=True) # con check true, si hay un error se lanza una excepción

        # 2.b. git commit -m "mensaje"
        subprocess.run(["git", "commit", "-m", mensaje_commit], check=True)
        
        # 2.c. git push origin main (cambiá 'main' por 'master' si tu rama se llama así)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print("¡Subida a GitHub completada con éxito!")
        
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar comando de Git: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    automatizar_git()