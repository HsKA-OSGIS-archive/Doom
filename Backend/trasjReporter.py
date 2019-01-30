'''
@author: desweb
'''
# 1.system libraries
import os, sys
# 2.second part libraries
from flask import Flask,render_template, flash, request, url_for, redirect, session, jsonify
from wtforms import Form, validators, StringField, PasswordField,SelectField as sf, FloatField, TextAreaField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
from datetime import datetime
from geopy.geocoders import Nominatim
import uuid
from fileinput import filename
from psycopg2._psycopg import IntegrityError
from threading import Thread
from itsdangerous import  URLSafeTimedSerializer


# 3 .my libraries
DES_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(DES_PATH)


from pg_operations2 import pg_operations2
from settings import settings

user = settings.USER
password = settings.PASSWORD
host = settings.HOST
port = settings.PORT
database = settings.DATABASE

app = Flask(__name__)

app.config.update(
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'xxxxxxxx@sss',
    MAIL_PASSWORD = 'xxxxxxx',
    MAIL_DEFAULT_SENDER ='SECURITY_EMAIL_SENDER'
    )

MAIL_SERVER='smtp.gmail.com',
MAIL_PORT=587,
MAIL_USE_TLS=True,
MAIL_USERNAME = 'xxxxxxxx@xxxx',
MAIL_PASSWORD = 'xxxxxxx'
app.config['SECURITY_EMAIL_SENDER'] = 'xxxxxxxx@sss'
mail = Mail(app)

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif', 'tif', 'jpeg'])

#mail.init_app(app)
app.config['SECRET_KEY'] = 'super-secret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_HASH'] = 'sha256_crypt'
app.config['SECURITY_PASSWORD_SALT'] = 'fhasdgihwntlgy8f'
app.config['SECURITY_RECOVERABLE'] = True
app.debug = True



@app.route('/')
def index():
    
    
    pointX = [0, 10, 10, 0, 6, 3]
    pointY = [0, 0, 10, 10, 6, 8]
    pointZ = [1, 4, 10,5, 5, 6]
    
    point1 = []
    point2 = []
    point3 = []
    point4 = []
    point5 = []
    point6 = []
    
    for i in xrange(len(pointX) - 1):
        point1x1 = pointX[0]
        x2 = pointX[i + 1]
        point2x1 = pointX[1]
        point3x1 = pointX[2]
        point4x1 = pointX[3]
        point5x1 = pointX[4]
        point6x1 = pointX[5]
        for j in xrange(len(pointY) - 1):
            point1y1 = pointY[0]
            y2 = pointY[j + 1]
            point2y1 = pointY[1]
            point3y1 = pointY[2]
            point4y1 = pointY[3]
            point5y1 = pointY[4]
            point6y1 = pointY[5]
        print (x2 - point1x1)**2 + (y2 - point1y1)**2    
        point1.append(((x2 - point1x1)**2 + (y2 - point1y1)**2)**0.5)
        point2.append(((x2 - point2x1)**2 + (y2 - point2y1)**2)**0.5)
        point3.append(((x2 - point3x1)**2 + (y2 - point3y1)**2)**0.5)
        point4.append(((x2 - point4x1)**2 + (y2 - point4y1)**2)**0.5)
        point5.append(((x2 - point5x1)**2 + (y2 - point5y1)**2)**0.5)
        point6.append(((x2 - point6x1)**2 + (y2 - point6y1)**2)**0.5)


    print point1, point2, point3, point4, point5, point6    
                  
           
    

    
    """
    import random
    d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
    conn=d_conn['conn']
    cursor=d_conn['cursor']
    trashChoices = [] 
    cursor.execute("select trash from d.trash_type")
    data = cursor.fetchall()
    for row in data:
        trashChoices.append(row[0])
    
    print trashChoices
    cursor.execute("select longitude from d.point")
    data = cursor.fetchall()
    lonList = []
    for row in data:
        lonList.append(row[0])
    cursor.execute("select latitude from d.point")
    data = cursor.fetchall()
    latList = []
    for row in data:
        latList.append(row[0])
    import time
    for x in range(400, 1420): 
        time.sleep(25)
        lat = random.uniform(48.92919,49.11004)      
        lon = random.uniform(8.26770,8.5637)

        print lat, lon
        if lat not in latList and lon not in lonList:
    
            #lat = random.randint(48.92919921875,49.1100463867188)
            #lon = random.randint(8.2677001953125,8.56378173828125)
            trashType=  random.randint(0,len(trashChoices)-1)
            print trashType
            trashKey = trashChoices[ trashType]
            fk_trash_type = fkTrashType(trashKey)
            address = nominatim(str(lat), str(lon))
            print address
            city = address[0]
            suburb = address[1]
            neighbourhood = address[2]
            params = paramsInsertNoImg(lat, lon, trashType, address, fk_trash_type, city, suburb, neighbourhood)
            query = queryInsertNoImg()
            cursor.execute(query, params)   
            conn.commit()
        else:
            continue    
    d_conn = pg_operations2.pg_disconnect2(d_conn)                    
    flash('Point uploaded', 'success')
    """
    return render_template("main.html")

 

class ContactForm(Form):
  name = StringField("Name",  [validators.Required("Please enter your name.")])
  email = StringField("Email",  [validators.Required("Please enter your email address."), Email()])
  subject = StringField("Subject",  [validators.Required("Please enter a subject.")])
  message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
  
  
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    
  form = ContactForm(request.form)
  try:
      if request.method == 'POST' and form.validate():
          msg = Message(form.subject.data, sender=form.email.data, recipients=['compruebaGaspar@gmail.com'])
          msg.body = """
            From: %s\t %s\n
          %s
          """ % (form.name.data, form.email.data, form.message.data)
          mail.send(msg)
          flash('Message sent. Thanks.', 'success')
          return redirect(url_for('map'))
     
      elif request.method == 'GET':
        return render_template('contact.html', form=form)       
  except:
        flash('Error has occured.', 'danger')
        return render_template('contact.html', form=form)
  return render_template('contact.html', form=form)       
           
  
@app.route('/map')
def map():
    return render_template("mapTrashReporter.html")

def dbAccessChoices():
    d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
    cursor=d_conn['cursor'] 
    cursor.execute("select acess_type from d.remove_access")
    data = cursor.fetchall()
    choices = []
    for row in data:
        choices.append((row[0], row[0]))
    choices =  (choices[2], choices[1])    
    d_conn = pg_operations2.pg_disconnect2(d_conn)
    print choices
    return choices 


class RegistrationForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=50),validators.DataRequired(), Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'), validators.Length(min=6, max=50)
    ])
    confirm = PasswordField('Repeat Password')
    choices = dbAccessChoices()    
    requestAccess= sf(choices[1],choices=choices)

def paramsRegister(email, passwordUser, fk_request_access):
    params = {
        '_email' : email,
        '_password' : passwordUser,
        '_fk_request_access' : fk_request_access,
        }
    return params

def queryRegister():
    query = """insert into d.user (email, encrypted_password, fk_request_access) 
                 values (%(_email)s,%(_password)s, %(_fk_request_access)s)"""
    return query

@app.route('/register', methods=['GET', 'POST'])
def register():
    d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
    conn=d_conn['conn']
    form = RegistrationForm(request.form)
    try:        
        if request.method == 'POST' and form.validate():
            email = form.email.data
            passwordUser = sha256_crypt.encrypt(form.password.data)
            cursor=d_conn['cursor']
            requestAccess =  form.requestAccess.data
            if requestAccess == 'No':
                fk_request_access = 3
            else: 
                fk_request_access = 2 
            params = paramsRegister(email, passwordUser, fk_request_access)      
            query = queryRegister()
            cursor.execute(query, params)
            conn.commit()
            d_conn = pg_operations2.pg_disconnect2(d_conn)
            newUserEmail(email)

            flash('Thanks for registering! Please confirm your registration via email', 'success')
            return redirect(url_for('map'))
        return render_template('register.html', form=form)
    except:
        conn=d_conn['conn']
        conn.rollback()
        d_conn = pg_operations2.pg_disconnect2(d_conn)

        flash('ERROR! Email ({}) already exists.'.format(form.email.data), 'danger')
        return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
    cursor=d_conn['cursor']
    if request.method == 'POST':
        email = request.form['email']
        password_candidate = request.form['password']
        cursor.execute("SELECT encrypted_password FROM d.user WHERE email = %s",[email])     
        if cursor.fetchone() is None:
            flash('Not such email/password', 'danger')
            d_conn = pg_operations2.pg_disconnect2(d_conn)
            return render_template('login.html')
        else:
            cursor.execute("SELECT encrypted_password FROM d.user WHERE email = %s",[email])
            data = cursor.fetchone()[0]
            if sha256_crypt.verify(password_candidate, data):
                data = cursor.execute("SELECT remove_access FROM d.user WHERE email = %s",[email])
                data = cursor.fetchone()[0]
                if data:
                    session['remove_access'] = True
                session['logged_in'] = True
                #session['email'] = request.form['email']
                flash('You are now logged in as ' + email, 'success')
                d_conn = pg_operations2.pg_disconnect2(d_conn)
                return redirect(url_for('map'))
            else:
                flash('Not such email/password', 'danger')
                d_conn = pg_operations2.pg_disconnect2(d_conn)
                return render_template('login.html')    
    return render_template('login.html')



def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap



# Check if has access
def is_municipality(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'remove_access' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please CONTACT US for access', 'danger')
            return redirect(url_for('map'))
    return wrap



@app.route('/logout/')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('map'))



def send_async_email(msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, recipients, html_body):
    msg = Message(subject, recipients=recipients)
    #msg.body = text_body
    msg.html = html_body
    thr = Thread(target=send_async_email, args=[msg])
    thr.start()


class EmailForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])



def send_password_reset_email(user_email):
    password_reset_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

    password_reset_url = url_for(
        'resetPass_with_token',
        token=password_reset_serializer.dumps(user_email, salt='password-reset-salt'),
        _external=True)

    html = render_template(
        'email_password_reset.html',
        password_reset_url=password_reset_url)

    send_email('Password Reset Requested', [user_email], html)
    
    
def newUserEmail(user_email):
    password_reset_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    password_reset_url = url_for(
        'confirmUser_with_token',
        token=password_reset_serializer.dumps(user_email, salt='password-reset-salt'),
        _external=True)
    html = render_template(
        'newUserConf.html',
        password_reset_url=password_reset_url)
    send_email('Confirmation Requested', [user_email], html)
    


@app.route('/reset-password', methods=('GET', 'POST',))
def forgot_password():
    form = EmailForm(request.form) 
    if form.validate():
        email = form.email.data
        d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
        cursor=d_conn['cursor']
        cursor.execute("SELECT encrypted_password FROM d.user WHERE email = %s",[email])
        if cursor.fetchone() is None:
            flash('Not such email.', 'danger')
            return render_template('emailForgotPass.html', form=form)
        else:
            d_conn = pg_operations2.pg_disconnect2(d_conn)
            send_password_reset_email(email)
            flash('Please check your email for a password reset link.', 'success')
            return redirect(url_for('login'))
    return render_template('emailForgotPass.html', form=form)




class PasswordForm(Form):
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=6, max=50)
    ])
    confirm = PasswordField('Repeat Password')


@app.route('/resetPassword/<token>', methods=['GET', 'POST'])
def resetPass_with_token(token):
    d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
    conn=d_conn['conn']
    try:
        form = PasswordForm(request.form)
        password_reset_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        email = password_reset_serializer.loads(token, salt='password-reset-salt', max_age=3600)
        if form.validate():
            password2 = sha256_crypt.encrypt(form.password.data)
            cursor=d_conn['cursor']
            cursor.execute("UPDATE d.user set encrypted_password = %s WHERE  email = %s;",[password2,email])
            conn.commit()
            d_conn = pg_operations2.pg_disconnect2(d_conn)
            flash('Your password has been updated!', 'success')
            return redirect(url_for('login'))
        return render_template('emailForgotPassToken.html', form=form, token=token)
    except:
        flash('The link is invalid or has expired.', 'danger')
        return redirect(url_for('login'))
    

@app.route('/confirmUser/<token>', methods=['GET', 'POST'])
def confirmUser_with_token(token):
    d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
    conn=d_conn['conn']
    try:
        reset_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        email = reset_serializer.loads(token, salt='password-reset-salt', max_age=3600)
        cursor=d_conn['cursor']
        cursor.execute("UPDATE d.user set confirmed = True WHERE  email = %s;",[email])
        conn.commit()
        d_conn = pg_operations2.pg_disconnect2(d_conn)
        flash('Your are now confirmed!', 'success')
        return redirect(url_for('map'))
    except:
        flash('The link is invalid or has expired.', 'danger')
        return redirect(url_for('login'))    


def dbTrashChoices():
    d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
    cursor=d_conn['cursor'] 
    cursor.execute("select trash from d.trash_type")
    data = cursor.fetchall()
    choices = []
    for row in data:
        choices.append((row[0], row[0]))
    d_conn = pg_operations2.pg_disconnect2(d_conn)

    return choices 





class addPointForm(Form):
    lat = FloatField('Latitude', [validators.DataRequired(), validators.NumberRange(min=-90, max=90)])
    lon = FloatField('Longitude', [validators.DataRequired(), validators.NumberRange(min=-180, max=180)])
    choices = dbTrashChoices()
    trashType= sf(choices[0],choices=choices)

def checkPol(lat, lon, form):
    d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
    cursor=d_conn['cursor'] 
    cursor.execute("SELECT st_xmin(ST_Extent(geom)), st_xmax(ST_Extent(geom)),st_ymin(ST_Extent(geom)),st_ymax(ST_Extent(geom)) as bextent FROM bbox")
    data = cursor.fetchall()
    for row in data:
        minX =  row[0]
        maxX = row[1]
        minY = row[2]
        maxY = row[3]
    print data     
    if lon < minX or lon > maxX or lat < minY or lat > maxY:
            d_conn = pg_operations2.pg_disconnect2(d_conn)
            #flash('ERROR! Coordinates are out of Karlsruhe.', 'danger')
    d_conn = pg_operations2.pg_disconnect2(d_conn)    
        
def fkTrashType(trashType):
    d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
    cursor=d_conn['cursor'] 
    cursor.execute("select id from d.trash_type where trash = %s",[trashType])
    fk_trash_type = cursor.fetchall() 
    for row in fk_trash_type:
        fk_trash_type = row[0]
    d_conn = pg_operations2.pg_disconnect2(d_conn)

    return  fk_trash_type   
        
    
def nominatim(lat, lon):
    geolocator = Nominatim(user_agent="app")
    location = geolocator.reverse(str(lat) + ", " + str(lon),  addressdetails=True)
    if location.address is None or location.address  == '':
        address = 'Unknown'
    else:
        addressDict = location.raw.get("address")
        city = addressDict.get("city")
        suburb = addressDict.get('suburb')
        neighbourhood = addressDict.get('neighbourhood')
        road = addressDict.get('road')
        print road
        address = [city, suburb, neighbourhood, road]
        """
        address = location.address.split(',')[0] + ", " \
        + location.address.split(',')[1] + ", " \
        +location.address.split(',')[2] + ", " \
        +location.address.split(',')[3] + ", " \
        +location.address.split(',')[4] 
        """
    print address    
    return address

def imageUpload():
    if request.files['file']:
        file = request.files['file']
        ext = file.filename.split(".")[-1]
        #if file.filename  is None or file.filename  == '':
            #file.filename = ''
            #return file.filename  
        if ext.lower() in ALLOWED_EXTENSIONS:
            filename = secure_filename(file.filename)
            file.filename = filename.split('.')[0] + '_' + str(uuid.uuid4()) + '.' + filename.split('.')[1]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return file.filename
        elif ext.lower() not in ALLOWED_EXTENSIONS:
            print ext.lower()
            #flash('ERROR! Please upload only jpeg, png, gif or tif.', 'danger')
            return redirect(request.url)
    else:
        return 0        
  
def paramsInsert(lat, lon, trashType, filename, address, fk_trash_type, city, suburb, neighbourhood,road):
    params = {
                        '_lat': lat,      
                        '_lon' : lon,
                        '_cp_file_name': filename,
                        '_address': address,
                        '_fk_trash_type' :fk_trash_type,
                        '_city': city,
                        '_suburb': suburb,
                        '_neighbourhood': neighbourhood,
                        '_road': road
                    }
     
    return params

def paramsInsertNoImg(lat, lon, trashType, address, fk_trash_type, city, suburb, neighbourhood,road):
    params = {
                        '_lat': lat,      
                        '_lon' : lon,
                        '_address': address,
                        '_fk_trash_type' :fk_trash_type,
                        '_city': city,
                        '_suburb': suburb,
                        '_neighbourhood': neighbourhood,
                        '_road': road
                    }
     
    return params


def queryInsert():
    query = """insert into d.point
                    (latitude, longitude, geom, cp_file_name, address, fk_trash_type,
                     city, suburb, neighbourhood,road) 
                     values (%(_lat)s,%(_lon)s,
                     ST_SetSRID(ST_MakePoint(%(_lat)s, %(_lon)s), 4326) 
                     , %(_cp_file_name)s, %(_address)s, %(_fk_trash_type)s,
                     %(_city)s, %(_suburb)s, %(_neighbourhood)s,
                     %(_road)s)""" 
                     
    return query

def queryInsertNoImg():
    query = """insert into d.point
                    (latitude, longitude, geom, address, fk_trash_type,
                    city, suburb, neighbourhood, road) 
                     values (%(_lat)s,%(_lon)s,
                     ST_SetSRID(ST_MakePoint(%(_lat)s, %(_lon)s), 4326) 
                     , %(_address)s, %(_fk_trash_type)s,
                     %(_city)s, %(_suburb)s,%(_neighbourhood)s,
                      %(_road)s)""" 
                     
    return query

def imgExecption(e, d_conn, form):
    print e[0]
    conn=d_conn['conn']
    conn.rollback()
    d_conn = pg_operations2.pg_disconnect2(d_conn)
    return render_template('registerTrashReporter..html', form = form)  

def duplicateExecption( d_conn, form):
    conn=d_conn['conn']
    conn.rollback()
    d_conn = pg_operations2.pg_disconnect2(d_conn)
    flash('ERROR! Coords already exist', 'danger')
    return render_template('registerTrashReporter..html', form = form) 

"""
def pointInRadius(lat, lon, form):
    d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
    cursor=d_conn['cursor'] 
    cursor.execute('SELECT pointRadius(%s, %s)', [lat, lon])
    result = cursor.fetchone()[0]
    print result
    if result == 1:
        print result
        pg_operations2.pg_disconnect2(d_conn)
        flash('ERROR! Coords already exist 10 meters radius from there', 'danger')        
        return render_template('registerTrashReporter..html', form = form) 
"""
    
@app.route('/addPoint', methods=['GET', 'POST'])
def upload_file():
        try:
            form = addPointForm(request.form)
            d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
            conn=d_conn['conn']
            cursor=d_conn['cursor']  
            if request.method == 'POST':  
                if form.validate():
                     
                    filename = imageUpload()
                    lat = form.lat.data
                    lon = form.lon.data
                    
                    checkPol(lat, lon, form)
                    trashType= form.trashType.data
                    fk_trash_type = fkTrashType(trashType)
                    address = nominatim(str(lat), str(lon))
                    city = address[0]
                    suburb = address[1]
                    neighbourhood = address[2]
                    if address[3] is None:
                      address[3] = 'No location'  
                    road = address[3].encode('ascii', 'ignore')
                    print road
                    if filename != 0:     
                        params = paramsInsert(lat, lon, trashType, filename, address, fk_trash_type, city, suburb, neighbourhood, road)
                        query = queryInsert()
                        cursor.execute(query, params)
                    else:
                        params = paramsInsertNoImg(lat, lon, trashType, address, fk_trash_type, city, suburb, neighbourhood, road)
                        query = queryInsertNoImg()
                        cursor.execute(query, params)   
                    conn.commit()
                    d_conn = pg_operations2.pg_disconnect2(d_conn)                    
                    flash('Point uploaded', 'success')
                    return redirect(url_for('map'))
                    """
        except IntegrityError,  psycopg2.errors:
            flash('THere is already a point in the radius 10M from here!', 'danger')

            duplicateExecption(d_conn, form) 
        except ValueError, e:
            flash('THere is already a point in the radius 10M from here!', 'danger')
            print e[0]
            conn=d_conn['conn']
            conn.rollback()
            d_conn = pg_operations2.pg_disconnect2(d_conn)
            return render_template('registerTrashReporter..html', form = form)  
                
                
        """
        except Exception, e:
            print e[0]
            if e[0] == "can't adapt type 'Response'":
                flash('ERROR! Please upload only jpeg, png, gif or tif.', 'danger')
            elif e[0] == "'NoneType' object has no attribute '__getitem__'":
                flash('Coords are out of KA','danger')    
            else:
                flash('There is already a point in the radius 10M from here!', 'danger')

            conn=d_conn['conn']
            conn.rollback()
            d_conn = pg_operations2.pg_disconnect2(d_conn)
            return render_template('registerTrashReporter..html', form = form)

            #imgExecption(e, d_conn, form)   
        except:
            flash('Error!', 'danger')
            conn=d_conn['conn']
            conn.rollback()
            d_conn = pg_operations2.pg_disconnect2(d_conn)
            return render_template('registerTrashReporter..html', form = form)    
        return render_template('registerTrashReporter..html', form = form)
    

@app.route('/removePoint', methods=['GET', 'POST'])
@is_municipality
def removePoint():
        return render_template("mapTrashReporterRemove.html")



@app.route('/stats')
@is_logged_in
def stats():
    d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
    cursor=d_conn['cursor']  
    cons="""select COUNT(gid),
      timestamp without time zone 'epoch' + max(extract(epoch from created_at)) * interval '1 second',
       timestamp without time zone 'epoch' + min(extract(epoch from created_at)) * interval '1 second'
        from d.point"""
    cursor.execute(cons)
    data = cursor.fetchall()
    for i in data:
        counter = i[0]
        maxTime = str(i[1])
        minTime = str(i[2]) 
    maxTime =  str(maxTime[:19]) 
    fmt = '%Y-%m-%d %H:%M:%S'
    maxTime = datetime.strptime(maxTime, fmt)
    minTime =  str(minTime[:19]) 
    minTime = datetime.strptime(minTime, fmt)
    timeDiff = str(maxTime - minTime)
    lista = []
    lista2 = []
    dict = {}
    cons = """
    select a.trash, count(b.fk_trash_type) 
    from d.trash_type AS a INNER JOIN d.point AS b
    ON a.id = b.fk_trash_type
    group by a.trash, b.fk_trash_type
    order by b.fk_trash_type
    """    
    cursor.execute(cons)
    for i in cursor.fetchall():
        trashType = i[0]
        trashCounter = i[1]  
        lista2.append(trashType) 
        lista2.append(trashCounter) 
    neiCounterList = []    
    cons = """
    select  neighbourhood, count(b.fk_trash_type) 
    from d.trash_type AS a INNER JOIN d.point AS b
    ON a.id = b.fk_trash_type
    where neighbourhood is not null
    group by  neighbourhood, b.fk_trash_type
    order by count(b.fk_trash_type) desc
    """    
    cursor.execute(cons)
    for i in cursor.fetchall():
        nei = i[0]
        neiCounter = i[1]  
        neiCounterList.append(nei) 
        neiCounterList.append(neiCounter)
        
    
    neiCounterTrashTypeList = []    
    cons = """
    select  neighbourhood, a.trash, count(b.fk_trash_type) 
    from d.trash_type AS a INNER JOIN d.point AS b
    ON a.id = b.fk_trash_type
    where neighbourhood is not null 
    group by  neighbourhood, a. trash
    order by count(neighbourhood) desc  
    """    
    cursor.execute(cons)
    for i in cursor.fetchall():
        nei = i[0]
        trash = i[1]
        neiCounter = i[2] 
        neiCounterTrashTypeList.append(nei)  
        neiCounterTrashTypeList.append(trash)  
        neiCounterTrashTypeList.append(neiCounter)
    
    subCounterTrashTypeList = []    
    cons = """
    select  suburb, a.trash, count(b.fk_trash_type) 
    from d.trash_type AS a INNER JOIN d.point AS b
    ON a.id = b.fk_trash_type
    where suburb is not null
    group by  suburb, a.trash
    order by count(suburb) desc 
    """    
    cursor.execute(cons)
    for i in cursor.fetchall():
        nei = i[0]
        trash = i[1]
        neiCounter = i[2] 
        subCounterTrashTypeList.append(nei)  
        subCounterTrashTypeList.append(trash)  
        subCounterTrashTypeList.append(neiCounter)
    
    subCounterList = []    
    cons = """
    select  suburb,  count(b.fk_trash_type) 
    from d.trash_type AS a INNER JOIN d.point AS b
    ON a.id = b.fk_trash_type
    where suburb is not null
    group by  suburb
    order by count(b.fk_trash_type) desc
    """    
    cursor.execute(cons)
    for i in cursor.fetchall():
        nei = i[0]
        neiCounter = i[1]  
        subCounterList.append(nei) 
        subCounterList.append(neiCounter)
        
    
             
    meas = {"counter": counter, "maxTime": maxTime, "minTime":minTime, "timeDiff":timeDiff,
             "lista2":lista2, "neiCounterList":neiCounterList,
             "neiCounterTrashTypeList":neiCounterTrashTypeList,
              "subCounterTrashTypeList": subCounterTrashTypeList,
              "subCounterList":subCounterList}
    lista.append(meas)
    dict["data"]=lista
    d_conn = pg_operations2.pg_disconnect2(d_conn)
    return jsonify(dict)


@app.route('/statistics')
@is_logged_in
def statistics():
    return render_template("statsTrashReporter.html")


@app.route('/interactive/')
def interactive():
        lista = []
        dict = {}
        d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
        conn=d_conn['conn']
        cursor=d_conn['cursor']

        data = cursor.execute("SELECT  gid, st_astext(geom), address FROM d.point")
        data = cursor.fetchall()
        print data
        for row in data:
            gid = row[0]
            geom = row[1]
            address = row[2]
            meas = {"gid": gid, "geom": geom, "address":address}
            lista.append(meas)
            dict["data"]=lista
        #print dict    
        d_conn = pg_operations2.pg_disconnect2(d_conn)
        return jsonify(dict)

   
def geoJsonMaker(x,y,  road):

    data = [     {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [lon,lat]
      },
      "properties": {
        "road": road
      }
    } for lon,lat,road in zip(y,x, road)]
  
    return data

"""  
@app.route('/interactive2/')
def interactive2():
        d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
        cursor=d_conn['cursor']
        cursor.execute("SELECT longitude, latitude, road FROM d.point")
        data = cursor.fetchall()
        x = []
        y = []
        road = []
        for row in data:
            if row[2] != '' or row[2] is not None or row[2] != "None":          
                x.append(row[0])
                y.append(row[1])
                #city.append(row[2])
                road.append(row[2])
                #nei.append(row[4])
            else:
                road.append('Unknown')   
        data = geoJsonMaker(x,y,  road) 
        print len(road)   
       
        d_conn = pg_operations2.pg_disconnect2(d_conn)
        return jsonify(data)
"""   
    
@app.route('/interactive2/')
def interactive2():
        d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
        cursor=d_conn['cursor']
        cursor.execute("""SELECT b.longitude, b.latitude, a.trash
            from d.trash_type as a inner join d.point as b 
            on a.id = b.fk_trash_type""")
        data = cursor.fetchall()
        x = []
        y = []
        trash = []
        for row in data:
            x.append(row[0])
            y.append(row[1])
            trash.append(row[2])
            

        data = geoJsonMaker(x,y,  trash) 
        
           
        d_conn = pg_operations2.pg_disconnect2(d_conn)
        return jsonify(data)

@app.route('/background_process')
def background_process():
    try:
        result = request.args.get('coords', 0, type=str)       
        return jsonify(result=result)
    except Exception as e:
        return str(e)


@app.route('/deleteRowSim/<gid>', methods=('GET', 'POST',))
def deleteRowSim(gid):
    d_conn = pg_operations2.pg_connect2(database, user, password, host, port)
    conn=d_conn['conn']
    cursor=d_conn['cursor']
    cursor.execute("DELETE FROM d.point WHERE gid = %s",[gid])
    conn.commit()
    data = interactive2()
    d_conn = pg_operations2.pg_disconnect2(d_conn)
    return data


if __name__ == '__main__':
    app.run()