from flask import Flask, render_template

app = Flask(__name__)

# -------------------------------
# HOME / MAIN ROUTE
# -------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# -------------------------------
# ADMIN ROUTES
# -------------------------------
@app.route('/admin/home')
def admin_home():
    return render_template('Admin/HomepageAdmin.html')

@app.route('/admin/add-accounts')
def admin_add_accounts():
    return render_template('Admin/AddAccounts.html')

@app.route('/admin/add-teams')
def admin_add_teams():
    return render_template('Admin/AddTeams.html')

@app.route('/admin/list')
def admin_list():
    return render_template('Admin/List.html')

@app.route('/admin/profile')
def admin_profile():
    return render_template('Admin/Profile.html')

@app.route('/admin/teams')
def admin_teams():
    return render_template('Admin/Teams.html')


# -------------------------------
# STAFF ROUTES
# -------------------------------
@app.route('/staff/home')
def staff_home():
    return render_template('Staff/HomepageStaff.html')

@app.route('/staff/forms')
def staff_forms():
    return render_template('Staff/Forms.html')

@app.route('/staff/list')
def staff_list():
    return render_template('Staff/List.html')

@app.route('/staff/teams')
def staff_teams():
    return render_template('Staff/Teams.html')


# -------------------------------
# CIVILIANS ROUTES
# -------------------------------
@app.route('/civilians/template')
def civilians_template():
    return render_template('Civilians/template.html')


# -------------------------------
# ERROR HANDLER
# -------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# -------------------------------
# RUN APP
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)
