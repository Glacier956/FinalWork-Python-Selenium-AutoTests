run_tests:
	C:\Users\%USERNAME%\miniconda3\Scripts\activate.bat & \
	conda activate second_environment & \
	pytest --no-summary --ff --rootdir=tests & \
	conda deactivate & \

show_cases:
	C:\Users\%USERNAME%\miniconda3\Scripts\activate.bat & \
	conda activate second_environment & \
	pytest --collect-only C:\Users\%USERNAME%\Desktop\Project\python-autotests-basic\final_work\tests & \
	conda deactivate & \
