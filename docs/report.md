# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract

The "VistaShare Driving Aid" employs a Raspberry Pi-based system to enhance road safety. Utilizing camera modules and mini LiDAR, it detects when a driver's view of traffic lights is obstructed. In such events, it activates a live feed from a secondary vehicle, providing the obstructed driver with an alternative view. This innovative approach promises to improve situational awareness at intersections, potentially reducing accident rates and paving the way for collaborative safety features in smart transportation networks.

# 1. Introduction
# Motivation
In most modern cars, we have cameras, radars, and various other sensors to protect driving safety. However, in certain scenarios, the driver's vision might be blocked by large vehicles and trucks. This could be dangerous as the driver cannot see incoming cars, bikes, or pedestrians and can cause road accidents. Therefore, we aim to design an embedded system that detects such scenarios where the driver's vision is blocked and provides them with real-time video of the visually blocked area from a camera on a nearby car.

# State of the Art & Its Limitations
Traditionally, car networking refers to connecting components internal to the car using specialized communication protocols. This tech-driven infrastructure consists of many vehicle node networks that enable bidirectional interaction between vehicles and mobile devices to manage traffic, parking, and accidents. However, for safety purposes, the information gathered within one car is often insufficient to prevent traffic accidents, which motivates us to explore the feasibility of combining and sharing information across vehicles to prevent accidents. In recent years, there has been considerable research and projects in the field of V2V (vehicle-to-vehicle) communication. The main motivation for vehicular communication systems is safety and eliminating the excessive cost of traffic collisions. However, such a system can be heavily interfered with over the spectrum of other applications. Also, the widespread adoption of V2V communication in all vehicles is still evolving. Compatibility and interoperability between different vehicle manufacturers' systems can be a challenge.

# Novelty & Rationale
The primary goal of this project is to enhance road safety by addressing the issue of visual obstruction caused by large vehicles or trucks. Visual blockage can lead to accidents, especially when drivers can't see smaller vehicles, bicycles, or pedestrians in their blind spots. Providing real-time video from a nearby car can help drivers make more informed decisions. The novelty here is the idea of cars collaborating to improve road safety. By sharing real-time video, cars can "see" what other vehicles see, expanding their field of view beyond their physical limitations. This collaborative approach can help drivers make safer decisions. In our approach, we aim to use Wi-Fi to transport the live video. Leveraging Wi-Fi for communication between vehicles allows for a reliable, low-latency data link. It is also a common technology, making it accessible for most modern vehicles. We will use Raspberry Pi for our system. Implementing computer vision algorithms on the Raspberry Pi can allow the system to identify obstructions, such as large vehicles, and classify potential hazards like bicycles and pedestrians and use further AI models to fuse the stream images together to povide a vision without blockings. This is a novelty that adds intelligence to the system.

# Potential Impact
If the project is successful, it will provide technical benefits including improved road safety and enhanced situational awareness for the driver. The data fusion from camera and lidars, and sharing this data through Wi-Fi communication creates a multi-modal approach to safety, allowing for better detection and decision-making. The use of Raspberry Pi for local processing of data and real-time decision-making reduces the reliance on centralized cloud-based solutions, which can be beneficial for real-time applications. On a broader scale, if the project is successful, it will help to achieve reduced accidents and improved traffic efficiency. It could inspire further innovation in automotive safety and communication systems. It may also gain traction among consumers and become a sought-after feature in vehicles, further promoting road safety.

# Challenges
The principal challenge of this project is seamlessly fusing video streams from multiple vehicles into a cohesive and unobtrusive visual representation with minimal latency. Achieving this requires sophisticated algorithms capable of handling real-time data processing and integration. The system must seamlessly overlay the video feeds, ensuring there are no noticeable delays or distortions in the combined output. This is crucial for providing drivers with an accurate and timely view of their surroundings. Overcoming these technical hurdles is essential to ensure the system's reliability and effectiveness in real-world driving scenarios.

# Requirements for Success
To ensure the success of our project, a large and reliable dataset is essential for training our model to accurately fuse and interpret video feeds. We also require advanced machine learning and image processing expertise to develop algorithms capable of real-time video fusion. Essential resources include high-performance computing hardware for model training and testing, as well as access to a diverse range of video feeds for a comprehensive training dataset. Skills in computer vision, machine learning, and embedded system design will be crucial.

# Metrics of Success
The primary metric of success for our system is its ability to provide real-time video feeds with low latency while accurately reflecting the fused videos. Success will be measured by the system's latency, which should be minimal to ensure real-time functionality. The accuracy and seamlessness of the video fusion process are also critical, as they directly impact the driver's ability to make informed decisions. User testing and feedback will play a significant role in assessing the system's performance in real-world scenarios. Additionally, the system's reliability and consistency in various traffic conditions and environments will be evaluated.


# 2. Related Work

In the development of the VistaShare Project, several key research papers have been identified that align closely with our objectives of seamless video fusion and object removal in live streaming. These papers provide valuable insights into the methodologies and technologies that can be leveraged for our project.

Real-time VL/IR Video Fusion Leveraging Multiple VL Apertures on Resource-Constrained Computing Platform
Summary: This study presents a method for automatic visible light/infrared image registration using multiple visible light apertures, tailored for fast computation on resource-constrained systems. Its focus on dynamic registration of high-definition video is particularly relevant for our project's aim of real-time video fusion.

Intelligent Live Video Streaming for Object Detection
Summary: This paper proposes a live video stream processing system that integrates features to cope with dynamic networks and achieve low latency, crucial for our project's focus on real-time video streaming and object detection.

One-shot Logo Detection for Large Video Datasets and Live Camera Surveillance in Criminal Investigations
Summary: This research introduces a novel approach for logo detection in live camera streams or large video datasets. The techniques discussed could be adapted for detecting and removing specific objects in live video streams, aligning with our project's goals.

Multi-View Scheduling of Onboard Live Video Analytics to Minimize Frame Processing Latency
Summary: This paper presents a real-time multi-view scheduling framework for live video analytics at the edge, aiming to minimize frame processing latency. This is crucial for seamless video fusion, directly applicable to our project.

Color Reduction in an Authenticate Live 3D Point Cloud Video Streaming System
Summary: This research discusses a live 3D point cloud video streaming system, focusing on filtering, compression, and color reduction techniques. These methods could be relevant for processing and fusing live video streams in our project.

# 3. Technical Approach

### Hardware Setup
Our project utilizes two Raspberry Pi 4B models, each equipped with a Raspberry Pi camera module. These devices are installed on cars to function as endpoint devices for video streaming. The Raspberry Pis are powered through power banks and the car's power plug-ins. The setup does not involve any additional peripherals, ensuring a focused and streamlined hardware configuration.

### Software Setup
The Raspberry Pis operate on Python 3.8 with the 2023 Bulleye 64-bit OS. For video streaming, we employ a TCP protocol, with the video encoded and decoded using pybase64. The video streams have a resolution of 640x480 and a frame rate of 5 fps. The server, a laptop running Windows, is connected to the Raspberry Pis via SSH over Wi-Fi. This setup allows for remote commanding and efficient management of the devices.

### Data Processing and Analysis
The video data, once streamed to the laptop, undergoes object detection using the YOLOv8n model, chosen for its speed. The process involves analyzing the detection results to identify the bounding box of a car in view 2, which is intended for erasure. Additionally, we identify objects common to both views. By using these common objects, we calculate an average resize ratio for the target object. This calculated ratio is then used to appropriately resize and paste the bounding box from view 1 onto view 2, effectively replacing the specified area.

This approach demonstrates a robust combination of hardware efficiency and sophisticated software processing, leveraging the capabilities of the Raspberry Pi and advanced object detection algorithms for real-time video analysis and manipulation.

# 4. Evaluation and Results
Our field test results shows that our system works successfully. We initially tested the sensors and microprocessors’s connection to made sure they work well together and the connections are stable and robust. We also tested the camera capture ability and made sure they transmit video to the laptop’s screen synchronized and with low latency. Then we tested the object detection model, and the model works well in identifying almost all the objects in the classifying labels. Finally, we ran the whole system with video fusion capability in a real world setting. We prepared two cars, setup one camera in the front car and one in the back car, as shown in the picture below. Then we started driving both cars at the same time at a steady speed. We were able to visualize the two live videos captured by the two cameras and the synthesized video upon video fusion. The resulting videos are stored to a root directory of an Android phone in real time, which can be launched using a customized mobile application to view. The quality of the resulting video is pretty good in most scenarios. The detection of the front car as well as other obstructions are accurate, and the fused video looks natural with only a few exceptions in complicated road or lighting conditions. 
![20231210_154440](https://github.com/zhiwenwuZW/VistaShare/assets/77821123/acdcee0f-59af-4454-a9a9-01d4532e2975)
![Screenshot_20231212_022641_VistaShare](https://github.com/zhiwenwuZW/VistaShare/assets/77821123/b393ade1-ed27-4119-9830-017b7d9eba0d)



# 5. Discussion and Conclusions
In this project, we have managed to achieve most of the goals and objectives we formulated in the plan. We are satisfied with the progress we have made; however, there are still a few items and functionalities that we would like to improve in the future.
Firstly, the video fusion functionality can be enhanced. The smoothness and correctness of the video captured by the car in front are not optimal in some cases. With more data and a more optimized image fusion algorithm, we could minimize the overlapping areas between the videos from the two cameras and stitch the front car’s video frame into the cropped region more seamlessly, making the fused video look more natural.
Secondly, currently, we are using objects of selected classes, such as stop signs and surrounding cars, to determine the resizing factor of the fused region. However, if there are multiple objects of the same class, such as multiple stop signs in the video frame, it becomes challenging to correspond the objects in the two cameras and derive an accurate resizing factor. To address this issue, we might need a mechanism to select only one object from a single class or use a combination of different objects present in both camera's video frames to calculate the resizing factor.

# 6. References
#### Papers

1. Svagzdys, Anna, et al. "Real-time VL/IR video fusion leveraging multiple VL apertures on resource-constrained computing platform." *Proc. SPIE 12002, Imaging and Applied Optics 2022 (3D, AIO, COSI, IS, MATH, pcAOP)*, 2022, DOI: 10.1117/12.2618387. [Link](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/12002/120020Q/Real-time-VL-IR-video-fusion-leveraging-multiple-VL-apertures/10.1117/12.2618387.short)

2. Chen, Mingkang, et al. "Intelligent Live Video Streaming for Object Detection." *2021 IEEE 23rd International Conference on High Performance Computing and Communications; IEEE 19th International Conference on Smart City; IEEE 7th International Conference on Data Science and Systems (HPCC/SmartCity/DSS)*, 2021, pp. 1409-1416, DOI: 10.1109/hpcc-dss-smartcity-dependsys53884.2021.00214. [Link](https://ieeexplore.ieee.org/document/9662024)

3. Demertzis, Stefanos, et al. "One-shot logo detection for large video datasets and live camera surveillance in criminal investigations." *Proc. SPIE 12178, Crime and Terrorism Detection*, 2023, DOI: 10.1117/12.2681903. [Link](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/12178/121780I/One-shot-logo-detection-for-large-video-datasets-and-live/10.1117/12.2681903.short)

4. Liu, Shengzhong, et al. "Multi-View Scheduling of Onboard Live Video Analytics to Minimize Frame Processing Latency." *2022 IEEE 42nd International Conference on Distributed Computing Systems (ICDCS)*, 2022, pp. 287-297, DOI: 10.1109/ICDCS54860.2022.00055. [Link](https://ieeexplore.ieee.org/document/9835401)

5. Sultani, Zainab N., et al. "Color Reduction in an Authenticate Live 3D Point Cloud Video Streaming System." *Computers 5*, no. 4, 2016. [Link](https://www.mdpi.com/2073-431X/5/4/24)

6. Qiu, H., Ahmad, F., Bai, F., Gruteser, M., & Govindan, R. (2018). AVR: Augmented Vehicular Reality. Proceedings of the 16th Annual International Conference on Mobile Systems, Applications, and Services.[Link](https://www.winlab.rutgers.edu/~gruteser/papers/mobisys18-7-qiu.pdf)
   
#### Datasets

6. "Berkeley DeepDrive BDD100K." [Link](https://bdd-data.berkeley.edu/)

7. "KITTI Vision Benchmark Suite." [Link](http://www.cvlibs.net/datasets/kitti/)

#### Software

8. "OpenCV (Open Source Computer Vision Library)." [Link](https://opencv.org/)

9. "TensorFlow." [Link](https://www.tensorflow.org/)

10. "Debian Operating System." [Link](https://www.debian.org/)

11. "ZeroMQ (ZMQ)." [Link](https://zeromq.org/)

12. "Visual Studio Code (VSCode)." [Link](https://code.visualstudio.com/)

13. "Android Studio." [Link](https://developer.android.com/studio)
