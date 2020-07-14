
from app.utils.redprint import Redprint
from app.utils.tsk import test
from flask import jsonify

api = Redprint('tasks')


@api.route('/client', methods=['GET'])
def AddTask():
    print("ok")
    print("error")
    try:
        test.delay()
    except Exception as e:
        print(e)
    return jsonify('ok')