import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class ServiceNode(Node):
    def __init__(self):
        super().__init__("service_node")
        self.srv = self.create_service(AddTwoInts, "/penjumlahan", self.callback)

    def callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f"Hasil dari penjumlahan {request.a} + {request.b} adalah {response.sum}")
        return response

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(ServiceNode())
    rclpy.shutdown()

if __name__ == "__main__":
    main()