
class Camera:
    # Camera properties
    id = 0  # 0 for webcam, 1 for external camera
    width = 640 # pixels
    height = 480  # pixels
    horizontal_mount_offset = 0  # degrees
    vertical_mount_offset = 0  # degrees 
    horizontal_FOV = 24.45  # degrees ( 2 * arctan( sensor_width / 2 * focal_length ) )
    vertical_FOV =  14.07  # degrees ( 2 * arctan( sensor_height / 2 * focal_length ) )
    fps = 10  # frames per second
