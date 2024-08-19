# Aliyun-DSW-Building-SOP
本人在阿里云搭建DSW实例，挂载oss盘，nas盘，配置专有网络VPC的踩坑全流程



1. 如何开启DSW实例

1. 如何配置oss盘

2. 如何配置nas盘

3. 如何挂载nas盘

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





