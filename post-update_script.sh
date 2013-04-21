unset GIT_DIR
cd ~/nofour
git reset --hard master
sudo pkill python
sudo python manage.py runserver 0.0.0.0:80 & disown
