import os  
import sys  
import subprocess  
import ssl  
import urllib3  
import requests  
from urllib3.exceptions import InsecureRequestWarning  

class SmartPipInstaller:  
    def __init__(self):  
        self.proxy = "http://127.0.0.1:7890"  # 修改为您的代理地址  
        self.sources = {  
            'direct': [  
                'https://mirrors.aliyun.com/pypi/simple/',  
                'https://pypi.doubanio.com/simple/',  
                'https://pypi.mirrors.ustc.edu.cn/simple/',  
                'https://mirrors.cloud.tencent.com/pypi/simple/'  
            ],  
            'proxy': [  
                'https://pypi.org/simple/',  
                'https://python.cloudsmith.io/simple/',  
                'https://us-python.pkg.dev/python/pypi/simple/'  
            ]  
        }  
        
    def setup_ssl_context(self):  
        """配置SSL上下文"""  
        context = ssl.create_default_context()  
        context.check_hostname = False  
        context.verify_mode = ssl.CERT_NONE  
        return context  
    
    def install_package(self, package_name):  
        """智能安装包"""  
        # 首先尝试国内源  
        print(f"尝试使用国内源安装 {package_name}...")  
        for source in self.sources['direct']:  
            try:  
                result = subprocess.run([  
                    sys.executable, '-m', 'pip', 'install',  
                    '--index-url', source,  
                    '--trusted-host', urllib3.util.parse_url(source).host,  
                    package_name  
                ], capture_output=True, text=True)  
                
                if result.returncode == 0:  
                    print(f"成功从 {source} 安装!")  
                    return True  
            except Exception as e:  
                print(f"从 {source} 安装失败: {str(e)}")  
        
        # 如果国内源失败，尝试使用代理和国外源  
        print("\n尝试使用代理和国外源...")  
        os.environ['HTTP_PROXY'] = self.proxy  
        os.environ['HTTPS_PROXY'] = self.proxy  
        
        for source in self.sources['proxy']:  
            try:  
                result = subprocess.run([  
                    sys.executable, '-m', 'pip', 'install',  
                    '--index-url', source,  
                    '--trusted-host', urllib3.util.parse_url(source).host,  
                    '--cert', None,  # 禁用证书验证  
                    package_name  
                ], capture_output=True, text=True)  
                
                if result.returncode == 0:  
                    print(f"成功从 {source} 安装!")  
                    return True  
            except Exception as e:  
                print(f"从 {source} 安装失败: {str(e)}")  
        
        return False  

def main():  
    if len(sys.argv) < 2:  
        print("使用方法: python smart_pip_install.py package_name")  
        sys.exit(1)  
    
    package_name = sys.argv[1]  
    installer = SmartPipInstaller()  
    
    # 禁用SSL警告  
    urllib3.disable_warnings(InsecureRequestWarning)  
    
    if installer.install_package(package_name):  
        print(f"\n成功安装 {package_name}!")  
    else:  
        print(f"\n安装 {package_name} 失败。")  
        sys.exit(1)  

if __name__ == "__main__":  
    main()