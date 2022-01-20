from cloudify.decorators import operation
from cloudify.exceptions import NonRecoverableError

@operation
def my_task(ctx, **kwargs):
    try:
        ctx.logger.info("Message from pluging > my_task.")
    except BaseException:
        ctx.logger.info('My task failed')
        raise NonRecoverableError("Failed to start HTTP webserver")