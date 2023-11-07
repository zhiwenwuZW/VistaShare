# VistaShare Project Proposal

## 1. Motivation & Objective

In most modern cars, we have cameras and radar and various other sensors to protect driving safety. However, in certain scenarios, the driver's vision might be blocked by large vehicles and trucks. This could be dangerous as the driver can not see incoming cars, bikes, or pedestrians and can cause road accidents. Therefore, we aim to design an embedded system that detects such scenarios where the driver's vision is blocked and provide them with real-time video of the visually blocked area from camera on a nearby car. 

## 2. State of the Art & Its Limitations

Traditionally, car networking refers to connecting components internal to the car using specialized communication protocols. This tech-driven infrastructure consists of many vehicle node networks that enable bidirectional interaction between vehicles and mobile devices to manage traffic, parking, and accidents. However, for safety purposes, the information gathered within one car is often insufficient to prevent traffic accidents, which motivates us to explore the feasibility of combining and sharing information across vehicles to prevent accidents. In recent years, there have been considerable research and projects in the field of V2V (vehicle-to-vehicle) communication. The main motivation for vehicular communication systems is safety and eliminating the excessive cost of traffic collisions. However, such system can be heavily interfered over the spectrum of other applications. Also, the widespread adoption of V2V communication in all vehicles is still evolving. Compatibility and interoperability between different vehicle manufacturers' systems can be a challenge.

## 3. Novelty & Rationale

The primary goal for this project is to enhance road safety by addressing the issue of visual obstruction caused by large vehicles or trucks. Visual blockage can lead to accidents, especially when drivers can't see smaller vehicles, bicycles, or pedestrians in their blind spots. Providing real-time video from a nearby car can help drivers make more informed decisions. The novelty here is the idea of cars collaborating to improve road safety. By sharing real-time video, cars can "see" what other vehicles see, expanding their field of view beyond their physical limitations. This collaborative approach can help drivers make safer decisions.
In our approach, we aim to use Wi-Fi to transport the live video. Leveraging Wi-Fi for communication between vehicles allows for a reliable, low-latency data link. It is also a common technology, making it accessible for most modern vehicles. We will use Raspberry Pi for our system. Implementing computer vision algorithms on the Raspberry Pi can allow the system to identify obstructions, such as large vehicles, and classify potential hazards like bicycles and pedestrians. This is a novelty that adds intelligence to the system.

## 4. Potential Impact

If the project is successful, it will provide technical benefits including improved road safety and enhanced situational awareness for the driver. The data fusion from camera and lidars, and sharing this data through Wi-Fi communication creates a multi-modal approach to safety, allowing for better detection and decision-making. The use of Raspberry Pi for local processing of data and real-time decision-making reduces the reliance on centralized cloud-based solutions, which can be beneficial for real-time applications. On a broader scale, if the project is successful, it will help to achieve reduced accidents and improved traffic efficiency. It could inspire further innovation in automotive safety and communication systems. It may also gain traction among consumers and become a sought-after feature in vehicles, further promoting road safety.
## 5. Challenges

What are the challenges and risks?

## 6. Requirements for Success

What skills and resources are necessary to perform the project?

## 7. Metrics of Success

What are metrics by which you would check for success?

## 8. Execution Plan

Describe the key tasks in executing your project, and in case of team project describe how will you partition the tasks.

## 9. Related Work

### 9.a. Papers

Collaborative driving, V2V, CV detection of human and moving objects, etc.
List the key papers that you have identified relating to your project idea, and describe how they related to your project. Provide references (with full citation in the References section below).


### 9.b. Datasets

List datasets that you have identified and plan to use. Provide references (with full citation in the References section below).

### 9.c. Software

List softwate that you have identified and plan to use. Provide references (with full citation in the References section below).

## 10. References

List references correspondign to citations in your text above. For papers please include full citation and URL. For datasets and software include name and URL.
