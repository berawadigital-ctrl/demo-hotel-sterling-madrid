# Contenido de la demo Hotel Sterling (Madrid) (es/ca/en/fr). Hechos de hotelsterlingmadrid.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble con vistas y terraza privada','Triple con vistas','Cuádruple con vistas y terraza privada'],'ca':['Doble amb vistes i terrassa privada','Triple amb vistes','Quàdruple amb vistes i terrassa privada'],'en':['Double with views and private terrace','Triple with views','Quadruple with views and private terrace'],'fr':['Double avec vue et terrasse privée','Triple avec vue','Quadruple avec vue et terrasse privée']}
RD={
'es':['Para dos personas, amplia, con vistas y terraza privada; 21m².','Para un máximo de 3 personas con excelentes vistas; 18 m².','Para un máximo de 4 personas, con vistas y terraza privada; 22 m².'],
'ca':['Per a dues persones, àmplia, amb vistes i terrassa privada; 21m².','Per a un màxim de 3 persones amb vistes excel·lents; 18 m².','Per a un màxim de 4 persones, amb vistes i terrassa privada; 22 m².'],
'en':['For two guests, spacious, with views and a private terrace; 21m².','For up to 3 guests with excellent views; 18 m².','For up to 4 guests, with views and a private terrace; 22 m².'],
'fr':['Pour deux personnes, spacieuse, avec vue et terrasse privée ; 21m².','Pour 3 personnes maximum avec une vue excellente ; 18 m².','Pour 4 personnes maximum, avec vue et terrasse privée ; 22 m².']}
ART={
'hero':('skyline',3001,['#3a2440','#e0905f','#f7d39c','#39233f','#2a1a2f','#1b111f']),
'intro':('columns',3002,['#f1e6ec','#f7eef2','#b8893e','#5a2a4a','#33172a']),
'r1':('skyline',3011,['#2f3c5e','#e48a5f','#f9d19b','#2e3b5c','#212c46','#151d30']),
'r2':('arches',3012,['#f0e5eb','#d9b2c4','#a46a86','#5a2a4a','#33172a']),
'r3':('skyline',3013,['#44324a','#e8935f','#fbd9a0','#433149','#33253a','#221827']),
'g1':('arches',3021,['#f0e4ea','#d6aec1','#a26884','#5a2a4a','#33172a']),
'g2':('columns',3022,['#efe4ea','#f6edf1','#c08c40','#5e2d4e','#35182c']),
'g3':('skyline',3023,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f']),
'g4':('hills',3024,['#e6e6d1','#f3e5c3','#f6cf8a','#a9c19e','#80a085','#587767']),
'g5':('arches',3025,['#efe3e9','#d4abbe','#a06682','#5a2a4a','#33172a']),
'g6':('columns',3026,['#eee3e9','#f5ecf0','#bb8c42','#5a2a4a','#33172a'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Sterling · Hotel junto a la Gran Vía de Madrid, en la calle San Bernardo',see_rooms='Ver habitaciones',hero_k='Madrid · Gran Vía',hero_t='Siente la magia de una gran ciudad',hero_s='En la calle San Bernardo, una de las conexiones de la Gran Vía; algunas habitaciones tienen terraza con vistas.',
 intro_t='Un hotel a dos pasos del metro',intro_p1='El Hotel Sterling está en San Bernardo, 29 y 31, junto a la Gran Vía, conocida como el Broadway de Madrid por sus teatros y cines.',
 intro_p2='Tiene habitaciones dobles, triples y cuádruples, varias con terraza privada; desayuno bufet cada mañana, recepción 24 horas e instalaciones adaptadas. Admite mascotas pequeñas.',
 stats=['Junto a la Gran Vía','Terrazas con vistas','Recepción 24 horas','Mascotas pequeñas'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de los tipos de habitación del hotel.',
 svcs=['Desayuno bufet','Recepción 24 horas','Wifi en el hotel','Aire acondicionado','Consigna de equipajes','Accesos adaptados','Aparcamiento anexo con reserva','Servicio de niñera bajo petición'],
 loc_p='San Bernardo, 29 y 31 · 28015 Madrid, en una de las conexiones de la Gran Vía y a dos pasos de varias estaciones de metro.',
 chips=['¿Qué habitaciones tiene?','¿Hay parking?','¿Admiten mascotas?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Sterling · Hotel al costat de la Gran Vía de Madrid, al carrer San Bernardo',see_rooms='Veure habitacions',hero_k='Madrid · Gran Vía',hero_t='Sent la màgia d\'una gran ciutat',hero_s='Al carrer San Bernardo, una de les connexions de la Gran Vía; algunes habitacions tenen terrassa amb vistes.',
 intro_t='Un hotel a dos passos del metro',intro_p1='L\'Hotel Sterling és a San Bernardo, 29 i 31, al costat de la Gran Vía, coneguda com el Broadway de Madrid pels seus teatres i cinemes.',
 intro_p2='Té habitacions dobles, triples i quàdruples, diverses amb terrassa privada; esmorzar bufet cada matí, recepció 24 hores i instal·lacions adaptades. Admet mascotes petites.',
 stats=['Al costat de la Gran Vía','Terrasses amb vistes','Recepció 24 hores','Mascotes petites'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres dels tipus d\'habitació de l\'hotel.',
 svcs=['Esmorzar bufet','Recepció 24 hores','Wifi a l\'hotel','Aire condicionat','Consigna d\'equipatges','Accessos adaptats','Aparcament annex amb reserva','Servei de mainadera a petició'],
 loc_p='San Bernardo, 29 i 31 · 28015 Madrid, en una de les connexions de la Gran Vía i a dos passos de diverses estacions de metro.',
 chips=['Quines habitacions té?','Hi ha pàrquing?','Admeteu mascotes?','Com es reserva?']),
'en':dict(title='Hotel Sterling · Hotel next to Madrid\'s Gran Vía, on Calle San Bernardo',see_rooms='See the rooms',hero_k='Madrid · Gran Vía',hero_t='Feel the magic of a great city',hero_s='On Calle San Bernardo, one of the Gran Vía\'s connecting streets; some rooms have a terrace with views.',
 intro_t='A hotel steps from the metro',intro_p1='Hotel Sterling is at San Bernardo, 29 and 31, next to the Gran Vía, known as Madrid\'s Broadway for its theatres and cinemas.',
 intro_p2='It has double, triple and quadruple rooms, several with a private terrace; a buffet breakfast every morning, 24-hour reception and adapted facilities. Small pets are welcome.',
 stats=['Next to the Gran Vía','Terraces with views','24-hour reception','Small pets'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the hotel\'s room types.',
 svcs=['Buffet breakfast','24-hour reception','Wifi in the hotel','Air conditioning','Luggage storage','Adapted access','Adjoining car park with booking','Babysitting on request'],
 loc_p='San Bernardo, 29 and 31 · 28015 Madrid, on one of the Gran Vía\'s connecting streets and steps from several metro stations.',
 chips=['What rooms does it have?','Is there parking?','Are pets allowed?','How do I book?']),
'fr':dict(title='Hotel Sterling · Hôtel près de la Gran Vía de Madrid, calle San Bernardo',see_rooms='Voir les chambres',hero_k='Madrid · Gran Vía',hero_t='Ressentez la magie d\'une grande ville',hero_s='Calle San Bernardo, l\'une des rues qui relient la Gran Vía ; certaines chambres ont une terrasse avec vue.',
 intro_t='Un hôtel à deux pas du métro',intro_p1='L\'Hotel Sterling se trouve San Bernardo, 29 et 31, près de la Gran Vía, surnommée le Broadway de Madrid pour ses théâtres et cinémas.',
 intro_p2='Il propose des chambres doubles, triples et quadruples, plusieurs avec terrasse privée ; petit-déjeuner buffet chaque matin, réception 24 heures et installations adaptées. Les petits animaux sont acceptés.',
 stats=['Près de la Gran Vía','Terrasses avec vue','Réception 24 heures','Petits animaux'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des types de chambre de l\'hôtel.',
 svcs=['Petit-déjeuner buffet','Réception 24 heures','Wifi dans l\'hôtel','Climatisation','Consigne à bagages','Accès adaptés','Parking attenant sur réservation','Baby-sitting sur demande'],
 loc_p='San Bernardo, 29 et 31 · 28015 Madrid, dans l\'une des rues reliant la Gran Vía et à deux pas de plusieurs stations de métro.',
 chips=['Quelles chambres a-t-il ?','Y a-t-il un parking ?','Les animaux sont-ils admis ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://www.hotelsterlingmadrid.com/reservar'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':RES,'fr':RES})
D=dict(name='Hotel Sterling',ac='#5a2a4a',ac2='#b8893e',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address='San Bernardo, 29 y 31 · 28015 Madrid',phones=['+34 91 5420400'],emails=['reservas@hotelsterlingmadrid.com'],maps='Hotel Sterling, Calle de San Bernardo 29, Madrid',t=T)
META=dict(repo='demo-hotel-sterling-madrid',name='Hotel Sterling',legal_name='Hoteles Gestión Madrid S.L. (HOTELES GESTIÓN MADRID - HOTEL STERLING)',registry_ids=['CIF B-85557585'],
 url='https://www.hotelsterlingmadrid.com/',domain='hotelsterlingmadrid.com',municipality='Madrid',province='Madrid',sector='hotel junto a la Gran Vía',
 read_at='2026-10-29T07:55:00+01:00',created_at='2026-10-29T08:05:00+01:00',built_at='2026-10-29T08:05:00+01:00',audit_date='2026-10-29T07:44:00+01:00',
 rating=dict(value=4.2,coincide=['telefono','web'],date='2026-10-29T06:51:44+01:00',url='https://www.google.com/maps/place/Hotel+Sterling+Madrid+%7C+Hotel+3+estrellas+en+Madrid/@40.4230619,-3.7076458,17z/data=!3m1!5s0xd42286354886d4d:0x26b68735de0854d5!4m9!3m8!1s0xd42286353a0f2d5:0x195ac8405c87afc0!5m2!4m1!1i2!8m2!3d40.4230619!4d-3.7076458!16s%2Fg%2F1tdvr102'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van a la pagina Reservar del propio hotel (hotelsterlingmadrid.com/reservar, motor de su web); la demo no construye ningun motor. El telefono +34 91 5420400 figura en el HTML de su portada (no en el texto visible) y coincide con su ficha de Google Maps; el chat solo da el correo del aviso legal.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Qué equipamiento tienen las habitaciones?','K02'),('¿Hay desayuno?','K03'),('¿Hay parking?','K04'),('¿Es accesible para silla de ruedas?','K05'),('¿Admiten mascotas?','K06'),('¿Dónde está el hotel?','K07'),('¿Qué ver cerca?','K08'),('¿Qué ventajas tiene reservar en la web?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el correo?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Tienen gimnasio?',None),('¿Hay piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Quin equipament tenen les habitacions?','K02'),('Hi ha esmorzar?','K03'),('Hi ha pàrquing?','K04'),('És accessible amb cadira de rodes?','K05'),('Admeteu mascotes?','K06'),('On és l\'hotel?','K07'),('Què es pot veure a prop?','K08'),('Quins avantatges té reservar al web?','K09'),('Com reservo?','K10'),('Quin és el correu?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Teniu gimnàs?',None),('Hi ha piscina?',None)],
'en':[('What rooms does it have?','K01'),('What equipment do the rooms have?','K02'),('Is there breakfast?','K03'),('Is there parking?','K04'),('Is it wheelchair accessible?','K05'),('Are pets allowed?','K06'),('Where is the hotel?','K07'),('What is there to see nearby?','K08'),('What are the advantages of booking on the website?','K09'),('How do I book?','K10'),('What is the email?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Do you have a gym?',None),('Is there a swimming pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Quel équipement ont les chambres ?','K02'),('Y a-t-il un petit-déjeuner ?','K03'),('Y a-t-il un parking ?','K04'),('Est-il accessible en fauteuil roulant ?','K05'),('Les animaux sont-ils admis ?','K06'),('Où est l\'hôtel ?','K07'),('Que voir à proximité ?','K08'),('Quels avantages à réserver sur le site ?','K09'),('Comment réserver ?','K10'),('Quel est l\'e-mail ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Avez-vous une salle de sport ?',None),('Y a-t-il une piscine ?',None)]}
