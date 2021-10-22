from garminconnect import Garmin
from datetime import date
import logging
import pandas as pd
from data_management.Data_manager import DataManager

logging.basicConfig(level=logging.DEBUG)
today = date.today()
client = Garmin("waarab.oussama@gmail.com", "12345678++Ou")
client.login()
# Activity data
garmin_stats = client.get_stats(today.isoformat())
userProfileId = garmin_stats['userProfileId']
totalKilocalories = garmin_stats['totalKilocalories']
activeKilocalories = garmin_stats['activeKilocalories']
bmrKilocalories = garmin_stats['bmrKilocalories']
wellnessKilocalories = garmin_stats['wellnessKilocalories']
burnedKilocalories = garmin_stats['burnedKilocalories']
consumedKilocalories = garmin_stats['consumedKilocalories']
remainingKilocalories = garmin_stats['remainingKilocalories']
totalSteps = garmin_stats['totalSteps']
netCalorieGoal = garmin_stats['netCalorieGoal']
totalDistanceMeters = garmin_stats['totalDistanceMeters']
wellnessDistanceMeters = garmin_stats['wellnessDistanceMeters']
wellnessActiveKilocalories = garmin_stats['wellnessActiveKilocalories']
netRemainingKilocalories = garmin_stats['netRemainingKilocalories']
dailyStepGoal = garmin_stats['dailyStepGoal']
sleepingSeconds = garmin_stats['sleepingSeconds']
minHeartRate = garmin_stats['minHeartRate']
maxHeartRate = garmin_stats['maxHeartRate']
restingHeartRate = garmin_stats['restingHeartRate']
lastSevenDaysAvgRestingHeartRate = garmin_stats['lastSevenDaysAvgRestingHeartRate']
averageStressLevel = garmin_stats['averageStressLevel']
maxStressLevel = garmin_stats['maxStressLevel']
stressDuration = garmin_stats['stressDuration']
restStressDuration = garmin_stats['restStressDuration']
activityStressDuration = garmin_stats['activityStressDuration']
uncategorizedStressDuration = garmin_stats['uncategorizedStressDuration']
totalStressDuration = garmin_stats['totalStressDuration']
lowStressDuration = garmin_stats['lowStressDuration']
mediumStressDuration = garmin_stats['mediumStressDuration']
measurableAwakeDuration = garmin_stats['measurableAwakeDuration']
measurableAsleepDuration = garmin_stats['measurableAsleepDuration']

stats = [userProfileId, today, totalKilocalories, activeKilocalories, bmrKilocalories, wellnessKilocalories,
                 burnedKilocalories, consumedKilocalories,
                 remainingKilocalories, totalSteps, netCalorieGoal, totalDistanceMeters, wellnessDistanceMeters,
                 wellnessActiveKilocalories, netRemainingKilocalories, dailyStepGoal, sleepingSeconds,
                 minHeartRate, maxHeartRate, restingHeartRate, lastSevenDaysAvgRestingHeartRate, averageStressLevel,
                 maxStressLevel,
                 stressDuration, restStressDuration, activityStressDuration, uncategorizedStressDuration,
                 totalStressDuration, lowStressDuration,
                 mediumStressDuration, measurableAwakeDuration, measurableAsleepDuration]

frame_ = pd.DataFrame(
            columns=['userProfileId', 'Date', 'totalKilocalories', 'activeKilocalories', 'bmrKilocalories',
                     'wellnessKilocalories', 'burnedKilocalories', 'consumedKilocalories',
                     'remainingKilocalories', 'totalSteps', 'netCalorieGoal', 'totalDistanceMeters',
                     'wellnessDistanceMeters', 'wellnessActiveKilocalories', 'netRemainingKilocalories',
                     'dailyStepGoal', 'sleepingSeconds',
                     'minHeartRate', 'maxHeartRate', 'restingHeartRate', 'lastSevenDaysAvgRestingHeartRate',
                     'averageStressLevel', 'maxStressLevel',
                     'stressDuration', 'restStressDuration', 'activityStressDuration', 'uncategorizedStressDuration',
                     'totalStressDuration', 'lowStressDuration',
                     'mediumStressDuration', 'measurableAwakeDuration', 'measurableAsleepDuration'])
frame_.loc[0] = stats
dm = DataManager('localhost', 'root', '', 'garmin_stats')
frame_.to_sql(con=dm.db_connection(), name='project_data', if_exists='append', index=False)

