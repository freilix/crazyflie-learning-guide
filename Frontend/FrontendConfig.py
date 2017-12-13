from Frontend.ElementWidget import IncXWidget, LandWidget, PosSetWidget, IncYawWidget, IncZWidget, IncYWidget

ElementMimeType = {
    'INC_X':   'application/x-cf-element-inc-x',
    'INC_Y':   'application/x-cf-element-inc-y',
    'INC_Z':   'application/x-cf-element-inc-z',
    'INC_YAW': 'application/x-cf-element-inc-yaw',
    'POS_SET': 'application/x-cf-element-pos-set',
    'LAND':    'application/x-cf-element-land',
}


def isElementMimeType(inMime):
    for elMime in ElementMimeType.values():
        if inMime.hasFormat(elMime):

            return True
    return False





ElementIconPath = {
    'INC_X': 'Icons\IncX.svg',
    'INC_Y': 'Icons\IncY.svg',
    'INC_Z': 'Icons\IncZ.svg',
    'INC_YAW': 'Icons\IncYaw.svg',
    'POS_SET': 'Icons\PosSet.svg',
    'LAND': 'Icons\Land.svg',
}

ElementWidgetType = {
    'INC_X': 'IncXWidget',
    'INC_Y': 'IncYWidget',
    'INC_Z': 'IncZWidget',
    'INC_YAW': 'IncYawWidget',
    'POS_SET': 'PosSetWidget',
    'LAND': 'LandWidget',
}

TrashIconPath = 'Icons\Trash.svg'
