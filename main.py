import sys;
sys.path.append("/modules/login/login.py");

from modules.login.login import Login;

login_test_cls = Login();

login_test_cls.open_login_page();
login_test_cls.apply_wait();
login_test_cls.give_username();
login_test_cls.give_password();
login_test_cls.submit_login_form();
login_test_cls.apply_wait();
login_test_cls.close_popups();
login_test_cls.login_test_result();

login_test_cls.apply_wait();
login_test_cls.close_browser();



