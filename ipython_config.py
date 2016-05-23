try:
    from manage import *
    initialize_settings()
except:
    pass
# Password to use for web authentication
# c = get_config()
# c.NotebookApp.password = 'sha1:96b6954d678f:630c0a102b0b7e498dfed0b972f1b5ec19719c02'


c = get_config()

# Notebook config
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
# Ref: https://ipython.org/ipython-doc/dev/notebook/public_server.html1
# In [1]: from IPython.lib import passwd
# In [2]: passwd()
# c.NotebookApp.password = u'sha1:bcd259ccf...[your hashed password here]'
c.NotebookApp.password = 'sha1:96b6954d678f:630c0a102b0b7e498dfed0b972f1b5ec19719c02'
# It is a good idea to put it on a known, fixed port
c.NotebookApp.port = 9999

#Added for IPython 4.0
c.ConnectionFileMixin.ip = u'0.0.0.0'