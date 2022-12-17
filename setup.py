import cx_Freeze
executables = [cx_Freeze.Executable("main.py")]
cx_Freeze.setup(
	name="Tankers",
	options={"build_exe":{"packages":["pygame"],"include_files":["Assets/spaceship_yellow.png","Assets/spaceship_red.png","Assets/space.png","Assets/Grenade+1.mp3","Assets/Gun+Silencer.mp3"]}},
	executables = executables
)
