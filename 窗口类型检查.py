from maa.toolkit import Toolkit

for i in Toolkit.find_desktop_windows():
    print(i)


@staticmethod
def find_desktop_windows() -> List[DesktopWindow]:
    """查询所有窗口信息 / Query all window info

    Returns:
        List[DesktopWindow]: 窗口列表 / Window list
    """
    Toolkit._set_api_properties()
