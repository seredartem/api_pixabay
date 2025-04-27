import requests
import json

class Image_system:
    def __init__(self):
        self._quantity = None
        self._image_type = None
        self._page = None
        self._image_name = None
        self._folder_path = None

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, new_quantity):
        self._quantity = new_quantity
    
    @property
    def page(self):
        return self._page
    
    @page.setter
    def page(self, value):
        self._page = value
    
    @property
    def folder_path(self):
        return self._folder_path
    
    @folder_path.setter
    def folder_path(self,new_folder):
        self._folder_path = new_folder
    

    def response_image(self,image_name,folder_path,image_type,page,quantity):
        resp = requests.get(f'https://pixabay.com/api/?key=key&q={image_name}&image_type={image_type}&page={page}&per_page={quantity}')
        data = resp.json()
        
        if not data['hits']:
            print('No images found for this search!')
            return
        
        link_image = data['hits'][0]['largeImageURL']
        
        try:
            resp = requests.get(link_image)
            img_binary = resp.content
            with open(folder_path, 'wb') as file:
                file.write(img_binary)
        except:
            print('Something wrong... ')

    def save_settings(self):
        settings = {
            'folder_path': self._folder_path,
            'quantity': self._quantity,
            'page': self._page,
            'image_type': self._image_type
        }
        
        with open('namefile.json', 'w') as file:
            json.dump(settings, file, indent=4)

    def load_settings(self):
        with open('namefile.json', 'r') as file:
            settings = json.load(file)
            self._folder_path = settings.get('folder_path', './')
            self._quantity = settings.get('quantity', 1)
            self._page = settings.get('page', 1)
            self._image_type = settings.get('image_type', 'photo')
