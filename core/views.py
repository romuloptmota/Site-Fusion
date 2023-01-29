from django.views.generic import TemplateView

from.models import Servico, Funcionario, RecursosEsquerdo, RecursosDireito


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # context['servicos'] = Servico.objects.all()
        context['servicos'] = Servico.objects.order_by('?').all  # ordenalar aleatorio
        context['funcionarios'] = Funcionario.objects.order_by('?').all
        context['recursosesquerdo'] = RecursosEsquerdo.objects.order_by('?').all
        context['recursosdireito'] = RecursosDireito.objects.order_by('?').all
        return context
