import pandas as pd

asistenciaDataFrame = pd.read_csv("./data/asistencia_estudiantes_completo.csv")

# FILTROS O CONSULTAS DETALLADAS
#Necesito encontrar los estudiantes que SI ASISTIERON 
estudiantesQueAsistieron=asistenciaDataFrame.query('estado == "asistio"')
print (estudiantesQueAsistieron)

#Necesito encontrar los estudiantes que FALTARON 
estudiantesQueNoAsistieron=asistenciaDataFrame.query('estado == "inasistencia"')
print (estudiantesQueNoAsistieron)


#Necesito encontrar los estudiantes que LLEGARON TARDE (Justificaron la inasistencia)
estudiantesQueJustificaron=asistenciaDataFrame.query('estado == "justificado"')
print (estudiantesQueJustificaron)

#Necesito encontrar los estudiantes de estrato 1
estudiantesEstraroUno=asistenciaDataFrame.query('estrato == 1')
print (estudiantesEstraroUno)

#Necesito encontrar los estudiantes de estratos altos 5-6
estudiantesEstratoAltos = asistenciaDataFrame.query('estrato == 5 or estrato == 6')
print(estudiantesEstratoAltos)

#Necesito encontrar los estudiantes que llegan en metro
estudiantesMetro = asistenciaDataFrame.query('medio_transporte == "metro"')
print(estudiantesMetro)

#Necesito encontrar estudiantes que llegaron en bicicleta 
estudiantesBicicleta = asistenciaDataFrame.query('medio_transporte == "bicicleta"')
print(estudiantesBicicleta)

#Necesito encontrar todos los estudiantes MENOS los que llegaron a pie
estudiantesNoLlegaronPie = asistenciaDataFrame.query('medio_transporte != "a pie"')
print(estudiantesNoLlegaronPie)

#Necesito todos los registros de asistencia de junio
asistenciaDataFrame['fecha'] = pd.to_datetime(asistenciaDataFrame['fecha'])

asistenciaJunio = asistenciaDataFrame[asistenciaDataFrame['fecha'].dt.month == 6]
if asistenciaJunio.empty:
    print("No asistió nadie en el mes de junio")
else:
    print(asistenciaJunio)

#Necesito todos los estudiantes que usan transportes ecologicos
estudiantesTransporteEcologico = asistenciaDataFrame.query('medio_transporte in ["bicicleta", "a pie", "metro"]')
print(estudiantesTransporteEcologico)

#Necesito los que usan bus y son de estrato alto
estudiantesBusEstratoAlto = asistenciaDataFrame[(asistenciaDataFrame['medio_transporte'] == 'bus') & (asistenciaDataFrame['estrato'] == 6)]
print(estudiantesBusEstratoAlto)

#Necesito los estudiantes que usan bus y son de estrato bajo
estudiantesBusEstratoBajo = asistenciaDataFrame[(asistenciaDataFrame['medio_transporte'] == 'bus') & (asistenciaDataFrame['estrato'] == 1)]
print(estudiantesBusEstratoBajo)

#Necesito estudiantes que caminan para llegar a clases 
estudiantesCaminan = asistenciaDataFrame.query('medio_transporte == "a pie"')
print(estudiantesCaminan)

# CONTEOS POR AGRUPACIONES 
#Necesito el conteo por registros por estado de asistencia 
conteo=asistenciaDataFrame.groupby('estado').size()
print(conteo)

#Necesito obtener el número de registros por estrato 
numeroRegistrosEstrato = asistenciaDataFrame.groupby('estrato').size()
print(numeroRegistrosEstrato)

#Necesito la cantidad de estudiantes por medio de transporte cuantos los que usan x o y transporte, conteo 
conteoTransporte= asistenciaDataFrame.groupby('medio_transporte').size()
print(conteoTransporte)

#Necesito el promedio de estrato por estado de asistencia - el promedio de los que asisten que estratos son y etc
promedioAsistenciaEstrato = asistenciaDataFrame.groupby('estado')['estrato'].mean()
print(promedioAsistenciaEstrato)

#Máximo de estrato por estado 
maximoEstratoPorEstado = asistenciaDataFrame.groupby('estado')['estrato'].max()
print(maximoEstratoPorEstado)

#Minimo de estrato por estado
minimoEstratoPorEstado = asistenciaDataFrame.groupby('estado')['estrato'].min()
print(minimoEstratoPorEstado)

#Necesito un conteo de asistencias por grupo y estado
conteoAsistenciasGrupoyEstado = asistenciaDataFrame.groupby(['id_grupo', 'estado']).size()
print(conteoAsistenciasGrupoyEstado)