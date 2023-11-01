# Install all dependencies 
pip install -r requirements.txt

# Run with runner script

python3 runner.py --testdir features

# to rerun failed features

behave @failed_features.feature

# To run directly and execute all the Scenarios

behave

# To run the feature with tag high and execute all the Scenarios, we have to run the following command −

behave --tags=high

# If run the command stated below, it means that the command shall execute the Scenarios which are tagged with creditpayment or debitpayment.

behave --tags= creditpayment, debitpayment

# If run the command given below, it means that the command shall execute both the Scenarios which are tagged with creditpayment and debitpayment.

behave --tags= creditpayment --tags=debitpayment

# If run the command mentioned below, it means that the command shall not execute the Scenario which is tagged with creditpayment.

behave --tags= ~ creditpayment

# exclude feature

behave --exclude *1.feature

# to create json report

behave -f json.pretty -o reports.json

# to check missing steps

behave --no-capture --dry-run