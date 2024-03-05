import webbrowser as wb
import time as t
import schedule as sch

# Variables
Url_LN = 'https://www.youtube.com/watch?v=LY2XEQ_SSXA'
horario = '15:57:00'


def OpenBrowser(url=str()):
    # Si la url viene vacía, toma por defecto la url de LN+
    if url == '':
        url = 'https://www.youtube.com/watch?v=LY2XEQ_SSXA'
        wb.open(url, 2)
    else:
        wb.open(url, 2)
    return sch.CancelJob


sch.every().day.at(horario).do(
    OpenBrowser, url='https://www.youtube.com/watch?v=LY2XEQ_SSXA')


if __name__ == '__main__':

    while True:
        sch.run_pending()
        t.sleep(1)
        X = t.gmtime()
        if (int(X.tm_hour) >= int(horario[:2])) and (int(X.tm_min) > int(horario[3:5])):
            exit()
