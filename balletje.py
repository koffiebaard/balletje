import pygame

# Begin met Pygame - een spel maken
pygame.init()

# We maken een scherm, om blokjes op te zetten. 500 pixels hoog en 500 pixels breed
scherm = pygame.display.set_mode([500, 500])

# We willen een mooie titel op het scherm
pygame.display.set_caption("Balletje!")

# Kleur van de achtergrond
achtergrond_kleur = "darkolivegreen3"

# Grootte en kleur van de bal
bal_grootte = 30
bal_kleur = "darkolivegreen4"

# We gaan heel vaak de code hieronder herhalen
while True:

  # Opzoeken welke toetsen zijn ingedrukt op het toetsenbord
  toetsen = pygame.key.get_pressed()

  # De pijl omhoog toets maakt de bal groter
  if toetsen[pygame.K_UP]:
    bal_grootte += 0.1

  # De pijl omlaag toets maakt de bal kleiner
  if toetsen[pygame.K_DOWN]:
    bal_grootte -= 0.1

  # Achtergrond kleur voor het scherm
  scherm.fill(pygame.Color(achtergrond_kleur))

  # Teken een bal op het scherm
  pygame.draw.circle(scherm, pygame.Color(bal_kleur), (250, 250), bal_grootte)

  # Alle veranderingen hierboven worden getoond
  pygame.display.flip()

  # Als het scherm gesloten wordt, moeten we hier alles netjes afsluiten
  for gebeurtenis in pygame.event.get():
    if gebeurtenis.type == pygame.QUIT:
      pygame.quit()
