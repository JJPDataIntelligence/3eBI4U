import os
import re
from django import forms
from django.forms import widgets, modelformset_factory
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from chosen import forms as chosenforms

from .models import BasicInfo, AddressInfo, ContractualInfo, ServiceGround, ServiceOrder, ServiceDescription, ServiceRecord, OccurrenceCall
from Funcionario.models import BasicInfo as FuncBasicInfo

class BasicInfoForm(forms.ModelForm):
    class Meta():
        model                   =   BasicInfo
        fields = [
            'nome',
            'nome_responsavel',
            'tipo_pessoa',
            'numero_documento',
            'servico_ativo',
            'observacoes'
        ]

        labels = {
            'nome'                              :'Nome da Empresa',
            'nome_responsavel'                  :'Nome do Responsável',
            'tipo_pessoa'                       :'Tipo de Pessoa',
            'numero_documento'                  :'Número do Documento',
            'servico_ativo'                     :'Serviço Ativo',
            'observacoes'                       :'Observações'
        }
        widgets = {
            'nome'                              :   widgets.TextInput,              
            'nome_responsavel'                  :   widgets.TextInput,
            'numero_documento'                  :   widgets.TextInput,
            'servico_ativo'                     :   widgets.CheckboxInput
            }

        error_messages = {
            'numero_documento'                  :   {'invalid' : 'Número de Documento Inválido'}
        }

class AddressInfoForm(forms.ModelForm):
    class Meta():
        model = AddressInfo
        fields = [
            'end_fiscal_CEP',
            'end_fiscal',
            'end_fiscal_numero',
            'end_fiscal_bairro',
            'end_fiscal_complemento',
            'end_fiscal_municipio',
            'end_fiscal_estado',
            'end_fiscal_pais',
            'cont_tel_fixo',
            'cont_tel_fixo_adicional',
            'cont_tel_cel',
            'cont_tel_cel_adicional',
            'cont_email',
            'cont_email_adicional'
        ]

        labels = {
            'end_fiscal_CEP'            :   'CEP', 
            'end_fiscal'                :   'Endereço',
            'end_fiscal_numero'         :   'Número',
            'end_fiscal_bairro'         :   'Bairro',
            'end_fiscal_complemento'    :   'Complemento',
            'end_fiscal_municipio'      :   'Município',
            'end_fiscal_estado'         :   'Estado',
            'end_fiscal_pais'           :   'País',
            'end_servico_CEP'           :   'CEP',
            'cont_tel_fixo'             :   'Telefone Fixo',
            'cont_tel_fixo_adicional'   :   'Telefone Fixo',
            'cont_tel_cel'              :   'Telefone Celular',
            'cont_tel_cel_adicional'    :   'Telefone Celular',
            'cont_email'                :   'E-mail',
            'cont_email_adicional'      :   'E-mail'            
        }

        widgets = {
            'end_fiscal_numero'         :   widgets.TextInput,
            'end_servico_numero'        :   widgets.TextInput,
        }

class ChosenModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChosenModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].__class__.__name__ in ['ChoiceField', 'TypedChoiceField', 'MultipleChoiceField']:
                choices = self.fields[field].choices
                self.fields[field] = chosenforms.ChosenChoiceField(choices=choices)
            elif self.fields[field].__class__.__name__ in ['ModelChoiceField', 'ModelMultipleChoiceField']:
                queryset = self.fields[field].queryset
                self.fields[field] = chosenforms.ChosenModelMultipleChoiceField(queryset=queryset)

    def label_from_instance(self, obj):
            return obj.primeiro_nome

class ContractualInfoForm(ChosenModelForm):
    class Meta:
        model = ContractualInfo

        fields = [
            'funcionario_atrib'
        ]

        labels = {
            'funcionario_atrib' :   'Funcionários Atribuidos'
        }

class ServiceOrderForm(forms.ModelForm):
    class Meta():
        model = ServiceOrder
        fields = [
            'local_servico',
            'produto',
            'observacao'
        ]
        label = {
            'produto' : 'Possui Produto ?',
            'observacao' : 'Observações'
        }

class ServiceDescriptionForm(forms.ModelForm):
    categoria = forms.ChoiceField(choices=lambda: [('---------','---------')]+[(x['categoria'], x['categoria']) for x in FuncBasicInfo.objects.order_by().values('categoria').distinct()])
    class Meta():
        model = ServiceDescription
        fields = [
            'funcionario',
            'qtd_horas',
            'descricao'
        ]
        labels = {
            'funcionario' : 'Funcionário',
            'qtd_horas' : 'Horas',
            'descricao' : 'Descrição'
        }

        widgets = {
            'qtd_horas' : widgets.TextInput
        }

class ServiceGroundForm(forms.ModelForm):
    class meta():
        model = ServiceGround

        fields = [
            'cliente'
            'nome',
            'funcionario_responsavel',
            'CEP',
            'endereco',
            'numero',
            'bairro',
            'complemento',
            'municipio',
            'estado'
        ]

        labels = {
            'nome'  :   'Nome',
            'funcionario_responsavel'   :   'Funcionário Responsável',
            'CEP'   :   'CEP',
            'endereco'  :   'Endereço',
            'numero'    :   'Número',
            'bairro'    :   'Bairro',
            'complemento'   :   'Complemento',
            'municipio' :   'Município',
            'estado'    :   'Estado'
        }

        widgets = {
            'numero'    :   widgets.TextInput
        }

class ServiceRecordForm(forms.Form):
    description = forms.CharField(label = 'Relatório', widget = widgets.Textarea())
    
class LSListing(forms.Form):  
    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente')
        super(LSListing, self).__init__(*args, **kwargs)
        if cliente:
            self.fields.update({'LS' : forms.ModelChoiceField(ServiceGround.objects.filter(cliente = cliente), label = "Local de Serviço")})
        else:
            self.fields.update({'LS' : forms.ModelChoiceField(ServiceGround.objects.all(), label = "Local de Serviço")})
        
class OccurrenceCallForm(forms.ModelForm):
    class Meta:
        model = OccurrenceCall

        fields = ['description']
        label  = {'description' : 'Descrição'}

class OccurrenceCallEditionForm(forms.Form):
    description = forms.CharField(label = 'Descrição', widget = widgets.Textarea())
    status = forms.ChoiceField(choices = (('-----',  '-----'), ('Aberto', 'Aberto'), ('Em Andamento', 'Em Andamento'), ('Fechado', 'Fechado')), label = 'Status do Chamado')

ServiceGroundFormSet = forms.modelformset_factory(
    ServiceGround,
    ServiceGroundForm,
    extra = 1,
    can_delete = True,
    exclude = ['cliente'],
    widgets = {
        'numero'    :   widgets.TextInput
    }
    )

ServiceFormSet = forms.inlineformset_factory(ServiceOrder, ServiceDescription, form = ServiceDescriptionForm, extra = 1, fields=('funcionario', 'qtd_horas', 'descricao'))

TEMPLATES = {
        'Basic Info'        :   'wizard_template_basic_info_cliente.html',
        'Address Info'      :   'wizard_template_address_info_cliente.html',
        'Contractual Info'  :   'wizard_template_contractual_info_cliente.html',
        }

# Form Wizard View Class ----------------------

class CadastroClienteWizard(SessionWizardView):

    file_storage = FileSystemStorage(location = os.path.join(settings.MEDIA_ROOT, 'formwizard_temp_file_storage'))

    def get_template_names(self):
        t = [TEMPLATES[self.steps.current]]
        return t

    def done(self, form_list, form_dict, **kwargs):
        
        # UPDATING OBJECT
        if 'id' in self.kwargs:
            eid = self.kwargs['id']

            for k, v in form_dict.items():
                if k == 'Basic Info' and v.changed_data:
                    cdata = v.cleaned_data
                    basicinfo = BasicInfo.objects.get(id = eid)

                    for attr, value in basicinfo.__dict__.items():
                        if attr in cdata.keys():
                            if not cdata[attr] == "None" and not cdata[attr] == None:
                                exec('basicinfo.' + attr + ' = "' +  str(cdata[attr]) + '"')

                    basicinfo.data_ultima_modificacao = timezone.now()
                    basicinfo.save()

                elif k == 'Address Info' and v.changed_data:
                    cdata = v.cleaned_data
                    addressinfo = AddressInfo.objects.get(basicinfo = eid)
                    
                    for attr, value in addressinfo.__dict__.items():
                        if attr in cdata.keys():
                            if not cdata[attr] == "None" and not cdata[attr] == None:
                                exec('addressinfo.' + attr + ' = "' +  str(cdata[attr]) + '"')
                    addressinfo.save()

                elif k == 'Contractual Info' and v.changed_data:
                    cdata = v.cleaned_data
                    contractualinfo = ContractualInfo.objects.get(basicinfo = eid)

                    funcionarios_atribuidos = [x.id for x in list(cdata.get('funcionario_atrib'))]
                    
                    contractualinfo.funcionario_atrib.set(funcionarios_atribuidos)
                    contractualinfo.save()

                    basicinfo = contractualinfo.basicinfo

                    basicinfo.quantidade_funcionarios_alocados = len(funcionarios_atribuidos)
                    basicinfo.save()

        # CREATING OBJECT
        else:
            eid =  False 

            for k, v in form_dict.items():
                if k == 'Basic Info':
                    cdata = v.cleaned_data
                    cdata['data_cadastro'] = timezone.now()
                    cdata['data_ultima_modificacao'] = timezone.now()
                    if cdata['servico_ativo'] == True:
                        cdata['data_inicio_servico'] = timezone.now()
                    basicinfo = BasicInfo.objects.create(**cdata)
                elif k == 'Address Info':
                    cdata = v.cleaned_data
                    cdata['basicinfo'] = basicinfo
                    AddressInfo.objects.create(**cdata)
                elif k == 'Contractual Info':
                    cdata = v.cleaned_data
                    
                    contractualinfo = ContractualInfo()
                    contractualinfo.basicinfo = basicinfo
                    contractualinfo.save()

                    funcionarios_atribuidos = [x.id for x in list(cdata.get('funcionario_atrib'))]
                    
                    contractualinfo.funcionario_atrib.add(*funcionarios_atribuidos)
                    contractualinfo.save()
                    
                    basicinfo.quantidade_funcionarios_alocados = len(funcionarios_atribuidos)
                    basicinfo.save()
                
        return redirect('/cliente/visualizar/' + (str(eid) if eid else str(basicinfo.id)))

    def get_form_initial(self, step):
        if 'id' in self.kwargs:
            eid = self.kwargs['id']
            if step == 'Basic Info':
                obj = BasicInfo.objects.get(id=eid)
            elif step == "Address Info":
                obj = AddressInfo.objects.get(basicinfo=eid)
            elif step == "Contractual Info":
                obj = ContractualInfo.objects.get(basicinfo=eid)

            modeldict = model_to_dict(obj)
            return modeldict
        else:
            return self.initial_dict.get(step, {})



