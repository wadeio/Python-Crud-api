from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)
arrs=[{
    "id":1,
    "name":"買早餐",
    "status":1
}]

@app.route("/tasks", methods=['GET'])
def get_tasks():
    #return jsonify({'result':result})
    return Response(json.dumps({'result':arrs},ensure_ascii=False), mimetype='application/json')


@app.route("/task", methods=['POST'])
def post_task():
    req_data = request.get_json(force=True)
    print(req_data['name'])
   
    result={
        "name":req_data['name'],
        "status":0,
        "id":len(arrs)+1
    }
    arrs.append(result)
    return Response(json.dumps({'result':result},ensure_ascii=False), status=201, mimetype='application/json')

@app.route("/task/<int:id>", methods=['PUT'])
def put_task(id):
    req_data = request.get_json(force=True)
    for i,arr in enumerate(arrs):
        if arr['id']==id:
            del arrs[i]
            
            result={
                "name":req_data['name'],
                "status":req_data['status'],
                "id":id
            }
            arrs.append(result)

            return Response(json.dumps({'result':result},ensure_ascii=False), status=200,  mimetype='application/json')

    return Response(json.dumps({'error':'error'},ensure_ascii=False), status=404,  mimetype='application/json')



@app.route("/task/<int:id>", methods=['DELETE'])
def delete_task(id):
    for i,arr in enumerate(arrs):
        if arr['id']==id:
            print('Find')
            del arrs[i]
            
            return Response(json.dumps({'status_code':200}), status=200, mimetype='application/json')

    return Response(json.dumps({'error':'error'},ensure_ascii=False), status=404,  mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)