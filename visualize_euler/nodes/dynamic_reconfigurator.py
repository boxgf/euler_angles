#!/usr/bin/env python

import rospy
from dynamic_reconfigure.server import Server
from visualize_euler.cfg import EulerAnglesConfig
import tf
import numpy as np

class DynamicReconfigurator:
  def __init__(self):
    self.tf_braodcaster = tf.TransformBroadcaster()
    self.quaternion_from_euler = tf.transformations.quaternion_from_euler
  def callback(self, config, level):
    self.tf_braodcaster.sendTransform((0, 0, 0),
						 self.quaternion_from_euler(np.pi/180*config['rot_1'], np.pi/180*config['rot_2'], np.pi/180*config['rot_3'], config['convention']),
						 rospy.Time.now(),
						 '/base_link',
						 '/transformed')
                     
    return config
    
def main():
  rospy.init_node('euler_angles', anonymous=True)
  dynamic_reconfigurator = DynamicReconfigurator()
  server = Server(EulerAnglesConfig, dynamic_reconfigurator.callback)
  rospy.spin()
if __name__ == "__main__":
  main()
