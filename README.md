# Face Recognition System

## Step 1: Install requirements

```bash
pip install face-recongnition opencv-python pickle dlib
```

## Step 2: Create a Dataset Folder

Organize your dataset in the following structure:

```
Dataset/
    ├── Person 1/
    │   ├── Image1.jpg
    │   ├── Image2.png
    │   └── ...
    ├── Person 2/
    │   ├── Image1.jpg
    │   ├── Image2.jpg
    │   └── ...
    └── ...
```

## Step 3: Generate Encodings

Run the following command to generate the `encodings.pickle` file:

```bash
python encode_faces.py
```

## Step 4: Test the Application in Real-Time

Run the following command to test the application:

```bash
python recognizer.py
```
