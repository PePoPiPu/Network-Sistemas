import os, subprocess, json

def comprobar_estado_ip(ip):
    try:
        # Run the ping command with a timeout of 1 second
        subprocess.run(["ping", "-c", "1", "-W", "1", ip], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # -c: Le dice a ping que envía solo un paquete ICMP
        # -W: Le pone un límite de tiempo de un segundo a ping. Si no se recibe nada se considera que se ha perdido el paquete
        return True  # Si el comando es exitoso, la IP está activa
    except subprocess.CalledProcessError:
        return False  # Si el comando no es exitoso, la IP no está activa

def analizar_red(inicio_i, fin_i, inicio_j, fin_j):
    resultados = {}
    for i in range(inicio_i, fin_i + 1):
        for j in range(inicio_j, fin_j + 1):
            ip = f"192.168.{i}.{j}"
            estado = comprobar_estado_ip(ip)
            if estado:
                print(f"IP activa encontrada: {ip}")
            resultados[ip] = estado;
    return resultados

def escribir_json_activas(resultados, directory="../NetInsightWeb", filename="ips_activas.json"):
    ips_activas = [{"activa": ip} for ip, status in resultados.items() if status]
    filepath = os.path.join(directory, filename)

    with open(filepath, "w") as json_file:
        json.dump({"activas": ips_activas}, json_file, indent=2)

def imprimir_logo():
    logo = """
NNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTTTTT     IIIIIIIIIINNNNNNNN        NNNNNNNN   SSSSSSSSSSSSSSS IIIIIIIIII      GGGGGGGGGGGGGHHHHHHHHH     HHHHHHHHHTTTTTTTTTTTTTTTTTTTTTTT
N:::::::N       N::::::NE::::::::::::::::::::ET:::::::::::::::::::::T     I::::::::IN:::::::N       N::::::N SS:::::::::::::::SI::::::::I   GGG::::::::::::GH:::::::H     H:::::::HT:::::::::::::::::::::T
N::::::::N      N::::::NE::::::::::::::::::::ET:::::::::::::::::::::T     I::::::::IN::::::::N      N::::::NS:::::SSSSSS::::::SI::::::::I GG:::::::::::::::GH:::::::H     H:::::::HT:::::::::::::::::::::T
N:::::::::N     N::::::NEE::::::EEEEEEEEE::::ET:::::TT:::::::TT:::::T     II::::::IIN:::::::::N     N::::::NS:::::S     SSSSSSSII::::::IIG:::::GGGGGGGG::::GHH::::::H     H::::::HHT:::::TT:::::::TT:::::T
N::::::::::N    N::::::N  E:::::E       EEEEEETTTTTT  T:::::T  TTTTTT       I::::I  N::::::::::N    N::::::NS:::::S              I::::I G:::::G       GGGGGG  H:::::H     H:::::H  TTTTTT  T:::::T  TTTTTT
N:::::::::::N   N::::::N  E:::::E                     T:::::T               I::::I  N:::::::::::N   N::::::NS:::::S              I::::IG:::::G                H:::::H     H:::::H          T:::::T        
N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE           T:::::T               I::::I  N:::::::N::::N  N::::::N S::::SSSS           I::::IG:::::G                H::::::HHHHH::::::H          T:::::T        
N::::::N N::::N N::::::N  E:::::::::::::::E           T:::::T               I::::I  N::::::N N::::N N::::::N  SS::::::SSSSS      I::::IG:::::G    GGGGGGGGGG  H:::::::::::::::::H          T:::::T        
N::::::N  N::::N:::::::N  E:::::::::::::::E           T:::::T               I::::I  N::::::N  N::::N:::::::N    SSS::::::::SS    I::::IG:::::G    G::::::::G  H:::::::::::::::::H          T:::::T        
N::::::N   N:::::::::::N  E::::::EEEEEEEEEE           T:::::T               I::::I  N::::::N   N:::::::::::N       SSSSSS::::S   I::::IG:::::G    GGGGG::::G  H::::::HHHHH::::::H          T:::::T        
N::::::N    N::::::::::N  E:::::E                     T:::::T               I::::I  N::::::N    N::::::::::N            S:::::S  I::::IG:::::G        G::::G  H:::::H     H:::::H          T:::::T        
N::::::N     N:::::::::N  E:::::E       EEEEEE        T:::::T               I::::I  N::::::N     N:::::::::N            S:::::S  I::::I G:::::G       G::::G  H:::::H     H:::::H          T:::::T        
N::::::N      N::::::::NEE::::::EEEEEEEE:::::E      TT:::::::TT           II::::::IIN::::::N      N::::::::NSSSSSSS     S:::::SII::::::IIG:::::GGGGGGGG::::GHH::::::H     H::::::HH      TT:::::::TT      
N::::::N       N:::::::NE::::::::::::::::::::E      T:::::::::T           I::::::::IN::::::N       N:::::::NS::::::SSSSSS:::::SI::::::::I GG:::::::::::::::GH:::::::H     H:::::::H      T:::::::::T      
N::::::N        N::::::NE::::::::::::::::::::E      T:::::::::T           I::::::::IN::::::N        N::::::NS:::::::::::::::SS I::::::::I   GGG::::::GGG:::GH:::::::H     H:::::::H      T:::::::::T      
NNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEE      TTTTTTTTTTT           IIIIIIIIIINNNNNNNN         NNNNNNN SSSSSSSSSSSSSSS   IIIIIIIIII      GGGGGG   GGGGHHHHHHHHH     HHHHHHHHH      TTTTTTTTTTT                                                                                                                                                        
    """
    print(logo)


def main():
    imprimir_logo()
    print("Bienvenido al Analizador de Red")

    inicio_i = int(input("Ingrese el valor de inicio para el primer octeto: "))
    fin_i = int(input("Ingrese el valor de final para el primer octeto: "))
    inicio_j = int(input("Ingrese el valor de inicio para el segundo octeto: "))
    fin_j = int(input("Ingrese el valor de final para el segundo octeto: "))

    print("\nAnalizando la red...\n")

    resultados = analizar_red(inicio_i, fin_i, inicio_j, fin_j)

    escribir_json_activas(resultados)
    print("\nIPs activas guardadas en ips_activas.json.")

    print("\nAnálisis completo.")

if __name__ == "__main__":
    main()