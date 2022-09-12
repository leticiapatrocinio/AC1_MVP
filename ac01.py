import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST', 'GET'])
def cadastrar():
    nome=request.form['nome']
    cpf=request.form['cpf']
    end=request.form['end']

    if nome and cpf and end:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tbl_aluno (nome_aluno, cpf_aluno, endereco_aluno) VALUES (%s, %s, %s)', (nome, cpf, end))
        conn.commit()
    return render_template('cadastro.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select nome_aluno, cpf_aluno, endereco_aluno from tbl_aluno')
  data = cursor.fetchall()
  conn.commit()
  return render_template('listagem.html', dados=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
