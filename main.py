import sys
import timetablepy

if __name__ == "__main__":

	# print(sys.argv)
	subject = sys.argv[1]
	interface = sys.argv[2]

	elapsed_time = 0
	if len(sys.argv) > 3:
		elapsed_time = sys.argv[3]

	if interface == 'reminder':
		if subject == 'database':
			timetablepy.reminder('Base de Datos Avanzadas', '2305', 'Teórica y Práctica', '7:00 - 8:30', subject)
		elif subject == 'etica':
			timetablepy.reminder('Sociedad, Desarrollo y Ciudad de México', '2301', 'Teórica', '13:00 - 14:30', subject)
		elif subject == 'machine':
			timetablepy.reminder('Aprendizaje Automático', '1405', 'Teórica y Práctica', '19:00 - 22:00', subject)
		elif subject == 'model':
			timetablepy.reminder('Análisis y Modelo de Sistemas Software', '1302', 'Teórica', '11:30 - 13:00', subject)
		elif subject == 'redes':
			timetablepy.reminder('Interconexión de Redes', 'LAB-004', 'Teórica y Práctica', '18:00 - 20:00', subject)
		elif subject == 'web':
			timetablepy.reminder('Desarrollo de Aplicaciones Web', '2306', 'Teórica y Práctica', '18:00 - 22:00', subject)
		elif subject == 'cvc1':
			timetablepy.reminder('Estrategia vinculación laboral', '2307', 'Pendeja', '10:00 - 11:30', subject)
		elif subject == 'spinning':
			timetablepy.reminder('Ciclismo Indoor', 'CE101', 'Sport', '18:00 - 22:00', subject, False)
		else:
			print('Error en argumentos')
	elif interface == 'timer':
		if subject == 'database':
			timetablepy.timer('Base de Datos Avanzadas', elapsedTime=elapsed_time)
		elif subject == 'etica':
			timetablepy.timer('Sociedad, Desarrollo y Ciudad de México', elapsedTime=elapsed_time)
		elif subject == 'machine':
			timetablepy.timer('Aprendizaje Automático', duration=180, elapsedTime=elapsed_time)
		elif subject == 'model':
			timetablepy.timer('Análisis y modelo de sistemas software', 'Sociedad, Desarrollo y Ciudad de México', elapsedTime=elapsed_time)
		elif subject == 'redes':
			timetablepy.timer('Interconexión de Redes', duration=120, elapsedTime=elapsed_time)
		elif subject == 'web':
			timetablepy.timer('Desarrollo de Aplicaciones Web', duration=240, elapsedTime=elapsed_time)
		elif subject == 'cvc1':
			timetablepy.timer('Estrategia vinculación laboral', elapsedTime=elapsed_time)
		else:
			print('Error en argumentos')
	else:
		print("Error en los argumentos| timer | reminder")
