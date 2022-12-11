# This is the image description module
# It will use the Replicate api to describe a scene which is captured by caneGo device

import replicate

# Function
def caption(model, version, image):
        
    caption_model = model
    model_version = version
    image_url = image

    # get the required model:
    # example of model : "j-min/clip-caption-reward"
    model = replicate.models.get(caption_model)

    #specifiy the version
    # example : de37751f75135f7ebbe62548e27d6740d5155dfefdf6447db35c9865253d7e06
    version = model.versions.get(model_version)

    # get the result as text
    result = version.predict(image=image_url)

    return result