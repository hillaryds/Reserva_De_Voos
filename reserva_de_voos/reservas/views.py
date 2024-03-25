from django.shortcuts import render, redirect
from .models import Usuario, Admin, Voo
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import UsuarioForm
from datetime import datetime, date


def index(request):
    return render(request, 'index.html')

def main_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)
        usuarios = Usuario.objects.all()
        
        for usuario in usuarios:
            if usuario.email == email and usuario.senha == password:
                print("Logado com sucesso")
                return redirect('main_page2')
            else:
                user = None
        if user is None:
            print("Login inválido")
            messages.error(request, 'Email ou senha inválidos.')
    
    return render(request, 'pages/main-login.html')
    
def login_adm(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        administrador = authenticate(request, email=email, password=password)
        admins = Admin.objects.all()
        
        for admin in admins:
            if admin.email_admin == email and admin.senha_admin == password:
                print("Logado com sucesso")
                return redirect('adm_voo')
            else:
                administrador = None
        
        if administrador is None:
            print("Login inválido")
            messages.error(request, 'Email ou senha inválidos.')

    return render(request, 'pages/login-adm.html')

# def cad_user(request):
#     if request.method == 'POST':
#         nome = request.POST.get('nome')
#         email = request.POST.get('email')
#         cpf = request.POST.get('cpf')
#         data_nascimento = request.POST.get('data_nascimento')
#         senha = request.POST.get('senha')
        
#         if nome == '' or email == '' or  cpf == '' or data_nascimento == '' or senha == '':
#             messages.error(request, 'Preencha todos os campos.')
#             print("Preencha todos os campos")
#             return redirect('cad_user')
#         else:
#             usuarios = Usuario.objects.all()
        
#             for usuario in usuarios:
#                 if usuario.email == email or usuario.cpf == cpf:
#                     print("Esse user ja existe, cadastre um novo user")
#                     return redirect('cad_user')
            
#             try:
#                 # Tenta salvar o usuário
#                 usuario = Usuario(nome = nome, email = email, cpf = cpf, data_nascimento = data_nascimento, senha = senha)
#                 usuario.save()
#                 print("Usuario salvo com sucesso")
#                 return redirect('index')reservas_
#             except ValueError as e:
#                 print("O usuario não pode ser menor de idade")
#                 return redirect('cad_user')
#     return render(request, 'pages/cad-user.html')

def cad_user(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('input-cpf')
        data_nascimento = request.POST.get('data-nascimento')
        senha = request.POST.get('senha')
        
        if nome == '' or email == '' or  cpf == '' or data_nascimento == '' or senha == '':
            messages.error(request, 'Preencha todos os campos.')
            print("Preencha todos os campos")
            return redirect('cad_user')
        
        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, 'CPF já cadastrado.')
            return redirect('cad_user')
        
        # Verifica se o e-mail já está cadastrado
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
            return redirect('cad_user')
        
        try:

            if data_nascimento:
                data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()
            else:
                raise ValueError("Data de nascimento não fornecida.")
            
            today = date.today()
            age = today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
            if age < 18:
                raise ValueError("O usuário deve ter mais de 18 anos.")
            usuario = Usuario(nome=nome, email=email, cpf=cpf, data_nascimento=data_nascimento, senha=senha)
            
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('index')
        except ValueError as e:
            messages.error(request, str(e))  # A mensagem de erro será a que foi definida no método save do modelo
            return redirect('cad_user')
    
    return render(request, 'pages/cad-user.html')

def main_page2(request):
    return render(request, 'pages/main-page2.html')

def adm_voo(request):
    return render(request, 'pages/adm-voo.html')

def cad_voo(request):
    if request.method == 'POST':
        id_voo = request.POST.get('input-assentos')
        origem = request.POST.get('input-origem')
        destino = request.POST.get('nome')
        data_voo = request.POST.get('data-voo')
        horario_saida = request.POST.get('senha')
        horario_chegada = request.POST.get('voo-chegada')
        preco_economica = request.POST.get('preco-economica')
        preco_executiva = request.POST.get('preco-executiva')

        if '' in [id_voo, origem, destino, data_voo, horario_saida, horario_chegada, preco_economica, preco_executiva]:
            messages.error(request, 'Preencha todos os campos.')
            return redirect('cad_voo')

    
        if Voo.objects.filter(id_voo=id_voo).exists():
            messages.error(request, 'Já existe um voo com esse ID.')
            return redirect('cad_voo')

        try:
            voo = Voo.objects.create(
                id_voo=id_voo,
                origem=origem,
                destino=destino,
                data=data_voo,
                horario_saida=horario_saida,
                horario_chegada=horario_chegada,
                preco_economica=preco_economica,
                preco_executiva=preco_executiva,
                assentos='133'
            )
            messages.success(request, 'Voo cadastrado com sucesso!')
            return redirect('adm_voo')
        except Exception:
            messages.error(request, f'Erro ao cadastrar o voo ')

    return render(request, 'pages/cad-voo.html')

def list_voo(request):
    return render(request, 'pages/list-voo.html')



