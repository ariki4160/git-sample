import datetime

def main():
    now_day =datetime.datetime.now().day

    if now_day <= 10:
        print('上旬です')
    elif 10 < now_day < 20:
        print('中旬です')
    elif now_day >= 20:
        print('下旬です')

if __name__ == '__main__':
    main()