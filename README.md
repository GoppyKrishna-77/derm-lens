<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="https://github.com/GoppyKrishna-77/derm-lens/assets/83293163/1c3a1988-276b-4c95-840d-e1616616e70d" type="png" alt="png" width="750">

  <h1 align="center">DermLens</h1>

  <p align="left">
   An AI-based Mobile and Web App to identify dermatological
diseases 
    <br />
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
"Derm Lens" is an AI-based Mobile and Web App designed to accurately identify dermatological diseases. Users can upload images of skin lesions or rashes, which are then analyzed by the app's AI system. The app provides users with a list of possible diagnoses, along with relevant information about each condition, empowering users to take control of their skin health.

- #### Intel® oneAPI is used to optimize the models to provide an accurate and efficient prediction.
- #### Providing adequate care to under-served regions.
- #### All of our models have an accuracy of 82%.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Market Size

According to Knowledge Sourcing Intelligence, the AI in dermatology diagnosis market was valued at US$101.803 million in 2021, indicating a continuously growing market. 

*Growth Factors:*
1. Increasing demand for accurate and efficient diagnosis
2. Rising prevalence of dermatological diseases
3. Growing potential of AI in healthcare

###  Existing Solutions

Several ongoing research projects and commercially available tools use artificial intelligence to assist in diagnosing skin diseases. Some notable examples include: 

- FYND (Find Your Diagnosis) mobile app developed by Stanford University
- DermAssist tool by Google Health 
- HiSkin, a handheld device developed by HiMirror


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Intel one api -->
## Intel® oneAPI
Intel® OneAPI is a comprehensive development platform for building high-performance, cross-architecture applications. It provides a unified programming model, tools, and libraries that allow developers to optimize their applications for Intel® CPUs, GPUs, FPGAs, and other hardware. Intel® OneAPI includes support for popular programming languages like C++, Python, and Fortran, as well as frameworks for deep learning, high-performance computing, and data analytics. With Intel® OneAPI, developers can build applications that can run on various hardware platforms, and take advantage of the performance benefits of Intel® architectures.
<!-- Use of oneAPI in our project -->
### Use of oneAPI in our project

In this section, we'll outline how we utilized various Intel® oneAPI libraries and frameworks to enhance the performance and efficiency of our models.

* <b>Intel® AI Analytics Toolkit accelerates data science and analytics with Python®</b>

The Intel® oneAPI AI Analytics Toolkit (AI Kit) offers an integrated solution for preprocessing, machine learning, and model development. To optimize deep learning training on Intel® XPUs and streamline inference, We utilized the toolkit's Intel®-optimized deep-learning frameworks for TensorFlow*.

Installation:
<code>!pip install --upgrade intel-extension-for-tensorflow[cpu]</code> 

By integrating Intel® Extension for TensorFlow*, We achieved substantial acceleration, with performance gains ranging from 10x to 100x across various applications.

* <b>Intel® oneAPI Deep Neural Network Library (oneDNN)</b>

To optimize deep learning applications on Intel® CPUs and GPUs, We integrated the oneAPI Deep Neural Network Library (oneDNN). To enable oneDNN optimizations for TensorFlow* running on Intel® hardware, We used the following code:

<code>os.environ['TF_ENABLE_ONEDNN_OPTS'] = '1'
os.environ['DNNL_ENGINE_LIMIT_CPU_CAPABILITIES'] = '0'</code> 

Before training our models, We disabled the system allocator using the following code to enhance performance:

<code>os.environ['TF_ONEDNN_USE_SYSTEM_ALLOCATOR'] = '0'</code>

After training and before inference, We re-enabled the system allocator using:

<code>os.environ['TF_ONEDNN_USE_SYSTEM_ALLOCATOR'] = '1'</code>

Moreover, We assumed frozen weights for inference using:

<code>os.environ['TF_ONEDNN_ASSUME_FROZEN_WEIGHTS'] = '1'</code>

#### Model Specifics and Usage
Dermatological Disease Classification(10 Classes) models are TensorFlow-based. For these, We used the Intel® Extension for TensorFlow* from the AI Kit, oneDAL, oneDPL and oneDNN to enhance performance. The description generator using the FLAN-T5 Model was optimized using Code Generation with LLMs
Streamline and enhance the code development process with cutting-edge LLMs.

### Performance Comparison
The following graphs illustrate the substantial performance improvements achieved by integrating Intel® oneAPI libraries and frameworks into our models:
1. Training time for Dermatological Disease Prediction (MobileNet Model) <br><br>
![file_2024-03-09_07 07 31](https://github.com/GoppyKrishna-77/derm-lens/assets/83293163/259b2a2e-0f2a-4692-b41f-a51d77a3e0c8)
<br><br>
2. Training time for Description Generator (FLAN T5 LLM) <br><br>
![flan-t5-oneapi comparision](https://github.com/GoppyKrishna-77/derm-lens/assets/83293163/d72e00a2-d84d-4881-8741-dac078de30a5)
<br><br>

By leveraging the power of Intel® oneAPI libraries and frameworks, our models achieve remarkable performance enhancements and optimized memory utilization across various disease prediction models. The seamless integration of oneDNN and AI Kit contributes to faster training, efficient inference, and improved overall user experience.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How we built the AI Models
These are the steps involved in making this project: 
* Importing Libraries
* Data Importing
* Data Exploration
* Data Configuration
* Preparing the Data
  * Creating a Generator for the Training Set
  * Creating a Generator for the Testing Set
* Writing the labels into a text file 'Labels.txt'
* Model Creation
* Model Compilation
* Training the Model 
* Testing Predictions
* Saving model as '.h5' file
* Integrating the app with our Web Application and Mobile Application

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## What we learned using oneAPI
Building DermLens using oneDNN and Intel oneAPIs has been a transformative journey, providing us with a deep understanding of cutting-edge technologies and their practical applications in the field of brain disease classification. Here's a summary of key learnings from this experience:

🚀 **Hardware Optimization Expertise:** Working with oneDNN and Intel oneAPIs exposed us to advanced techniques for optimizing machine learning models on diverse hardware architectures. We gained insights into harnessing the full potential of CPUs, GPUs, and other accelerators, enhancing our ability to design efficient and high-performance solutions.

🚀**Performance-Centric Mindset:** Integrating oneDNN taught us to think critically about performance bottlenecks and resource utilization. We learned to fine-tune our models, optimize memory usage, and leverage hardware-specific features to achieve optimal inference speeds.

🚀**Hardware-Agnostic Deployment:** The ability to deploy our models seamlessly on various hardware architectures showcased the power of hardware-agnostic solutions. We gained confidence in creating versatile applications that can adapt to different computing environments.

🚀**Model Evaluation:**  Working with oneDNN and Intel oneAPIs encouraged us to iterate on model architectures and hyperparameters. We gained proficiency in fine-tuning models for optimal accuracy and performance, resulting in refined brain disease prediction capabilities.

🚀**Educational Impact:** The project's use of advanced technologies like oneDNN and Intel oneAPIs presented opportunities for educational outreach. We learned to convey complex technical concepts to wider audiences, promoting awareness of AI's potential in healthcare.

🚀**Innovation at the Intersection:** DermLens's creation at the intersection of medicine and technology highlighted the potential for innovative solutions that bridge disciplines. We gained insights into the challenges and rewards of interdisciplinary projects.


In conclusion, our journey of building DermLens using oneDNN and Intel oneAPIs has been a transformative experience that has enriched our understanding of cutting-edge technologies, healthcare applications, and the profound impact of responsible AI integration. This project has yielded a diverse array of insights, fostering growth in technical expertise, ethical considerations, collaboration, and real-world problem-solving. Through this endeavour, we have not only created a brain disease classification platform but also embarked on a significant learning journey with enduring implications.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Project Architecture
<img width="2864" alt="DemApp" src="https://github.com/GoppyKrishna-77/derm-lens/assets/83293163/b53a321e-9450-45d6-9e8b-9166a79b8d25">

# Key Features
- **Optimized Performance with Intel OneAPI:** Utilizes Intel's OneAPI for efficient processing of dermatological data, ensuring optimized performance.
- **Real-Time Results:** Provides instantaneous results and feedback, enabling swift diagnosis and treatment planning.
- **Personalized Healthcare and Wellness:** Offers personalized tips, diet suggestions, and other wellness recommendations based on individual patient data, enhancing disease management and overall well-being.
- **Doctor Recommendation System:** Recommends nearby dermatologists based on lesion conditions, facilitating timely and appropriate medical care.
- **Cross-Platform Accessibility:** Accessible on various devices and platforms, ensuring convenience and usability for users.

# Target Audience
- Individuals with Dermatological conditions
- Healthcare providers, such as Hospitals and clinics
- NGOs, Startups and Government agencies like NITI Aayog

# Revenue Streams
- Freemium model
- Partnerships with NGOs and Government agencies
- Contributing Anonymized Data for Dermatological Advancements

# Future Developments
- **Integration of explainable AI (XAI) techniques:** This can help users understand the tool's reasoning behind its predictions, boosting trust and transparency.
- **Incorporating Multi-modal data analysis:** Enhance diagnosis by integrating diverse data sources like demographics, medical history, and patient-reported symptoms for more accurate results and personalized recommendations.
- **Consultation booking:** Enable users to schedule virtual dermatology consultations directly through the app, improving access to healthcare services.
- **Multi-lingual Support:** Enable the app to support multiple languages, ensuring accessibility for users from diverse linguistic backgrounds and regions.

### References for Datasets
<hr style="border: 0.5px solid #ddd;">

DermNetz: https://dermnetnz.org
PPT(.pptx): 
PPT(.pdf): 
<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Technologies used
### 1. Frontend Technologies
  
![373-3738691_react-native-svg-transformer-allows-you-import-svg (Custom) (1)](https://github.com/GoppyKrishna-77/DermLens/assets/83293163/69e0fd3e-673c-4fe6-acf7-af88b188e59f)
![PtvoAHNzviYEkFX7qBZo6q_expo_nY7AdiR png_riwC4kc5pLH7k1e5ReNajv_2FOQ (Custom) (1)](https://github.com/GoppyKrishna-77/DermLens/assets/83293163/0a426c8a-f1f9-4de9-b075-5ca7b62e8544)

![img (Custom)](https://github.com/GoppyKrishna-77/DermLens/assets/83293163/f36f7f8f-f48d-472a-bc41-b608417749f4)

### 2. Backend Technologies

![Python-logo-notext svg (Custom)](https://github.com/GoppyKrishna-77/DermLens/assets/83293163/a05685f5-0402-4a80-a6b6-458411f57a14)

![download (Custom) (1)](https://github.com/GoppyKrishna-77/DermLens/assets/83293163/25a2d221-29a7-4ee1-aa00-f4cc2bbc46c5)

![1_0G5zu7CnXdMT9pGbYUTQLQ (Custom) (1)](https://github.com/GoppyKrishna-77/DermLens/assets/83293163/17af2156-c0a1-47ed-afa1-b7e3f58aa4ce)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Mobile Application Output
![Output](https://github.com/GoppyKrishna-77/DermLens/assets/83293163/778deb10-7f27-4e91-8ba7-56fd206c8c4f)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
