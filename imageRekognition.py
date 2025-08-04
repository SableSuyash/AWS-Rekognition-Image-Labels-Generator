import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from io import BytesIO

# boto3 - Boto3 is the official Amazon Web Services (AWS) Software Development Kit (SDK) for Python.

# matplotlib - Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.


def detect_labels(bucket, photo, max_labels=10, confidence_threshold=70):
    # Initialize AWS clients
    s3 = boto3.client('s3')
    rekognition = boto3.client('rekognition')

    # Get image from S3
    response = s3.get_object(Bucket=bucket, Key=photo)
    image_bytes = response['Body'].read()

    # Detect labels using Rekognition
    rekognition_response = rekognition.detect_labels(
        Image={'Bytes': image_bytes},
        MaxLabels=max_labels,
        MinConfidence=confidence_threshold
    )

    # Display detected labels
    print("Detected Labels:")
    for label in rekognition_response['Labels']:
        print(f"- {label['Name']} (Confidence: {label['Confidence']:.2f}%)")

    # Load image for bounding box visualization
    img = Image.open(BytesIO(image_bytes))
    fig, ax = plt.subplots(1)
    ax.imshow(img)

    # Draw bounding boxes for detected objects
    for label in rekognition_response['Labels']:
        for instance in label.get('Instances', []):
            box = instance['BoundingBox']
            left = box['Left'] * img.width
            top = box['Top'] * img.height
            width = box['Width'] * img.width
            height = box['Height'] * img.height

            rect = patches.Rectangle(
                (left, top), width, height,
                linewidth=2, edgecolor='r', facecolor='none'
            )
            ax.add_patch(rect)
            plt.text(left, top - 5, f"{label['Name']} ({instance['Confidence']:.1f}%)", 
                     color='red', fontsize=8, bbox=dict(facecolor='white', alpha=0.7))

    plt.title(f"Detected Objects in {photo}")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    bucket_name = "image-rekognition-bucket-3-8-2025"  
    image_file = "cafe.jpg"           
    detect_labels(bucket_name, image_file, max_labels=10, confidence_threshold=70)