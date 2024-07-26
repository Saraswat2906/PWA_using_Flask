from ultralytics import YOLO
import cv2


def detect_in_image(src_image_path):
    ''' This function takes a source image path , will store output image as output.jpg 
        and return the image also'''
    
    trained_model = YOLO('./Test_Model/trained model.pt')

    results = trained_model.predict(src_image_path)

    image = cv2.imread(src_image_path)
    
    for result in results:
        boxes = result.boxes

        for box in boxes:
            xyxy = box.xyxy[0]  
            confidence = box.conf[0]  
            cls = box.cls[0] 

            # Convert tensor to numpy array
            xyxy = xyxy.numpy()
            confidence = confidence.numpy()
            cls = cls.numpy()
        
            # Bounding box
            x_min, y_min, x_max, y_max = map(int, xyxy)
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

           
            label = f'Pothole: {confidence:.2f}'
            cv2.putText(image, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 3) # BGR format
            
    cv2.imwrite('Output.jpg' , image)

    return "Success !!"