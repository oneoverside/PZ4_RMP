from flask import Flask, render_template, request, jsonify
from RoomControl import RoomControl

app = Flask(__name__)
roomControl = RoomControl()
roomControl.cycle_temp_update()


@app.route('/', methods=['get'])
def index():
    return render_template('index.html')


@app.route('/getInfo', methods=['GET'])
def get_info():
    return jsonify({
        'kitchen': roomControl.kitchen,
        'room1': roomControl.room1,
        'room2': roomControl.room2,
        'livingRoom': roomControl.livingRoom,
        'toilet': roomControl.toilet,
        'temperature': roomControl.temperature,
    })


@app.route('/updateData', methods=['POST'])
def log():
    data = request.get_json()
    room_name = data.get('room')
    status = data.get('status')

    if room_name == 'kitchen':
        roomControl.kitchen = status
    if room_name == 'room1':
        roomControl.room1 = status
    if room_name == 'room2':
        roomControl.room2 = status
    if room_name == 'livingRoom':
        roomControl.livingRoom = status
    if room_name == 'toilet':
        roomControl.toilet = status
    print(f"{room_name} lightStatus: {status}")

    return jsonify({'success': True}), 200


if __name__ == '__main__':
    app.run()
