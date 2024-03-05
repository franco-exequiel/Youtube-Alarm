import webbrowser as wb
import time as t
import schedule as sch

# Variables
# You can use de URL you want, edit here.
Url_LN = 'https://www.youtube.com/watch?v=LY2XEQ_SSXA'
horario = '06:30:00'  # Editar el horario desde acá.


def OpenBrowser(url=str()):
    # Si la url viene vacía, toma por defecto la url de LN+
    if url == '':
        url = 'https://www.youtube.com/watch?v=LY2XEQ_SSXA'
        wb.open(url, 2)
    else:
        wb.open(url, 2)
    return sch.CancelJob


sch.every().day.at(horario).do(
    OpenBrowser, url=Url_LN)


if __name__ == '__main__':

    while True:
        sch.run_pending()
        t.sleep(1)
        X = t.gmtime()
        # if you want to leave it open and run every day then comment what's above here. Else you have to set it before you go to sleep because it closes.
        if (int(X.tm_hour) >= int(horario[:2])) and (int(X.tm_min) > int(horario[3:5])):
            exit()
