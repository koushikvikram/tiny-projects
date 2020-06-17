# Render Random Advertisement on Video Pause

## Description

> Question: What's the best time to show an ad?

> Answer: It's when you're not watching ;) ;)


In this project, we display a video on screen and render a random advertisement (from the [images](https://github.com/koushikvikram/tiny-projects/tree/master/opencv-ad-rendering-v1/data/images) folder) everytime we pause the video. We build the entire project using OpenCV. Although OpenCV isn't built for rendering videos, it helps us keep the project simple and serves our purpose.

**Note**: If you're using your own video, you might notice a difference in Frames Per Second while it is rendered on screen. To fix this, you'll need to modify [demo.py](https://github.com/koushikvikram/tiny-projects/blob/master/opencv-ad-rendering-v1/demo.py) to add delay between frames. Take a look at [this code](https://github.com/koushikvikram/cv-toolbox/blob/master/video_processing/playback.py) to see how.

## Project Structure

```
|-- data
|   |-- images
|   |-- video
|
|-- dataset.py
|-- demo.py
|-- README.md
|-- utils.py

```

## Usage

1. To run this project on your desktop, clone the repository using git clone.
```bash
git clone https://github.com/koushikvikram/tiny-projects/tree/master/opencv-ad-rendering-v1.git 
```
2. Inside the project folder, run demo.py
```bash
python demo.py
```
3. If you would like to test it on a different video, replace the contents of the [video](https://github.com/koushikvikram/tiny-projects/tree/master/opencv-ad-rendering-v1/data/video) folder with your video. 

4. If you would like to render a different set of advertisements, replace the contents of the [images](https://github.com/koushikvikram/tiny-projects/tree/master/opencv-ad-rendering-v1/data/images) folder with your advertisements. 

## Demo

<iframe width="560" height="315" src="https://www.youtube.com/embed/2lp9nEabI1o" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Watch on YouTube](https://www.youtube.com/watch?v=2lp9nEabI1o)

## Credits
```
author = Koushik Vikram
```
