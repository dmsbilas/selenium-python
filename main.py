import sys;
sys.path.append("/modules/login/login.py");

from modules.login.login import Login;
from modules.admin.admin import AdminDashboard;

login_test_cls = Login();
admin_dashboard_test_cls = AdminDashboard(login_test_cls.get_driver_instance());

# Processing login
login_test_cls.open_login_page();
login_test_cls.apply_wait();
login_test_cls.give_username();
login_test_cls.give_password();
login_test_cls.submit_login_form();
login_test_cls.apply_wait();
login_test_cls.close_popups();
login_test_cls.login_test_result();
login_test_cls.apply_wait();

# Traversing Admin panel dashboard
# admin_test_cls.click_admin_menu();
count = 0 ;
# h = 360 ;
while (count<720):
    admin_dashboard_test_cls.traverse_admin_dashboard();
    count +=1;





