import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32  # Harus sama dengan tipe data publisher

class AltitudeSubscriber(Node):
    def __init__(self):
        super().__init__("altitude_subscriber")
        self.subscription = self.create_subscription(Float32, "/altitude", self.altitude_callback, 10)

    def altitude_callback(self, msg):
        self.get_logger().info(f"Menerima data ketinggian: {msg.data:.2f} meter")

def main(args=None):
    rclpy.init(args=args)
    node = AltitudeSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
