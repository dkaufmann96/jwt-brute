# jwt-brute
A Tool to brute force JSON Web Token secrets using a naive implementation.
For educational purposes only.

Currently only supports tokens signed using HMAC-SHA256.

# Usage

- Clone repository with
```git clone git@github.com:dkaufmann96/jwt-brute.git```
- Start with
```python jwt-brute```
- Insert a valid JWT (e.g. from https://jwt.io) and the maximum length of keys to be guessed.

# Todo

- [ ] Add support for Python3
- [ ] Validate JWT
- [ ] Add support for more algorithms
