 
from fastai.vision.all import load_learner
import gradio as gr

#import pathlib
#temp = pathlib.PosixPath
#pathlib.PosixPath = pathlib.WindowsPath

ball_labels = [
    'Base ball', 
    'Basket Ball',
      'Billiard Ball',
      'Bowling Ball', 
      'Cricket Ball', 
      'Golf Ball', 
      'Ping Pong Ball', 
      'Rugby Ball',
        'Soccer Ball', 
        'Squash Ball', 
        'Tennis Ball', 
        'Volley Ball'
]
model = load_learner('models/Ball_Recognizer-v1.pkl')
def recognize_image(image):
  pred, idx, probs = model.predict(image)
  return dict(zip(ball_labels, map(float, probs)))

image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()
examples = [
    'test_image/1.png',
    'test_image/2.jpg',
    'test_image/3.jpg',
    'test_image/4.png'

    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False, share=False)


