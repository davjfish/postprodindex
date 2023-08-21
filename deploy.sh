#!/bin/bash
cd /opt/postprodindex_root/postprodindex
echo "######################### Sync repository with Master branch of remote repository (origin)"
git fetch origin
git reset --hard HEAD
git checkout master
git reset --hard origin/master
chown -R www-data:www-data .
chmod -R 771 .
echo "######################### activating the virtual environment"
source ../venv/bin/activate
echo "######################### updating python dependencies"
chown -R www-data:www-data ../venv
pip install -r requirements.txt
chown -R www-data:www-data ../venv
echo "######################### migrate, collect static, compile messages"
rm -r ./staticfiles # just safest to delete all the staticfiles and reimport
python manage.py compilemessages
python manage.py collectstatic --no-input
python manage.py migrate
echo "######################### clean up"
deactivate
sudo service apache2 restart
cd ~
