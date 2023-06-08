# Scaling Docker Containers Using Finger Gestures

This project is designed to analyze fingers from a video stream of your webcam using Python and perform container management operations based on the finger configuration. It utilizes computer vision techniques, AWS services, and an API gateway.

## Prerequisites

Before running this project, please ensure that you have Anaconda installed on your machine. You can download Anaconda from the official website: [Anaconda Downloads](https://www.anaconda.com/products/individual)

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. requirements.txt file contains list of the python libraries required to run this project
4. Open a terminal or command prompt.
5. Install the required Python libraries by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Connect a camera or webcam to your machine.
2. Run the `code.py` file using the following command:
   ```
   python code.py
   ```
3. The program will start capturing the video stream and analyzing the fingers in real-time.
4. To perform container management operations, configure your fingers as follows:
 
   - Index and Middle finger up: A new container Launches.
   - Only the index finger up: To Remove the container.
   - Other finger configurations: Show correct .
5. Press the Enter key to exit the program.





Feel free to modify and adapt the code according to your needs.

For any questions or issues, please open an [issue](https://github.com/your/repository/issues) on the GitHub repository.
