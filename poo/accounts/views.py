from abc import ABCMeta
from django.shortcuts import render, redirect
from .person_controller import Usuario, Admin
from .forms import ClienteForm, AdminForm

# Create your views here.


def crear_cliente(request):

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        print(">>", request)
        print("nombre: ", form['first_name'].value())

        primer_nombre = form['first_name'].value()
        apellido = form['last_name'].value()
        fecha_nacimiento = form['fecha_nacimiento'].value()
        email = form['email'].value()

        usuario = Usuario()
        usuario.set_nombre(primer_nombre)
        usuario.set_apellido(apellido)
        usuario.set_fecha_nacimiento(fecha_nacimiento)
        usuario.set_correo(email)

        ok, response = usuario.crear_usuario()

        if ok:
            return redirect('/lugares/listar')
        else:
            print(response)

    else:
        form = ClienteForm()

        return render(request, 'usuarios/usuarios_crear.html', {'form': form})


def crear_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)

        print(">>", request)
        print("nombre: ", form['first_name'].value())

        primer_nombre = form['first_name'].value()
        apellido = form['last_name'].value()
        fecha_nacimiento = form['fecha_nacimiento'].value()
        email = form['email'].value()
        rol = form['rol'].value()
        print("rol: ", form['rol'].value())
        is_super_admin = form['is_super_admin'].value()

        usuario = Admin()
        usuario.set_nombre(primer_nombre)
        usuario.set_apellido(apellido)
        usuario.set_fecha_nacimiento(fecha_nacimiento)
        usuario.set_correo(email)
        usuario.set_rol(rol)
        usuario.is_super_admin(is_super_admin)

        ok, response = usuario.crear_usuario()

        if ok:
            return redirect('/lugares/listar')
        else:
            print(response)

    else:
        form = AdminForm()

        return render(request, 'usuarios/usuarios_admin_crear.html', {'form': form})


def editar_perfil(request, usuario_id):
    usuario_obj = Usuario()
    usuario = usuario_obj.search_client(usuario_id)

    if request.method == 'GET':
        form = ClienteForm(instance=usuario)
    else:
        form = ClienteForm(request.POST, instance=usuario)
        primer_nombre = form['first_name'].value()
        apellido = form['last_name'].value()
        fecha_nacimiento = form['fecha_nacimiento'].value()
        email = form['email'].value()

        usuario_obj.set_nombre(primer_nombre)
        usuario_obj.set_apellido(apellido)
        usuario_obj.set_fecha_nacimiento(fecha_nacimiento)
        usuario_obj.set_correo(email)

        print(">>>", usuario_id)
        ok, response = usuario_obj.editar_perfil(usuario_id)
        if ok:
            return redirect('/lugares/listar')

    return render(request, 'usuarios/usuarios_crear.html', {'form': form})
