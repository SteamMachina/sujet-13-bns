def tri_selection(tab):
  id = 0
  for i in range(len(tab)):
    id = i
    for j in range(i, len(tab)):
      if tab[j] < tab[id]:
        id = j
    temp = tab[i]
    tab[i] = tab[id]
    tab[id] = temp
  return tab
