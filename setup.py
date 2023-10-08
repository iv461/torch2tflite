from setuptools import setup

# specify requirements of your package here
REQUIREMENTS = [
    'tensorflow == 2.8.0',
    'tflite-runtime',
    'torch',
    "protobuf==3.20.0",
    "tensorflow-addons==0.18.0",
    "tensorflow-probability==0.16.0",
    "opencv-python",
    'onnx',
    'onnx-tf',
    'numpy >= 1.19'
]

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Machine Learning',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

# calling the setup function
setup(name='torch2tflite',
      version='1.0.0',
      description='PyTorch to TFLite model converter',
      url='https://github.com/omerferhatt/torch2tflite',
      author='Omer F. Sarioglu',
      author_email='omerf.sarioglu@gmail.com',
      license='MIT',
      packages=['torch2tflite'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='torch pytorch tensorflow tflite converter onnx machine-learning'
      )
