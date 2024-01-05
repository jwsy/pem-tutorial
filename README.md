# pem-tutorial

Code for the medium article https://itnext.io/pem-file-basics-with-mkcert-and-docker-07a7b99d9353

In this article, we’ll learn about certificates & keys in PEM (Privacy Enhanced Mail) format, root Certificate Authorities, and use them so that my internal offline systems can access a server with a custom (self-signed) certificate. This article is a basic overview of PEM files, what they look like, and how to add them to a Amazon Linux (and also Fedora/RedHat) server running in a Docker container on your laptop. As a cybersecurity professional, doing these tasks was very enlightening to me! 🧠 ⚡️

Table of Contents
- What is a PEM (Privacy Enhanced Mail) file❓ (1/10)
- Get a PEM file from your browser 🗺 (2/10)
- Inspect the PEM file with openssl 🔍 (3/10)
- What is a root Certificate Authority (CA)? Create one with mkcert to understand (4/10)
- Create a self-signed certificate and key for https://dev.localhost 🖋 (5/10)
- Run an internal HTTPS service with the cert with Python 🐍 (6/10)
- Un-trust the CA and make a successful curl request by specifying the CA cert (7/10)
- Make a new Amazon Linux host with Docker that will trust the self-signed CA 🐳 (8/10)
- Update the Linux server to trust this new CA (9/10)
- Conclusion (10/10) 🙌