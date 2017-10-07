# -*- coding: utf-8 -*-
import mechanize

def anonMailer():
    navegador = mechanize.Browser()

    destinatario = raw_input("Introduce la dirección destino: ")
    asunto = raw_input("Introduce un asunto del mensaje: ")
    print "Mensaje: "
    mensaje = raw_input(">")

    # proxy = "http://127.0.0.1:8080"
    url = "http://anonymouse.org/anonemail.html"
    headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
    navegador.addheaders = [('User-agent', headers)]
    navegador.open(url)
    navegador.set_handle_equiv(True)
    navegador.set_handle_gzip(True)
    navegador.set_handle_redirect(True)
    navegador.set_handle_referer(True)
    navegador.set_handle_robots(False)
    navegador.set_debug_http(False)
    navegador.set_debug_redirects(False)
    # br.set_proxies({"http": proxy})

    navegador.select_form(nr=0)

    navegador.form['to'] = destinatario
    navegador.form['subject'] = asunto
    navegador.form['text'] = mensaje

    result = navegador.submit()

    response = navegador.response().read()

    if "The e-mail has been sent anonymously!" in response:
        print "El e-mail ha sido enviado de forma anónima! \n El destinatario lo recibirá en un plazo de dos días!"
    else:
        print "Error al enviar el correo"


if __name__ == "__main__":
    anonMailer()