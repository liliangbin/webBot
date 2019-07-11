# 项目简介 flask+pymysql + roslibjs 
#### 项目前提 
- roscore 
- usb 摄像头得起来，我们使用usb_cam 口我们需要起来，前端网页需要订阅这个接口 
- rosrun web_video_server web_video_server 
- roslaunch rosbridge_server rosbridge_websocket.launch 
- web_video_server 是将我们的视频信号传输到8080端口 http://localhost:8080/stream?topic=/usb_cam/image_raw&type=ros_compressed
-  rosbridge_server 则是将ros的东西转化为json的接口 运行于9090 端口

## flask 应用启动 。后期我们可以写一个启动脚本 ，例如migrate 我们可以再建   
- 在config中我们使用环境变量来作为我们的配置，
- source activate flask-info 
- export FLAK_APP=flasky.py
- export FLASK_DEBUG=1  # 开启debug  模式
- flask run 

- flask db init 
- flask db migrate -m '{迁移的版本号}'
- flask db upgrade # 他的自动的迁移一般有问题，我们修改后再upgrade  在migrations 这个文件夹下的version文件夹下 
- flask db downgrade # 
## ERROR [root] Error: Can't locate revision identified by '1d80834f7e7b'
- 原因：删除了alembic迁移文件，导致数据库版本号（alembic_version）跟迁移文件版本号不一致

- 解决办法：

- 删除数据库的表，从新创建数据表 
### 但是又会有一个问题，flask 一般我们只是用于小应用的开发，例如一些嵌入式快速开发，例如我们现在使用的这个架构其实并不适用于小型的架构，小型的项目开发其实我们可以只用在一个页面或是在几个页面中搞定便可以的了。
