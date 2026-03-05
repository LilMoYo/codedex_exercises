def dompier_music(switches):
  
  def notedec2(notedec):
    if notedec == 261:
      notedec = "C4"
    elif notedec == 294:
      notedec = "D4"
    elif notedec == 329:
      notedec = "E4"
    elif notedec == 349:
      notedec = "F4"
    elif notedec == 392:
      notedec = "G4"
    elif notedec == 440:
      notedec = "A4"
    elif notedec == 494:
      notedec = "B4"
    elif notedec == 523:
      notedec = "C5"
    elif notedec == 0:
      notedec = "REST"
    else: 
      notedec = "Unknown"
    return notedec

  switch_int = []
  notes = []
  
  for switch in switches:
    switch = int(switch, 2)
    switch_int.append(switch)
    
  for note in switch_int:
    note = notedec2(note)
    notes.append(note)
  
  return notes

switches = ["0100000101", "0100000101", "0110001000", "0110001000", "0110111000", "0110111000", "0110001000", "0000000000"]
switches_check = dompier_music(switches)
print(switches_check)

switches2 = ["0101001001", "0101001001", "0101001001", "0000000000", "0101001001", "0101001001", "0101001001", "0000000000", "0101001001", "0110001000", "0100000101", "0100100110", "0101001001", "0000000000", "0000000000"]
switches_check2 = dompier_music(switches2)
print(switches_check2)

switches3 = ["0100000101", "0000000000", "0100000101", "0100100110", "0000000000", "0100000101", "0000000000", "0101011101", "0000000000", "0101001001", "0000000000", "0000000000"]
switches_check3 = dompier_music(switches3)
print(switches_check3)

### NOT ACCEPTED SOLUTION WITH MATCH CASE ###

  # def notedec(notedec):
  #   match notedec:
  #     case 261:
  #       notedec = "C4"
  #     case 294:
  #       notedec = "D4"
  #     case 329:
  #       notedec = "E4"
  #     case 349:
  #       notedec = "F4"
  #     case 392:
  #       notedec = "G4"
  #     case 440:
  #       notedec = "A4"
  #     case 494:
  #       notedec = "B4"
  #     case 523:
  #       notedec = "C5"
  #     case 0:
  #       notedec = "REST"
  #     case _:
  #       notedec = "Unknown"
  #   return notedec