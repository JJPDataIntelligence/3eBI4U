from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from .utilities import validateCPF, validateCNPJ, validateCEP, validateNoFutureDates, validateCPFCNPJ
from Funcionario.models import BasicInfo as Funcionario
from django.utils import timezone
import datetime

# App Logic ------------------------------------------------------------------------------------------------------------------------------------------

# Choice Fields Lists
brazilian_states_choices    = [
    ('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'),
    ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')
]
race_choices                = [
    ('INDIGENA', 'Indigena'), ('BRANCA', 'Branca'), ('NEGRA', 'Negra'), ('AMARELA', 'Amarela'), ('PARDA', 'Parda'), ('NAO_INFORMADO', 'Prefiro Não Informar')
]
gender_choices              = [
    ('MASCULINO', 'Masculino'), ('FEMININO', 'Feminino'), ('OUTRO', 'Outro'), ('NAO_INFORMADO', 'Prefiro Não Informar')
]
civil_state_choices         = [
    ('CASADO', 'Casado(a)'), ('SOLTEIRO', 'Solteiro(a)'), ('VIUVO', 'Viuvo(a)'), 
    ('DIVORCIADO', 'Divorciado(a)'), ('UNIAO ESTAVEL', 'União Estável')
]
country_choices             = [
    ('Afeganistão', 'Afeganistão'), ('África do Sul', 'África do Sul'), ('Akrotiri', 'Akrotiri'), ('Albânia', 'Albânia'), ('Alemanha', 'Alemanha'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguila', 'Anguila'), ('Antárctida', 'Antárctida'), ('Antígua e Barbuda', 'Antígua e Barbuda'), ('Arábia Saudita', 'Arábia Saudita'), ('Arctic Ocean', 'Arctic Ocean'), ('Argélia', 'Argélia'), ('Argentina', 'Argentina'), ('Arménia', 'Arménia'), ('Aruba', 'Aruba'), ('Ashmore and Cartier Islands', 'Ashmore and Cartier Islands'), ('Atlantic Ocean', 'Atlantic Ocean'), ('Austrália', 'Austrália'), ('Áustria', 'Áustria'), ('Azerbaijão', 'Azerbaijão'), ('Baamas', 'Baamas'), ('Bangladeche', 'Bangladeche'), ('Barbados', 'Barbados'), ('Barém', 'Barém'), ('Bélgica', 'Bélgica'), ('Belize', 'Belize'), ('Benim', 'Benim'), ('Bermudas', 'Bermudas'), ('Bielorrússia', 'Bielorrússia'), ('Birmânia', 'Birmânia'), ('Bolívia', 'Bolívia'), ('Bósnia e Herzegovina', 'Bósnia e Herzegovina'), ('Botsuana', 'Botsuana'), ('Brasil', 'Brasil'), ('Brunei', 'Brunei'), ('Bulgária', 'Bulgária'), ('Burquina Faso', 'Burquina Faso'), ('Burúndi', 'Burúndi'), ('Butão', 'Butão'), ('Cabo Verde', 'Cabo Verde'), ('Camarões', 'Camarões'), ('Camboja', 'Camboja'), ('Canadá', 'Canadá'), ('Catar', 'Catar'), ('Cazaquistão', 'Cazaquistão'), ('Chade', 'Chade'), ('Chile', 'Chile'), ('China', 'China'), ('Chipre', 'Chipre'), ('Clipperton Island', 'Clipperton Island'), ('Colômbia', 'Colômbia'), ('Comores', 'Comores'), ('Congo-Brazzaville', 'Congo-Brazzaville'), ('Congo-Kinshasa', 'Congo-Kinshasa'), ('Coral Sea Islands', 'Coral Sea Islands'), ('Coreia do Norte', 'Coreia do Norte'), ('Coreia do Sul', 'Coreia do Sul'), ('Costa do Marfim', 'Costa do Marfim'), ('Costa Rica', 'Costa Rica'), ('Croácia', 'Croácia'), ('Cuba', 'Cuba'), ('Curacao', 'Curacao'), ('Dhekelia', 'Dhekelia'), ('Dinamarca', 'Dinamarca'), ('Domínica', 'Domínica'), ('Egipto', 'Egipto'), ('Emiratos Árabes Unidos', 'Emiratos Árabes Unidos'), ('Equador', 'Equador'), ('Eritreia', 'Eritreia'), ('Eslováquia', 'Eslováquia'), ('Eslovénia', 'Eslovénia'), ('Espanha', 'Espanha'), ('Estados Unidos', 'Estados Unidos'), ('Estónia', 'Estónia'), ('Etiópia', 'Etiópia'), ('Faroé', 'Faroé'), ('Fiji', 'Fiji'), ('Filipinas', 'Filipinas'), ('Finlândia',
    'Finlândia'), ('França', 'França'), ('Gabão', 'Gabão'), ('Gâmbia', 'Gâmbia'), ('Gana', 'Gana'), ('Gaza Strip', 'Gaza Strip'), ('Geórgia', 'Geórgia'), ('Geórgia do Sul e Sandwich do Sul', 'Geórgia do Sul e Sandwich do Sul'), ('Gibraltar', 'Gibraltar'), ('Granada', 'Granada'), ('Grécia', 'Grécia'), ('Gronelândia', 'Gronelândia'), ('Guame', 'Guame'), ('Guatemala', 'Guatemala'), ('Guernsey', 'Guernsey'), ('Guiana', 'Guiana'), ('Guiné', 'Guiné'), ('Guiné Equatorial', 'Guiné Equatorial'), ('Guiné-Bissau', 'Guiné-Bissau'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hong Kong', 'Hong Kong'), ('Hungria', 'Hungria'), ('Iémen', 'Iémen'), ('Ilha Bouvet', 'Ilha Bouvet'), ('Ilha do Natal', 'Ilha do Natal'), ('Ilha Norfolk', 'Ilha Norfolk'), ('Ilhas Caimão', 'Ilhas Caimão'), ('Ilhas Cook', 'Ilhas Cook'), ('Ilhas dos Cocos', 'Ilhas dos Cocos'), ('Ilhas Falkland', 'Ilhas Falkland'), ('Ilhas Heard e McDonald', 'Ilhas Heard e McDonald'), ('Ilhas Marshall', 'Ilhas Marshall'), ('Ilhas Salomão', 'Ilhas Salomão'), ('Ilhas Turcas e Caicos', 'Ilhas Turcas e Caicos'), ('Ilhas Virgens Americanas', 'Ilhas Virgens Americanas'), ('Ilhas Virgens Britânicas', 'Ilhas Virgens Britânicas'), ('Índia', 'Índia'), ('Indian Ocean', 'Indian Ocean'), ('Indonésia', 'Indonésia'), ('Irão', 'Irão'), ('Iraque', 'Iraque'), ('Irlanda', 'Irlanda'), ('Islândia', 'Islândia'), ('Israel', 'Israel'), ('Itália', 'Itália'), ('Jamaica', 'Jamaica'), ('Jan Mayen', 'Jan Mayen'), ('Japão', 'Japão'), ('Jersey', 'Jersey'), ('Jibuti', 'Jibuti'), ('Jordânia', 'Jordânia'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Laos', 'Laos'), ('Lesoto', 'Lesoto'), ('Letónia', 'Letónia'), ('Líbano', 'Líbano'), ('Libéria', 'Libéria'), ('Líbia', 'Líbia'), ('Listenstaine', 'Listenstaine'), ('Lituânia', 'Lituânia'), ('Luxemburgo', 'Luxemburgo'), ('Macau',
    'Macau'), ('Macedónia', 'Macedónia'), ('Madagáscar', 'Madagáscar'), ('Malásia', 'Malásia'), ('Malávi', 'Malávi'), ('Maldivas', 'Maldivas'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Man, Isle of', 'Man, Isle of'), ('Marianas do Norte', 'Marianas do Norte'), ('Marrocos', 'Marrocos'), ('Maurícia', 'Maurícia'), ('Mauritânia', 'Mauritânia'), ('México', 'México'), ('Micronésia', 'Micronésia'), ('Moçambique', 'Moçambique'), ('Moldávia', 'Moldávia'), ('Mónaco', 'Mónaco'), ('Mongólia', 'Mongólia'), ('Monserrate', 'Monserrate'), ('Montenegro', 'Montenegro'), ('Mundo', 'Mundo'), ('Namíbia', 'Namíbia'), ('Nauru', 'Nauru'), ('Navassa Island', 'Navassa Island'), ('Nepal', 'Nepal'), ('Nicarágua', 'Nicarágua'), ('Níger', 'Níger'), ('Nigéria', 'Nigéria'), ('Niue', 'Niue'), ('Noruega', 'Noruega'), ('Nova Caledónia', 'Nova Caledónia'), ('Nova Zelândia', 'Nova Zelândia'), ('Omã', 'Omã'), ('Pacific Ocean', 'Pacific Ocean'), ('Países Baixos', 'Países Baixos'), ('Palau', 'Palau'), ('Panamá', 'Panamá'), ('Papua-Nova Guiné', 'Papua-Nova Guiné'), ('Paquistão', 'Paquistão'), ('Paracel Islands', 'Paracel Islands'), ('Paraguai', 'Paraguai'), ('Peru', 'Peru'), ('Pitcairn', 'Pitcairn'), 
    ('Polinésia Francesa', 'Polinésia Francesa'), ('Polónia', 'Polónia'), ('Porto Rico', 'Porto Rico'), ('Portugal', 'Portugal'), ('Quénia', 'Quénia'), ('Quirguizistão', 'Quirguizistão'), ('Quiribáti', 'Quiribáti'), ('Reino Unido', 'Reino Unido'), ('República Centro-Africana', 'República Centro-Africana'), ('República Checa', 'República Checa'), ('República Dominicana', 'República Dominicana'), ('Roménia', 'Roménia'), ('Ruanda', 'Ruanda'), ('Rússia', 'Rússia'), ('Salvador', 'Salvador'), ('Samoa', 'Samoa'), ('Samoa Americana', 'Samoa Americana'), ('Santa Helena', 'Santa Helena'), ('Santa Lúcia', 'Santa Lúcia'), ('São Bartolomeu', 'São Bartolomeu'), ('São Cristóvão e Neves', 'São Cristóvão e Neves'), ('São Marinho', 'São Marinho'), ('São Martinho', 'São Martinho'), ('São Pedro e Miquelon', 'São Pedro e Miquelon'), ('São Tomé e Príncipe', 'São Tomé e Príncipe'), ('São Vicente e Granadinas', 'São Vicente e Granadinas'), ('Sara Ocidental', 'Sara Ocidental'), ('Seicheles', 'Seicheles'), ('Senegal', 'Senegal'), ('Serra Leoa', 'Serra Leoa'), ('Sérvia', 'Sérvia'), ('Singapura', 'Singapura'), ('Sint Maarten', 'Sint Maarten'), ('Síria', 'Síria'), ('Somália', 'Somália'), ('Southern Ocean', 'Southern Ocean'), ('Spratly Islands', 'Spratly Islands'), ('Sri Lanca', 'Sri Lanca'), ('Suazilândia', 'Suazilândia'), ('Sudão', 'Sudão'), ('Sudão do Sul', 'Sudão do Sul'), ('Suécia', 'Suécia'), ('Suíça', 'Suíça'), ('Suriname', 'Suriname'), ('Svalbard e Jan Mayen', 'Svalbard e Jan Mayen'), ('Tailândia', 'Tailândia'), ('Taiwan', 'Taiwan'), ('Tajiquistão', 'Tajiquistão'), ('Tanzânia', 'Tanzânia'), ('Território Britânico do Oceano Índico', 'Território Britânico do Oceano Índico'), ('Territórios Austrais Franceses', 'Territórios Austrais Franceses'), ('Timor Leste', 'Timor Leste'), ('Togo', 'Togo'), ('Tokelau', 'Tokelau'), ('Tonga', 'Tonga'), ('Trindade e Tobago', 'Trindade e Tobago'), ('Tunísia', 'Tunísia'), ('Turquemenistão', 'Turquemenistão'), ('Turquia', 'Turquia'), ('Tuvalu', 'Tuvalu'), ('Ucrânia', 'Ucrânia'), ('Uganda', 'Uganda'), ('União Europeia', 'União Europeia'), ('Uruguai', 'Uruguai'), ('Usbequistão', 'Usbequistão'), ('Vanuatu', 'Vanuatu'), ('Vaticano', 'Vaticano'), ('Venezuela', 'Venezuela'), ('Vietname', 'Vietname'), ('Wake Island', 'Wake Island'), ('Wallis e Futuna', 'Wallis e Futuna'), ('West Bank', 'West Bank'), ('Zâmbia', 'Zâmbia'), ('Zimbabué', 'Zimbabué')
]
CNH_category_choices        = [ 
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E')   
]
disableness_choices         = [
    ('Motora', 'Motora'),
    ('Visual', 'Visual'),
    ('Fisica', 'Fisica'),
    ('Auditiva', 'Auditiva'),
    ('Mental', 'Mental'),
    ('Intelectual', 'Intelectual'),
    ('Reabilitado', 'Reabilitado')
]
bank_choices                = [
    ('Banco do Brasil', 'Banco do Brasil'), ('Banco Central do Brasil', 'Banco Central do Brasil'), ('Banco da Amazônia', 'Banco da Amazônia'), ('Banco do Nordeste do Brasil', 'Banco do Nordeste do Brasil'), ('Banco Nacional de Desenvolvimento Econômico e Social', 'Banco Nacional de Desenvolvimento Econômico e Social'), ('Caixa Econômica Federal', 'Caixa Econômica Federal'), ('Banco Regional de Desenvolvimento do Extremo Sul', 'Banco Regional de Desenvolvimento do Extremo Sul'), ('Banco de Desenvolvimento de Minas Gerais', 'Banco de Desenvolvimento de Minas Gerais'), ('Banco de Brasília', 'Banco de Brasília'), ('Banco do Estado de Sergipe', 'Banco do Estado de Sergipe'), ('Banco do Estado do Espírito Santo', 'Banco do Estado do Espírito Santo'), ('Banco do Estado do Pará', 'Banco do Estado do Pará'), ('Banco do Estado do Rio Grande do Sul', 'Banco do Estado do Rio Grande do Sul'), ('Banco ABN Amro S.A.', 'Banco ABN Amro S.A.'), ('Banco Alfa', 'Banco Alfa'), ('Banco Banif', 'Banco Banif'), ('Banco BBM', 'Banco BBM'), ('Banco BMG', 'Banco BMG'),
    ('Banco Bonsucesso', 'Banco Bonsucesso'), ('Banco BTG Pactual', 'Banco BTG Pactual'), ('Banco Cacique', 'Banco Cacique'), ('Banco Caixa Geral - Brasil', 'Banco Caixa Geral - Brasil'), ('Banco Citibank', 'Banco Citibank'), ('Banco Credibel', 'Banco Credibel'), ('Banco Credit Suisse', 'Banco Credit Suisse'), ('Banco Fator', 'Banco Fator'), ('Banco Fibra', 'Banco Fibra'), ('Agibank', 'Agibank'), ('Banco Guanabara', 'Banco Guanabara'), ('Banco Industrial do Brasil', 'Banco Industrial do Brasil'), ('Banco Industrial e Comercial', 'Banco Industrial e Comercial'), ('Banco Indusval', 'Banco Indusval'), ('Banco Inter', 'Banco Inter'), ('Banco Itaú BBA', 'Banco Itaú BBA'), ('Banco ItaúBank', 'Banco ItaúBank'), ('Banco Itaucred Financiamentos', 'Banco Itaucred Financiamentos'), ('Banco Mercantil do Brasil', 'Banco Mercantil do Brasil'), ('Banco Modal', 'Banco Modal'), ('Banco Morada', 'Banco Morada'), ('Banco Pan', 'Banco Pan'), ('Banco Paulista', 'Banco Paulista'), ('Banco Pine', 'Banco Pine'), ('Banco Renner', 'Banco Renner'), ('Banco Ribeirão Preto', 'Banco Ribeirão Preto'), ('Banco Safra', 'Banco Safra'), ('Banco Santander', 'Banco Santander'), ('Banco Sofisa', 'Banco Sofisa'), 
    ('Banco Topázio', 'Banco Topázio'), ('Banco Votorantim', 'Banco Votorantim'), ('Bradesco', 'Bradesco'), ('Itaú Unibanco', 'Itaú Unibanco'), ('Banco Original', 'Banco Original'), ('Nu Pagamentos S.A', 'Nu Pagamentos S.A')
]
intern_schooling_choices    = [
    ('Fundamental','Fundamental'),
    ('Médio', 'Médio'),
    ('Técnico', 'Técnico'),
    ('Superior', 'Superior')      
]
position_choices            = [
    ('Supervisor 1', 'Supervisor 1'),
    ('Supervisor 2', 'Supervisor 2'),
    ('Supervisor 3', 'Supervisor 3'),
    ('Seguranca 1', 'Seguranca 1'),
    ('Seguranca 2', 'Seguranca 2'),
    ('Seguranca 3', 'Seguranca 3'),
    ('Aux Limpeza', 'Aux Limpeza'),
    ('Aux administrativo', 'Aux administrativo'),
    ('Gerente', 'Gerente'),
    ('Diretor', 'Diretor')
]
grau_parentesco_choices     = [
    ('1', 'Cônjuge'),
    ('2','Companheiro (a) com o (a) qual tenha filhos ou viva a mais de 05 anos ou possua Declaração de união Estável '),
    ('3','Filho(a) ou Enteado(a)'),
    ('4','Filho(a) ou Enteado(a), universitario(a) ou cursando escola técnica de 2º Grau'),
    ('5','Irmão(ã), Neto(a) ou Bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial '),
    ('6','Irmão(ã), Neto(a) ou Bisneto(a) sem arrimo dos pais, universitário(a) ou cursando escola técnica de 2º Grau do(a) qual detenha Guarda Judicial'),
    ('7','Pais, avós e bisavós'),
    ('8','Menor pobre do qual detenha guarda judicial'),
    ('9','A pessoa absolutamente incapaz, do qual seja tutor ou curador'),
    ('10','Ex-Cônjuge')
]

# Regex Validators 
phoneRegex = RegexValidator(
    regex=r'^(\+\d{0,4})?(\(\d{0,3}\))?([0-9\-]{7,15})$',
    message="Entre Telefone no Formato: '(DDD)99999-9999'."
)

# Models --------------------------------------------------------------------------------------------------------------------------------------------

# 1 - Basic Info
class BasicInfo(models.Model):



    id                                  =   models.BigAutoField(primary_key = True)

    nome                                =   models.CharField(max_length = 100, null = True, blank = True, verbose_name = "Nome")
    nome_responsavel                    =   models.CharField(max_length = 100, null = True, blank = True, verbose_name = "Nome do Responsável" )

    tipo_pessoa                         =   models.CharField(max_length = 1, null = True, blank = True, choices = [('F', 'Física'), ('J', 'Jurídica')], verbose_name = "Tipo de Pessoa")
    numero_documento                    =   models.CharField(max_length = 18, validators = [validateCPFCNPJ], null = True, blank = True, verbose_name = "Número do Documento")

    servico_ativo                       =   models.BooleanField(default = True, verbose_name = "Serviço Ativo")

    quantidade_funcionarios_alocados    =   models.IntegerField(default = 1, verbose_name = "Qtd. Funcionários Alocados")

    observacoes                         =   models.TextField(null = True, blank = True, verbose_name = "Observações")

    data_cadastro                       =   models.DateTimeField(null = True, blank = True, verbose_name = "Data de Cadastro")
    data_ultima_modificacao             =   models.DateTimeField(null = True, blank = True, verbose_name = "Data Ultima Modificação")

    data_inicio_servico                 =   models.DateTimeField(null = True, blank = True, verbose_name = "Data Início de Serviço")
    data_fim_servico                    =   models.DateTimeField(null = True, blank = True, verbose_name = "Data Fim de Serviço")

    def __str__(self):
        return str(self.nome)

# 2 - Address Info
class AddressInfo(models.Model):

    basicinfo                   =   models.OneToOneField(BasicInfo, models.CASCADE, primary_key = True, related_name = "address_info")

    end_fiscal_CEP              =   models.CharField(max_length = 9, null = True, blank = True, validators=[validateCEP])
    end_fiscal                  =   models.CharField(max_length = 500, null = True, blank = True)
    end_fiscal_numero           =   models.IntegerField(null = True, blank = True)
    end_fiscal_bairro           =   models.CharField(max_length = 200, null = True, blank = True)
    end_fiscal_complemento      =   models.CharField(max_length = 100, null = True, blank = True)
    end_fiscal_municipio        =   models.CharField(max_length = 200, null = True, blank = True)
    end_fiscal_estado           =   models.CharField(max_length = 2, choices = brazilian_states_choices, null = True, blank = True)
    end_fiscal_pais             =   models.CharField(max_length = 200, choices = country_choices, null = True, blank = True)
    
    cont_tel_fixo               =   models.CharField(validators=[phoneRegex], max_length = 17, null = True, blank = True)
    cont_tel_fixo_adicional     =   models.CharField(validators=[phoneRegex], max_length = 17, null = True, blank = True)
    cont_tel_cel                =   models.CharField(validators=[phoneRegex], max_length = 17, null = True, blank = True)
    cont_tel_cel_adicional      =   models.CharField(validators=[phoneRegex], max_length = 17, null = True, blank = True)
    
    cont_email                  =   models.EmailField(null = True, blank = True)
    cont_email_adicional        =   models.EmailField(null = True, blank = True)

# 3 - Contractual Info
class ContractualInfo(models.Model):

    basicinfo                   =   models.OneToOneField(BasicInfo, models.CASCADE, primary_key = True, related_name = "contractual_info")

    funcionario_atrib           =   models.ManyToManyField(Funcionario, related_name = "funcionarios_atribuidos")

# 4 - SERVICE GROUNDS
class ServiceGround(models.Model):
    
    cliente                     =   models.ForeignKey(BasicInfo, models.CASCADE, related_name = "local_servico_cliente")

    nome                        =   models.CharField(max_length = 300, null = True, blank = True)
    funcionario_responsavel     =   models.ForeignKey(Funcionario, models.CASCADE, related_name = "local_servico_responsavel")

    CEP                         =   models.CharField(max_length = 9, null = True, blank = True, validators=[validateCEP])
    endereco                    =   models.CharField(max_length = 500, null = True, blank = True)
    numero                      =   models.IntegerField(null = True, blank = True)
    bairro                      =   models.CharField(max_length = 200, null = True, blank = True)
    complemento                 =   models.CharField(max_length = 100, null = True, blank = True)
    municipio                   =   models.CharField(max_length = 200, null = True, blank = True)
    estado                      =   models.CharField(max_length = 2, choices = brazilian_states_choices, null = True, blank = True)

    def __str__(self):
        return str(self.cliente) + ' | ' + str(self.nome)

# 5 -SERVICE ORDERS
class ServiceOrder(models.Model):
    
    # PRIMARY KEY
    id = models.BigAutoField(primary_key = True)

    # RELATIONAL FIELDS
    cliente         =   models.ForeignKey(BasicInfo, models.CASCADE, related_name = "ordem_servico_cliente", verbose_name = 'Cliente', null = True, blank = True)
    local_servico   =   models.ForeignKey(ServiceGround, models.CASCADE, related_name = "ordem_servico_ls", verbose_name = 'Local de Serviço', null = True, blank = True)
    fatura          =   models.ForeignKey("Financeiro.Fatura", models.CASCADE, related_name = "ordem_servico_fatura", null = True, blank = True)


    # MAIN MODEL FIELDS
    data_emissao    =   models.DateField(null = True, blank = True, auto_now_add = True, verbose_name = 'Data de Emissão')
    observacao      =   models.TextField(blank = True, null = True, verbose_name = 'Observações')

    # BOOLEAN FIELDS
    produto         =   models.BooleanField(default = False, verbose_name = 'Possui Produto ?')
    faturado        =   models.BooleanField(default = False, verbose_name = 'Faturado')

    @property
    def has_LS(self):
        return True if self.local_servico else False
    
    @property
    def has_OBS(self):
        return True if self.observacao else False
    
    @property
    def has_SD(self):
        return True if self.descricao_servico_OS.all().count() > 0 else False

    @property
    def is_empty(self):
        return False if self.has_LS or self.has_OBS or self.has_SD else True

    @property
    def Total(self):
        return sum([x.valor_total for x in list(self.descricao_servico_OS.all())])

    @property
    def OS(self):
        return str(self.data_emissao.strftime('%Y')) + str(self.data_emissao.strftime('%m')) + str(self.id)

    def __str__(self):
        return self.OS

    class Meta:
        permissions = (
            ("can_view_OSList", "Grants Permission to OS Listing View"),
            
        )

# 6 - SERVICE DESCRIPTION
class ServiceDescription(models.Model):
    
    # PRIMARY KEY
    id = models.BigAutoField(primary_key = True)

    # RELATIONAL FIELDS
    funcionario     =   models.ForeignKey(Funcionario, models.CASCADE, related_name = 'descricao_servico_funcionario')
    SO              =   models.ForeignKey(ServiceOrder, models.CASCADE, null = True, blank = True, related_name = 'descricao_servico_OS')

    # MAIN MODEL FIELDS
    qtd_horas       =   models.IntegerField(null = True, blank = True)
    valor_hora      =   models.DecimalField(max_digits = 8, decimal_places = 2, null = True, blank = True)
    valor_total     =   models.DecimalField(max_digits = 11, decimal_places = 2, null = True, blank = True)
    descricao       =   models.CharField(max_length = 200, null = True, blank = True, verbose_name = 'Descrição')

    def save(self,force_insert = False, force_update = False):
        self.valor_hora = self.funcionario.valor_hora_receita
        self.valor_total = self.valor_hora * self.qtd_horas
        super(ServiceDescription, self).save(force_insert, force_update)

# 7 - PRODUCT DESCRIPTION

# 8 - DAILY SERVICE RECORD
class ServiceRecord(models.Model):
    
    # PRIMARY KEY
    id = models.BigAutoField(primary_key = True)

    # RELATIONAL FIELDS
    LS = models.ForeignKey(ServiceGround, models.CASCADE, 'service_record')
    
    # REGULAR FIELDS
    data = models.DateField(auto_now_add = True)
    description = models.TextField(verbose_name = 'Relatório')

    def __str__(self):
        return str(self.LS) + ' | ' +  str(self.data)

    class Meta:
        unique_together = ('data', 'LS')

# 9 - OCCURRENCE CALL
class OccurrenceCall(models.Model):
    
    # PRIMARY KEY
    id = models.BigAutoField(primary_key = True)

    # RELATIONAL FIELDS
    LS = models.ForeignKey(ServiceGround, models.CASCADE, 'ServiceOccurence')

    # REGULAR FIELDS
    data = models.DateField(auto_now_add = True)
    description = models.TextField()
    motive = models.TextField()
    status = models.CharField(max_length = 100, choices = [('Aberto','Aberto'), ('Fechado', 'Fechado'),('Em Andamento', 'Em Andamento')])

    @property
    def OC(self):
        return str(self.data.strftime('%Y')) + str(self.data.strftime('%m')) + str(self.id)

    def __str__(self):
        return "Chamado #" + str(self.OC)

    class Meta:
        permissions = (
            ("occurrence_listing_viewer", "Grants Permission to Occurrence Listing View"),
            ("occurrence_manage", "Grants Permission to manage Occurrence Calls"),
            
        )
