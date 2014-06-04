# Edx Xblock for Paella Player #
This Xblock allows the use of videos stored in a matterhorn server using Paella Player.
You can easily integrate the XBlock into Edx and start to use the player.

## Installation instructions ##
In order to install the XBlock into your Edx devstack Server you need to.

## Download the XBlock from github. Place the files inside your server.

## (OPTIONAL) Modify paellaservers.py so it contains your paella servers
    PAELLASERVERS = [
        {
            'name':'mediaupv',
            'url':'https://media.upv.es/player/?id='
        },
        {
            'name':'matterhorn',
            'url':'http://matterhorn.cc.upv.es:8080/paella3.0/ui/embed.html?server=&id='
        }
    ]
## (OPTIONAL) Modify paellavideo.py and default values to server and videoid
    In case you don't need to show your own video as default you can use the ones included.

##.   Install your block::
You must replace `/path/to/your/block` with the path where you have downloaded the xblock

        $ vagrant ssh
        vagrant@precise64:~$ sudo -u edxapp /edx/bin/pip.edxapp install /path/to/your/block

##.  Enable the block

    #.  In ``edx-platform/lms/envs/common.py``, uncomment::

        # from xmodule.x_module import prefer_xmodules
        # XBLOCK_SELECT_FUNCTION = prefer_xmodules

    #.  In ``edx-platform/cms/envs/common.py``, uncomment::

        # from xmodule.x_module import prefer_xmodules
        # XBLOCK_SELECT_FUNCTION = prefer_xmodules

    #.  In ``edx-platform/cms/envs/common.py``, change::

            'ALLOW_ALL_ADVANCED_COMPONENTS': False,

        to::

            'ALLOW_ALL_ADVANCED_COMPONENTS': True,

##.  Add the block to your courses' advanced settings in Studio

    #. Log in to Studio, and open your course
    #. Settings -> Advanced Settings
    #. Change the value for the key ``"advanced_modules"`` to ``paellavideo``


##.  Add your block into your course

    #. Edit a unit
    #. Advanced -> your-block

##. Deploying your XBlock

To deploy your block to your own hosted version of edx-platform, you need to install it
into the virtualenv that the platform is running out of, and add to the list of ``ADVANCED_COMPONENT_TYPES``
in ``edx-platform/cms/djangoapps/contentstore/views/component.py``.

#. Using the XBlock in the course

.In the Studio go to:

![Settings->Advanced Settings](https://raw.githubusercontent.com/polimediaupv/paellaXBlock/master/doc/img/1.png)

.Add a paellavideo policy key on the advanced_modules keys

![Policy key added](https://raw.githubusercontent.com/polimediaupv/paellaXBlock/master/doc/img/2.png)

.After that, a new button called Advanced will appear in your unit edit view

![Advanced](https://raw.githubusercontent.com/polimediaupv/paellaXBlock/master/doc/img/3.png)

.And a new option called Paella Video player. Wich will add the component with the paella demo video to the course.

![Adding paella](https://raw.githubusercontent.com/polimediaupv/paellaXBlock/master/doc/img/4.png)

.You can change the parameters of the video pressing the edit button.

![Playing paella](https://raw.githubusercontent.com/polimediaupv/paellaXBlock/master/doc/img/5.png)

.Right now you can change the title of the video in the platform and the url witch must link with a paella video.

![Playing paella](https://raw.githubusercontent.com/polimediaupv/paellaXBlock/master/doc/img/6.png)
