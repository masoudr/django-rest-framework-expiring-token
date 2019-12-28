# Expiring Tokens for Django REST framework

A Django based project with token authentication expiration. Inspired by this StackOverflow answer.

## Usage

Set `EXPIRING_TOKEN_LIFESPAN` in `settings.py`.

* Generated tokens will expire after token lifespan.
* Calling `login/` API would create a new token each time.
* Fully tested with `Django 3.0` and `DRF 3.11.0`.

## Credits

* Masoud Rahimi: [masoudrahimi.com](http://masoudrahimi.com)
