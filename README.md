# flask-test

## 红图
- 蓝图升级版本
  例： /api/v1/user/[get、put、delete]  蓝图为 @app.route('/user/get') 红图为：@app.route('/get')

## 权限
- scope 
  通过 api接口(endpoint)、modules、排除；三种方式来规定权限

## models 升级
- base.py 
  重构 query 与 delete，并非真正删除，软删除，设置status为0

## Exception
- 规范化Exception
  全部以 APIException 的方式返回信息，包括系统错误
  
## Hide方法
- 实例化时，隐藏model中某些字段