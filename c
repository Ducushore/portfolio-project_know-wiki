server {
    listen 80;
    server_name 167.172.109.205;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/djangodldeploy/portfolio-project_know-wiki;
    }
    location /media/ {
        root /home/djangodldeploy/portfolio-project_know-wiki;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    #    proxy_pass http://unix:/home/djangodldeploy/portfolio-project_know-wiki/portfolio.sock;
    }
}

