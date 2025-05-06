import pandas as pd

UsuarioDataFrame = pd.read_excel("./data/usuarios_sistema_completo.xlsx")

UsuarioDataFrame['direccion'] = UsuarioDataFrame['direccion'].fillna('sin direccion')
print(UsuarioDataFrame)

UsuarioDataFrame['especialidad'] = UsuarioDataFrame['especialidad'].fillna('Otras ingenierias')
print(UsuarioDataFrame)

#Necesito solo un listado de tabla con los aprendices o estudiantes
listadoEstudiantes = UsuarioDataFrame.loc[UsuarioDataFrame['tipo_usuario'] == 'estudiante', ['id', 'nombre_usuario']]
print(listadoEstudiantes)

#Necesito solo un listado con instructores o profesores 
listadoProfesores = UsuarioDataFrame.loc[UsuarioDataFrame['tipo_usuario'] == 'docente', ['id', 'nombre_usuario']]
print(listadoProfesores)

#Necesito un listado de especialistas en desarrollo web o sistemas 
especialistasSistemas = UsuarioDataFrame.query('especialidad == "Ingenieria de Sistemas"')
print(especialistasSistemas)

#Necesito un listado con solo usuarios de la ciudad de Medellin
usuariosMedellin = UsuarioDataFrame.query('direccion == "Medellin"')

if usuariosMedellin.empty:
    print("No existe nadie en la ciudad de Medellín")
else:
    print(usuariosMedellin)
    
#Necesito un listado de los usuarios que cuyas direcciones terminen en sur 
usuariosDireccionSur = UsuarioDataFrame[UsuarioDataFrame['direccion'].str.endswith('sur', na=False)]
print(usuariosDireccionSur)


#Necesito un listado de especialistas o de profesores que contengan la palabra DATOS 
profesoresPalabraDatos = UsuarioDataFrame[(UsuarioDataFrame['tipo_usuario'] == 'docente') & (UsuarioDataFrame['especialidad'].str.contains('datos', na=False))]
print(profesoresPalabraDatos)

#Necesito docentes de Itagui
docentesItagui = UsuarioDataFrame.query('tipo_usuario == "docente" and direccion == "Itagui"')
if docentesItagui.empty:
    print("No tenemos disponibles docentes en Itagui")
else:
    print(docentesItagui)

#Necesito una lista de nacidos en los 90 o antes
UsuarioDataFrame['fecha_nacimiento'] = pd.to_datetime(UsuarioDataFrame['fecha_nacimiento'], errors='coerce')

nacidos90s = UsuarioDataFrame.query('fecha_nacimiento.dt.year <= 1999')
print(nacidos90s)

#Necesito un listado de instructores o profesores mayores osea viejitos 
instructoresMayores40 = UsuarioDataFrame.query('tipo_usuario == "docente" and fecha_nacimiento.dt.year <= 1984')
if instructoresMayores40.empty:
    print("No tenemos profesores mayores de 40 años")
else:
    print(instructoresMayores40)


#Necesito un listado de profesores o estudiantes nacidos en el nuevo milenium
nacidosNuevoMilenio = UsuarioDataFrame.query('fecha_nacimiento.dt.year >= 2000 and (tipo_usuario == "docente" or tipo_usuario == "estudiante")')
print(nacidosNuevoMilenio)








# errors='coerce': Si encuentras un valor que no se pueda convertir, en lugar de lanzar un error, coloca NaT
# str.endswith: Verifica si la dirección termina con sur