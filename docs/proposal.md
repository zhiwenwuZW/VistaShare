# VistaShare Project Proposal

## 1. Motivation & Objective

In most modern cars, we have cameras, radars, and various other sensors to protect driving safety. However, in certain scenarios, the driver's vision might be blocked by large vehicles and trucks. This could be dangerous as the driver cannot see incoming cars, bikes, or pedestrians and can cause road accidents. Therefore, we aim to design an embedded system that detects such scenarios where the driver's vision is blocked and provides them with real-time video of the visually blocked area from a camera on a nearby car.

## 2. State of the Art & Its Limitations

Traditionally, car networking refers to connecting components internal to the car using specialized communication protocols. This tech-driven infrastructure consists of many vehicle node networks that enable bidirectional interaction between vehicles and mobile devices to manage traffic, parking, and accidents. However, for safety purposes, the information gathered within one car is often insufficient to prevent traffic accidents, which motivates us to explore the feasibility of combining and sharing information across vehicles to prevent accidents. In recent years, there has been considerable research and projects in the field of V2V (vehicle-to-vehicle) communication. The main motivation for vehicular communication systems is safety and eliminating the excessive cost of traffic collisions. However, such a system can be heavily interfered with over the spectrum of other applications. Also, the widespread adoption of V2V communication in all vehicles is still evolving. Compatibility and interoperability between different vehicle manufacturers' systems can be a challenge.

## 3. Novelty & Rationale

The primary goal of this project is to enhance road safety by addressing the issue of visual obstruction caused by large vehicles or trucks. Visual blockage can lead to accidents, especially when drivers can't see smaller vehicles, bicycles, or pedestrians in their blind spots. Providing real-time video from a nearby car can help drivers make more informed decisions. The novelty here is the idea of cars collaborating to improve road safety. By sharing real-time video, cars can "see" what other vehicles see, expanding their field of view beyond their physical limitations. This collaborative approach can help drivers make safer decisions.
In our approach, we aim to use Wi-Fi to transport the live video. Leveraging Wi-Fi for communication between vehicles allows for a reliable, low-latency data link. It is also a common technology, making it accessible for most modern vehicles. We will use Raspberry Pi for our system. Implementing computer vision algorithms on the Raspberry Pi can allow the system to identify obstructions, such as large vehicles, and classify potential hazards like bicycles and pedestrians and use further AI models to fuse the stream images together to povide a vision without blockings. This is a novelty that adds intelligence to the system.

## 4. Potential Impact

If the project is successful, it will provide technical benefits including improved road safety and enhanced situational awareness for the driver. The data fusion from camera and lidars, and sharing this data through Wi-Fi communication creates a multi-modal approach to safety, allowing for better detection and decision-making. The use of Raspberry Pi for local processing of data and real-time decision-making reduces the reliance on centralized cloud-based solutions, which can be beneficial for real-time applications. On a broader scale, if the project is successful, it will help to achieve reduced accidents and improved traffic efficiency. It could inspire further innovation in automotive safety and communication systems. It may also gain traction among consumers and become a sought-after feature in vehicles, further promoting road safety.

## 5. Challenges

The principal challenge of this project is seamlessly fusing video streams from multiple vehicles into a cohesive and unobtrusive visual representation with minimal latency. Achieving this requires sophisticated algorithms capable of handling real-time data processing and integration. The system must seamlessly overlay the video feeds, ensuring there are no noticeable delays or distortions in the combined output. This is crucial for providing drivers with an accurate and timely view of their surroundings. Overcoming these technical hurdles is essential to ensure the system's reliability and effectiveness in real-world driving scenarios.

## 6. Requirements for Success

To ensure the success of our project, a large and reliable dataset is essential for training our model to accurately fuse and interpret video feeds. We also require advanced machine learning and image processing expertise to develop algorithms capable of real-time video fusion. Essential resources include high-performance computing hardware for model training and testing, as well as access to a diverse range of video feeds for a comprehensive training dataset. Skills in computer vision, machine learning, and embedded system design will be crucial.

## 7. Metrics of Success

The primary metric of success for our system is its ability to provide real-time video feeds with low latency while accurately reflecting the fused videos. Success will be measured by the system's latency, which should be minimal to ensure real-time functionality. The accuracy and seamlessness of the video fusion process are also critical, as they directly impact the driver's ability to make informed decisions. User testing and feedback will play a significant role in assessing the system's performance in real-world scenarios. Additionally, the system's reliability and consistency in various traffic conditions and environments will be evaluated.

## 8. Execution Plan

Research and Development: This phase involves thorough research into current image fusion techniques and the development of a prototype algorithm for video fusion. We are currently in this step.

Data Collection and Model Training: Gathering a diverse range of video feeds from multiple vehicles and environments to train our fusion model. This will involve collaboration with automotive partners. An object detection model has been trained but it does not satisfied all our needs. More dataset is needed.

Algorithm Optimization: Refining the fusion algorithm to ensure low latency and high accuracy. This includes testing various machine learning models and selecting the most efficient one. TODO

Hardware Integration: Implementing the algorithm on suitable hardware platforms like Raspberry Pi and testing for real-time processing capabilities. Two Raspberry pi has been set up and communications are build. 

Field Testing: Deploying the system in a controlled environment with multiple vehicles to test its effectiveness in real-world scenarios. TODO

Final Implementation: Finalizing the system. TODO

## 9. Related Work

### 9.a. Papers

In the development of the VistaShare Project, several key research papers have been identified that align closely with our objectives of seamless video fusion and object removal in live streaming. These papers provide valuable insights into the methodologies and technologies that can be leveraged for our project.

Real-time VL/IR Video Fusion Leveraging Multiple VL Apertures on Resource-Constrained Computing Platform

Summary: This study presents a method for automatic visible light/infrared image registration using multiple visible light apertures, tailored for fast computation on resource-constrained systems. Its focus on dynamic registration of high-definition video is particularly relevant for our project's aim of real-time video fusion.
Reference: Anna Svagzdys, Richard W. Demar, Gregory F. S. Hewitt, Mark Bruneau, "Real-time VL/IR video fusion leveraging multiple VL apertures on resource-constrained computing platform," Proc. SPIE 12002, Imaging and Applied Optics 2022 (3D, AIO, COSI, IS, MATH, pcAOP), 120020Q (2022); DOI: 10.1117/12.2618387.
Intelligent Live Video Streaming for Object Detection

Summary: This paper proposes a live video stream processing system that integrates features to cope with dynamic networks and achieve low latency, crucial for our project's focus on real-time video streaming and object detection.
Reference: Mingkang Chen, Jingtao Sun, Kento Aida, Renato J. Figueiredo, Yun-Jung Ku, Kensworth C. Subratie, "Intelligent Live Video Streaming for Object Detection," 2021 IEEE 23rd International Conference on High Performance Computing and Communications; IEEE 19th International Conference on Smart City; IEEE 7th International Conference on Data Science and Systems (HPCC/SmartCity/DSS), 2021, pp. 1409-1416, DOI: 10.1109/hpcc-dss-smartcity-dependsys53884.2021.00214.
One-shot Logo Detection for Large Video Datasets and Live Camera Surveillance in Criminal Investigations

Summary: This research introduces a novel approach for logo detection in live camera streams or large video datasets. The techniques discussed could be adapted for detecting and removing specific objects in live video streams, aligning with our project's goals.
Reference: Stefanos Demertzis, Sabina B. van Rooij, M. Lazaridis, Henri Bouma, Manuel Alvarez Fernandez, Johan-Martijn ten Hove, Rodrigo Sainz Mendez, P. Daras, "One-shot logo detection for large video datasets and live camera surveillance in criminal investigations," Proc. SPIE 12178, Crime and Terrorism Detection, 121780I (2023); DOI: 10.1117/12.2681903.
Multi-View Scheduling of Onboard Live Video Analytics to Minimize Frame Processing Latency

Summary: This paper presents a real-time multi-view scheduling framework for live video analytics at the edge, aiming to minimize frame processing latency. This is crucial for seamless video fusion, directly applicable to our project.
Reference: Shengzhong Liu, Tianshi Wang, Hongpeng Guo, Xinzhe Fu, P. David, Maggie B. Wigness, Archan Misra, T. Abdelzaher, "Multi-View Scheduling of Onboard Live Video Analytics to Minimize Frame Processing Latency," 2022 IEEE 42nd International Conference on Distributed Computing Systems (ICDCS), 2022, pp. 287-297, DOI: 10.1109/ICDCS54860.2022.00055.
Color Reduction in an Authenticate Live 3D Point Cloud Video Streaming System

Summary: This research discusses a live 3D point cloud video streaming system, focusing on filtering, compression, and color reduction techniques. These methods could be relevant for processing and fusing live video streams in our project.
Reference: Zainab N. Sultani, Rana F. Al-Tuma, S. Wefel, "Color Reduction in an Authenticate Live 3D Point Cloud Video Streaming System," Computers 5, no.

### 9.b. Datasets

Berkeley DeepDrive Video Dataset (BDD100K):
Description: BDD100K is a diverse driving video database with 100K videos. It includes labeled data for various tasks like image tagging, object detection, and lane detection. This dataset can be particularly useful for developing video fusion algorithms tailored to real-world driving scenarios.
URL: [Berkeley DeepDrive BDD100K](https://bdd-data.berkeley.edu/)

KITTI Vision Benchmark Suite:
Description: The KITTI dataset is one of the most well-known benchmarks for autonomous driving. It includes a variety of sensor data, including high-resolution RGB, grayscale stereo cameras, and 3D point clouds. While primarily used for autonomous driving research, its rich video and image data can be invaluable for developing and testing video fusion algorithms.
URL: [KITTI Vision Benchmark Suite](http://www.cvlibs.net/datasets/kitti/)

### 9.c. Software

removal in live streaming:

OpenCV (Open Source Computer Vision Library):

Description: Essential for image and video processing tasks.
URL: opencv.org
TensorFlow:

Description: Open-source machine learning library for model training and deployment.
URL: tensorflow.org
Debian Operating System:

Description: Stable and secure Linux distribution for development.
URL: debian.org
ZeroMQ (ZMQ):

Description: ZeroMQ is an asynchronous messaging library, ideal for distributed or concurrent applications. It's particularly useful for managing data flow in real-time applications, making it a valuable tool for handling the complexities of live video streaming and processing in our project.
URL: zeromq.org
Visual Studio Code (VSCode):

Description: Free, lightweight, and powerful code editor.
URL: code.visualstudio.com
## 10. References

List references correspondign to citations in your text above. For papers please include full citation and URL. For datasets and software include name and URL.
