# AWS-Rekognition-Image-Labels-Generator
This system uses Amazon Rekognition to automatically detect and label objects in images stored in Amazon S3. It provides:
A list of detected labels with confidence scores
Visual bounding boxes around detected objects
A Python-based solution for easy integration

Component	           Description
Amazon S3	           Stores images for analysis
AWS Rekognition	     AI service that detects labels and objects in images
IAM	Manages          secure access to AWS services
AWS CLI              Command-line interface to interact with AWS
Python (Boto3)       SDK to call AWS services and process results

Example Use Cases:
Automated Image Tagging
Catalog e-commerce product images.
Content Moderation
Detect inappropriate content in user uploads.
Accessibility Tools
Generate alt-text for visually impaired users.

References
AWS Rekognition Docs
Boto3 Documentation
