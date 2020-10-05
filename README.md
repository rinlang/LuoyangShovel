# LuoyangShovel<sub>ver 0.0.0</sub>
## 项目简介
洛阳铲是一个子域名挖掘机。

愿景是能够把祖坟都给你挖出来。
## 当前阶段开发计划
### 子域名的收集模块
1.字典爆破

2.接口调用
    
3.DNS查询 nslookup

4.爬虫子页面爬取

5.文件收集 crossdomain.xml robots.txt

6.HTTPS证书搜集

7.ip反查

### 命令行UI及日志输出
banner
loguru

### 配置文件模块
使用toml格式配置文件

### 

## 目录结构
```
./LuoyangShovel
|   .gitignore
|   LICENSE
|   LuoyangShovel.py
|   README.md
|   requeirements.txt
|
+---common                      通用组件
|       __init__.py         
|       utils.py                    通用函数
|
+---conf                        配置模块
|       __init__.py         
|       config.toml                 配置文件
+---docs                        使用及开发文档
+---log                         日志模块
+---modules                     各组件模块
|       __init__.py
|   +---brute_force
|   |       __init__.py
|   |       default_dict.txt            默认字典

```