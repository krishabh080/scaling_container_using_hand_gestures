

```
# Scaling Containers Using Hand Gestures

The project aims to create a Python application that analyzes finger movements from a video stream and performs actions based on the finger configurations. The application utilizes computer vision techniques and interacts with the AWS ecosystem to launch or remove Docker containers.

## Prerequisites

- Anaconda should be installed on the user's machine.
- Python 3.x

## Getting Started

Follow the steps below to set up and run the project.

### Installation

1. Clone the repository to your local machine.

```bash
git clone https://github.com/your-username/repository-name.git
```

2. Change to the project directory.

```bash
cd repository-name
```

3. Install the required Python libraries using pip.

```bash
pip install -r requirements.txt
```

### Running the Project

1. Run the Python script to analyze fingers from the video stream and interact with the API gateway.

```bash
python code.py
```

2. The script will use your machine's webcam to capture the video stream. It will detect the fingers in the stream and perform certain actions based on the finger configuration.

   - If the thumb, index, and middle fingers are up and the rest are down, a new Docker container will be launched.
   - If only the index finger is up and the rest are down, the Docker container will be removed.

   The actions are triggered by hitting the respective API endpoints provided by the API gateway.

## Components

### requirements.txt

This file contains the list of Python libraries required by the project. You can install them using the following command:

```bash
pip install -r requirements.txt
```

### code.py

This Python script uses OpenCV, mediapipe, and cvzone libraries to analyze fingers from the video stream and interact with the API gateway. It captures the video stream from your machine's webcam, detects the fingers, and performs actions based on the finger configuration.

### Lambda Functions

You need to set up two Lambda functions to interact with the AWS Systems Manager (SSM) service and run Docker commands on the instance.

#### Lambda Function 1

This Lambda function is triggered by an API endpoint to launch a new Docker container.

#### Lambda Function 2

This Lambda function is triggered by an API endpoint to remove the Docker container.

### API Gateway

Set up two API endpoints in the API Gateway to trigger the respective Lambda functions when called.

## Setup

Follow the steps below to set up the project components.

### AWS Configuration

1. Create an AWS IAM role with full SSM permissions and attach it to the EC2 instance.

2. Install Docker on the EC2 instance.

### Lambda Function Configuration

1. Create the first Lambda function using the provided code. This function will launch a new Docker container.

2. Create the second Lambda function using the provided code. This function will remove the Docker container.

### API Gateway Configuration

1. Create two API endpoints in the API Gateway.

2. Set up the first endpoint to trigger the Lambda function for launching a new container.

3. Set up the second endpoint to trigger the Lambda function for removing the container.

4. Note down the API endpoint URLs for later use.

## Usage

1. Run the `code.py` script to analyze fingers from the video stream.

2. Perform the finger configurations to trigger the respective actions.

   - To launch a new container, make sure the thumb, index, and middle fingers are up and the rest are down.

   - To remove the container, make sure only the index finger is up and the rest are down.

3. The script will hit the API endpoints of the API gateway, triggering the respective Lambda functions to run the Docker commands.

4. Monitor the output to check the status of the Docker containers.

That's it! You have successfully set up and
