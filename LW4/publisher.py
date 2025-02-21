import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__("publisher_node")
        self.publisher = self.create_publisher(String, "/ngobrol", 10)
        self.angka = 99
        self.pub = self.create_timer(0.5, self.publish)
    
    def publish(self):
        msg = String()
        msg.data = str(self.angka)
        self.publisher.publish(msg)
        self.get_logger().info("Halo rek gua angka " + str(self.angka))
        self.angka += 1

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
