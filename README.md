# CRAZYFLIES ROS PACKAGE

(Note -- These are just basic files, no pkg has actually been created or tested yet)

## Functionality
--------------
###### CFNode{id}:
* subscribes to cf/{id}/command and motion
* publishes to cf/{id}/data and image


###### GroundStation:
* for each {id}
* subscribes to cf/{id}/data and image
* publishes to cf/{id}/command and motion



## ROS Layout
--------------
#### NODES
* cf_node.py
* ground_node.py


#### TOPICS
* /cf/{id}/image
* /cf/{id}/data
* /cf/{id}/motion
* /cf/{id}/command
       

#### MESSAGES

###### CFData
* float accel_x
* float accel_y
* float accel_z

###### CFMotion
* float vel_x
* float vel_y
* float altitude

###### CFCommand
* EMERGENCY-STOP = 0, LAND = 1, TAKEOFF = 2
* int cmd


