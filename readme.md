<!-- TOC -->

- [1. 用途](#1-用途)
- [2. 说明](#2-说明)

<!-- /TOC -->


<a id="markdown-1-用途" name="1-用途"></a>
# 1. 用途

解决:  
动态IP地址变化问题.  

方法:  
调用阿里云解析接口,每隔一段时间更新域名绑定的IP.  


<a id="markdown-2-说明" name="2-说明"></a>
# 2. 说明

配置/日志
```bash
# 日志
/var/log/dynamic_dns/dynamic_dns.log

# ACCESS_KEY_ID
/etc/dynamic_dns/access_key_id

# ACCESS_KEY_SECRET
/etc/dynamic_dns/access_key_secret
```

如何启动
```bash
git clone https://github.com/yqsy/dynamic_dns.git
cd dynamic_dns
docker build -t="yqsy021/dynamic_dns:latest" .

mkdir -p ~/env/dynamic_dns && cd ~/env/dynamic_dns

# 从 https://ak-console.aliyun.com/?spm=5176.200001.0.0.twALLa#/accesskey 获得
echo 'access_key_id' > ./access_key_id
echo 'access_key_secret' > ./access_key_secret
chmod 400 ./access_key_id ./access_key_secret

docker run -d --name dynamic_dns \
    -v `pwd`/access_key_id:/etc/dynamic_dns/access_key_id:ro \
    -v `pwd`/access_key_secret:/etc/dynamic_dns/access_key_secret:ro \
    -v `pwd`/:/var/log/dynamic_dns:rw \
    yqsy021/dynamic_dns \
    dynamic_dns -n yqsycloud.top
```
