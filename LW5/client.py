import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class ClientNode(Node):
    def __init__(self):
        super().__init__("client_node")
        self.cl = self.create_client(AddTwoInts, "/penjumlahan")
        self.req_angka = AddTwoInts.Request()
        self.req_angka.a = 10
        self.req_angka.b = 10

        while not self.cl.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Menunggu service...")
        
        future = self.cl.call_async(self.req_angka)
        future.add_done_callback(self.callback)
    
    def callback(self, future):
        self.get_logger().info(f"Hasilnya adalah {future.result().sum}")

def main(args=None):
    rclpy.init(args=args)
    node = ClientNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()