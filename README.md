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

5. 如何配置专有网络（VPC）

6. 如何给RAM用户授权

7. 如何配置RAM用户的权限列表，以及各个字段的常见含义

1. oss盘无法用git拉取或推送，只能使用nas

1. 推送github失败，配置ssh，公钥私钥。。。



### ssh配置 (在DSW中)
与git相关的问题请首先查阅 (github文档)[https://docs.github.com/en]
(Generating a new SSH key and adding it to the ssh-agent)[https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux]

()[]

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
