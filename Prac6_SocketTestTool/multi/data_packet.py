import socket

def send_data(ip_addr, port, modem, type, mppt, err, com, count):
  type_status = {"단상":"01", "3상":"02"}
  com_status = {"정상":"00", "통신 실패":"39"}
  station_num = f"{count:02}"
  data = ""

  # 데이터 타입 선정
  print(f"{modem} {type} {mppt} {err} {com}")

  pre_set_lora = f"1401{type_status[type]}{station_num}{com_status[com]}"
  pre_set_lte = f"01xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx{station_num}1401{type_status[type]}{station_num}{com_status[com]}"
  end_set = f"xxxxxxxxxxxxxxxx00{err}"

  if modem=="Lora" and type=="단상" and mppt=="미포함" :
    data = pre_set_lora + f"aaaabbbbccccddddeeeeffff03e80258" + end_set
  elif modem=="Lora" and type=="단상" and mppt=="포함" :
    data = pre_set_lora + f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccddddeeeeffff03ef0258" + end_set
  elif modem=="Lora" and type=="3상" and mppt=="미포함" :
    data = pre_set_lora + f"aaaabbbbccccccccddddeeeeffffgggghhhhiiiijjjjjjjj03ef0258"+ end_set
  elif modem=="Lora" and type=="3상" and mppt=="포함" :
    data = pre_set_lora + f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccddddeeeeffffgggghhhhiiiijjjjjjjj03ef0258" + end_set
  elif modem=="LTE" and type=="단상" and mppt=="미포함" :
    data = pre_set_lte + f"aaaabbbbccccddddeeeeffff03e80258" + end_set
  elif modem=="LTE" and type=="단상" and mppt=="포함" :
    data = pre_set_lte + f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccddddeeeeffff03ef0258" + end_set
  elif modem=="LTE" and type=="3상" and mppt=="미포함" :
    data = pre_set_lte + f"aaaabbbbccccccccddddeeeeffffgggghhhhiiiijjjjjjjj03ef0258"+ end_set
  elif modem=="LTE" and type=="3상" and mppt=="포함" :
    data = pre_set_lte + f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccddddeeeeffffgggghhhhiiiijjjjjjjj03ef0258" + end_set
  else :
    pass

  # 소켓 통신
  try :
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((ip_addr, int(port)))
    print("서버와 연결되었습니다.")

    try :
      client_socket.send(data.encode())
      print(data, len(data))
      # print(station_num)
      print("데이터가 정상적으로 전송되었습니다.")
    except :
      print("데이터 전송에 실패했습니다.")

    client_socket.close()

  except ConnectionRefusedError :
    print("서버와 연결할 수 없습니다.")
