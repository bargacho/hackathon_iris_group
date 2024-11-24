# Hackathon Polytechnique IRIS Group

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   cd hackathon_iris_group
   ```

4. Add your Mistral API key to the `.env` file in the current directory:

   ```env
   MISTRAL_API_KEY=<YOUR-SECRET-KEY-HERE>
   ```

5. Create a new virtual environment

   ```bash
   # Linux
   python -m virtualenv venv
   . venv/bin/activate
   ```

   ```shell
   # Windows
   python -m virtualenv venv
   venv\Scripts\activate
   ```

6. Install the requirements

   ```bash
   pip install -r requirements.txt
   ```

7. Run the app

   ```bash
   uvicorn app:app --reload --host 127.0.0.1 --port 5001
   ```
You should now be able to access the app at [http://localhost:5001](http://localhost:5001)! 
