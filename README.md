# flask-test

## 红图
- 蓝图升级版本
  例： /api/v1/user/[get、put、delete]  蓝图为 @app.route('/user/get') 红图为：@app.route('/get')

## models 升级
- base.py 
  重构 query 与 delete，并非真正删除，软删除，设置status为0

## Exception
- 规范化Exception
  全部以 APIException 的方式返回信息，包括系统错误
  
## celery异步
- ticket/app/utils/tsk.py 为task文件，所有异步操作方法在这创建
- ticket/celerywork.py 为 celery启动文件，分开不会有循环调用的风险
- celery启动：
```shell
  venv/bin/celery -A celerywork.celery worker -l INFO --beat
```
