# 常用的PyPI源地址
```python
# 中国科技大学源  
https://pypi.mirrors.ustc.edu.cn/simple/  

# 华为云源  
https://repo.huaweicloud.com/repository/pypi/simple/  

# 网易源  
https://mirrors.163.com/pypi/simple/  

# 腾讯云源  
https://mirrors.cloud.tencent.com/pypi/simple/

# 阿里源
https://mirrors.aliyun.com/pypi/simple/


# 豆瓣源
https://pypi.doubanio.com/simple/

# 清华源
https://pypi.tuna.tsinghua.edu.cn/simple/
```




### 使用 pip config list 命令
```bash
pip config list
```
这个命令会显示所有当前生效的配置，包括配置文件的位置和具体的配置项。


### 使用 pip config debug 命令
这个命令会显示更详细的配置信息，包括配置文件的位置和加载顺序：
```bash
pip config debug  
```

### 查看特定配置文件的内容
如果您想查看具体配置文件的内容：

```bash
# Windows CMD  
type %APPDATA%\pip\pip.ini
```

```bash
# Windows PowerShell  
Get-Content $env:APPDATA\pip\pip.ini
```

### 使用 pip debug 命令
这个命令会显示更多系统信息和调试信息：

```bash
pip debug
```

### 查看单个命令的详细执行过程
如果您想查看pip在执行特定命令时使用的配置：

```bash
# 使用 -v 参数查看详细信息  
pip install -v package_name  

# 使用 -vv 查看更详细的信息  
pip install -vv package_name  

# 使用 -vvv 查看最详细的调试信息  
pip install -vvv package_name  
```



### Python代码查看pip配置
```python
import os  
import site  
import pip  
from pip._internal.configuration import Configuration  
from pip._internal.locations import site_config_files, user_config_file  

def show_pip_config():  
    """显示所有pip配置信息"""  
    print("="*50)  
    print("PIP 配置信息")  
    print("="*50)  
    
    # 1. 显示配置文件位置  
    print("\n1. 配置文件位置:")  
    print(f"用户配置文件: {user_config_file}")  
    print("全局配置文件:", site_config_files)  
    
    # 2. 显示当前配置  
    print("\n2. 当前生效的配置:")  
    config = Configuration(isolated=False)  
    config.load()  
    
    for key, value in config.items():  
        print(f"{key} = {value}")  
    
    # 3. 显示环境变量中的pip配置  
    print("\n3. 环境变量中的PIP配置:")  
    pip_env_vars = [var for var in os.environ if var.startswith('PIP_')]  
    for var in pip_env_vars:  
        print(f"{var} = {os.environ[var]}")  
    
    # 4. 显示Python/pip版本信息  
    print("\n4. 版本信息:")  
    import sys  
    print(f"Python 版本: {sys.version}")  
    print(f"Pip 版本: {pip.__version__}")  
    
    # 5. 显示安装路径信息  
    print("\n5. 安装路径信息:")  
    print(f"用户site-packages: {site.getusersitepackages()}")  
    print("全局site-packages:", site.getsitepackages())  

if __name__ == "__main__":  
    show_pip_config()
```


### 常见配置项说明
```ini
[global]  
# 主包源  
index-url = https://pypi.org/simple  

# 额外包源  
extra-index-url = https://other-index.org/simple  

# 信任的主机  
trusted-host = pypi.org  

# 超时设置（秒）  
timeout = 60  

# 缓存目录  
cache-dir = ~/.cache/pip  

# 是否使用缓存  
no-cache-dir = false  

# 代理设置  
proxy = http://user:password@proxy.server:8080  

# 重试次数  
retries = 5  

# 是否需要验证HTTPS  
verify = true
```


### 配置项优先级
当您查看配置时，需要注意pip配置的优先级（从高到低）：

命令行选项（如 --index-url）
环境变量（如 PIP_INDEX_URL）
用户配置文件（pip.ini 或 pip.conf）
全局配置文件


### 常见问题解决
如果您在查看配置时遇到问题：

配置文件不存在

```bash
# 创建配置文件  
mkdir %APPDATA%\pip  
echo [global] > %APPDATA%\pip\pip.ini
```
查看是否有环境变量覆盖

```bash
# Windows  
set | findstr PIP_

# PowerShell  
Get-ChildItem env: | Where-Object { $_.Name -like "PIP_*" }
```
检查配置文件权限

```bash
# Windows  
icacls %APPDATA%\pip\pip.ini  
```


### 添加新源
```ini

[global]  
# 主源（第一优先级）  
index-url = https://pypi.tuna.tsinghua.edu.cn/simple  

# 额外源（按顺序依次查找）  
extra-index-url =   
    https://mirrors.aliyun.com/pypi/simple/  
    https://pypi.doubanio.com/simple/  
    https://pypi.org/simple/  
    https://repo.huaweicloud.com/repository/pypi/simple/  

# 信任的主机  
trusted-host =   
    pypi.tuna.tsinghua.edu.cn  
    mirrors.aliyun.com  
    pypi.doubanio.com  
    pypi.org  
    repo.huaweicloud.com
```


## 给国外的源配置Proxy
### 方案一：使用 proxifier 或 clash 的分流规则
```yaml
proxies:  
  # 您的代理服务器配置...  

proxy-groups:  
  - name: Proxy  
    type: select  
    proxies:  
      - Auto  
      - Direct  
      - 您的代理服务器名称...  

  - name: Auto  
    type: url-test  
    proxies:  
      - 您的代理服务器名称...  
    url: http://www.gstatic.com/generate_204  
    interval: 300  

# PyPI镜像源分流规则  
rules:  
  # 国内源 - DIRECT（直连）  
  - DOMAIN-SUFFIX,mirrors.aliyun.com,DIRECT  
  - DOMAIN-SUFFIX,pypi.doubanio.com,DIRECT  
  - DOMAIN-SUFFIX,repo.huaweicloud.com,DIRECT  
  - DOMAIN-SUFFIX,pypi.mirrors.ustc.edu.cn,DIRECT  
  - DOMAIN-SUFFIX,mirrors.cloud.tencent.com,DIRECT  
  
  # 国外源 - Proxy（代理）  
  - DOMAIN-SUFFIX,pypi.org,Proxy
  - DOMAIN-SUFFIX,pythonhosted.org,Proxy  # PyPI的文件托管域名  
  - DOMAIN-SUFFIX,cloudsmith.io,Proxy  
  - DOMAIN-SUFFIX,pkg.dev,Proxy  
  
  # 相关依赖域名  
  - DOMAIN-SUFFIX,files.pythonhosted.org,Proxy  
  - DOMAIN-SUFFIX,test.pypi.org,Proxy  
  - DOMAIN-SUFFIX,upload.pypi.org,Proxy  
  - DOMAIN-SUFFIX,google-analytics.com,Proxy  
  - DOMAIN-SUFFIX,googleapis.com,Proxy  
  
  # 包下载相关CDN  
  - DOMAIN-SUFFIX,cloudfront.net,Proxy  
  - DOMAIN-SUFFIX,fastly.net,Proxy

  # 确保 PyPI 相关域名走代理  
  - DOMAIN-SUFFIX,pypi.org,Proxy  
  - DOMAIN-SUFFIX,pythonhosted.org,Proxy  
  - DOMAIN-SUFFIX,python.org,Proxy  
  
  # SSL证书验证相关域名  
  - DOMAIN-SUFFIX,digicert.com,Proxy  
  - DOMAIN-SUFFIX,lets-encrypt.org,Proxy  
  - DOMAIN-SUFFIX,sectigo.com,Proxy  
  
  # 时间同步服务器（用于证书验证）  
  - DOMAIN-SUFFIX,ntp.org,DIRECT  
  - DOMAIN-SUFFIX,pool.ntp.org,DIRECT

tls:  
  # TLS配置  
  enable: true  
  skip-cert-verify: false  
  # 可选：自定义证书  
  certificates:  
    - domain: "*.pypi.org"  
      skip-verify: true  
```


## 智能pip配置脚本
见`smart_pip_install.py`

