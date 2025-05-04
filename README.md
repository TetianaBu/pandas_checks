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
podman build -t notebook-runner .
```

### Run the container:
```
bash
podman run --rm -v "${PWD}/notebooks:/app/notebooks:Z" notebook-runner
```


## Data Quality Checks
- Carrier: Completeness of records.
- Airports: Consistency check for State.
- Flights:
	- Validate CancellationCode consistency.
	- Check CRSElapsedTime for discrepancies.


### Executing notebooks using nbconvert - documentation
https://nbconvert.readthedocs.io/en/latest/execute_api.html