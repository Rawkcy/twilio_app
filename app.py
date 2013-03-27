from twilio.rest import TwilioRestClient
from flask import Flask
from flask import request, redirect, render_template
app = Flask(__name__)

#account_sid = 'ACa95d4833ae0e1fcde23ef249b0cf76e2'
#auth_token = 'deb69cf87422539b98e424b01173ea3d'
#call = client.calls.create(to='+14082215170',\
#                           from_='+17204663863',\
#                           url='http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient')

@app.route('/', methods=['GET', 'POST'])
def index():
  """
  Website landing page
  """
  if request.method == 'POST':
    fm = request.form
    return redirect('%s/%s/%s/%s' \
        % (fm['account_sid'], fm['auth_token'], fm['from_'], fm['to']))
  return render_template('index.html')

@app.route('/<account_sid>/<auth_token>/<from_>/<to>')
def make_call(account_sid, auth_token, from_, to):
  """
  Make a phone call
  """
  client = TwilioRestClient(account_sid, auth_token)
  call = client.calls.create(to='+1%s' % to, from_='+1%s' % from_, \
      url='http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient')
  return 'Sucessfully called!'

if __name__=='__main__':
  app.run(debug=True)

