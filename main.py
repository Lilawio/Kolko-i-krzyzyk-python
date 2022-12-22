def czy_remis(gra):
  if (gra[0][0]!="" and gra[0][1]!="" and gra[0][2]!="" and gra[1][0]!="" and gra[1][1]!="" and gra[1][2]!="" and gra[2][0]!="" and gra[2][1]!="" and gra[2][2]!=""):
    return True
  else:
    return False

def wpisz(f):
  z=int(input(f))
  if z < 0 or z > 2:
    raise ValueError;
  return z    

def sprawdz(gra,gracz):
  if ((gra[0][0]==gracz and gra[0][1]==gracz and gra[0][2]==gracz)
or (gra[1][0]==gracz and gra[1][1]==gracz and gra[1][2]==gracz)
or (gra[2][0]==gracz and gra[2][1]==gracz and gra[2][2]==gracz)
or (gra[0][0]==gracz and gra[1][0]==gracz and gra[2][0]==gracz)
or (gra[0][1]==gracz and gra[1][1]==gracz and gra[2][1]==gracz)
or (gra[0][2]==gracz and gra[1][2]==gracz and gra[2][2]==gracz)
or (gra[0][0]==gracz and gra[1][1]==gracz and gra[2][2]==gracz)
or (gra[0][2]==gracz and gra[1][1]==gracz and gra[2][0]==gracz)):
    return True
  else:
    return False 

def rysuj(gra1):
  for n in range(len(gra1)):
    print(gra1[n])

def zmien(gracz):
  if (gracz=="x"):
    return "o"
  else:
    return "x"

print("NIE POWTARZAJ TYCH SAMYCH WSPÓŁRZĘDNYCH!")
print("instrukcja do gry: ")
print("")
print("- każde pole ma swój własny kod i są to: ")
gra1 = [["0,0","0,1","0,2"],["1,0","1,1","1,2"],["2,0","2,1","2,2"]]
rysuj(gra1)
print("")
print("Pisz tylko liczby (0,1,2) ")
print("")
print("Zaczyna krzyżyk ")
print("")
print("Gra :")
winner=False
gra = [["","",""],["","",""],["","",""]]
gracz="x"
a=0
b=0
remis=False
rysuj(gra)
while winner==False and remis==False:
  print("wpisz współrzędną")
  try:   
    a=wpisz("współrzedne 1- ")
    b=wpisz("współrzedne 2- ")
  except:   
    print("Podano nieprawidłowy znak (dozwolone: 0, 1, 2)")
  else:
    if gra[a][b]=="":
      gra[a][b]=gracz  
      rysuj(gra)  
      winner=sprawdz(gra, gracz)
      if winner==True: 
        print("wygrał ", gracz)
      else:
        gracz=zmien(gracz)
        remis=czy_remis(gra)
        if remis==True: 
          print("remis")
    else:
      print("To pole jest zajęte")