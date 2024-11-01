# Aliyun-DSW-Building-SOP
本人在阿里云搭建DSW实例，挂载oss盘，nas盘，配置专有网络VPC的踩坑全流程



1. 如何开启DSW实例

   - 进入PAI工作台
   - 在左侧边栏选择交互式建模，点击DSW

1. 如何配置oss盘

   打开对象存储控制台
   创建bucket，注意bucket的区域必须和容器一致
   配置bucket接入点（需要用到专有网络的id）

   oss盘在哪里挂载：创建DSW实例的时候自动会让你选择

3. 如何配置nas盘
   (文件存储NAS)[https://nasnext.console.aliyun.com/overview?spm=a2c4g.2510079.0.0.6cb11436djubUj]
   
4. 如何挂载nas盘

   <br>
   
   - 如果是ECS容器：先进入到容器里，然后用mount挂载命令去挂载。
   - 如果是DSW实例：在创建时的数据集一栏中选择NAS即可。

6. 如何配置专有网络（VPC）
    - 先在主页点击产品，然后搜索VPC

8. 如何给RAM用户授权

9. 如何配置RAM用户的权限列表，以及各个字段的常见含义

1. oss盘无法用git拉取或推送，只能使用nas

1. 推送github失败，配置ssh，公钥私钥。。。



### ssh配置 (在DSW中)
与git相关的问题请首先查阅 (github文档)[https://docs.github.com/en]
(Generating a new SSH key and adding it to the ssh-agent)[https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux]

添加git邮箱和用户名：
```shell
git config --global user.name "NJUxlj"
git config --global user.email "1016509070@qq.com"
```

一键生成公钥和密钥
```shell
ssh-keygen -t ed25519 -C "your_email@example.com"
```

<br>

在linux上开启ssh-agent (Start the ssh-agent in the background.)
```shell
eval "$(ssh-agent -s)"
```


把你的私钥给ssh-agent
```shell
ssh-add ~/.ssh/id_ed25519

```

把ssh公钥添加到你的Github账户, 以便为您的账户启用 SSH 访问
For more information, see ("Adding a new SSH key to your GitHub account.")[https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account]
1. 将 SSH 公钥复制到剪贴板
```shell
$ cat ~/.ssh/id_ed25519.pub
# 把其中的内容复制到剪贴板
```

2. 在 GitHub 上任何页面的右上角，单击您的个人资料照片，然后单击 Settings（设置）。
3. 在侧边栏的 “Access（访问）”部分，单击 SSH 和 GPG 密钥。
4. 单击 New SSH key （新建 SSH 密钥） 或 Add SSH key （添加 SSH 密钥）。
5. 在“Title（标题）”字段中，为新键添加描述性标签。例如，如果您使用的是个人笔记本电脑，则可以将此键称为“个人笔记本电脑”。
6. 选择密钥类型，即 authentication 或 signing。有关提交签名的详细信息，请参阅“关于提交签名验证”。
7. 在 “Key” 字段中，粘贴您的公钥。
8. 单击 Add SSH key（添加 SSH 密钥）。


测试ssh是否生效
```shell
ssh -T git@github.com
```

如过他显示welcome xxx， 但是你依然git push不上去
```shell
ssh -T GITHUB-USERNAME@github.com
```
如果显示
```shell
$ ssh -T GITHUB-USERNAME@github.com
> Permission denied (publickey).
```

下一步，你可能需要 (修改并验证remote仓库)[https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories]
[这个错误经常会发生，特别是当你刚刚拉取了一个新仓库的时候]
```shell
$ git remote add origin https://github.com/OWNER/REPOSITORY.git

# 查看新仓库
git remote -v
```

如果你发现报错 fatal：仓库已经存在，那么非常可能是远端的地址用了https格式，而你需要ssh格式
```shell
git remote set-url origin git@github.com:NJUxlj/Travel-Agent-based-on-LLM-and-SFT.git
```

ssh推送的问题就解决了




<br>

## 人工智能平台PAI

### 什么是DSW（Data Science Workshop）







### NAT网关
(NAT配置)[https://mp.weixin.qq.com/s?__biz=MzI4OTMyODUwNA==&mid=2247485016&idx=1&sn=0526d9c396a0d9ea3e280e67b617ac46&chksm=ec319a4fdb4613598b5231a618cda173e8f531e87dc95a518d31700b736679a1a577dd04e8a5#rd]


![image](https://github.com/user-attachments/assets/717a0404-0f31-4239-905c-9d1c59d10452)








### Clash for linux 配置
首先解压zip

使用须知
- 此项目不提供任何订阅信息，请自行准备Clash订阅地址。
- 运行前请手动更改`.env`文件中的`CLASH_URL`变量值，否则无法正常运行。
- 当前在RHEL系列和Debian系列Linux系统中测试过，其他系列可能需要适当修改脚本。
- 支持 x86_64/aarch64 平台

- 
使用教程
1. 进入到项目目录，编辑`.env`文件，修改变量`CLASH_URL`的值为订阅地址。
```shell
cd clash-for-linux-master
vim .env
```
`.env` 文件中的变量 `CLASH_SECRET` 为自定义 Clash Secret，值为空时，脚本将自动生成随机字符串，可以空着。

3. 启动程序
```shell
sudo bash start.sh
```
会有很简单明确的提示信息，按照提示执行
注意：文件夹中有`Readme.md`，有更加详细的内容！！！这里不重复写了




Clash Dashboard 访问地址: http://<ip>:9090/ui
Secret: cd1995ae866114387f46ce4419f4472004dbddd2fd97cb010696086fe3686de3

请执行以下命令加载环境变量: ```source /etc/profile.d/clash.sh```

请执行以下命令开启系统代理: ```proxy_on```

若要临时关闭系统代理，请执行: ```proxy_off```



- 查看系统代理是否设置了
```shell
echo $http_proxy
```

- 查看终端中是否可以访问外网
```shell
curl https://www.google.com
```

- 如果没有添加系统代理，需要添加一下：
- 方法1. 临时设置代理（仅对当前会话有效）
```shell
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
curl http://www.google.com
```

- 方法2. 永久设置代理（对所有新会话有效）
```shell
vim ~/.bashrc
```

- 在文件末尾添加以下行：
```shell
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

- 执行
```shell
source ~/.bashrc
```
#### 现在还有另外一个问题，默认情况下，sudo 会清除环境变量。

如果你需要在使用 sudo 时保留代理设置，可以使用 -E 选项：
```shell
sudo -E http_proxy=http://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890 your_command
```


这样每次运行会有点麻烦，于是可以在文件中写死
```shell
sudo chmod +w /etc/sudoers
sudo vim /etc/sudoers
```

在文件中添加以下行：
```shell
Defaults env_keep += "http_proxy https_proxy"
```

### 至此，结束！！！


