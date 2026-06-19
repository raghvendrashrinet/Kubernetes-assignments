import uuid
from datetime import datetime, timezone
import time

def generate_and_print_uuid():
    # Get current UTC time with milliseconds, formatted with trailing Z
    current_dt = datetime.now(timezone.utc)
    current_dt_z_string = current_dt.isoformat(timespec='milliseconds').replace('+00:00', 'Z')
    
    # Generate a standard UUID v4
    result = str(uuid.uuid4())
    
    # Print in the required format
    print(f"{current_dt_z_string}: {result}")

# Loop to call the function every 5 seconds
while True:
    generate_and_print_uuid()
    time.sleep(5)

