 import time

import psutil


def collect_metrics():

    print("--- Agent de Monitorizare DevOps Pornit ---")

    try:

        while True:

            cpu = psutil.cpu_percent(interval=1)

            ram = psutil.virtual_memory().percent

            print(f"[METRICI] CPU: {cpu}% | RAM: {ram}%")

            time.sleep(4)

    except KeyboardInterrupt:

        print("\nAgent oprit.")



if __name__ == "__main__":

    co

llect_metrics()

