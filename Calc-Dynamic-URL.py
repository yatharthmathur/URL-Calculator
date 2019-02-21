from flask import Flask
app=Flask("Simple Calculator")
@app.route('/')
def f1():
    form='<head><title>Simple Calculator</title></head><h1 align=center><font color=RED>Simple Calculator</h1></font><br><h2 align=center><b>'
    return form + 'Append the binary operation to the URL to compute the result. (eg. 127.0.0.1:5000/12+21)<br>' + 'For division use $. (eg. 127.0.0.1/12$3)'
@app.route('/<a>') #passing argument in a url
def f(a):
    str1=""
    form='<head><title>Simple Calculator</title></head><h1 align=center><font color=RED>Simple Calculator</h1></font><br><h2 align=center><b>'
    i=0

    while(1):
        if a[i].isnumeric() or a[i]=='.' or a[i]=='-':
            str1=str1+a[i]
        else:
            break
        i+=1
    ch=a[i]
    if ch == '$':
        ch = '/'
    str1=float(str1)
    print(str1)
    str2=a[i+1::]
    str2=float(str2)
    print(str2)
    if ch == '+':
        str3=str1+str2
    elif ch == '-':
        str3=str1-str2
    elif ch == '*':
        str3=str1*str2
    elif ch == '/':
        str3=str1/str2
    elif ch == '^':
        str3=str1**str2
    else:
        return form+'Invalid operator.'
    str3=str(round(str3,9))
    return form+str(str1) + ' ' + ch +' '+ str(str2) + ' = ' + str3

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)
