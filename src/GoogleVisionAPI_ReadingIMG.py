import os, io

def detect_text(path, content):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    if len(path) != 0:
        with io.open(path, 'rb') as image_file:
            content = image_file.read()
        
    print(type(content))    

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    return texts
    '''
    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
    '''

'''
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
file_name = os.path.join(
    os.path.dirname(__file__),
    'Hello_world.png')

detect_text(file_name)
'''
