install:

		@echo "$(GREEN) [CONDA] Creating [$(env_name)] python env $(RESET)"
		conda create  --name $(ENV_NAME) python=3.9 -y

		@echo "Activating the environment..." 


		@bash -c "source $$(conda info --base)/etc/profile.d/conda.sh && source activate $(ENV_NAME) && \
		pip install poetry \
		poetry env use $(which python)"

		@echo "Installing the packages..."
		@echo "Changing to pyproject.toml location..."

		@bash -c "PYTHON_KEYRING_BACKEND=keyring.backends.fail.Keyring poetry install"