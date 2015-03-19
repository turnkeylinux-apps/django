COMMON_OVERLAYS = tkl-webcp apache
COMMON_CONF = postfix-local tkl-webcp apache-vhost

include $(FAB_PATH)/common/mk/turnkey/mysql.mk
include $(FAB_PATH)/common/mk/turnkey.mk
