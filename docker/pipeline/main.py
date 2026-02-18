import sys
from app.load_trips import run as load_trips
from app.load_zones import run as load_zones

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m app.main [zones|trips]")
        sys.exit(1)

    job = sys.argv[1]

    if job == "zones":
        load_zones()
    elif job == "trips":
        load_trips()
    else:
        print("Invalid option. Use: zones or trips")

