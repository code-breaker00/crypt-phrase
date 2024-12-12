import tkinter as tk #line:1
from tkinter import messagebox #line:2
import hashlib #line:3
import base64 #line:4
from cryptography .fernet import Fernet #line:5
historique ={"texte_crypte":"","mot_de_passe":""}#line:8
def mot_de_passe_vers_cle (OO0O0OOOO000O0000 ):#line:11
    O0O000000OO00O00O =b'ToudraLangueSelFixe'#line:12
    O0OOO0O0OOO000O0O =hashlib .pbkdf2_hmac ('sha256',OO0O0OOOO000O0000 .encode (),O0O000000OO00O00O ,100000 )#line:15
    return base64 .urlsafe_b64encode (O0OOO0O0OOO000O0O )#line:16
def crypter_texte (O00O0O0O00OOOOOOO ,OO0O000OO000OO0O0 ):#line:19
    OOOO0O000OOO000O0 =mot_de_passe_vers_cle (OO0O000OO000OO0O0 )#line:20
    O0OOO000OO0OOOOOO =Fernet (OOOO0O000OOO000O0 )#line:21
    O0O0OO0OO0OOO0OOO =O0OOO000OO0OOOOOO .encrypt (O00O0O0O00OOOOOOO .encode ())#line:22
    return O0O0OO0OO0OOO0OOO #line:23
def decrypter_texte (O000OO0O0000O0OO0 ,O0OO0OO0O0OO0O0O0 ):#line:26
    O00000O0000OOO0O0 =mot_de_passe_vers_cle (O0OO0OO0O0OO0O0O0 )#line:27
    O000OO00O0O000000 =Fernet (O00000O0000OOO0O0 )#line:28
    try :#line:29
        return O000OO00O0O000000 .decrypt (O000OO0O0000O0OO0 ).decode ()#line:30
    except :#line:31
        return "Mot de passe incorrect ou texte invalide."#line:32
def afficher_historique ():#line:35
    O00O0O000OO00O0OO =tk .Toplevel (root )#line:36
    O00O0O000OO00O0OO .title ("Historique de cryptage")#line:37
    O00O0O000OO00O0OO .configure (bg ="black")#line:38
    tk .Label (O00O0O000OO00O0OO ,text ="Dernier texte crypté :",bg ="black",fg ="#800080",font =("Helvetica",14 )).pack (pady =5 )#line:40
    O0OO0OO000O0OO000 =tk .Text (O00O0O000OO00O0OO ,height =5 ,width =50 ,bg ="black",fg ="white")#line:41
    O0OO0OO000O0OO000 .insert ("1.0",historique ["texte_crypte"])#line:42
    O0OO0OO000O0OO000 .config (state ="normal")#line:43
    O0OO0OO000O0OO000 .pack (pady =5 )#line:44
    tk .Label (O00O0O000OO00O0OO ,text ="Mot de passe utilisé :",bg ="black",fg ="#00FF00",font =("Helvetica",14 )).pack (pady =5 )#line:46
    O0O0OO0OO0O0O000O =tk .Text (O00O0O000OO00O0OO ,height =2 ,width =50 ,bg ="black",fg ="white")#line:47
    O0O0OO0OO0O0O000O .insert ("1.0",historique ["mot_de_passe"])#line:48
    O0O0OO0OO0O0O000O .config (state ="normal")#line:49
    O0O0OO0OO0O0O000O .pack (pady =5 )#line:50
def interface_crypter ():#line:53
    def O0000O000OOO000O0 ():#line:54
        OOOO0OOOO00000OOO =O0O000OOOOO00O00O .get ("1.0",tk .END ).strip ()#line:55
        OOO0OOO0O00OO0O0O =O0OOOO00O0OOO0OOO .get ()#line:56
        if not OOOO0OOOO00000OOO or not OOO0OOO0O00OO0O0O :#line:58
            messagebox .showerror ("Erreur","Le texte et le mot de passe ne doivent pas être vides.")#line:59
            return #line:60
        OOO0000O00OO000O0 =crypter_texte (OOOO0OOOO00000OOO ,OOO0OOO0O00OO0O0O )#line:62
        historique ["texte_crypte"]=OOO0000O00OO000O0 .decode ()#line:63
        historique ["mot_de_passe"]=OOO0OOO0O00OO0O0O #line:64
        afficher_resultat_cryptage (OOO0000O00OO000O0 ,OOO0OOO0O00OO0O0O )#line:65
    O00O0O00OOO0O00OO =tk .Toplevel (root )#line:67
    O00O0O00OOO0O00OO .title ("Crypter une phrase")#line:68
    O00O0O00OOO0O00OO .configure (bg ="black")#line:69
    tk .Label (O00O0O00OOO0O00OO ,text ="Entrez la phrase à crypter :",bg ="black",fg ="white").pack (pady =5 )#line:71
    O0O000OOOOO00O00O =tk .Text (O00O0O00OOO0O00OO ,height =5 ,width =50 ,bg ="black",fg ="white")#line:72
    O0O000OOOOO00O00O .pack (pady =5 )#line:73
    tk .Label (O00O0O00OOO0O00OO ,text ="Entrez votre mot de passe :",bg ="black",fg ="white").pack (pady =5 )#line:75
    O0OOOO00O0OOO0OOO =tk .Entry (O00O0O00OOO0O00OO ,show ="*",width =50 ,bg ="black",fg ="white")#line:76
    O0OOOO00O0OOO0OOO .pack (pady =5 )#line:77
    tk .Button (O00O0O00OOO0O00OO ,text ="Crypter",command =O0000O000OOO000O0 ,bg ="#800080",fg ="white").pack (pady =10 )#line:79
def afficher_resultat_cryptage (O00O0OO00O00000O0 ,O00OOOO0OOOO0OOO0 ):#line:82
    O0OOO0OOOOO000O00 =tk .Toplevel (root )#line:83
    O0OOO0OOOOO000O00 .title ("Résultat du cryptage")#line:84
    O0OOO0OOOOO000O00 .configure (bg ="black")#line:85
    tk .Label (O0OOO0OOOOO000O00 ,text ="Texte crypté :",font =("Helvetica",14 ),bg ="black",fg ="#800080").pack (pady =5 )#line:93
    O0OOOOO00000000O0 =tk .Text (O0OOO0OOOOO000O00 ,height =5 ,width =50 ,bg ="black",fg ="white")#line:94
    O0OOOOO00000000O0 .insert ("1.0",O00O0OO00O00000O0 .decode ())#line:95
    O0OOOOO00000000O0 .config (state ="normal")#line:96
    O0OOOOO00000000O0 .pack (pady =5 )#line:97
    tk .Label (O0OOO0OOOOO000O00 ,text ="Mot de passe :",font =("Helvetica",14 ),bg ="black",fg ="#00FF00").pack (pady =5 )#line:105
    OO0OO0000O0OOOOOO =tk .Text (O0OOO0OOOOO000O00 ,height =2 ,width =50 ,bg ="black",fg ="white")#line:106
    OO0OO0000O0OOOOOO .insert ("1.0",O00OOOO0OOOO0OOO0 )#line:107
    OO0OO0000O0OOOOOO .config (state ="normal")#line:108
    OO0OO0000O0OOOOOO .pack (pady =5 )#line:109
def interface_decrypter ():#line:112
    def O0OOO00O0OO0O0O00 ():#line:113
        OO000000O0OO0O000 =OOOOOO0O00O00OO0O .get ("1.0",tk .END ).strip ()#line:114
        O000000O0O0OO0O0O =O0O0OOOO0OO0O0OOO .get ()#line:115
        if not OO000000O0OO0O000 or not O000000O0O0OO0O0O :#line:117
            messagebox .showerror ("Erreur","Le texte crypté et le mot de passe ne doivent pas être vides.")#line:118
            return #line:119
        OOO0O00OOOO00O0O0 =decrypter_texte (OO000000O0OO0O000 .encode (),O000000O0O0OO0O0O )#line:121
        O0O00O0O000000O0O =tk .Toplevel (root )#line:123
        O0O00O0O000000O0O .title ("Résultat du décryptage")#line:124
        O0O00O0O000000O0O .configure (bg ="black")#line:125
        tk .Label (O0O00O0O000000O0O ,text ="Texte décrypté :",font =("Helvetica",14 ),bg ="black",fg ="#00FF00").pack (pady =5 )#line:133
        OOOO0O0OO00O0000O =tk .Text (O0O00O0O000000O0O ,height =5 ,width =50 ,bg ="black",fg ="white")#line:134
        OOOO0O0OO00O0000O .insert ("1.0",OOO0O00OOOO00O0O0 )#line:135
        OOOO0O0OO00O0000O .config (state ="normal")#line:136
        OOOO0O0OO00O0000O .pack (pady =5 )#line:137
    O00O00O0OOO00000O =tk .Toplevel (root )#line:139
    O00O00O0OOO00000O .title ("Décrypter une phrase")#line:140
    O00O00O0OOO00000O .configure (bg ="black")#line:141
    tk .Label (O00O00O0OOO00000O ,text ="Entrez le texte crypté :",bg ="black",fg ="white").pack (pady =5 )#line:143
    OOOOOO0O00O00OO0O =tk .Text (O00O00O0OOO00000O ,height =5 ,width =50 ,bg ="black",fg ="white")#line:144
    OOOOOO0O00O00OO0O .pack (pady =5 )#line:145
    tk .Label (O00O00O0OOO00000O ,text ="Entrez votre mot de passe :",bg ="black",fg ="white").pack (pady =5 )#line:147
    O0O0OOOO0OO0O0OOO =tk .Entry (O00O00O0OOO00000O ,show ="*",width =50 ,bg ="black",fg ="white")#line:148
    O0O0OOOO0OO0O0OOO .pack (pady =5 )#line:149
    tk .Button (O00O00O0OOO00000O ,text ="Décrypter",command =O0OOO00O0OO0O0O00 ,bg ="#00FF00",fg ="black").pack (pady =10 )#line:151
root =tk .Tk ()#line:154
root .title ("Langue de Toudra")#line:155
root .geometry ("400x400")#line:156
root .configure (bg ="black")#line:157
tk .Label (root ,text ="Langue de Toudra",font =("Helvetica",20 ),bg ="black",fg ="white").pack (pady =10 )#line:160
tk .Button (root ,text ="Crypter une phrase",fg ="#800080",bg ="black",font =("Helvetica",14 ),cursor ="hand2",command =interface_crypter ).pack (pady =10 )#line:164
tk .Button (root ,text ="Décrypter une phrase",fg ="#00FF00",bg ="black",font =("Helvetica",14 ),cursor ="hand2",command =interface_decrypter ).pack (pady =10 )#line:166
tk .Button (root ,text ="Historique de cryptage",fg ="white",bg ="black",font =("Helvetica",14 ),cursor ="hand2",command =afficher_historique ).pack (pady =10 )#line:168
tk .Button (root ,text ="Quitter",fg ="white",bg ="black",font =("Helvetica",14 ),cursor ="hand2",command =root .quit ).pack (pady =10 )#line:169
root .mainloop ()#line:171