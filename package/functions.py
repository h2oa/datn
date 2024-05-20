from pymetasploit3.msfrpc import MsfRpcClient
import time
import re
import json
from colorama import Fore

client = MsfRpcClient(password = 'password', ssl = False, server = '192.168.81.130', port = 55553) # máy nhà
# client = MsfRpcClient(password='password', ssl=False, server='192.168.142.128', port=55553) # công ty

def information_load():
    with open('./information/info.json', 'r') as file:
        return(json.load(file))

def setRHOSTS(module, domain):
    module["RHOSTS"] = domain

# Search module from keyword
def search_module(keyword):
    search_result = client.modules.search(keyword)
    # return search_result
    for module in search_result:
        print(module)

# Information of the module
def infor_module(module_name):
    module = module_name['type'] + '/' + module_name['module_name']
    infors = client.modules.use(module_name['type'], module_name['module_name'])
    # print(dir(infors))
    print("-------------------------------")
    print("Module: %s" % module)
    print("-------------------------------")
    print("Description:\n\n%s" % str(infors.description))
    print("-------------------------------")
    print("Options:\n\n%s" % str(infors.options))
    print("-------------------------------")
    print("Required:\n\n%s" % str(infors.required))
    print("-------------------------------")
    print("Missing required:\n\n%s" % str(infors.missing_required))
    print("-------------------------------")

def port_scan():
    service = "auxiliary/scanner/portscan/syn"
    port_scan = client.modules.use("auxiliary", "scanner/portscan/syn")
    # print(dir(port_scan))
    print(port_scan.missing_required)
    # # Check if the module can be run
    # print("Check: %s" % port_scan.check().get('status'))
    missings = []
    for missing in port_scan.missing_required:
        print("Nhập vào giá trị %s: " % missing)
        port_scan[missing] = input()
        missings.append(port_scan[missing])
    print("Tất cả giá trị missing required đã nhập: %s" % missings)
    # # Recheck if the module can be run
    # print("Check: %s" % port_scan.check().get('status'))
    port_scan["PORTS"] = "8079-8083"
    print("Start port scanning ...")
    print(dir(port_scan))
    print("-----------------")
    print(port_scan.runoptions)
    # Scan result
    # scan_results = client.jobs.list[service] if service in client.jobs.list else None
    # print(scan_results)

# Get IP from domain (input from user)
def ip_from_domain(domain):
    command = "host " + domain
    cid = client.consoles.console().cid
    client.consoles.console(cid).write(command)
    time.sleep(2)
    output = client.consoles.console(cid).read()
    regex = r'(\b\w+\.\w+\s+has\s+address\s+\d+\.\d+\.\d+\.\d+\b)'
    match = re.search(regex, output['data'])
    # regex = r'(\b\d+\.\d+\.\d+\.\d+\b)'
    # match = re.search(regex, match1.group(0))
    return match.group(0).split(" ")[3]

def webserver_testing(domain, module_name):
    module_name = "auxiliary/scanner/http/" + module_name
    console_id = client.consoles.console().cid
    command = f"use {module_name}\nset RHOSTS {domain}\nrun"
    client.consoles.console(console_id).write(command)
    time.sleep(5)
    result = client.consoles.console(console_id).read()
    print(result['data'])
    client.consoles.console(console_id).destroy()

def file_dir_testing(domain, module_name):
    module_name = "auxiliary/scanner/http/" + module_name
    console_id = client.consoles.console().cid
    command = f"use {module_name}\nset RHOSTS {domain}\nrun"
    client.consoles.console(console_id).write(command)
    time.sleep(5)
    result = client.consoles.console(console_id).read()
    print(result["data"])
    client.consoles.console(console_id).destroy()

# cần bổ sung phần port
# wordpress check
def wordpress_check(domain):
    check = False
    module_name = "auxiliary/scanner/http/wordpress_scanner"
    console_id = client.consoles.console().cid
    command = f"use {module_name}\nset RHOSTS {domain}\nrun"
    client.consoles.console(console_id).write(command)
    while True:
        time.sleep(3)
        result = client.consoles.console(console_id).read()
        if "Auxiliary module execution completed" in result["data"]:
            # print(result["data"])
            if "Detected Wordpress" in result["data"]:
                regex = r'(Detected Wordpress \d+\.\d+(\.\d+)?)'
                match = re.search(regex, result["data"])
                print(match.group(0))
                check = True
        break
    client.consoles.console(console_id).destroy()
    if check == True:
        return True
    else:
        return False

# cần bổ sung phần port
# --> cần khởi động postgresql trước
# root@kali:~# service postgresql start
# root@kali:~# msfdb init
# root@kali:~# msfdb start
def wmap(domain):
    console_id = client.consoles.console().cid
    # Load wmap --> Add site --> Add target --> Attack
    command = f"load wmap\nwmap_sites -a {domain}\nwmap_targets -t {domain}\nwmap_run -e"
    console_id = client.consoles.console().cid
    client.consoles.console(console_id).write(command)
    while True:
        time.sleep(5)
        result = client.consoles.console(console_id).read()
        print(result["data"])
        if "[*] Done." in result["data"]:
            print(result["data"])
            break
    client.consoles.console(console_id).destroy()
    # In kết quả
    command = "vulns"
    console_id = client.consoles.console().cid
    client.consoles.console(console_id).write(command)
    time.sleep(5)
    result = client.consoles.console(console_id).read()
    print(result["data"])
    client.consoles.console(console_id).destroy()

# cần bổ sung phần port
# joomla check
def joomla_check(domain):
    check = False
    module_name = "auxiliary/scanner/http/joomla_version"
    console_id = client.consoles.console().cid
    command = f"use {module_name}\nset RHOSTS {domain}\nrun"
    client.consoles.console(console_id).write(command)
    while True:
        time.sleep(3)
        result = client.consoles.console(console_id).read()
        if "Auxiliary module execution completed" in result["data"]:
            # print(result["data"])
            if "Joomla version" in result["data"]:
                regex = r'(Joomla version\: \d+\.\d+(\.\d+)?)'
                match = re.search(regex, result["data"])
                print(match.group(0))
                check = True
        break
    client.consoles.console(console_id).destroy()
    if check == True:
        return True
    else:
        return False

# Joomla scan
def joomla_scan(domain):
    # 'auxiliary/scanner/http/joomla_bruteforce_login'
    # 'auxiliary/scanner/http/joomla_plugins'
    joomla_auxiliary_modules = ['auxiliary/scanner/http/joomla_gallerywd_sqli_scanner','auxiliary/admin/http/joomla_registration_privesc','auxiliary/scanner/http/joomla_pages','auxiliary/gather/joomla_com_realestatemanager_sqli','auxiliary/gather/joomla_contenthistory_sqli','auxiliary/gather/joomla_weblinks_sqli','auxiliary/scanner/http/joomla_ecommercewd_sqli_scanner']
    for joomla_module in joomla_auxiliary_modules:
        print("[*] Module: " + joomla_module)
        console_id = client.consoles.console().cid
        command = f"use {joomla_module}\nset RHOSTS {domain}\nrun"
        client.consoles.console(console_id).write(command)
        while True:
            time.sleep(5)
            result = client.consoles.console(console_id).read()
            if "Auxiliary module execution completed" in result["data"]:
                # print(result["data"])
                regex = r'(RHOSTS =>(.*\n)*\[\*] Auxiliary module execution completed)'
                match = re.search(regex, result["data"])
                print(match.group(0))
                break
        client.consoles.console(console_id).destroy()

# custom scan (includes custom modules)
def custom_scan(domain, infor_data):
    target = domain
    print("Start Custom checking ...")
    # 'auxiliary/customs/Joomla_CVE-2015-8562', 'auxiliary/customs/Joomla_CVE-2017-8917', 'auxiliary/customs/Joomla_CVE-2023-23752'
    modules = ['auxiliary/scanner/http/robots_txt', 'auxiliary/customs/git_expose', 'auxiliary/customs/admin_expose', 'auxiliary/customs/phpinfo_expose', 'auxiliary/customs/htaccess_expose', 'auxiliary/gather/coldfusion_pwd_props', 'auxiliary/customs/solr_endpoint']
    # for testing 
    modules = ['auxiliary/customs/admin_expose']
    vuls = []
    responses = []
    for module in modules:
        time.sleep(3)
        print(Fore.WHITE + "================================================================")
        print(Fore.GREEN + "Module: " + module)
        print(Fore.WHITE + "================================================================")
        console_id = client.consoles.console().cid
        command = f"use {module}\nset RHOSTS {domain}\nrun"
        client.consoles.console(console_id).write(command)
        while True:
            print("sleep 3")
            time.sleep(3)
            result = client.consoles.console(console_id).read()
            if "Auxiliary module execution completed" in result["data"]:
                # print(result["data"])
                regex = r'(RHOSTS =>(.*\n)*\[\*] Auxiliary module execution completed)'
                match = re.search(regex, result["data"])
                print(match.group(0))
                if "[+]" in result["data"]:
                    # print(Fore.RED + infor_data[module])
                    regex = r'(===Response start===(.*\n)*===Response end===)'
                    match = re.search(regex, result["data"])
                    # value insert to database if have bug
                    response = match.group(0).split('===')[2]
                    print(Fore.RED + "--------Result--------")
                    print(Fore.RED + "Target: " + target)
                    print(Fore.RED + "Module: " + module)
                    print(Fore.RED + "Response: " + response)
                    
                    # insert to database
                    ###
                    # vuls.append(module)
                    # with open("/tmp/response.txt", "r") as f:
                    #     data = f.read()
                    #     responses.append(data)
                    #####
                    # command_read = "cat /tmp/response.txt"
                    # client.consoles.console(console_id).write(command_read)
                    # result = client.consoles.console(console_id).read()
                    # print(result["data"])
                break
        client.consoles.console(console_id).destroy()

# wp scan
def wp(domain):
    time.sleep(1)
    wp_check = wordpress_check(domain)
    if wp_check:
        print("CMS Wordpress detected! Start scanning ...")
        wmap(domain)
    else:
        print("The target domain is not using CMS Wordpress")

# joomla scan
def joomla(domain):
    time.sleep(1)
    jm_check = joomla_check(domain)
    if jm_check:
        print("CMS Joomla detected! Start scanning ...")
        joomla_scan(domain)
    else:
        print("The target domain is not using CMS Joomla")

# custom scan
def custom(domain):
    time.sleep(1)
    infor_data = information_load()
    # domain = "172.26.3.142"
    custom_scan(domain, infor_data)