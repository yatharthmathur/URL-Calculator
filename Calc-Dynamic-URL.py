from flask import Flask
app=Flask("Simple Calculator")
@app.route('/')
def f1():
    form='<head><title>Simple Calculator</title></head><h1 align=center><font color=RED>Simple Calculator</h1></font><br><h2 align=center><b>'
    return form + 'Append the binary operation to the URL to compute the result. (eg. 127.0.0.1:5000/12+21)<br>' + 'For division use $. (eg. 127.0.0.1/12$3)'
@app.route('/<a>') #passing argument in a url
def f(a):
    form='<head><title>Simple Calculator</title></head><h1 align=center><font color=RED>Simple Calculator</h1></font><br><h2 align=center><b>'

    a=a.replace('$','/')
    a=a.replace('^','**')
    return form+a+'='+str(eval(a))

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)
