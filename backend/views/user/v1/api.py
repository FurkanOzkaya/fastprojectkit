from fastapi import APIRouter
from views.user.v1.register import router as register_view
from views.user.v1.all_users import router as all_users
from views.user.v1.get_user import router as get_user
from views.user.v1.update import router as update_user
from views.user.v1.login import router as login_user
from views.user.v1.password_change import router as password_change
from views.user.v1.statistic.access_level_ratio import router as access_level_ratio
from views.user.v1.statistic.monthly_user_ratio import router as monthly_user_ratio
from views.user.v1.change_avatar import router as change_avatar


router = APIRouter()

prefix = "/user"

router.include_router(get_user, prefix=prefix)
router.include_router(all_users, prefix=prefix)
router.include_router(register_view, prefix=prefix)
router.include_router(login_user, prefix=prefix)
router.include_router(change_avatar, prefix=prefix)
router.include_router(update_user, prefix=prefix)
router.include_router(password_change, prefix=prefix)
router.include_router(access_level_ratio, prefix=prefix)
router.include_router(monthly_user_ratio, prefix=prefix)
