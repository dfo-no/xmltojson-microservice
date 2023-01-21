from service.ehf import bp


@bp.route("/")
@bp.route("/invoice")
def ehf():
    return "Hello, World!"
