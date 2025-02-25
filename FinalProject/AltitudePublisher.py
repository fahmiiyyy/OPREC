import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32  # Menggunakan Float32 untuk data ketinggian
import random  # Untuk mensimulasikan perubahan ketinggian drone

class AltitudePublisher(Node):
    def __init__(self):
        super().__init__("altitude_publisher")
        self.publisher = self.create_publisher(Float32, "/altitude", 10)
        self.timer = self.create_timer(1.0, self.publish_altitude)  # Publish setiap 1 detik

    def publish_altitude(self):
        altitude = random.uniform(0.0, 100.0)  # Simulasi ketinggian antara 0 - 100 meter
        msg = Float32()
        msg.data = altitude
        self.publisher.publish(msg)
        self.get_logger().info(f"Ketinggian drone saat ini: {altitude:.2f} meter")

def main(args=None):
    rclpy.init(args=args)
    node = AltitudePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
