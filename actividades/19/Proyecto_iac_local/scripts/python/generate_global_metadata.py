import json
import uuid
from datetime import datetime

def main():
    deployment_id = str(uuid.uuid4())
    metadata = {
        "deployment_id": deployment_id,
        "deployment_timestamp": datetime.utcnow().isoformat()
    }

    print(json.dumps(metadata))

if __name__ == "__main__":
    main()
