try:
	import Tkinter
except:
	import tkinter as Tkinter

import math	# Necessário para Cálculo de Coordenadas
import time	# Necessário para manuseio de tempo
#
#
# classe
class main(Tkinter.Tk):
	def __init__(self):
		Tkinter.Tk.__init__(self)
		self.x=150	# Ponto central x
		self.y=150	# Ponto central
		self.length=50	# Comprimento do bastão
		self.creating_all_function_trigger()

	# Criando gatilho para outras funções
	def creating_all_function_trigger(self):
		self.create_canvas_for_shapes()
		self.creating_background_()
		self.creating_sticks()
		return

	# Criando plano de fundo
	def creating_background_(self):
		self.image=Tkinter.PhotoImage(file='clock.gif')
		self.canvas.create_image(150,150, image=self.image)
		return

	# criando Canvas
	def create_canvas_for_shapes(self):
		self.canvas=Tkinter.Canvas(self, bg='black')
		self.canvas.pack(expand='yes',fill='both')
		return

	# Criando Bastões em Movimento
	def creating_sticks(self):
		self.sticks=[]
		for i in range(3):
			store=self.canvas.create_line(self.x, self.y,self.x+self.length,self.y+self.length,width=2, fill='red')
			self.sticks.append(store)
		return

	# Função Precisa de Atualização Regular
	def update_class(self):
		now=time.localtime()
		t = time.strptime (str(now.tm_hour), "%H")
		hour = int(time.strftime( "%I", t ))*5
		now=(hour,now.tm_min,now.tm_sec)
		# Alterando as Coordenadas do Stick
		for n,i in enumerate(now):
			x,y=self.canvas.coords(self.sticks[n])[0:2]
			cr=[x,y]
			cr.append(self.length*math.cos(math.radians(i*6)-math.radians(90))+self.x)
			cr.append(self.length*math.sin(math.radians(i*6)-math.radians(90))+self.y)
			self.canvas.coords(self.sticks[n], tuple(cr))
		return

# Acionador da função principal
if __name__ == '__main__':
	root=main()

	# Criando Loop Principal
	while True:
		root.update()
		root.update_idletasks()
		root.update_class()