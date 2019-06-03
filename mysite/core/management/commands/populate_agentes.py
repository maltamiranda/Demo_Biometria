from django.core.management.base import BaseCommand
from mysite.core.models import Audio, Agente, Campaña
import os
from datetime import datetime
from mysite.core.transcriptor import Transcriptor
from mysite.core.ponderacion import Evaluador

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'
	#path = 'M:\FreeLance\18-05\static\media\audios\files'
	path = 'M:\\FreeLance\\18-05\\static\\media\\audios\\files'
	cantidad = ''
	
	
	def _cargarAgentes(self):
		Agente.objects.create(nombre="Lopez Cruz Jenny")
		Agente.objects.create(nombre="Gimenez Florencia")
		Agente.objects.create(nombre="Infantino Lucia")
		Agente.objects.create(nombre="Lellamo Alan")
		Agente.objects.create(nombre="Bazan Alicia Mabel")
		Agente.objects.create(nombre="Martinez Analia Soledad")
		Agente.objects.create(nombre="Varela Ayrton")
		Agente.objects.create(nombre="Juárez Eliana Carolina")
		Agente.objects.create(nombre="Nelstadt Ezequiel")
		Agente.objects.create(nombre="Alvarado Barbara Micaela")
		Agente.objects.create(nombre="Napoli Cynthia Rita")
		Agente.objects.create(nombre="Bujons Paula Soledad")
		Agente.objects.create(nombre="Rodriguez Eugenia")
		Agente.objects.create(nombre="Gonzalez De Azcuenaga Mateo")
		Agente.objects.create(nombre="Grecco Rocío Belen")
		Agente.objects.create(nombre="Ochoa Maria Fernanda")
		Agente.objects.create(nombre="Hidalgo Pasco Luis Giancarlo")
		Agente.objects.create(nombre="Albornoz Johana")
		Agente.objects.create(nombre="Tintilay Evelyn")
		Agente.objects.create(nombre="Soria Luciano")
		Agente.objects.create(nombre="Tabarez Maria Belen")
		Agente.objects.create(nombre="Zygadlo Gabriela Noemí")
		Agente.objects.create(nombre="Aguilar Erica")
		Agente.objects.create(nombre="Duarte Camila Ariadna")
		Agente.objects.create(nombre="Akike Juan Ignacio")
		Agente.objects.create(nombre="Villarruel María Luz")
		Agente.objects.create(nombre="Pensa Gaston")
		Agente.objects.create(nombre="De Monte Brenda")
		Agente.objects.create(nombre="Prado Mati Guido Gonzalo")
		Agente.objects.create(nombre="Czertok Nair")
		Agente.objects.create(nombre="Riquelme Carla")
		Agente.objects.create(nombre="Hilgemberg Jimena")
		Agente.objects.create(nombre="Sanmarco Jonatan Pablo Ivan")
		Agente.objects.create(nombre="Regla Rodriguez Alberto Basilio")
		Agente.objects.create(nombre="Rolon Viviana Laura")
		Agente.objects.create(nombre="Giarmana Giuliana Belen")
		Agente.objects.create(nombre="Vazquez Ana Ruth")
		Agente.objects.create(nombre="Simonetti Carolina")
		Agente.objects.create(nombre="Danchuk Cynthia Ayelen")
		Agente.objects.create(nombre="Caputo Estefania")
		Agente.objects.create(nombre="Rechou Sol Agustina")
		Agente.objects.create(nombre="Muñoz Carina")
		Agente.objects.create(nombre="Cordoba Carina")
		Agente.objects.create(nombre="Foradoni Fernanda")
		Agente.objects.create(nombre="Birarelli Carolina Anahi")
		Agente.objects.create(nombre="Pergola Camila Graciela Edith")
		Agente.objects.create(nombre="Gaetani Nancy Roxana")
		Agente.objects.create(nombre="Quiñonez Maximiliano")
		Agente.objects.create(nombre="Montero Paula Viviana")
		Agente.objects.create(nombre="Sires Florencia Natalia")
		Agente.objects.create(nombre="Cespedes Priscila Daiana")
		Agente.objects.create(nombre="Fernandez Rocio")
		Agente.objects.create(nombre="Nievas Olga Patricia")
		Agente.objects.create(nombre="Benvenuto Agustin")
		Agente.objects.create(nombre="Holmquist Maximiliano")
		Agente.objects.create(nombre="Morales Romina Carol")
		Agente.objects.create(nombre="Yañez Alfonsina Laura")
		Agente.objects.create(nombre="Vazquez Daniela")
		Agente.objects.create(nombre="Ferrari Patricia Liliana")
		Agente.objects.create(nombre="Broto Berenice")
		Agente.objects.create(nombre="Merino Maria Paula")
		Agente.objects.create(nombre="De Lisio Elida Noemi")
		Agente.objects.create(nombre="Cuadrio Bisso Camila Maribel")
		Agente.objects.create(nombre="Diaz Yanina Marianela")
		Agente.objects.create(nombre="Avila Nancy")
		Agente.objects.create(nombre="Cubilla Elizabeth Victoria")
		Agente.objects.create(nombre="Carmona Alexis Andres")
		Agente.objects.create(nombre="Chavez Ayelen Marisol")
		Agente.objects.create(nombre="Ruzak Valdes Yasmin")
		Agente.objects.create(nombre="Gallardo Tamara Cristina")
		Agente.objects.create(nombre="Veliz Paladino Brenda")
		Agente.objects.create(nombre="Urbina Jesica Andrea")
		Agente.objects.create(nombre="Ianello Pablo")
		Agente.objects.create(nombre="Teniente Yasmin Carolina")
		Agente.objects.create(nombre="Acevedo Nazarena Soledad")
		Agente.objects.create(nombre="Puente Paula")
		Agente.objects.create(nombre="Carloni Laura Victoria")
		Agente.objects.create(nombre="Ribes Contrera Camila")
		Agente.objects.create(nombre="Cocha Micaela")
		Agente.objects.create(nombre="Escudero Maria Jose")
		Agente.objects.create(nombre="Quiroz Fuentes Stephanie Flavia")
		Agente.objects.create(nombre="Garcia Lidia Teresa")
		Agente.objects.create(nombre="Hughetti Aixa Sofia")
		Agente.objects.create(nombre="Skurnik Sofia Antonella")
		Agente.objects.create(nombre="Olveira Tobias")
		Agente.objects.create(nombre="Balboa Marisa Fanny")
		Agente.objects.create(nombre="Pagliara Sabrina")
		Agente.objects.create(nombre="Lujan Noelia")
		Agente.objects.create(nombre="Torrese Mariela Alejandra")
		Agente.objects.create(nombre="Lopez Delfina")
		Agente.objects.create(nombre="Nachajon Cinthia")
		Agente.objects.create(nombre="Bogado Karen Luciana")
		Agente.objects.create(nombre="Mercchenco Gisela")
		Agente.objects.create(nombre="De Felice Daniela")
		Agente.objects.create(nombre="Villafañe Lourdes Mariana")
		Agente.objects.create(nombre="Larrauri Maria Beatriz")
		Agente.objects.create(nombre="Suarez Lucila Sol")
		Agente.objects.create(nombre="Maldonado Milagros")
		Agente.objects.create(nombre="Caruso Candela Viviana")
		Agente.objects.create(nombre="Bernard Ezequiel")
		Agente.objects.create(nombre="Santillan Yesica")
		Agente.objects.create(nombre="Gulla Valeria")
		Agente.objects.create(nombre="Fava Lucas")
		Agente.objects.create(nombre="Manson Virginia")
		Agente.objects.create(nombre="Rodriguez Rocío Belén")
		Agente.objects.create(nombre="Fabrizi Maria Victoria")
		Agente.objects.create(nombre="Fernandez Julieta Alejandra")
		Agente.objects.create(nombre="Gonzalez Noelia")
		Agente.objects.create(nombre="Turri Valeria")
		Agente.objects.create(nombre="Rinaldi Laura")
		Agente.objects.create(nombre="Vazquez Micaela Mariel")
		Agente.objects.create(nombre="Daza Daniela Gimena")
		Agente.objects.create(nombre="Acuña Alicia Elizabeth")
		Agente.objects.create(nombre="Cortes Torres Laura Patricia")
		Agente.objects.create(nombre="Stella Cecilia")
		Agente.objects.create(nombre="Ramirez Menguez Franco Agustin")
		Agente.objects.create(nombre="Fuentecilla Marcia")
		Agente.objects.create(nombre="Verdes Andrea Veronica")
		Agente.objects.create(nombre="Benitez Jonatan")
		Agente.objects.create(nombre="Arriola Maria Jose")
		Agente.objects.create(nombre="Ceriani Gisela")
		Agente.objects.create(nombre="Bruno Nadia Gisele")
		Agente.objects.create(nombre="Barja Melany Soledad")
		Agente.objects.create(nombre="Manno Gabriela Fernanda")
		Agente.objects.create(nombre="Nocera Antonella Magali")
		Agente.objects.create(nombre="Gaiarin  Priscila Melanie")
		Agente.objects.create(nombre="Palacios Gimena Elizabeth")
		Agente.objects.create(nombre="Franchina Mayra Eliana")
		Agente.objects.create(nombre="Diaz Florencia Anahi")
		Agente.objects.create(nombre="Sosa Metel Nadia Yemina")
		Agente.objects.create(nombre="Cella Jesica Eliana")
		Agente.objects.create(nombre="Bisio Florencia")
		Agente.objects.create(nombre="La Delfa Camila Victoria")
		Agente.objects.create(nombre="Racciati Gisela")
		Agente.objects.create(nombre="Garcia Romina Carla")
		Agente.objects.create(nombre="Barletta Sebastían")
		Agente.objects.create(nombre="Landriel Yesica Daiana")
		Agente.objects.create(nombre="Villalba Jesica Mabel")
		Agente.objects.create(nombre="Linzing Julieta")
		Agente.objects.create(nombre="Barran Camila Maria")
		Agente.objects.create(nombre="Ovejero Denise")
		Agente.objects.create(nombre="Fernandez Karina Paola")
		Agente.objects.create(nombre="Espinoza Jessica Milagros")
		Agente.objects.create(nombre="Molina Yanina")
		Agente.objects.create(nombre="Piñero Cueto Maria del Carmen")
		Agente.objects.create(nombre="Frassi Maria Florencia")
		Agente.objects.create(nombre="De La Cruz Monasterio Rita Paola")
		Agente.objects.create(nombre="Serra Maria Sol")
		Agente.objects.create(nombre="Ciuffo Cristian")
		Agente.objects.create(nombre="Carbajal Rosana")
		Agente.objects.create(nombre="Cerrudo Carmen Soledad")
		Agente.objects.create(nombre="Lopez Oriana Giselle")
		Agente.objects.create(nombre="Ramirez Florencia")
		Agente.objects.create(nombre="Agüero Andrea Verónica")
		Agente.objects.create(nombre="Benetti Romina Soledad")
		Agente.objects.create(nombre="Morales Pajaro Lucia del Carmen")
		Agente.objects.create(nombre="Pennacchio Florencia Luz")
		Agente.objects.create(nombre="Suarez Luciana Sabrina")
		Agente.objects.create(nombre="Guzman Jimenez Gimena Edith")
		Agente.objects.create(nombre="Teran Rocio Salome")
		Agente.objects.create(nombre="Ybarra Laura")
		Agente.objects.create(nombre="Ricalde Brenda Luciana")
		Agente.objects.create(nombre="Anta Maria Belen")
		Agente.objects.create(nombre="Carnero Gabriela Lorena")
		Agente.objects.create(nombre="Manrrique Cristian")
		Agente.objects.create(nombre="Discrecsenso Daniela")
		Agente.objects.create(nombre="Russo Maria Soledad")
		Agente.objects.create(nombre="Gonzalez Florencia")
		Agente.objects.create(nombre="Basanisi Rodrigo")
		Agente.objects.create(nombre="Amore Mariela")
		Agente.objects.create(nombre="Ramirez Javier Hernan")
		Agente.objects.create(nombre="Lopez Andrea Celeste")
		Agente.objects.create(nombre="Francisco Maria Florencia")
		Agente.objects.create(nombre="Herrera María Jesús")
		Agente.objects.create(nombre="Cambaceres Mariana")
		Agente.objects.create(nombre="Pardini Camila")
		Agente.objects.create(nombre="Ocampo Ezequiel Francisco")
		Agente.objects.create(nombre="Javier Veronica Belen")
		Agente.objects.create(nombre="Mogro Natalia Cristina")
		Agente.objects.create(nombre="Troncelliti Dana")
		Agente.objects.create(nombre="Rey Marlene")
		Agente.objects.create(nombre="Martinez Juan Sebastian")
		Agente.objects.create(nombre="De Bartolis Agostina")
		Agente.objects.create(nombre="Zambrano Erika Estefanía")
		Agente.objects.create(nombre="Andrade Elsa Fabiana")
		Agente.objects.create(nombre="Iñiguez Samanta")
		Agente.objects.create(nombre="Mercante Paola")
		Agente.objects.create(nombre="Garro Giselle")
		Agente.objects.create(nombre="Lopez Yamila")
		Agente.objects.create(nombre="Vidal Sanchez Belén Mayra Yanil")
		Agente.objects.create(nombre="Nunes Bispo Paola")
		Agente.objects.create(nombre="Astorga Camila")
		Agente.objects.create(nombre="Solan Nadia Soledad")
		Agente.objects.create(nombre="Gomez Micaela")
		Agente.objects.create(nombre="Sabatino Paola Susana")
		Agente.objects.create(nombre="Mendez Diego Leandro")
		Agente.objects.create(nombre="Aguilar Melina Noel")
		Agente.objects.create(nombre="Cardenas Micaela Marisel")
		Agente.objects.create(nombre="Torres Silvia Lorena")
		Agente.objects.create(nombre="Diaz Erika Judith")
		Agente.objects.create(nombre="Laime Daiana Ximena")
		Agente.objects.create(nombre="Ferraro Cynthia Soledad")
		Agente.objects.create(nombre="Abrahan Cerimeli Romina")
		Agente.objects.create(nombre="Garcia Agustina Belen")
		Agente.objects.create(nombre="Rojas Karen")
		Agente.objects.create(nombre="Sasia Maria Belen")
		Agente.objects.create(nombre="Sersen Pampillon Antonella Belen")
		Agente.objects.create(nombre="Antonuccio Debora Esther")
		Agente.objects.create(nombre="Cejas Nadia Soledad")
		Agente.objects.create(nombre="Borneo Lucas")
		Agente.objects.create(nombre="Recchini Lucas Tadeo")
		Agente.objects.create(nombre="Herrán Rocío Soledad")
		Agente.objects.create(nombre="Sanchez Emmanuel Alejandro")
		Agente.objects.create(nombre="Galan Tamara Gisele")
		Agente.objects.create(nombre="Motta Camila")
		Agente.objects.create(nombre="Tantachelo Alicia")
		Agente.objects.create(nombre="Duarte Alcaraz Liz Patricia")
		Agente.objects.create(nombre="Vargas Lacalle Mayra Anabel")
		Agente.objects.create(nombre="Martinez Olmedo Gloria")
		Agente.objects.create(nombre="Figueredo Noelia Elizabeth")
		Agente.objects.create(nombre="Lanza Lucrecia")
		Agente.objects.create(nombre="Mansilla Maria De Los Angeles")
		Agente.objects.create(nombre="Regos Sabrina Antonella")
		Agente.objects.create(nombre="Martinez Mariño Yesica Denise")
		Agente.objects.create(nombre="Rearte Daniela Soledad")
		Agente.objects.create(nombre="Mora Maria Belen")
		Agente.objects.create(nombre="Rivera Jimena")
		Agente.objects.create(nombre="Bisio Vanesa")
		Agente.objects.create(nombre="Figueroa Tania Elizabeth")
		Agente.objects.create(nombre="Lucero Daiana")
		Agente.objects.create(nombre="Mayochi Stefania")
		Agente.objects.create(nombre="Pronesti Rotondi Elizabhet")
		Agente.objects.create(nombre="Cutuli Lucas Esteban")
		Agente.objects.create(nombre="Romer Jonatan")
		Agente.objects.create(nombre="Guillen Maria Laura")
		Agente.objects.create(nombre="Ojeda Celeste")
		Agente.objects.create(nombre="Liberti Micaela Daira")
		Agente.objects.create(nombre="Godoy Keila")
		Agente.objects.create(nombre="Premiani Jesica")
		Agente.objects.create(nombre="Santa Cruz Silvana Alejandra")
		Agente.objects.create(nombre="Acosta Mariela Melina")
		Agente.objects.create(nombre="Godoy Agustina Ayelén")
		Agente.objects.create(nombre="Garcia Laura Fernanda")
		Agente.objects.create(nombre="Koyaoghlanian Melissa")
		Agente.objects.create(nombre="Pereira Daniela Giselle")
		Agente.objects.create(nombre="Paschetta Mariana")
		Agente.objects.create(nombre="Martinez  Maria Noel")
		Agente.objects.create(nombre="Martinez Carla")
		Agente.objects.create(nombre="Muchelac Delia Susana")
		Agente.objects.create(nombre="Saladino Bianca Carolina")
		Agente.objects.create(nombre="Somoza Gabriela")
		Agente.objects.create(nombre="Devesa Ramirez Camila Anahí")
		Agente.objects.create(nombre="Escartin Samanta")
		Agente.objects.create(nombre="Rivaroli Daniela")
		Agente.objects.create(nombre="Alejo Aylen Alejandra")
		Agente.objects.create(nombre="Gomez Yamila Ayelén")
		Agente.objects.create(nombre="Guarino Tomas")
		Agente.objects.create(nombre="Cruchaga Marcelo")
		Agente.objects.create(nombre="Ortiz Alicia")
		Agente.objects.create(nombre="Landro Claudia Beatriz")
		Agente.objects.create(nombre="Rodriguez Sabrian Gisele")
		Agente.objects.create(nombre="Dalvano Ignacio Rodrigo")
		Agente.objects.create(nombre="Tellechea Candela")
		Agente.objects.create(nombre="Garcia Urga Agustina")
		Agente.objects.create(nombre="Topatigh Veronica Gabriela")
		Agente.objects.create(nombre="Trejo Vanesa Mariel")
		Agente.objects.create(nombre="Tavasci Ana Carolina")
		Agente.objects.create(nombre="Diaz Noelia Celeste")
		Agente.objects.create(nombre="Jauregui Lucero")
		Agente.objects.create(nombre="Chavez Candela")
		Agente.objects.create(nombre="Colombo Ignacio")
		Agente.objects.create(nombre="Bertoli Luciana")
		Agente.objects.create(nombre="Ibarra Camila Soledad")
		Agente.objects.create(nombre="Castillo Ignacio")
		Agente.objects.create(nombre="Cordoba Ana Maria Laura")
		Agente.objects.create(nombre="Rosales Juan Cruz")
		Agente.objects.create(nombre="Devia Lopez Melanie")
		Agente.objects.create(nombre="Silva Nadia Rocio")
		Agente.objects.create(nombre="Talavera Biondi Rocio")
		Agente.objects.create(nombre="Diaz Judith")
		Agente.objects.create(nombre="Mendoza Nadia Daniela")
		Agente.objects.create(nombre="Da Silva Alejandro")
		Agente.objects.create(nombre="Centurion Lilian")
		Agente.objects.create(nombre="Cortopassi María Emilia")
		Agente.objects.create(nombre="Ghelerman Marcelo Ariel")
		Agente.objects.create(nombre="Burgueño Romina")
		Agente.objects.create(nombre="Moroni Milagros")
		Agente.objects.create(nombre="Lemos Cristian Emanuel")
		Agente.objects.create(nombre="Garcilazo Carla")
		Agente.objects.create(nombre="Schiavo Melisa Denisa")
		Agente.objects.create(nombre="Borsani Ignacio Abel")
		Agente.objects.create(nombre="Lopez Milagros Jazmin")
		Agente.objects.create(nombre="Mendez Cardoza Kimberly Desiree")
		Agente.objects.create(nombre="Perez Camila Rocío")
		Agente.objects.create(nombre="Agra Julieta")
		Agente.objects.create(nombre="Benites Carol")
		Agente.objects.create(nombre="Vicente Juan Cruz")
		Agente.objects.create(nombre="Correa Alexis Joel")
		Agente.objects.create(nombre="Nuñez Fernanda Beatriz")
		Agente.objects.create(nombre="Paz Sofia Maria")
		Agente.objects.create(nombre="Carabajal Sofia Belen")
		Agente.objects.create(nombre="Calderon Andrea Celeste")
		Agente.objects.create(nombre="Clementti Ximena")
		Agente.objects.create(nombre="Mastroianni Carlos Alberto")
		Agente.objects.create(nombre="Ruartes Acosta Nair Fernanda")
		Agente.objects.create(nombre="Yachinto Matias Mariano")
		Agente.objects.create(nombre="Martinez Lucia Marcela")
		Agente.objects.create(nombre="Mosquera Araceli")
		Agente.objects.create(nombre="Zerda Ivana")
		Agente.objects.create(nombre="Ramirez Lorena Paola")
		Agente.objects.create(nombre="Cejas Cynthia")
		Agente.objects.create(nombre="Gill Camila Aylen")
		Agente.objects.create(nombre="Allevato Anahi")
		Agente.objects.create(nombre="Cordera Carolina")
		Agente.objects.create(nombre="Dullmon Manuel")
		Agente.objects.create(nombre="Vasquez Sabrina Vanesa")
		Agente.objects.create(nombre="Valzacchi Gaston")
		Agente.objects.create(nombre="Iza Lautaro Bautista")
		Agente.objects.create(nombre="Genolet Alejandra Elisabet")
		Agente.objects.create(nombre="Palacios Saracho Karen Giselle")
		Agente.objects.create(nombre="Medone Cecilia Constanza")
		Agente.objects.create(nombre="Caporalin Victoria")
		Agente.objects.create(nombre="Serrizuela Celia Nancy")
		Agente.objects.create(nombre="Poggio Gisela Delia")
		Agente.objects.create(nombre="Hernando Evelyn")
		Agente.objects.create(nombre="Quiroga Melisa")
		Agente.objects.create(nombre="Ceriani Davina")
		Agente.objects.create(nombre="Rodriguez Angel")
		Agente.objects.create(nombre="Ferreyra Ivana Barbara Noraly")
		Agente.objects.create(nombre="Cruz Maria De Los Angeles")
		Agente.objects.create(nombre="David Ivan Ezequiel")
		Agente.objects.create(nombre="Campero Guzman Dalma Daniela")
		Agente.objects.create(nombre="Martinez Valeria Soledad")
		Agente.objects.create(nombre="Hughes Brian Joel")
		Agente.objects.create(nombre="Topatigh Silvana Paola")
		Agente.objects.create(nombre="Monzon Noelia")
		Agente.objects.create(nombre="Lopez Vazquez Lucia Belen")
		Agente.objects.create(nombre="Ojeda Nadine")
		Agente.objects.create(nombre="Quinteros Brenda Yanina")
		Agente.objects.create(nombre="Aguero Reiter Ana Laura")
		Agente.objects.create(nombre="Yopolo Daiana")
		Agente.objects.create(nombre="Chiesa Carlos Ignacio")
		Agente.objects.create(nombre="Pepolino Evelyn Mariel")
		Agente.objects.create(nombre="Luna Medina Camila")
		Agente.objects.create(nombre="Rodriguez Gisela Marlene")
		Agente.objects.create(nombre="Campo Marianella")
		Agente.objects.create(nombre="Vigna Axel")
		Agente.objects.create(nombre="Verea Micaela Lucia")
		Agente.objects.create(nombre="Allo Macarena")
		Agente.objects.create(nombre="Martins Cardozo Natalia")
		Agente.objects.create(nombre="Valdez Jimena")
		Agente.objects.create(nombre="Garcia Arrieta Daniela")
		Agente.objects.create(nombre="Manassero Cecilia")
		Agente.objects.create(nombre="Lencina Mauro Lucas")
		Agente.objects.create(nombre="Rainer Julian")
		Agente.objects.create(nombre="Quinteros Valeria")
		Agente.objects.create(nombre="Larrosa Maria Pia")
		Agente.objects.create(nombre="Chamot Francisco")
		Agente.objects.create(nombre="Romero Leonor")
		Agente.objects.create(nombre="Reinaga Francisco Javier")
		Agente.objects.create(nombre="Lanzani Lara Belen")
		Agente.objects.create(nombre="Altube Santiago")
		Agente.objects.create(nombre="Verasay Pamela Soledad")
		Agente.objects.create(nombre="Tinte Yañez Sebastian")
		Agente.objects.create(nombre="Lizarraga Rendo Nadia Soledad")
		Agente.objects.create(nombre="Bravo Quisbert Florencia")
		Agente.objects.create(nombre="Rossini Gabriel Adrian")
		Agente.objects.create(nombre="Chumbita Vanina Sandra")
		Agente.objects.create(nombre="Garcia Natalia Eloisa")
		Agente.objects.create(nombre="Godoy Florencia Daniela")
		Agente.objects.create(nombre="Zuidwjik Geraldine Eliana")
		Agente.objects.create(nombre="Falcon Rocco Ana Victoria")
		Agente.objects.create(nombre="Diaz Mauro")
		Agente.objects.create(nombre="Vazquez Barbara Daniela")
		Agente.objects.create(nombre="Daich Sofia Yael")
		Agente.objects.create(nombre="Perez Edgardo")
		Agente.objects.create(nombre="Marcucci Victor Sebastian")
		Agente.objects.create(nombre="Godoy Jimena Stefania")
		Agente.objects.create(nombre="Iribarren Echegaray Jorge Nicolas")
		Agente.objects.create(nombre="Vazquez Vallejo Maribel Antonella")
		Agente.objects.create(nombre="Ferreira Daiana")
		Agente.objects.create(nombre="Renzo Santiago")
		Agente.objects.create(nombre="Rodriguez Nahuel Alejandro")
		Agente.objects.create(nombre="Dalinger Rosana")
		Agente.objects.create(nombre="Granatelli Stephanie")
		Agente.objects.create(nombre="Mulet Maria Noelia")
		Agente.objects.create(nombre="Riego Maria Mercedes")
		Agente.objects.create(nombre="Morales Maria Belen")
		Agente.objects.create(nombre="Pagliaro Maria Ester")
		Agente.objects.create(nombre="Frican Karina")
		Agente.objects.create(nombre="Scalfoni Romina Magali")
		Agente.objects.create(nombre="Fernandez Victor")
		Agente.objects.create(nombre="SteinBach Julieta")
		Agente.objects.create(nombre="Ferreyra Rivero Ezequiel")
		Agente.objects.create(nombre="Laguzzi Castro Sabrina")
		Agente.objects.create(nombre="Roig Greta")
		Agente.objects.create(nombre="Mauna Nicolás")
		Agente.objects.create(nombre="Pellegrino Sofia Giulina")
		Agente.objects.create(nombre="Di Bello Maria Julieta")
		Agente.objects.create(nombre="Di Tomaso Monica")
		Agente.objects.create(nombre="Lopez Carolina Giselle")
		Agente.objects.create(nombre="Olivera Julián Andrés")
		Agente.objects.create(nombre="Maalnica Nicolas")
		Agente.objects.create(nombre="Condori Ibarrra Ayelen")
		Agente.objects.create(nombre="Contrera Giannina")
		Agente.objects.create(nombre="Loureiro Natalia")
		Agente.objects.create(nombre="Rossi Fernanda")
		Agente.objects.create(nombre="Espinosa Natalia Alejandra")
		Agente.objects.create(nombre="Goldberg Irina Ailin")
		Agente.objects.create(nombre="Escobar Eliana Valeria")
		Agente.objects.create(nombre="Mansilla Mariano Nahuel")
		Agente.objects.create(nombre="Lopez Ojeda Maria Belen")
		Agente.objects.create(nombre="Tovar Martinez Mayerlin Rosmari")
		Agente.objects.create(nombre="Leguizamon Maria Pilar")
		Agente.objects.create(nombre="Garcia Andrea Daniela")
		Agente.objects.create(nombre="Mendoza Chahuayla Julio Cesar")
		Agente.objects.create(nombre="Gianni Franco Gabriel")
		Agente.objects.create(nombre="Pittaluga Ezequiel")
		Agente.objects.create(nombre="Aguado Maria Guadalupe")
		Agente.objects.create(nombre="Perez Daniela Celeste")
		Agente.objects.create(nombre="Martinez Aldana")
		Agente.objects.create(nombre="Dalia Florencia")
		Agente.objects.create(nombre="Jackard Maria Belen")
		Agente.objects.create(nombre="Alderete Paula Nicole")
		Agente.objects.create(nombre="Rios Oscar")
		Agente.objects.create(nombre="Sofarelli Gaston")
		Agente.objects.create(nombre="Higa Santiago")
		Agente.objects.create(nombre="Molina Florencia")
		Agente.objects.create(nombre="Viscontin julian")
		Agente.objects.create(nombre="Sandoval Daiana")
		Agente.objects.create(nombre="Corbalan Florencia")
		Agente.objects.create(nombre="Martinez Lucio")
		Agente.objects.create(nombre="Paire Cynthia")
		Agente.objects.create(nombre="Villarreal Claudia romina")
		Agente.objects.create(nombre="Raffaele Micaela")
		Agente.objects.create(nombre="Soto Daiana Solange")
		Agente.objects.create(nombre="Pacheco Jimena")
		Agente.objects.create(nombre="Mon Macarena Luciana")
		Agente.objects.create(nombre="Davila Julian")
		Agente.objects.create(nombre="Ayala Diego")
		Agente.objects.create(nombre="Aroca Carrizo Maria Amanda")
		Agente.objects.create(nombre="Alvarez Ward Guido Nicolas")
		Agente.objects.create(nombre="Cano Barros Agustina Camila")
		Agente.objects.create(nombre="Schonholz Brenda")
		Agente.objects.create(nombre="Cordoba Maximiliano")
		Agente.objects.create(nombre="Beñatena Florencia")
		Agente.objects.create(nombre="Pose Agustin")
		Agente.objects.create(nombre="Negrin Camila")
		Agente.objects.create(nombre="Repetto Andrea")
		Agente.objects.create(nombre="Carbonaro Ignacio Andres")
		Agente.objects.create(nombre="Juarez Natacha")
		Agente.objects.create(nombre="Ramos Evelyn")
		Agente.objects.create(nombre="Mina Evangellina")
		Agente.objects.create(nombre="Garcia Ibarra Adriana")
		Agente.objects.create(nombre="Riquelme Mariana")
		Agente.objects.create(nombre="Sanguinetti Silvina")
		Agente.objects.create(nombre="Feher Marta")

	
	def handle(self, *args, **options):
		self._cargarAgentes()
		