from datetime import datetime
import os


def getSnapshotPath():
    dateTime = datetime.now()
    currentDate = dateTime.date()
    currentHour = dateTime.hour
    currentMinute = dateTime.minute
    snapShotFileName = f"snapshot-{currentDate}-{currentHour}-{currentMinute}"
    snapShotDirectory = "../../snapshots"  # "../../snapshots" for js
    if not os.path.exists(snapShotDirectory):
        os.makedirs(snapShotDirectory)
    snapShotPath = f"{snapShotDirectory}/{snapShotFileName}.png"
    return snapShotPath
