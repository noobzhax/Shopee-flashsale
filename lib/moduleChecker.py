import importlib.util, sys, subprocess, json, os

def clearConsole():
    command = 'cls' if os.name in {'nt', 'dos'} else 'clear'
    os.system(command)

def readFileJson(file):
    with open(file, 'r') as f:
        data = json.loads(f.read())
    return data

def writeFileJson(obj, file):
    jsonObj = json.dumps(obj, indent = 4)
    
    with open("sample.json", "w") as outfile:
        outfile.write(jsonObj)

def checkModules(name):
    if name in sys.modules:
        print(f"{name!r} Berhasil Terpasang ✔️")
    elif (spec := importlib.util.find_spec(name)) is not None:
        # If you choose to perform the actual import ...
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        print(f"{name!r} Install Berhasil ✔️")
    else:
        print(f"{name!r} Tidak Ada, Installer Packing ⚠️")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])


        
        
