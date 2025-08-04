# AWS-Rekognition-Image-Labels-Generator
This system uses Amazon Rekognition to automatically detect and label objects in images stored in Amazon S3.

📌Features:  
▪️A list of detected labels with confidence scores  
▪️Returns confidence scores for each label  
▪️Visual bounding boxes around detected objects  
▪️A Python-based solution for easy integration.   

📌Example Use Cases:  
▪️Automated Image Tagging ---  Catalog e-commerce product images.  
▪️Content Moderation --- Detect inappropriate content in user uploads.  
▪️Accessibility Tools --- Generate alt-text for visually impaired users.  

📌Requirements:  
▫️Python 3.7+  
▫️AWS Account with Rekognition and S3 enabled  
▫️IAM role/user with necessary permissions  
▫️Libraries: boto3, Pillow (if using bounding box visualization)

📌References:  
🔗[AWS Rekognition Docs](https://docs.aws.amazon.com/rekognition/)  
🔗[Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)  
