### ali_image_api
采用flask编写结合jenkins动态参数获取阿里云镜像版本
### 使用说明
##### 打包镜像
```shell
docker build -t ali_image_api:v1 .
```
##### 启动
需要阿里云有镜像仓库读取权限的AK SK
```shell
docker run -p 5000:5000 -e ak=${ak} -e secret=${secret} ali_image_api:v1
```
##### 使用
http://IP:5000/image?endpoint=cn-shanghai&repo_namespace=ops&repo_name=soe&simple=1
endpoint:镜像仓库区域
repo_namespace:镜像仓库NAMESPACE
repo_name:镜像名字
simple:如果等于1,则简单方式传入，否则是完整返回json信息
