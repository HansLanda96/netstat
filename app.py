from flask import Flask, render_template
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/unix_sockets')
def unix_sockets():
    result = subprocess.run(['netstat', '-x'], capture_output=True, text=True)
    return render_template('result.html', title='Unix Sockets', output=result.stdout)


@app.route('/tcp_sockets')
def tcp_sockets():
    result = subprocess.run(['netstat', '-ant'],
                            capture_output=True, text=True)
    return render_template('result.html', title='TCP Sockets', output=result.stdout)


@app.route('/udp_sockets')
def udp_sockets():
    result = subprocess.run(['netstat', '-un'], capture_output=True, text=True)
    return render_template('result.html', title='UDP Sockets', output=result.stdout)


@app.route('/routing_table')
def routing_table():
    result = subprocess.run(['netstat', '-r'], capture_output=True, text=True)
    return render_template('result.html', title='Routing Table', output=result.stdout)


if __name__ == '__main__':
    app.run()
