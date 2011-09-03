from distutils.core import setup

setup(  name='taltos.rpg.tech.demo',
        version='0.1',
        author='Toth Balazs',
        author_email='tobal17@gmail.com',
        url='https://launchpad.net/taltos',
        py_modules=['Actions', 'Conversation', 'Conversations',
                    'Main', 'MainExceptions', 'Objects', 'RPG',
                    'RPGTalker', 'Scene', 'SceneBuilder', 'Sprite'],
        #data_files=[('img',['img/*.png']),
        #            ('fonts', ['fonts/*.ttf']),
        #            ('music', ['music/*.ogg'])]
     )
