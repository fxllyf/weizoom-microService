# -*- coding: utf-8 -*-

"""@package eaglet.core.watchdog.utils

Watchdog接口
需要settings里面配置SERVICE_NAME和设置logging格式
logging.basicConfig(
	format='[%(asctime)s] %(name)s %(levelname)s %(message)s', 
	datefmt="%Y-%m-%d %H:%M:%S", 
	level=logging.INFO
)
"""
__author__ = 'duhao'
import settings

DEBUG = 1
INFO = 2
WARNING = 3
ERROR = 4
ALERT = 5
logger = logging.getLogger(settings.SERVICE_NAME)

def watchdog_debug(message, log_type='WEB', user_id='0'):
	__watchdog(DEBUG, message, log_type, user_id='0')


def watchdog_info(message, log_type='WEB', user_id='0'):
	__watchdog(INFO, message, log_type, user_id='0')


def watchdog_warning(message, log_type='WEB', user_id='0'):
	__watchdog(WARNING, message, log_type, user_id='0')


def watchdog_error(message, log_type='WEB', user_id='0'):
	__watchdog(ERROR, message, log_type, user_id='0')


def watchdog_alert(message, log_type='WEB', user_id='0'):
	__watchdog(ALERT, message, log_type, user_id='0')


def __watchdog(level, message, log_type, user_id='0'):
	"""
	@param[in] level 日志级别
	@param[in] message 日志信息，通常是json格式
	@param[in] log_type 日志类型，如WEB, API, H5
	@param[in] user_id 系统账号的user id，用来追踪是哪个用户的系统中出的问题
	"""
	if type(user_id) == int:
		user_id = str(user_id)

	#由于logging的限制，自定义的输出信息都拼装到message里进行打印
	message = '%s %s %s' % (log_type, user_id, message)
	if level == DEBUG:
		logger.debug(message)
	elif level == INFO:
		logger.info(message)
	elif level == WARNING:
		logger.warn(message)
	elif level == ERROR:
		logger.error(message)
	elif level == ALERT:
		logger.critical(message)