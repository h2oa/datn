from pymetasploit3.msfrpc import MsfRpcClient
from package.arguments import *
from package.functions import *

if args.search:
    search_keyword = args.search
    search_module(search_keyword)

if args.infor:
    module_name = {}
    parts = args.infor.split('/', 1)
    module_name['type'] = parts[0]
    module_name['module_name'] = parts[1]
    infor_module(module_name)

if args.portscan:
    port_scan()

if args.d2ip:
    domain = args.d2ip
    print(ip_from_domain(domain))

def main():
    # domain = "testphp.vulnweb.com"
    # # webserver_testing_list = ["http_version", "tomcat_administration", "tomcat_utf8_traversal", "drupal_views_user_enum", "frontpage_login", "host_header_injection", "options", "robots_txt", "scraper", "svn_scanner", "trace", "vhost_scanner", "webdav_internal_ip", "webdav_scanner", "webdav_website_content"]
    # # for module in webserver_testing_list:
    # #     webserver_testing(domain, module)
    
    # file_dir_testing_list = ["backup_file", "brute_dirs", "copy_of_file", "dir_listing", "dir_scanner", "dir_webdav_unicode_bypass", "file_same_name_dir", "files_dir", "http_put", "ms09_020_webdav_unicode_bypass", "prev_dir_same_name_file", "replace_ext", "soap_xml", "trace_axd", "verb_auth_bypass"]
    # for module in file_dir_testing_list:
    #     file_dir_testing(domain, module)
    domain = "192.168.81.130"
    # load information of vul for result
    infor_data = information_load()

    # # wordpress scan
    # wp(domain)

    # # joomla scan
    # joomla(domain)
    
    # custom scan
    custom(domain)

main()