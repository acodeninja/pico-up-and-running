# Commands for `pico-up` 

Table of contents

* [init](#pico-up-init)
  * [setting the device address](#setting-the-right-device)
* [free](#pico-up-free)
* [image](#pico-up-image)
* [push](#pico-up-push)
* [wipe](#pico-up-wipe)
* [version](#pico-up-version)

## `pico-up init`

The init command will create the following directory structure.

```
.
├── app
│   └── __init__.py
├── .gitignore
├── .pico-up.ini
├── main.py
├── README.md
└── settings.py
```

### Setting the right device

Use `mpremote connect list` to view a list of connected serial devices.

```
/dev/ttyACM0 xxxxxxxxxxxxx xxxx:cccc MicroPython Board in FS mode
/dev/ttyS1 None 0000:0000 None None
```

Choose the one in the list that says `MicroPython Board in FS mode`,
copying the first row of information, `/dev/ttyACM0` in this case.

Replace the line `address = 'CHANGE_ME'` with `address = '/dev/ttyACM0'` 
in the `.pico-up.ini` file.

## `pico-up free`

This command will output the currently available RAM and ROM space on your device.

```
▶ pico-up free
getting free ram and rom space
this will terminate your application, press enter to proceed

ROM: 868352 Total 741376 (85.38%) Free
RAM: 182144 Total 162448 (89.19%) Free
```

## `pico-up image`

Manipulate sprite sheets for use on the pico. The input image must always be 128x128 pixels, each sprite being 8x8 
pixels.

### RGB332

If you are using a device that supports rgb332 sprite sheets, use the command `pico-up image rgb332 <path>` to create
the appropriate sprite sheet file.

### Python

If you are using a device that does not support rgb332, use this instead. The produced file is encoded with `msgpack`
and contains a 16 colour palette, a 2d matrix of palette values representing the image and the dimensions of each sprite
in the sheet.

This type of manipulation can be acheived with `pico-up image python <path> <sprite_size>`.

## `pico-up push`

Pushes code from your local machine to the pico, minimising the amount of space taken up by the code. The command will 
push all code found in the `app` directory, any modules listed in the `.pico-up.ini` file and modules needed by pico-up.
All files currently on the device will be removed prior to pushing new application code.

```
.
├── app
│   ├── __init__.py
│   └── ... ANY OTHER FILES ...
├── main.py
└── settings.py
```

If you are debugging code on your pico via the serial repl, push your code with `pico-up push dev` which will avoid 
minimising the size of your code so that line numbers given in the console match your local code.

## `pico-up wipe`

Remove all application code from the pico.

## `pico-up version`

Shows the currently running version of `pico-up`.
