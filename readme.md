# Secure Login Page with Flask

This project is a Flask application that implements a secure login page with additional features for enhanced security, including Public Key encryption using the RSA algorithm.

## Features

- **User Authentication:** Allows users to log in securely
- **Password Hashing:** User passwords are securely hashed using SHA-256 with a unique salt for each user.
- **Public Key Encryption (RSA):** Generates a key pair on each page load. The public key is rendered to the front end, and the private key is kept securely with the server.
- **Enhanced Security Measures:**
  - Users cannot paste anything into the password field.
  - Users cannot submit the form with the "Enter" key.
  - Throttling-resistant login button: The login button is enabled only 3 seconds after a request.

## Getting Started

```bash
git clone https://github.com/DhanushMuralidharan/SecureLoginPage.git
cd your-flask-app
pipenv sync