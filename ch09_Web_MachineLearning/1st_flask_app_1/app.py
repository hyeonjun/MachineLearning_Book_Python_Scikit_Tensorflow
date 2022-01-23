from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

app = Flask(__name__)

class HelloForm(Form): # validators.DataRequired() : 사용자의 입력 텍스트가 안전한지 아닌지를 자동으로 확인
    sayhello = TextAreaField('', [validators.DataRequired()])

@app.route('/') # 라우트 데코레이터 : 특정 URL이 index 함수를 실행도록 지정
def index(): # templates 폴더 아래에 있는 fitst_app.html HTML 파일을 화면에 출력
    form = HelloForm(request.form) # wtforms의 TextAreaField 클래스를 사용하여 시작 웹 페이지에 텍스트 필드 추가
    return render_template('first_app.html', form=form)

@app.route('/hello', methods=['POST']) # 폼에 입력된 데이터를 HTML 바디에 실어 서버로 전송하는 POST 메서드 사용
def hello(): # HTML 폼으로 전달된 내용을 검증한 후 hello.html 페이지 출력
    form = HelloForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['sayhello']
        return render_template('hello.html', name=name)

if __name__ == '__main__': # 새로운 플라스크 인스턴스 초기화
    app.run(debug=True) # 현재 디렉터리오하 같은 위치의 HTML 템플릿 폴더 templates를 찾는다.
    # debug=True 매개변수를 설정해서 플라스크 디버거를 활성화.