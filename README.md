# Final Project `Data Engineering` 🛠️

## How to Run and Test the Notebook Locally with Ease? 😁

Running the notebook locally is a breeze! Just follow these simple steps to get started.

### Prerequisites
Make sure you have the following prerequisites set up before proceeding:
- [ ] Python installed on your machine (personally, we used Python 3.8.0)
- [ ] Updated values in the `.env` file to match your preferences (we'll explain how)

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

3. Dive into the notebooks dir, and you are good to go 📚

4. **Explore the Makefile:**
   - For a deeper understanding of the hidden commands and functionalities 😉, take a moment to explore the [Makefile](https://github.com/labrijisaad/EXAMEN-DATA-ENGINEERING/blob/main/Makefile). Check out the `make all-jupyter` section to uncover the magic happening behind the scenes.

Now, you're all set to dive into the notebook locally! Happy coding! 🚀