server {
    listen 80;
    server_name your_github_username.github.io;

    # Serve GitHub Pages content
    location / {
        proxy_pass https://your_github_username.github.io;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Proxy requests to the application server
    location /app {
        proxy_pass http://0.0.0.0:800;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

