from Frontend.ElementWidget import IncXWidget, LandWidget, PosSetWidget, IncYawWidget, IncZWidget, IncYWidget

ElementMimeType = 'application/x-cf-element'

# {
#     'INC_X':   'application/x-cf-element-inc-x',
#     'INC_Y':   'application/x-cf-element-inc-y',
#     'INC_Z':   'application/x-cf-element-inc-z',
#     'INC_YAW': 'application/x-cf-element-inc-yaw',
#     'POS_SET': 'application/x-cf-element-pos-set',
#     'LAND':    'application/x-cf-element-land',
# }

#
# def isElementMimeType(inMime):
#     for elMime in ElementMimeType.values():
#         if inMime.hasFormat(elMime):
#
#             return True
#     return False





ElementIconPath = {
    '0_INC_X': 'Icons\IncX.svg',
    '1_INC_Y': 'Icons\IncY.svg',
    '2_INC_Z': 'Icons\IncZ.svg',
    '3_INC_YAW': 'Icons\IncYaw.svg',
    '4_POS_SET': 'Icons\PosSet.svg',
    '5_LAND': 'Icons\Land.svg',
    '6_LOOP': 'Icons\Loop.svg'
}

ElementWidgetType = {
    '0_INC_X': 'IncXWidget',
    '1_INC_Y': 'IncYWidget',
    '2_INC_Z': 'IncZWidget',
    '3_INC_YAW': 'IncYawWidget',
    '4_POS_SET': 'PosSetWidget',
    '5_LAND': 'LandWidget',
    '6_LOOP': 'LoopWidget'
}

TrashIconPath = 'Icons\Trash.svg'
