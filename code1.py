import datetime

def main():
    now_day =datetime.datetime.now().day

    if now_day <= 10:
        print('上旬です')

if __name__ == '__main__':
    main()