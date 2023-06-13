from datetime import timedelta


class Config:
    # SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/db_shop_g20"
    SQLALCHEMY_DATABASE_URI = "postgresql://db_shop_g20_lny8_user:mIc1hY6lqEoVfBIIqR45xwvU4gZ0GOLW@dpg-ci4en0lgkuvm71dm53jg-a.ohio-postgres.render.com/db_shop_g20_lny8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "asdfhasdfhlkasdfl32h"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
