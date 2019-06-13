import imgkit
import time

css = '/Users/leulshewangizaw/Programming/Exploring/Flask/cmboard_cp/app/static/css/style.css'

options = {
    'format': 'png',
}


imgkit.from_url( 'http://127.0.0.1:5000/work', 'out.png')