unset GIT_DIR
cd ~/cis191-final
git reset --hard master
sudo pkill python
gcc rabuissa.c -o rabuissa.o
sudo nohup python manage.py runserver 0.0.0.0:80 &
