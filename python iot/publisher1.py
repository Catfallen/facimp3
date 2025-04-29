import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode1(Node):
    def __init__(self):
        super().__init__('publisher_node1')
        self.publisher_ = self.create_publisher(String, 'topico1', 10)
        self.timer = self.create_timer(1.0, self.publish_message)  # Publica a cada 1 segundo

    def publish_message(self):
        msg = String()
        msg.data = 'Mensagem do Publisher 1'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: "{msg.data}"')

def main():
    rclpy.init()
    node = PublisherNode1()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
