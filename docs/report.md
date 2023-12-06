# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract

Provide a brief overview of the project objhectives, approach, and results.

# 1. Introduction
1. Motivation
In most modern cars, we have cameras, radars, and various other sensors to protect driving safety. However, in certain scenarios, the driver's vision might be blocked by large vehicles and trucks. This could be dangerous as the driver cannot see incoming cars, bikes, or pedestrians and can cause road accidents. Therefore, we aim to design an embedded system that detects such scenarios where the driver's vision is blocked and provides them with real-time video of the visually blocked area from a camera on a nearby car.

2. State of the Art & Its Limitations
Traditionally, car networking refers to connecting components internal to the car using specialized communication protocols. This tech-driven infrastructure consists of many vehicle node networks that enable bidirectional interaction between vehicles and mobile devices to manage traffic, parking, and accidents. However, for safety purposes, the information gathered within one car is often insufficient to prevent traffic accidents, which motivates us to explore the feasibility of combining and sharing information across vehicles to prevent accidents. In recent years, there has been considerable research and projects in the field of V2V (vehicle-to-vehicle) communication. The main motivation for vehicular communication systems is safety and eliminating the excessive cost of traffic collisions. However, such a system can be heavily interfered with over the spectrum of other applications. Also, the widespread adoption of V2V communication in all vehicles is still evolving. Compatibility and interoperability between different vehicle manufacturers' systems can be a challenge.

3. Novelty & Rationale
The primary goal of this project is to enhance road safety by addressing the issue of visual obstruction caused by large vehicles or trucks. Visual blockage can lead to accidents, especially when drivers can't see smaller vehicles, bicycles, or pedestrians in their blind spots. Providing real-time video from a nearby car can help drivers make more informed decisions. The novelty here is the idea of cars collaborating to improve road safety. By sharing real-time video, cars can "see" what other vehicles see, expanding their field of view beyond their physical limitations. This collaborative approach can help drivers make safer decisions. In our approach, we aim to use Wi-Fi to transport the live video. Leveraging Wi-Fi for communication between vehicles allows for a reliable, low-latency data link. It is also a common technology, making it accessible for most modern vehicles. We will use Raspberry Pi for our system. Implementing computer vision algorithms on the Raspberry Pi can allow the system to identify obstructions, such as large vehicles, and classify potential hazards like bicycles and pedestrians and use further AI models to fuse the stream images together to povide a vision without blockings. This is a novelty that adds intelligence to the system.

4. Potential Impact
If the project is successful, it will provide technical benefits including improved road safety and enhanced situational awareness for the driver. The data fusion from camera and lidars, and sharing this data through Wi-Fi communication creates a multi-modal approach to safety, allowing for better detection and decision-making. The use of Raspberry Pi for local processing of data and real-time decision-making reduces the reliance on centralized cloud-based solutions, which can be beneficial for real-time applications. On a broader scale, if the project is successful, it will help to achieve reduced accidents and improved traffic efficiency. It could inspire further innovation in automotive safety and communication systems. It may also gain traction among consumers and become a sought-after feature in vehicles, further promoting road safety.

5. Challenges
The principal challenge of this project is seamlessly fusing video streams from multiple vehicles into a cohesive and unobtrusive visual representation with minimal latency. Achieving this requires sophisticated algorithms capable of handling real-time data processing and integration. The system must seamlessly overlay the video feeds, ensuring there are no noticeable delays or distortions in the combined output. This is crucial for providing drivers with an accurate and timely view of their surroundings. Overcoming these technical hurdles is essential to ensure the system's reliability and effectiveness in real-world driving scenarios.

6. Requirements for Success
To ensure the success of our project, a large and reliable dataset is essential for training our model to accurately fuse and interpret video feeds. We also require advanced machine learning and image processing expertise to develop algorithms capable of real-time video fusion. Essential resources include high-performance computing hardware for model training and testing, as well as access to a diverse range of video feeds for a comprehensive training dataset. Skills in computer vision, machine learning, and embedded system design will be crucial.

7. Metrics of Success
The primary metric of success for our system is its ability to provide real-time video feeds with low latency while accurately reflecting the fused videos. Success will be measured by the system's latency, which should be minimal to ensure real-time functionality. The accuracy and seamlessness of the video fusion process are also critical, as they directly impact the driver's ability to make informed decisions. User testing and feedback will play a significant role in assessing the system's performance in real-world scenarios. Additionally, the system's reliability and consistency in various traffic conditions and environments will be evaluated.


# 2. Related Work

# 3. Technical Approach

# 4. Evaluation and Results

# 5. Discussion and Conclusions

# 6. References
