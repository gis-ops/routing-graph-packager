import logging
from flask import current_app, g
from flask_restx import abort
from flask_restx.errors import HTTPStatus
from sqlalchemy import exc

log = logging.getLogger(__name__)

HTTP_EXC = {
    HTTPStatus.CONFLICT.value: {
        "code": HTTPStatus.CONFLICT,
        "error": "Entity already exists, aborting.."
    }
}


def add_or_abort(object):
    """Commit the object or abort"""
    session = g.db.session
    success = False
    try:
        session.add(object)
        session.commit()
        success = True
    except exc.IntegrityError as e:
        log.error(f"Transaction aborted because: {e}")
        abort(**HTTP_EXC[HTTPStatus.CONFLICT])
    except Exception as e:  # pragma: no cover
        log.error(f"Transaction aborted because: {e}")
        abort(code=HTTPStatus.INTERNAL_SERVER_ERROR, status=str(e))
    finally:
        if not success:
            session.rollback()


def add_admin_user():
    """Add admin user before first request"""
    admin_email = current_app.config['ADMIN_EMAIL']
    admin_pass = current_app.config['ADMIN_PASS']

    from .api_v1.users.models import User
    if not User.query.filter_by(email=admin_email).first():
        admin_user = User(email=admin_email, password=admin_pass)
        session = g.db.session
        session.add(admin_user)
        session.commit()
