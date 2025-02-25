import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32  # Menggunakan Float32 untuk data ketinggian
import datetime

class AltitudeLogger(Node):
    def __init__(self):
        super().__init__('altitude_logger')
        self.subscription = self.create_subscription(
            Float32,
            '/altitude',
            self.altitude_callback,
            10
        )
        self.log_file = "altitude_log.txt"

    def altitude_callback(self, msg):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - Ketinggian: {msg.data:.2f} meter\n"
        
        with open(self.log_file, 'a') as file:
            file.write(log_entry)
        
        self.get_logger().info(f"Data ketinggian dicatat: {msg.data:.2f} meter")


def main(args=None):
    rclpy.init(args=args)
    node = AltitudeLogger()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()