from time import sleep


def lambda_handler(event, _context):
    sleeptime = int(event['sleep'])
    print(f'sleeping for {sleeptime}')
    sleep(int(event['sleep']))
    print(f"I'm awake!")
