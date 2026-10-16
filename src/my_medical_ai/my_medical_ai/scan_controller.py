#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration


class ScanController(Node):
    def __init__(self):
        super().__init__('scan_controller')
        self.publisher = self.create_publisher(
            JointTrajectory, '/joint_trajectory_controller/joint_trajectory', 10)
        self.timer = self.create_timer(2.0, self.scan)
        self.step = 0
        self.joint_names = [
            'joint1',
            'joint2',
            'joint3',
            'joint4',
            'joint5',
            'joint6',
            'joint7',
        ]
        self.positions = [
            # Home
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            # IK poses put the camera 0.20 m above the marker at (0.4, 0, 0.04),
            # with its optical axis pointing down.
            # Scan center: camera at (0.40, 0.00, 0.24)
            [0.609356, 1.431468, -1.514061, -1.819377, 0.151292, -1.683123, 0.020391],
            # Scan left: camera at (0.37, 0.00, 0.24)
            [0.587027, 1.428525, -1.501689, -1.913908, 0.159419, -1.703685, 0.016818],
            # Scan near side: camera at (0.40, 0.03, 0.24)
            [0.679811, 1.429196, -1.516518, -1.819386, 0.152189, -1.662472, 0.017409],
            # Scan right: camera at (0.43, 0.00, 0.24)
            [0.633897, 1.434801, -1.524612, -1.724814, 0.143517, -1.653147, 0.024487],
            # Scan far side: camera at (0.40, -0.03, 0.24)
            [0.538662, 1.434772, -1.511326, -1.813919, 0.149378, -1.693344, 0.024697],
            # Return to center, then home
            [0.609356, 1.431468, -1.514061, -1.819377, 0.151292, -1.683123, 0.020391],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        ]
        self.get_logger().info('[SCAN] Scan Controller started. Autonomous scan begins.')

    def scan(self):
        msg = JointTrajectory()
        msg.joint_names = self.joint_names
        point = JointTrajectoryPoint()
        point.positions = self.positions[self.step % len(self.positions)]
        point.time_from_start = Duration(sec=1, nanosec=0)
        msg.points.append(point)
        self.publisher.publish(msg)
        self.get_logger().info(f'[SCAN] Point {self.step + 1} of {len(self.positions)}')
        self.step += 1


def main(args=None):
    rclpy.init(args=args)
    node = ScanController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
