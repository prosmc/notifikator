 # -*- coding: utf-8 -*-

class Legend:

    @staticmethod
    def show(release, startup_time):
         legend_text = '''
  ___ ___ ___     ___ _____ _   ___ _  __
 | _ \ __| _ \___/ __|_   _/_\ / __| |/ /
 |   / _||  _/___\__ \ | |/ _ \ (__| ' < 
 |_|_\___|_|     |___/ |_/_/ \_\___|_|\_\\
                                         
 =============================================
 Notifikator v{release} - {startup_time}
 =============================================
    '''.format(release=release, startup_time=startup_time)
         print(legend_text, flush=True)