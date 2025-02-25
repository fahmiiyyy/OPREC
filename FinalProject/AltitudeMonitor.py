import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32  # Menggunakan Float32 untuk data ketinggian

class AltitudeMonitor(Node):
    def __init__(self):
        super().__init__('altitude_monitor')
        self.subscription = self.create_subscription(
            Float32,
            '/altitude',
            self.altitude_callback,
            10
        )
        self.threshold = 80.0  # Ambang batas ketinggian yang berbahaya

    def altitude_callback(self, msg):
        if msg.data > self.threshold:
            self.get_logger().warn(f"PERINGATAN! Ketinggian terlalu tinggi: {msg.data:.2f} meter")
        else:
            self.get_logger().info(f"Ketinggian aman: {msg.data:.2f} meter")


def main(args=None):
    rclpy.init(args=args)
    node = AltitudeMonitor()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()