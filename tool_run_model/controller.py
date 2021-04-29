from data_access import *
from variable import *
import shutil, os, subprocess
from datetime import datetime
def excute_code(file_path, language, code_test_name_file, code_train_name_file, input_file, output_file):
    try:
        os.chdir(file_path)
        # Load result
        data_output = open(os.path.join(file_path, output_file), 'r').readlines()
        data_output = [x.replace("\n","").strip() for x in data_output if x != "" or x != None]
        # Load input
        data_input = open(os.path.join(file_path, input_file), 'r').readlines()
        data_input = [x.replace("\n","").strip() for x in input_file if x != "" or x != None]
        # excute
        if language == "python2":
            count = 0
            list_test = []
            for inp, out in tuple(zip(data_input, data_output)):
                test_info = {}
                ttime = datetime.now().timestamp()
                output_test = subprocess.run(["python", code_test_name_file], stdout = subprocess.PIPE, text=True, input=inp)
                ttime = datetime.now().timestamp() - ttime
                test_info["time_excute"] = str(ttime)
                if str(out) == str(output_test.stdout).replace("\n","").strip():
                    test_info["status"] = True
                    count += 1
                else:
                    test_info["status"] = False
                list_test.append(test_info)
            print(list_test)
            accuracy = round(float(count/len(data_output)), 5)
            return (accuracy, list_test)
        elif language == "python3":
            count = 0
            list_test = []
            for inp, out in tuple(zip(data_input, data_output)):
                test_info = {}
                ttime = datetime.now().timestamp()
                output_test = subprocess.run([PYTHON3_VENV, code_test_name_file], stdout = subprocess.PIPE, text=True, input=inp)
                ttime = datetime.now().timestamp() - ttime
                test_info["time_excute"] = str(ttime)
                if str(out) == str(output_test.stdout).replace("\n","").strip():
                    test_info["status"] = True
                    count += 1
                else:
                    test_info["status"] = False
                list_test.append(test_info)
            print(list_test)
            accuracy = round(float(count/len(data_output)), 5)
            return (accuracy, list_test)
        elif language == "c++":
            count = 0
            list_test = []
            for inp, out in tuple(zip(data_input, data_output)):
                test_info = {}
                ttime = datetime.now().timestamp()
                output_test = subprocess.run(["g++", code_test_name_file], stdout = subprocess.PIPE, text=True, input=inp)
                ttime = datetime.now().timestamp() - ttime
                test_info["time_excute"] = str(ttime)
                if str(out) == str(output_test.stdout).replace("\n","").strip():
                    test_info["status"] = True
                    count += 1
                else:
                    test_info["status"] = False
                list_test.append(test_info)
            print(list_test)
            accuracy = round(float(count/len(data_output)), 5)
            return (accuracy, list_test)
        
        elif language == "javascript":
            count = 0
            list_test = []
            for inp, out in tuple(zip(data_input, data_output)):
                test_info = {}
                ttime = datetime.now().timestamp()
                output_test = subprocess.run(["node", code_test_name_file], stdout = subprocess.PIPE, text=True, input=inp)
                ttime = datetime.now().timestamp() - ttime
                test_info["time_excute"] = str(ttime)
                if str(out) == str(output_test.stdout):
                    test_info["status"] = True
                    count += 1
                else:
                    test_info["status"] = False
                list_test.append(test_info)
            print(list_test)
            accuracy = round(float(count/len(data_output)), 5)
            return (accuracy, list_test)
    except Exception as exc:
        print("Error in excute code: %s" % str(exc))
    return (None, None)
    
def process_result():
    db = DataBase()
    result = db.get_result()
    result["status"] = "I"
    db.update_result(result)
    language = db.get_language(str(result["language_id"]))
    result["accuracy"] = excute_code(result["path_code"], language, result["code_test"], result["code_train"], "input.csv", "output.csv")
    result["status"] = "S"
    db.update_result(result)

process_result()