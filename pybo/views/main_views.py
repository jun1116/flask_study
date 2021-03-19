from flask import Blueprint
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/bp')
def hellp_pybo():
    return 'HELLO PYBO BLUE PRINT'
