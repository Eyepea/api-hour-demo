api-hour-demo
=====

Start manually
--------------

In this current folder, launch: `api_hour -ac api-hour-demo:Container`

Deploy using Ansible
--------------------

#. `ansible-playbook ansible/install.yml -i ansible/inventory`
#. Customize config files in /etc/api-hour-demo/
#. Merge rsyslog config file
#. service api-hour-demo start

Deploy new version using Ansible
--------------------------------

#. `ansible-playbook ansible/update.yml`

Manual install
--------------

#. Follow pythonz install doc: https://github.com/saghul/pythonz
#. pythonz install 3.5.1
#. cd /opt
#. Git clone your app here
#. cd /opt/api-hour-demo/
#. /usr/local/pythonz/pythons/CPython-3.5.1/bin/pyvenv pyvenv
#. . pyvenv/bin/activate
#. pip install -r requirements.txt
#. cd /etc/init.d/ && ln -s /opt/api-hour-demo/etc/init.d/api-hour-demo
#. To define right boot order for your daemon (for example, your daemon needs PostgreSQL), customize file header of: /opt/api-hour-demo/etc/default/api-hour-demo
#. cd /etc/default/ && ln -s /opt/api-hour-demo/etc/default/api-hour-demo
#. update-rc.d api-hour-demo defaults
#. cp -a /opt/api-hour-demo/etc/api-hour-demo /etc/
#. Adapt rsyslog and logrotate
#. For logrotate config file, apply the access rights: rw-r--r--
#. service api-hour-demo start

To restart automatically daemon if it crashes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. apt-get install monit
#. cd /etc/monit/conf.d/ && ln -s /opt/api-hour-demo/etc/monit/conf.d/api-hour-demo
#. service monit restart
