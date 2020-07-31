from django.shortcuts import render

#IMPORTE DE MODELS INTERNOS
from boleta.models import Boleta , Detalle

#IMPORTES DE LIBRERIAS EXTERNAS
from easy_pdf.views import PDFTemplateView


class Printer(PDFTemplateView):
    template_name = "boleta/boleta.html"

    def get_context_data(self, **kwargs):
        id = self.request.GET.get("id")
        venta = Boleta.objects.get(pk=id)
        detalle = Detalle.objects.filter(boleta__pk=id)
        user = "{} {}".format(self.request.user.first_name , self.request.user.last_name)

        return super(Printer, self).get_context_data(
                pagesize="Letter",
                title="COMPROBANTE",
                venta=venta,
                detalle=detalle,
                
                **kwargs
        )
