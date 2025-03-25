import json
# from datetime import datetime, timedelta
from datetime import datetime
import os
import sys
import imp
import traceback
path = os.path.dirname(os.path.abspath(__file__))  + '/main.py'
main = imp.load_source('', path)
sys.path.insert(0, '/opt/linkprocess/')

plugin_folder_name =  "github_ddr_1730963632_general"
plugin_name = "github_ddr_1730963632"
from github_plugin import Plugin
commonFunction_obj = Plugin(plugin_folder_name)

dirname, filename = os.path.split(os.path.abspath(__file__))
statsPath = str(dirname + '/stats.json')

def read_file(path):
    data = ''
    if os.path.isfile(path):
        with open(path, "r") as file:
            data = file.read()
    return data

def read_json(path):
    data = {}
    if os.path.isfile(path):
        with open(path) as f:
            try:
                data = json.load(f)
            except:
                pass
    return data

def write_json(path, data):
    if os.path.isfile(path):
        with open(path, 'w') as json_file:
            json.dump(data, json_file)

def plugin_actions(data):
    if data.get('action') and data.get('action') == 'testconnection':
        res = main.test_connection(data)
        return res
    elif data.get('action') == 'saveCustomSettings':
        res_  = main.saveCustomSettings(data)
        return res_ 
    elif data.get('action') and data.get('action') == 'getCustomPluginSettings':
        res = main.getPluginSettings(data) 
        return res
    elif data.get('action') == 'saveCustomData':
        res = main.saveCustomData(data)
        return res 
    elif data.get('action') and data.get('action') == 'deleteSettings':
        res = main.deleteSettings(data)
        return res
    elif  data.get('action') == 'deleteFiles':
        res = main.deleteFiles(data)
        return res 

def initiate():
    try:
        main.main()
        status_json = read_json(statsPath)
        status_json["lastCronRuntime"] = str(datetime.now())
        write_json(statsPath, status_json)
        print ("completed everything, including updating last cron runtime") 
    except Exception as ex:
        print(traceback.format_exc())
        print(ex)

if __name__ == "__main__": 
    initiate()
    