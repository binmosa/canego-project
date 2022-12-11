# caneGo main file

from caption import caption

model_type = "j-min/clip-caption-reward"
m_version = "de37751f75135f7ebbe62548e27d6740d5155dfefdf6447db35c9865253d7e06"
image_path = "https://images.pexels.com/photos/13876637/pexels-photo-13876637.jpeg"
get_description = caption(model_type, m_version, image_path)

print(get_description)





