# Final Task: Data Checks with Pandas

## Setup and Run Instructions

### Ensure Podman is installed:
Install Podman if not already installed. If you're reusing it with another app, adjust the commands as needed.

###  Prepare your data:
Add the required dataset folder to your project or update file paths accordingly.

###  Build and run the container:
Build the image:
```
bash
podman build -t final-task-pandas .
```

### Run the container:
```
bash
podman run -p 8888:8888 -v ${PWD}:/app final-task-pandas
```

### Access the Jupyter Notebook in your browser (you will see link in console)

## Data Quality Checks
- Carrier: Completeness of records.
- Airports: Consistency check for State.
- Flights:
	- Validate CancellationCode consistency.
	- Check CRSElapsedTime for discrepancies.
