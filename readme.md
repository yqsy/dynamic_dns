<!-- TOC -->

- [1. 用途](#1-用途)
- [2. 说明](#2-说明)

<!-- /TOC -->


<a id="markdown-1-用途" name="1-用途"></a>
# 1. 用途

解决:  
动态IP地址变化问题.  

方法:  
调用阿里云解析接口,配合crontab实现每隔一段时间更新域名绑定的IP.  


<a id="markdown-2-说明" name="2-说明"></a>
# 2. 说明

```bash
# 安装
pip3 install git+git://github.com/yqsy/dynamic_dns.git@master

# 卸载
pip3 uninstall git+git://github.com/yqsy/dynamic_dns.git@master

# 日志
/var/log/dynamic_dns/dynamic_dns.log

# ACCESS_KEY_ID
/etc/dynamic_dns/access_key_id

# ACCESS_KEY_SECRET
/etc/dynamic_dns/access_key_secret

```

配置ID,key
```bash
mkdir -p /etc/dynamic_dns
echo 'xxx' > /etc/dynamic_dns/access_key_id
echo 'xxx' > /etc/dynamic_dns/access_key_secret

chmod 400 /etc/dynamic_dns/access_key_id /etc/dynamic_dns/access_key_secret
```
