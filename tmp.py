from datetime import date
from borax.calendars.lunardate import LunarDate
from borax.calendars.festivals2 import LunarFestival, Period

solar_birth = date(1997, 6, 24)
lunar_birth = LunarDate.from_solar(solar_birth) # 出生那天的农历日期
print(lunar_birth)  # LunarDate(1994, 4, 11, 0)

# 农历生日对应的节日对象
lunar_birth_festival = LunarFestival(month=lunar_birth.month, day=lunar_birth.day)

# [<WrappedDate:2020-05-03(二〇二〇年四月十一)>, <WrappedDate:2020-06-02(二〇二〇年闰四月十一)>]
wd_list = lunar_birth_festival.list_days(*Period.lunar_year(2021))

leap_day_included = True
if not leap_day_included:
    wd_list = [wd for wd in wd_list if wd.lunar.leap == 0] # 去掉其中的闰月日期
print(wd_list)