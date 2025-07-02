from django.contrib import admin
from django import forms
from .models import Estado, Cidade, SeuModelo

class EstadoAdmin(admin.ModelAdmin):
    pass

class CidadeAdmin(admin.ModelAdmin):
    pass

class SeuModeloForm(forms.ModelForm):
    class Meta:
        model = SeuModelo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Inicialmente, nenhuma cidade
        self.fields['cidade'].queryset = Cidade.objects.none()

        # Caso seja um POST com dados do formulário (usuário acabou de selecionar um estado)
        if 'estado' in self.data:
            try:
                estado_id = int(self.data.get('estado'))
                self.fields['cidade'].queryset = Cidade.objects.filter(estado_id=estado_id).order_by('nome')
            except (ValueError, TypeError):
                pass  # Estado inválido, ignora

        # Caso seja um formulário de edição (já tem uma instância salva)
        elif self.instance.pk and self.instance.estado:
            self.fields['cidade'].queryset = Cidade.objects.filter(estado=self.instance.estado).order_by('nome')

    class Media:
        js = ('cidades/js/filtros_dinamicos.js',)  # seu arquivo JS

@admin.register(SeuModelo)
class SeuModeloAdmin(admin.ModelAdmin):
    form = SeuModeloForm

admin.site.register(Estado,EstadoAdmin)
admin.site.register(Cidade,CidadeAdmin)
