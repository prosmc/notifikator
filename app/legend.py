 # -*- coding: utf-8 -*-

class Legend:

    @staticmethod
    def show(release, startup_time):
         legend_text = '''
  _   _       _   _  __ _ _         _             
 | \ | |     | | (_)/ _(_) |       | |            
 |  \| | ___ | |_ _| |_ _| | ____ _| |_ ___  _ __ 
 | . ` |/ _ \| __| |  _| | |/ / _` | __/ _ \| '__|
 | |\  | (_) | |_| | | | |   < (_| | || (_) | |   
 |_| \_|\___/ \__|_|_| |_|_|\_\__,_|\__\___/|_|   
  
 =================================================
 Release: {release} - {startup_time}
 =================================================
    '''.format(release=release, startup_time=startup_time)
         print(legend_text, flush=True)