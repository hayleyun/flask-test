from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/main')
def main():
    return render_template('method.html')

# /주소/변수명
@app.route('/user/<username>')
def show_user (username):
    return username + '!!!'

@app.route('/user/<username>/<int:age>')
def show_user_age(username,age):
    return username + ':' + str(age) + '!!!'

# request object
# Form(post,dictionary), args(get,?뒤에 있는 값 파싱), files, method(post냐 get이냐)
# post 방식으로 넘어오는지 get 방식으로 넘어오는지 체크
@app.route('/method',methods=['GET','POST'])
def method_test():
    if request.method == 'POST':
        return render_template('show_result.html', data=request.form)
    else:
        return render_template('show_result.html', data=request.args)

# files
@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('fileup.html')
    else:
        f = request.files['file']
        # path 설정해 원하는 디렉토리 안에 업로드한 파일 넣기
        # upload 폴더 만들어서 폴더 안에 저장
        path = os.path.dirname(__file__) + '/upload/' + f.filename
        print(path)
        f.save(path)
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True,port=80)