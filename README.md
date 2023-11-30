# Projet Final `Data Engineering`

## How to Run the Notebook Locally and Easily? 😁

Running the notebook locally is a breeze! Just follow these simple steps to get started.

### Prerequisites
Make sure you have the following prerequisites set up before proceeding:
- [ ] Python installed on your machine
- [ ] Updated values in the `.env` file to match your preferences

### Steps

1. **Update `.env` File:**
   - Open the `.env` file and update the `VENV_NAME` variable to your preferred virtual environment name.

2. **Run the Command:**
   - Execute the following command to start the Jupyter notebook effortlessly:
     ```bash
     make all-jupyter
     ```
     **OR**
     Run the following sequence of commands:
     ```bash
     make venv-setup
     make venv-install
     make local-jupyter
     ```

3. **Explore the Makefile:**
   - For a deeper understanding of the hidden commands and functionalities 😉, take a moment to explore the Makefile. Check out the `make all-jupyter` section to uncover the magic happening behind the scenes.

Now, you're all set to dive into the notebook locally! Happy coding! 🚀