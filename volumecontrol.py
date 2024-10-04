import comtypes
import comtypes.client
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume(volume_level):
    # Initialize COM library
    comtypes.CoInitialize()

    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(volume_level, None)
    finally:
        # Uninitialize COM library
        comtypes.CoUninitialize()


    return f"volume set to {volume_level}%"


