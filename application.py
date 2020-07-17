from flask import Flask

from nzt import create_app

# EB looks for an 'application' callable by default.
application = create_app()

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    
    application.debug = True
    application.run()
