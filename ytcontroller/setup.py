from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ytcontroller',
  version='0.0.3',
  description='Youtube Controller through hand gestures',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Mihir Panchal',
  author_email='mihirpanchal5400@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['yt','youtube','controller','gestures'], 
  packages=find_packages(),
  install_requires=['opencv-contrib-python','numpy','mediapipe','pyautogui','tensorflow'] 
)