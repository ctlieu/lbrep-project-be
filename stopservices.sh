sudo systemctl stop gunicorn.socket
sudo systemctl stop gunicorn
sudo systemctl stop nginx

sudo systemctl start gunicorn.socket
sudo systemctl start gunicorn
sudo systemctl start nginx

