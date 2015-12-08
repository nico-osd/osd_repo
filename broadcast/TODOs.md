# TODO - RECEIVE:
x wir brauchen run() Methode
  und register() Methode für Event à la update_list_available
  bei Aktualisierung der Liste: Dispatcher.notify(update_list_available)
x Liste muss sortiert werden(?)
x Keine CSV!
x Bei jedem Refresh wären Master(0/1) und Name weg(?)
x CALLBACKS

LISTE
ID        | Object
192.x.x.Y | -isMaster:Bool    - ME
          | -name:Str         - BC (???)
          | -URI:Str          - BC
          | -time (für keep alive) - BC
192.x.x.Z | -isMaster:Bool
          | -name:Str
          | -URI:Str
          
# TODO - SEND: