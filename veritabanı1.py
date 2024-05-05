import sqlite3
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem


def satirokuyucu(file,satir):

    db=sqlite3.connect(file)
    islemci = db.cursor()
    veri=islemci.execute("SELECT * FROM İNDEX_TABLO ").fetchall()
    return veri[0][satir-1]

def satiryazici(file, satir, veri):
 
    db=sqlite3.connect(file)
    islemci=db.cursor()
    if satir==1:
        islemci.execute("UPDATE İNDEX_TABLO SET P=?",(veri,))
    elif satir==2:
        islemci.execute("UPDATE İNDEX_TABLO SET K=?",(veri,))
    elif satir==3:
        islemci.execute("UPDATE İNDEX_TABLO SET Y=?",(veri,))
    elif satir==4:
        islemci.execute("UPDATE İNDEX_TABLO SET KA=?",(veri,))
    elif satir==5:
        islemci.execute("UPDATE İNDEX_TABLO SET SF=?",(veri,))
    db.commit()


        
        self.sorgu.execute("INSERT INTO PETROL_GEMİSİ (SERİ_NO,GEMİ_AD,GEMİ_AGİRLİK,YAPİM_YİLİ,PETROL_KAPASİTE) VALUES(?,?,?,?,?)",(self.seri_no,gemi_ad,gemi_agirlik,yapim_yil,petrol_kapasite))
        self.veritabanı.commit()
        self.sayac+=1
        satiryazici("veritabani41.db",1,str(self.sayac))

    def veri_sil(self,id):
        self.sorgu.execute("DELETE FROM PETROL_GEMİSİ WHERE SERİ_NO=? ",(id,))
        self.veritabanı.commit()
    def veri_güncelle(self,id,gemi_ad,gemi_agirlik,yapim_yil,petrol_kapasite):
        self.sorgu.execute("UPDATE PETROL_GEMİSİ SET GEMİ_AD=?,GEMİ_AGİRLİK=?,YAPİM_YİLİ=?,PETROL_KAPASİTE=? WHERE SERİ_NO=?",(gemi_ad,gemi_agirlik,yapim_yil,petrol_kapasite,id))
        self.veritabanı.commit()

class KONTEYNER_GEMİSİ(PETROL_GEMİSİ):

    def veri_ekle(self,gemi_ad,gemi_agirlik,yapim_yili,konteyner_sayisi_kapasite,max_agirlik):
        self.sayac=int(satirokuyucu("veritabani41.db",2))
        self.seri_no="K"+str(self.sayac)
        self.sorgu.execute("INSERT INTO KONTEYNER_GEMİSİ (SERİ_NO,GEMİ_AD,GEMİ_AGİRLİK,YAPİM_YİLİ,KONTEYNER_SAYISI_KAPASİTE,MAX_AGİRLİK) VALUES(?,?,?,?,?,?)",(self.seri_no,gemi_ad,gemi_agirlik,yapim_yili,konteyner_sayisi_kapasite,max_agirlik))
        self.veritabanı.commit()
        self.sayac+=1
        satiryazici("veritabani41.db",2,str(self.sayac))

    def veri_sil(self,id):
        self.sorgu.execute("DELETE FROM KONTEYNER_GEMİSİ WHERE SERİ_NO=? ",(id,))
        self.veritabanı.commit()   
    def veri_güncelle(self, id,gemi_ad,gemi_agirlik,yapim_yili,konteyner_sayisi_kapasite,max_agirlik):
        self.sorgu.execute("UPDATE KONTEYNER_GEMİSİ SET GEMİ_AD=?,GEMİ_AGİRLİK=?,YAPİM_YİLİ=?,KONTEYNER_SAYISI_KAPASİTE = ? , MAX_AGİRLİK = ?  WHERE SERİ_NO = ? ",(gemi_ad,gemi_agirlik,yapim_yili,konteyner_sayisi_kapasite,max_agirlik,id))        
        self.veritabanı.commit()     

class YOLCU_GEMİSİ(PETROL_GEMİSİ):

    def veri_ekle(self,gemi_ad,gemi_agirlik,yapim_yil,yolcu_kapasite):
        self.sayac=int(satirokuyucu("veritabani41.db",3))
        self.seri_no="Y"+str(self.sayac)
        self.sorgu.execute(" INSERT INTO YOLCU_GEMİSİ (SERİ_NO,GEMİ_AD,GEMİ_AGİRLİK,YAPİM_YİLİ,YOLCU_KAPASİTE) VALUES(?,?,?,?,?) ",(self.seri_no,gemi_ad,gemi_agirlik,yapim_yil,yolcu_kapasite))
        self.veritabanı.commit()
        self.sayac+=1
        satiryazici("veritabani41.db",3,str(self.sayac))

    def veri_sil(self,id):
        self.sorgu.execute("DELETE FROM YOLCU_GEMİSİ WHERE SERİ_NO = ? ",(id,))
        self.veritabanı.commit()
    def veri_güncelle(self,id,gemi_ad,gemi_agirlik,yapim_yil,yolcu_kapasite):
        self.sorgu.execute("UPDATE YOLCU_GEMİSİ SET  GEMİ_AD=?,GEMİ_AGİRLİK=?,YAPİM_YİLİ=?,YOLCU_KAPASİTE=? WHERE SERİ_NO=?",(gemi_ad,gemi_agirlik,yapim_yil,yolcu_kapasite,id))
        self.veritabanı.commit()

class KAPTAN_M(PETROL_GEMİSİ):
    def veri_ekle(self,kaptan_ad,kaptan_soyad,adres,dogum_tarih,ise_giris_tarih,gorev,lisans):
        self.sayac=int(satirokuyucu("veritabani41.db",4))
        self.seri_no="KA"+str(self.sayac)
        self.sorgu.execute("INSERT INTO KAPTAN_MÜRETTEBAT (KAPTAN_İD,KAPTAN_AD,KAPTAN_SOYAD,ADRES,DOGUM_TARİH,İSE_GİRİS_TARİH,GOREV,KAPTAN_LİSANS) VALUES(?,?,?,?,?,?,?,?)",(self.seri_no,kaptan_ad,kaptan_soyad,adres,dogum_tarih,ise_giris_tarih,gorev,lisans))
        self.veritabanı.commit()
        self.sayac+=1
        satiryazici("veritabani41.db",4,str(self.sayac))
    def veri_sil(self,id):
        self.sorgu.execute("DELETE FROM KAPTAN_MÜRETTEBAT WHERE KAPTAN_İD = ? ",(id,))
        self.veritabanı.commit()
    def veri_güncelle(self,id,kaptan_ad,kaptan_soyad,adres,dogum_tarih,ise_giris_tarih,gorev,lisans):
        self.sorgu.execute("UPDATE KAPTAN_MÜRETTEBAT SET KAPTAN_AD=?,KAPTAN_SOYAD=?,ADRES=?,DOGUM_TARİH=?,İSE_GİRİS_TARİH=?,GOREV=?,KAPTAN_LİSANS=? WHERE KAPTAN_İD=?",(kaptan_ad,kaptan_soyad,adres,dogum_tarih,ise_giris_tarih,gorev,lisans,id))
        self.veritabanı.commit()

class LİMAN_BİLGİ(PETROL_GEMİSİ):
    def veri_ekle(self,liman_ad,ulke_ad,nufus,pasaport_y_n,demirleme_ucret):

        if self.veri_listele()==[]:
            self.sorgu.execute("INSERT INTO LİMAN_BİLGİ (LIMAN_AD,ULKE_AD,NUFUS,PASAPORT_Y_N,DEMİRLEME_UCRET) VALUES(?,?,?,?,?)",(liman_ad,ulke_ad,nufus,pasaport_y_n,demirleme_ucret))
            self.veritabanı.commit()
            return 0
        
        for veri in self.veri_listele():
            if liman_ad==veri[0] and ulke_ad==veri[1]:
                return 0
        
        self.sorgu.execute("INSERT INTO LİMAN_BİLGİ (LIMAN_AD,ULKE_AD,NUFUS,PASAPORT_Y_N,DEMİRLEME_UCRET) VALUES(?,?,?,?,?)",(liman_ad,ulke_ad,nufus,pasaport_y_n,demirleme_ucret))
        self.veritabanı.commit()
        return 1
    def veri_sil(self,liman_ad,ulke_ad):
        self.sorgu.execute("DELETE FROM LİMAN_BİLGİ WHERE LIMAN_AD =? AND ULKE_AD=?",(liman_ad,ulke_ad))
        self.veritabanı.commit()
    def veri_güncelle(self,liman_ad,ulke_ad,nufus,pasaport_y_n,demirleme_ucret):
        self.sorgu.execute("UPDATE LİMAN_BİLGİ SET NUFUS=?,PASAPORT_Y_N=?,DEMİRLEME_UCRET=? WHERE LIMAN_AD=? AND ULKE_AD=? ",(nufus,pasaport_y_n,demirleme_ucret,liman_ad,ulke_ad))
        self.veritabanı.commit()
    
class SEFER_KAYİT(PETROL_GEMİSİ):

    def __init__(self,tabloname):
        self.veritabanı=sqlite3.connect("veritabani41.db")
        self.sorgu=self.veritabanı.cursor()
        self.tablo_name=tabloname
        self.denetle=True
        self.baslat()

    def baslat(self):
        self.gemi_idler=[]
        for gemi_id in self.sorgu.execute("SELECT * FROM SEFER_KAYİT").fetchall():
            self.gemi_idler.append(gemi_id[6])
        self.kaptan=[]
        for kaptan_id in self.sorgu.execute("SELECT * FROM SEFER_KAYİT").fetchall():
            self.kaptan.append(kaptan_id[5])
        self.liman=[]
        for liman in self.sorgu.execute("SELECT * FROM SEFER_KAYİT").fetchall():
            self.liman.append([liman[3],liman[4]]) 
        self.sefer=[]
        for sefer in self.sorgu.execute("SELECT * FROM SEFER_KAYİT").fetchall():
            self.sefer.append(sefer[0]) 
        self.bilgi_guncelle()    
    def bilgi_guncelle(self):
        self.selfkaptan=[]
        for selfkaptan in self.sorgu.execute("SELECT KAPTAN_İD FROM KAPTAN_MÜRETTEBAT ").fetchall():
            self.selfkaptan.append(selfkaptan)
        
        self.selfliman=[]
        for selfliman in self.sorgu.execute("SELECT LIMAN_AD,ULKE_AD FROM LİMAN_BİLGİ ").fetchall():
            self.selfliman.append([selfliman[0],selfliman[1]])
        self.selfgemi_id=[]
        for kgemi in self.sorgu.execute("SELECT SERİ_NO FROM KONTEYNER_GEMİSİ ").fetchall():
            self.selfgemi_id.append(kgemi[0])
        for pgemi in self.sorgu.execute("SELECT SERİ_NO FROM PETROL_GEMİSİ ").fetchall():
            self.selfgemi_id.append(pgemi[0])
        for ygemi in self.sorgu.execute("SELECT SERİ_NO FROM YOLCU_GEMİSİ ").fetchall():
            self.selfgemi_id.append(ygemi[0])

    def veri_ekle(self,yol_cikis_tarih,donus_tarih,gidilen_liman,gidilen_ulke,kaptan_id,gemi_seri_no,mode=True,sahte_id=0):
           
        if self.denetle:
            self.baslat()
            self.denetle=False
        self.bilgi_guncelle()
        self.sayac=int(satirokuyucu("veritabani41.db",5))
        self.seri_no="SF"+str(self.sayac)
        if (gemi_seri_no in self.selfgemi_id) and ((kaptan_id,) in self.selfkaptan) and ([gidilen_liman,gidilen_ulke] in self.selfliman) :

            if   [gidilen_liman,gidilen_ulke] in self.selfliman:

                if  gemi_seri_no in self.gemi_idler:
                    
                    return 0
                
                if  kaptan_id in self.kaptan:
                    
                    return 0

                self.gemi_idler.append(gemi_seri_no)
                self.kaptan.append(kaptan_id)
                self.liman.append([gidilen_liman,gidilen_ulke])
                if mode :
                    self.sorgu.execute("INSERT INTO SEFER_KAYİT (SEFER_İD,YOL_CİKİS_TARİH,DONUS_TARİH,GİDİLEN_LİMAN,GİDİLEN_ULKE,KAPTAN_İD,GEMİ_SERİ_NO) VALUES (?,?,?,?,?,?,?)" ,(self.seri_no,yol_cikis_tarih,donus_tarih,gidilen_liman,gidilen_ulke,kaptan_id,gemi_seri_no))
                    self.veritabanı.commit()
                    self.sayac+=1
                    satiryazici("veritabani41.db",5,str(self.sayac))
                    self.bilgi_guncelle()
                else:
                    self.sorgu.execute("INSERT INTO SEFER_KAYİT (SEFER_İD,YOL_CİKİS_TARİH,DONUS_TARİH,GİDİLEN_LİMAN,GİDİLEN_ULKE,KAPTAN_İD,GEMİ_SERİ_NO) VALUES (?,?,?,?,?,?,?)" ,(sahte_id,yol_cikis_tarih,donus_tarih,gidilen_liman,gidilen_ulke,kaptan_id,gemi_seri_no))
                    self.veritabanı.commit()
                return 1
               
    def veri_sil(self,sefer_id):
        if sefer_id in self.sefer:
            veri=self.sorgu.execute("SELECT * FROM SEFER_KAYİT WHERE SEFER_İD=?",(sefer_id,)).fetchall()
            self.sefer.remove(veri[0][0])
            self.liman.remove([veri[0][3],veri[0][4]])
            self.kaptan.remove(veri[0][5])
            self.gemi_idler.remove(veri[0][6])
            self.sorgu.execute("DELETE  FROM SEFER_KAYİT WHERE SEFER_İD=?",(sefer_id,))
            self.veritabanı.commit()
            self.bilgi_guncelle()
            return 1
        else:
            return 0

    def veri_güncelle(self,id,yol_cikis_tarih,donus_tarih,gidilen_liman,gidilen_ulke,kaptan_id,gemi_seri_no):
        mevcutveri=self.sorgu.execute("SELECT * FROM SEFER_KAYİT WHERE SEFER_İD=?",(id,)).fetchall()
        self.veri_sil(id)
        if self.veri_ekle(yol_cikis_tarih,donus_tarih,gidilen_liman,gidilen_ulke,kaptan_id,gemi_seri_no,False,id)==0:
            if mevcutveri==[]:
                return 0
            self.veri_ekle(mevcutveri[0][1],mevcutveri[0][2],mevcutveri[0][3],mevcutveri[0][4],mevcutveri[0][5],mevcutveri[0][6],False,mevcutveri[0][0])

               

        self.bilgi_guncelle()
        return 1
        

if not os.path.exists("veritabani41.db"):
    
    veritabani=sqlite3.connect("veritabani41.db")

    islem=veritabani.cursor()

    islem.execute(''' 

        CREATE TABLE İNDEX_TABLO(
                  
            P INTEGER NOT NULL,
            K INTEGER NOT NULL,
            Y INTEGER NOT NULL,
            KA INTEGER NOT NULL,
            SF INTEGER NOT NULL
        )
        ''')
    veritabani.commit()
    islem.execute("INSERT INTO İNDEX_TABLO (P,K,Y,KA,SF) VALUES (1,1,1,1,1)")
    islem.execute(''' 
    CREATE TABLE KONTEYNER_GEMİSİ(
                  
            SERİ_NO TEXT PRIMARY KEY ,
            GEMİ_AD TEXT NOT NULL,
            GEMİ_AGİRLİK INTEGER NOT NULL,
            YAPİM_YİLİ TIMESTAMP NOT NULL,
            KONTEYNER_SAYISI_KAPASİTE INTEGER NOT NULL,
            MAX_AGİRLİK INTEGER NOT NULL   )                         
                                
''') 
    islem.execute(''' 

    CREATE TABLE PETROL_GEMİSİ(
            SERİ_NO TEXT PRIMARY KEY ,
            GEMİ_AD TEXT NOT NULL,
            GEMİ_AGİRLİK INTEGER NOT NULL,
            YAPİM_YİLİ TIMESTAMP NOT NULL,
            PETROL_KAPASİTE INTEGER NOT NULL  )                      
                    
''')
    islem.execute(''' 
    CREATE TABLE YOLCU_GEMİSİ(
                  
        SERİ_NO TEXT PRIMARY KEY,
        GEMİ_AD TEXT NOT NULL,
        GEMİ_AGİRLİK INTEGER NOT NULL,
        YAPİM_YİLİ TIMESTAMP NOT NULL,
        YOLCU_KAPASİTE INTEGER NOT NULL   )
    
''')
    veritabani.commit()

    islem.execute(''' 

    CREATE TABLE KAPTAN_MÜRETTEBAT(
                  
    KAPTAN_İD TEXT NOT NULL,
    KAPTAN_AD TEXT NOT NULL,
    KAPTAN_SOYAD TEXT NOT NULL,
    ADRES TEXT NOT NULL,
    DOGUM_TARİH  TIMESTAMP NOT NULL,
    İSE_GİRİS_TARİH TIMESTAMP NOT NULL,
    GOREV TEXT NOT NULL,
    KAPTAN_LİSANS TEXT NOT NULL,
    PRIMARY KEY(KAPTAN_İD)

    )
''')
    veritabani.commit()
    islem.execute(''' 

    CREATE TABLE LİMAN_BİLGİ (
                  
        LIMAN_AD TEXT NOT NULL,
        ULKE_AD TEXT NOT NULL,
        NUFUS INTEGER NOT NULL,
        PASAPORT_Y_N TEXT NOT NULL,
        DEMİRLEME_UCRET INTEGER NOT NULL,
        PRIMARY KEY(LIMAN_AD,ULKE_AD)
        
                  
    )

''')
    veritabani.commit()
    islem.execute(''' 


    CREATE TABLE SEFER_KAYİT(
                  
        SEFER_İD TEXT NOT NULL,
        YOL_CİKİS_TARİH TIMESTAMP NOT NULL,
        DONUS_TARİH TIMESTAMP NOT NULL,
        GİDİLEN_LİMAN TEXT NOT NULL,          
        GİDİLEN_ULKE TEXT NOT NULL,
        KAPTAN_İD TEXT NOT NULL,
        GEMİ_SERİ_NO TEXT NOT NULL,
        PRIMARY KEY (SEFER_İD),
        FOREIGN KEY (GİDİLEN_LİMAN) REFERENCES  LİMAN_BiLGİ(LIMAN_AD) ON UPDATE CASCADE,
        FOREIGN KEY(GİDİLEN_ULKE) REFERENCES LİMAN_BİLGİ(ULKE_AD) ON UPDATE CASCADE,
        FOREIGN KEY(KAPTAN_İD) REFERENCES  KAPTAN_MÜRETTEBAT(KAPTAN_İD) ON UPDATE CASCADE
        
     
    )
   
''')
    veritabani.commit()


PETROL=PETROL_GEMİSİ("PETROL_GEMİSİ")

KONTEYNER=KONTEYNER_GEMİSİ('KONTEYNER_GEMİSİ')

YOLCU=YOLCU_GEMİSİ("YOLCU_GEMİSİ")

LİMAN=LİMAN_BİLGİ( 'LİMAN_BİLGİ')

KAPTAN=KAPTAN_M("KAPTAN_MÜRETTEBAT")

SEFER=SEFER_KAYİT('SEFER_KAYİT')

class Ui_window(object):

    def inputkontrol(self):
        if self.sefer_ekle_mode.isChecked():
            self.konteyner_gemi_id_2.setEnabled(False)
        else:
            self.konteyner_gemi_id_2.setEnabled(True)
        if self.konteyner_ekle_mode.isChecked():
            self.konteyner_gemi_id.setEnabled(False)
        else:
            self.konteyner_gemi_id.setEnabled(True)
        if self.petrol_guncelle_ekle.isChecked():
            self.petrol_gemi_id.setEnabled(False)
        else:
            self.petrol_gemi_id.setEnabled(True)
        if self.yolcu_ekle_mode.isChecked():
            self.yolcu_gemi_id.setEnabled(False)
        else:
            self.yolcu_gemi_id.setEnabled(True)
        if self.kaptan_ekle_mode.isChecked():
            self.mkaptan_id.setEnabled(False)
        else:
            self.mkaptan_id.setEnabled(True)
        
    def veritabani_iletisim_ekle_guncelle(self,no):
        
        if no==1:
            if self.sefer_ekle_mode.isChecked():
                SEFER.veri_ekle(self.yol_cikis_tarih.text(),self.donus_tarih.text(),self.gidilen_liman.text(),self.gidilen_ulke.text(),self.kaptan_id.text(),self.gemi_seri_no.text())
                self.tablo_gosterici()
            if self.sefer_guncelle_mode.isChecked():
                SEFER.veri_güncelle(self.konteyner_gemi_id_2.text(),self.yol_cikis_tarih.text(),self.donus_tarih.text(),self.gidilen_liman.text(),self.gidilen_ulke.text(),self.kaptan_id.text(),self.gemi_seri_no.text())
                self.tablo_gosterici()
        elif no==2:
            if self.konteyner_ekle_mode.isChecked():
                KONTEYNER.veri_ekle(self.konteyner_gemi_ad.text(),self.konteyner_gemi_agirlik.text(),self.konteyner_yapimyil.text(),self.konteyner_sayikapasite.text(),self.konteyner_max_agirlik.text())
                self.tablo_gosterici()
            if self.konteyner_guncelle_mode.isChecked():
                KONTEYNER.veri_güncelle(self.konteyner_gemi_id.text(),self.konteyner_gemi_ad.text(),self.konteyner_gemi_agirlik.text(),self.konteyner_yapimyil.text(),self.konteyner_sayikapasite.text(),self.konteyner_max_agirlik.text())
                self.tablo_gosterici()
        elif no==3:
            if self.petrol_guncelle_ekle.isChecked():
                PETROL.veri_ekle(self.petrol_gemi_ad.text(),self.petrol_gemi_agirlik.text(),self.petrol_yapimyil.text(),self.konteyner_petrol_kapasite.text())
                self.tablo_gosterici()
            if self.petrol_guncelle_mode.isChecked():
                PETROL.veri_güncelle(self.petrol_gemi_id,self.petrol_gemi_ad.text(),self.petrol_gemi_agirlik.text(),self.petrol_yapimyil.text(),self.konteyner_petrol_kapasite.text())
                self.tablo_gosterici()
        elif no==4:
            if self.yolcu_ekle_mode.isChecked():
                YOLCU.veri_ekle(self.yolcu_gemi_ad.text(),self.yolcu_gemi_agirlik.text(),self.yolcu_yapimyil.text(),self.yolcu_kapasite.text())
                self.tablo_gosterici()
            if self.yolcu_guncelle_mode.isChecked():
                YOLCU.veri_güncelle(self.yolcu_gemi_id.text(),self.yolcu_gemi_ad.text(),self.yolcu_gemi_agirlik.text(),self.yolcu_yapimyil.text(),self.yolcu_kapasite.text())
                self.tablo_gosterici()
        elif no==5:
            if self.kaptan_ekle_mode.isChecked():
                KAPTAN.veri_ekle(self.kaptan_ad.text(),self.kaptan_soyad.text(),self.kaptan_adres.text(),self.kaptan_dogum_tarih.text(),self.kaptan_ise_giris_tarih.text(),self.kaptan_gorev.text(),self.kaptan_lisans.text())
                self.tablo_gosterici()
            if self.kaptan_guncelle_mode.isChecked():
                KAPTAN.veri_güncelle(self.mkaptan_id.text(),self.kaptan_ad.text(),self.kaptan_soyad.text(),self.kaptan_adres.text(),self.kaptan_dogum_tarih.text(),self.kaptan_ise_giris_tarih.text(),self.kaptan_gorev.text(),self.kaptan_lisans.text())
                self.tablo_gosterici()
        elif no==6:
            if self.liman_ekle_mode.isChecked():
                LİMAN.veri_ekle(self.liman_ad.text(),self.liman_ulke_ad.text(),self.liman_nufus.text(),self.pasaport_var_yok.text(),self.liman_demirleme_ucret.text())
                self.tablo_gosterici()
            if self.liman_guncelle_mode.isChecked():
                LİMAN.veri_güncelle(self.liman_ad.text(),self.liman_ulke_ad.text(),self.liman_nufus.text(),self.pasaport_var_yok.text(),self.liman_demirleme_ucret.text())
                self.tablo_gosterici()
    def veritabani_iletisim_sil(self,no):
        if no==1:
            SEFER.veri_sil(self.silinecek_sefer_id.text())
        elif no==2:
            KONTEYNER.veri_sil(self.silinecek_konteyner_id.text())
        elif no==3:
            PETROL.veri_sil(self.silinecek_petrol_id.text())
        elif no==4:
            YOLCU.veri_sil(self.silinecek_yolcu_id.text())
        elif no==5:
            KAPTAN.veri_sil(self.silenecek_kaptan_id.text())
        elif no==6:
            liman_silincek_veri=self.silinecek_liman_id.text().split(",")
            LİMAN.veri_sil(liman_silincek_veri[0],liman_silincek_veri[1])
        self.tablo_gosterici()
    def tablo_gosterici(self):
        self.sefer_tablo.clearContents()
        self.konteyner_tablo.clearContents()
        self.petrol_tablo.clearContents()
        self.yolcu_tablo.clearContents()
        self.kaptan_tablo.clearContents()
        self.liman_tablo.clearContents()

        seferveriler=SEFER.veri_listele()
        konteynerveriler = KONTEYNER.veri_listele()
        petrolveriler=PETROL.veri_listele()
        yolcuveriler=YOLCU.veri_listele()
        kaptanveriler=KAPTAN.veri_listele()
        limanveriler=LİMAN.veri_listele()
        if seferveriler !=[]:
            
            for row_index,row_data in enumerate(seferveriler):
                
                self.sefer_tablo.insertRow(self.sefer_tablo.rowCount())
                for column_index,veri in enumerate(row_data):
                    item=QTableWidgetItem(str(veri))
                    self.sefer_tablo.setItem(row_index,column_index,item)
    # Konteyner verileri boş değilse tabloya ekleyin
        if konteynerveriler!=[]:
            for row_index, row_data in enumerate(konteynerveriler):
                
                self.konteyner_tablo.insertRow(self.konteyner_tablo.rowCount())
                for column_index, veri in enumerate(row_data):
                # Veriyi tabloya ekleyin
                    item = QTableWidgetItem(str(veri))  # Veriyi QTableWidgetItem'a dönüştür
                    self.konteyner_tablo.setItem(row_index, column_index, item)
        if petrolveriler!=[]:
            for row_index, row_data in enumerate(petrolveriler):
            # Tabloya yeni bir satır ekle
                self.petrol_tablo.insertRow(self.petrol_tablo.rowCount())
                for column_index, veri in enumerate(row_data):
                # Veriyi tabloya ekleyin
                    item = QTableWidgetItem(str(veri))  # Veriyi QTableWidgetItem'a dönüştür
                    self.petrol_tablo.setItem(row_index, column_index, item)
        if yolcuveriler!=[]:
            for row_index, row_data in enumerate(yolcuveriler):
            # Tabloya yeni bir satır ekle
                self.yolcu_tablo.insertRow(self.yolcu_tablo.rowCount())
                for column_index, veri in enumerate(row_data):
                # Veriyi tabloya ekleyin
                    item = QTableWidgetItem(str(veri))  # Veriyi QTableWidgetItem'a dönüştür
                    self.yolcu_tablo.setItem(row_index, column_index, item)
        if kaptanveriler!=[]:
            for row_index, row_data in enumerate(kaptanveriler):
            # Tabloya yeni bir satır ekle
                self.kaptan_tablo.insertRow(self.kaptan_tablo.rowCount())
                for column_index, veri in enumerate(row_data):
                # Veriyi tabloya ekleyin
                    item = QTableWidgetItem(str(veri))  # Veriyi QTableWidgetItem'a dönüştür
                    self.kaptan_tablo.setItem(row_index, column_index, item)
        if limanveriler!=[]:
            for row_index, row_data in enumerate(limanveriler):
            # Tabloya yeni bir satır ekle
                self.liman_tablo.insertRow(self.liman_tablo.rowCount())
                for column_index, veri in enumerate(row_data):
                # Veriyi tabloya ekleyin
                    item = QTableWidgetItem(str(veri))  # Veriyi QTableWidgetItem'a dönüştür
                    self.liman_tablo.setItem(row_index, column_index, item)        


    def setupUi(self, window):
        window.setObjectName("window")
        window.setEnabled(True)
        window.resize(1607, 1070)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        window.setFont(font)
        window.setTabletTracking(False)
        window.setStyleSheet("")
        window.setIconSize(QtCore.QSize(24, 24))
        window.setAnimated(True)
        window.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.yol_cikis_tarih = QtWidgets.QLineEdit(self.centralwidget)
        self.yol_cikis_tarih.setGeometry(QtCore.QRect(30, 170, 151, 31))
        self.yol_cikis_tarih.setObjectName("yol_cikis_tarih")
        self.donus_tarih = QtWidgets.QLineEdit(self.centralwidget)
        self.donus_tarih.setGeometry(QtCore.QRect(30, 220, 151, 31))
        self.donus_tarih.setObjectName("donus_tarih")
        self.gidilen_liman = QtWidgets.QLineEdit(self.centralwidget)
        self.gidilen_liman.setGeometry(QtCore.QRect(30, 270, 151, 31))
        self.gidilen_liman.setObjectName("gidilen_liman")
        self.gidilen_ulke = QtWidgets.QLineEdit(self.centralwidget)
        self.gidilen_ulke.setGeometry(QtCore.QRect(30, 320, 151, 31))
        self.gidilen_ulke.setObjectName("gidilen_ulke")
        self.kaptan_id = QtWidgets.QLineEdit(self.centralwidget)
        self.kaptan_id.setGeometry(QtCore.QRect(30, 370, 151, 31))
        self.kaptan_id.setObjectName("kaptan_id")
        self.gemi_seri_no = QtWidgets.QLineEdit(self.centralwidget)
        self.gemi_seri_no.setGeometry(QtCore.QRect(30, 420, 151, 31))
        self.gemi_seri_no.setObjectName("gemi_seri_no")
        self.sefer_kayit_buton = QtWidgets.QPushButton(self.centralwidget)
        self.sefer_kayit_buton.setGeometry(QtCore.QRect(30, 470, 151, 31))
        self.sefer_kayit_buton.setObjectName("sefer_kayit_buton")
        self.sefer_kayit_buton.clicked.connect(lambda: self.veritabani_iletisim_ekle_guncelle(1))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 510, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.silinecek_sefer_id = QtWidgets.QLineEdit(self.centralwidget)
        self.silinecek_sefer_id.setGeometry(QtCore.QRect(40, 580, 111, 31))
        self.silinecek_sefer_id.setObjectName("silinecek_sefer_id")
        
        self.sefer_kayit_sil_buton = QtWidgets.QPushButton(self.centralwidget)
        self.sefer_kayit_sil_buton.setGeometry(QtCore.QRect(40, 630, 111, 31))
        self.sefer_kayit_sil_buton.setObjectName("sefer_kayit_sil_buton")
        self.sefer_kayit_sil_buton.clicked.connect(lambda : self.veritabani_iletisim_sil(1))
        self.sefer_tablo = QtWidgets.QTableWidget(self.centralwidget)
        self.sefer_tablo.setGeometry(QtCore.QRect(10, 690, 251, 311))
        self.sefer_tablo.setObjectName("sefer_tablo")
        self.sefer_tablo.setColumnCount(7)
        self.sefer_tablo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sefer_tablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sefer_tablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sefer_tablo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sefer_tablo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.sefer_tablo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.sefer_tablo.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.sefer_tablo.setHorizontalHeaderItem(6, item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.konteyner_gemi_ad = QtWidgets.QLineEdit(self.centralwidget)
        self.konteyner_gemi_ad.setGeometry(QtCore.QRect(220, 220, 181, 31))
        self.konteyner_gemi_ad.setObjectName("konteyner_gemi_ad")
        self.konteyner_gemi_agirlik = QtWidgets.QLineEdit(self.centralwidget)
        self.konteyner_gemi_agirlik.setGeometry(QtCore.QRect(220, 270, 181, 31))
        self.konteyner_gemi_agirlik.setObjectName("konteyner_gemi_agirlik")
        self.konteyner_yapimyil = QtWidgets.QLineEdit(self.centralwidget)
        self.konteyner_yapimyil.setGeometry(QtCore.QRect(220, 320, 181, 31))
        self.konteyner_yapimyil.setObjectName("konteyner_yapimyil")
        self.konteyner_sayikapasite = QtWidgets.QLineEdit(self.centralwidget)
        self.konteyner_sayikapasite.setGeometry(QtCore.QRect(220, 370, 181, 31))
        self.konteyner_sayikapasite.setObjectName("konteyner_sayikapasite")
        self.konteyner_max_agirlik = QtWidgets.QLineEdit(self.centralwidget)
        self.konteyner_max_agirlik.setGeometry(QtCore.QRect(220, 420, 181, 31))
        self.konteyner_max_agirlik.setObjectName("konteyner_max_agirlik")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 510, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.silinecek_konteyner_id = QtWidgets.QLineEdit(self.centralwidget)
        self.silinecek_konteyner_id.setGeometry(QtCore.QRect(220, 580, 181, 31))
        self.silinecek_konteyner_id.setObjectName("silinecek_konteyner_id")
        self.konteyner_gemi_sil_buton = QtWidgets.QPushButton(self.centralwidget)
        self.konteyner_gemi_sil_buton.setGeometry(QtCore.QRect(220, 630, 181, 31))
        self.konteyner_gemi_sil_buton.setObjectName("konteyner_gemi_sil_buton")
        self.konteyner_gemi_sil_buton.clicked.connect(lambda : self.veritabani_iletisim_sil(2))
        self.konteyner_tablo = QtWidgets.QTableWidget(self.centralwidget)
        self.konteyner_tablo.setGeometry(QtCore.QRect(270, 690, 251, 311))
        self.konteyner_tablo.setObjectName("konteyner_tablo")
        self.konteyner_tablo.setColumnCount(6)
        self.konteyner_tablo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.konteyner_tablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.konteyner_tablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.konteyner_tablo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.konteyner_tablo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.konteyner_tablo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.konteyner_tablo.setHorizontalHeaderItem(5, item)
        self.petrol_tablo = QtWidgets.QTableWidget(self.centralwidget)
        self.petrol_tablo.setGeometry(QtCore.QRect(530, 690, 261, 311))
        self.petrol_tablo.setObjectName("petrol_tablo")
        self.petrol_tablo.setColumnCount(5)
        self.petrol_tablo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.petrol_tablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.petrol_tablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.petrol_tablo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.petrol_tablo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.petrol_tablo.setHorizontalHeaderItem(4, item)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.petrol_gemi_ad = QtWidgets.QLineEdit(self.centralwidget)
        self.petrol_gemi_ad.setEnabled(True)
        self.petrol_gemi_ad.setGeometry(QtCore.QRect(440, 250, 151, 31))
        self.petrol_gemi_ad.setObjectName("petrol_gemi_ad")
        self.petrol_gemi_agirlik = QtWidgets.QLineEdit(self.centralwidget)
        self.petrol_gemi_agirlik.setGeometry(QtCore.QRect(440, 310, 151, 31))
        self.petrol_gemi_agirlik.setObjectName("petrol_gemi_agirlik")
        self.petrol_yapimyil = QtWidgets.QLineEdit(self.centralwidget)
        self.petrol_yapimyil.setGeometry(QtCore.QRect(440, 370, 151, 31))
        self.petrol_yapimyil.setObjectName("petrol_yapimyil")
        self.konteyner_petrol_kapasite = QtWidgets.QLineEdit(self.centralwidget)
        self.konteyner_petrol_kapasite.setGeometry(QtCore.QRect(440, 420, 151, 31))
        self.konteyner_petrol_kapasite.setObjectName("konteyner_petrol_kapasite")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 510, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.silinecek_petrol_id = QtWidgets.QLineEdit(self.centralwidget)
        self.silinecek_petrol_id.setGeometry(QtCore.QRect(440, 580, 151, 31))
        self.silinecek_petrol_id.setObjectName("silinecek_petrol_id")
        self.petrol_gemi_sil_buton = QtWidgets.QPushButton(self.centralwidget)
        self.petrol_gemi_sil_buton.setGeometry(QtCore.QRect(440, 630, 151, 31))
        self.petrol_gemi_sil_buton.setObjectName("petrol_gemi_sil_buton")
        self.petrol_gemi_sil_buton.clicked.connect(lambda:self.veritabani_iletisim_sil(3))
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(680, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.liman_tablo = QtWidgets.QTableWidget(self.centralwidget)
        self.liman_tablo.setGeometry(QtCore.QRect(1340, 690, 251, 311))
        self.liman_tablo.setObjectName("liman_tablo")
        self.liman_tablo.setColumnCount(5)
        self.liman_tablo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.liman_tablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.liman_tablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.liman_tablo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.liman_tablo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.liman_tablo.setHorizontalHeaderItem(4, item)
        self.kaptan_tablo = QtWidgets.QTableWidget(self.centralwidget)
        self.kaptan_tablo.setGeometry(QtCore.QRect(1070, 690, 261, 311))
        self.kaptan_tablo.setObjectName("kaptan_tablo")
        self.kaptan_tablo.setColumnCount(8)
        self.kaptan_tablo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.kaptan_tablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaptan_tablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaptan_tablo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaptan_tablo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaptan_tablo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaptan_tablo.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaptan_tablo.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.kaptan_tablo.setHorizontalHeaderItem(7, item)
        self.yolcu_tablo = QtWidgets.QTableWidget(self.centralwidget)
        self.yolcu_tablo.setGeometry(QtCore.QRect(800, 690, 261, 311))
        self.yolcu_tablo.setObjectName("yolcu_tablo")
        self.yolcu_tablo.setColumnCount(5)
        self.yolcu_tablo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.yolcu_tablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.yolcu_tablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.yolcu_tablo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.yolcu_tablo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.yolcu_tablo.setHorizontalHeaderItem(4, item)
        self.yolcu_gemi_ad = QtWidgets.QLineEdit(self.centralwidget)
        self.yolcu_gemi_ad.setEnabled(True)
        self.yolcu_gemi_ad.setGeometry(QtCore.QRect(630, 250, 151, 31))
        self.yolcu_gemi_ad.setObjectName("yolcu_gemi_ad")
        self.yolcu_gemi_agirlik = QtWidgets.QLineEdit(self.centralwidget)
        self.yolcu_gemi_agirlik.setGeometry(QtCore.QRect(630, 310, 151, 31))
        self.yolcu_gemi_agirlik.setObjectName("yolcu_gemi_agirlik")
        self.yolcu_yapimyil = QtWidgets.QLineEdit(self.centralwidget)
        self.yolcu_yapimyil.setGeometry(QtCore.QRect(630, 370, 151, 31))
        self.yolcu_yapimyil.setObjectName("yolcu_yapimyil")
        self.yolcu_kapasite = QtWidgets.QLineEdit(self.centralwidget)
        self.yolcu_kapasite.setGeometry(QtCore.QRect(630, 420, 151, 31))
        self.yolcu_kapasite.setObjectName("yolcu_kapasite")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(630, 510, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.silinecek_yolcu_id = QtWidgets.QLineEdit(self.centralwidget)
        self.silinecek_yolcu_id.setGeometry(QtCore.QRect(630, 580, 151, 31))
        self.silinecek_yolcu_id.setObjectName("silinecek_yolcu_id")
        self.yolcu_gemi_sil_buton = QtWidgets.QPushButton(self.centralwidget)
        self.yolcu_gemi_sil_buton.setGeometry(QtCore.QRect(630, 630, 151, 31))
        self.yolcu_gemi_sil_buton.setObjectName("yolcu_gemi_sil_buton")
        self.yolcu_gemi_sil_buton.clicked.connect(lambda:self.veritabani_iletisim_sil(4))
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(900, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1250, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.kaptan_ad = QtWidgets.QLineEdit(self.centralwidget)
        self.kaptan_ad.setEnabled(True)
        self.kaptan_ad.setGeometry(QtCore.QRect(910, 130, 131, 31))
        self.kaptan_ad.setObjectName("kaptan_ad")
        self.kaptan_soyad = QtWidgets.QLineEdit(self.centralwidget)
        self.kaptan_soyad.setEnabled(True)
        self.kaptan_soyad.setGeometry(QtCore.QRect(910, 180, 131, 31))
        self.kaptan_soyad.setObjectName("kaptan_soyad")
        self.kaptan_adres = QtWidgets.QLineEdit(self.centralwidget)
        self.kaptan_adres.setEnabled(True)
        self.kaptan_adres.setGeometry(QtCore.QRect(910, 230, 131, 31))
        self.kaptan_adres.setObjectName("kaptan_adres")
        self.kaptan_dogum_tarih = QtWidgets.QLineEdit(self.centralwidget)
        self.kaptan_dogum_tarih.setEnabled(True)
        self.kaptan_dogum_tarih.setGeometry(QtCore.QRect(910, 280, 131, 31))
        self.kaptan_dogum_tarih.setObjectName("kaptan_dogum_tarih")
        self.kaptan_ise_giris_tarih = QtWidgets.QLineEdit(self.centralwidget)
        self.kaptan_ise_giris_tarih.setEnabled(True)
        self.kaptan_ise_giris_tarih.setGeometry(QtCore.QRect(910, 330, 131, 31))
        self.kaptan_ise_giris_tarih.setObjectName("kaptan_ise_giris_tarih")
        self.kaptan_gorev = QtWidgets.QLineEdit(self.centralwidget)
        self.kaptan_gorev.setEnabled(True)
        self.kaptan_gorev.setGeometry(QtCore.QRect(910, 380, 131, 31))
        self.kaptan_gorev.setObjectName("kaptan_gorev")
        self.kaptan_lisans = QtWidgets.QLineEdit(self.centralwidget)
        self.kaptan_lisans.setEnabled(True)
        self.kaptan_lisans.setGeometry(QtCore.QRect(910, 430, 131, 31))
        self.kaptan_lisans.setObjectName("kaptan_lisans")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(900, 510, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.silenecek_kaptan_id = QtWidgets.QLineEdit(self.centralwidget)
        self.silenecek_kaptan_id.setGeometry(QtCore.QRect(900, 580, 131, 31))
        self.silenecek_kaptan_id.setObjectName("silenecek_kaptan_id")
        self.kaptan_sil_buton = QtWidgets.QPushButton(self.centralwidget)
        self.kaptan_sil_buton.setGeometry(QtCore.QRect(900, 630, 131, 31))
        self.kaptan_sil_buton.setObjectName("kaptan_sil_buton")
        self.kaptan_sil_buton.clicked.connect(lambda:self.veritabani_iletisim_sil(5))
        self.liman_ad = QtWidgets.QLineEdit(self.centralwidget)
        self.liman_ad.setEnabled(True)
        self.liman_ad.setGeometry(QtCore.QRect(1220, 220, 131, 31))
        self.liman_ad.setObjectName("liman_ad")
        self.liman_ulke_ad = QtWidgets.QLineEdit(self.centralwidget)
        self.liman_ulke_ad.setEnabled(True)
        self.liman_ulke_ad.setGeometry(QtCore.QRect(1220, 270, 131, 31))
        self.liman_ulke_ad.setObjectName("liman_ulke_ad")
        self.liman_nufus = QtWidgets.QLineEdit(self.centralwidget)
        self.liman_nufus.setEnabled(True)
        self.liman_nufus.setGeometry(QtCore.QRect(1220, 320, 131, 31))
        self.liman_nufus.setObjectName("liman_nufus")
        self.pasaport_var_yok = QtWidgets.QLineEdit(self.centralwidget)
        self.pasaport_var_yok.setEnabled(True)
        self.pasaport_var_yok.setGeometry(QtCore.QRect(1220, 370, 131, 31))
        self.pasaport_var_yok.setObjectName("pasaport_var_yok")
        self.liman_demirleme_ucret = QtWidgets.QLineEdit(self.centralwidget)
        self.liman_demirleme_ucret.setEnabled(True)
        self.liman_demirleme_ucret.setGeometry(QtCore.QRect(1220, 420, 131, 31))
        self.liman_demirleme_ucret.setObjectName("liman_demirleme_ucret")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1220, 510, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.silinecek_liman_id = QtWidgets.QLineEdit(self.centralwidget)
        self.silinecek_liman_id.setGeometry(QtCore.QRect(1220, 580, 131, 31))
        self.silinecek_liman_id.setObjectName("silinecek_liman_id")
        self.liman_sil_buton = QtWidgets.QPushButton(self.centralwidget)
        self.liman_sil_buton.setGeometry(QtCore.QRect(1220, 620, 131, 31))
        self.liman_sil_buton.setObjectName("liman_sil_buton")
        self.liman_sil_buton.clicked.connect(lambda:self.veritabani_iletisim_sil(6))
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 40, 160, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.sefer_radio_alan = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.sefer_radio_alan.setContentsMargins(0, 0, 0, 0)
        self.sefer_radio_alan.setObjectName("sefer_radio_alan")
        self.sefer_guncelle_mode = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.sefer_guncelle_mode.setEnabled(True)
        self.sefer_guncelle_mode.setObjectName("sefer_guncelle_mode")
        self.sefer_guncelle_mode.toggled.connect(self.inputkontrol)
        self.sefer_radio_alan.addWidget(self.sefer_guncelle_mode, 2, 0, 1, 1)
        self.sefer_ekle_mode = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.sefer_ekle_mode.setObjectName("sefer_ekle_mode")
        self.sefer_radio_alan.addWidget(self.sefer_ekle_mode, 0, 0, 1, 1)
        self.sefer_ekle_mode.toggled.connect(self.inputkontrol)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(230, 40, 160, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.konteyner_radio_alan = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.konteyner_radio_alan.setContentsMargins(0, 0, 0, 0)
        self.konteyner_radio_alan.setObjectName("konteyner_radio_alan")
        self.konteyner_ekle_mode = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.konteyner_ekle_mode.setObjectName("konteyner_ekle_mode")
        self.konteyner_ekle_mode.toggled.connect(self.inputkontrol)
        self.konteyner_radio_alan.addWidget(self.konteyner_ekle_mode, 0, 0, 1, 1)
        self.konteyner_guncelle_mode = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.konteyner_guncelle_mode.setObjectName("konteyner_guncelle_mode")
        self.konteyner_radio_alan.addWidget(self.konteyner_guncelle_mode, 1, 0, 1, 1)
        self.konteyner_guncelle_mode.toggled.connect(self.inputkontrol)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(450, 40, 151, 80))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.petrol_radio_alan = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.petrol_radio_alan.setContentsMargins(0, 0, 0, 0)
        self.petrol_radio_alan.setObjectName("petrol_radio_alan")
        self.petrol_guncelle_ekle = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.petrol_guncelle_ekle.setObjectName("petrol_guncelle_ekle")
        self.petrol_radio_alan.addWidget(self.petrol_guncelle_ekle, 1, 0, 1, 1)
        self.petrol_guncelle_ekle.toggled.connect(self.inputkontrol)
        self.petrol_guncelle_mode = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.petrol_guncelle_mode.setObjectName("petrol_guncelle_mode")
        self.petrol_radio_alan.addWidget(self.petrol_guncelle_mode, 3, 0, 1, 1)
        self.petrol_guncelle_mode.toggled.connect(self.inputkontrol)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(900, 40, 160, 80))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.kaptan_radio_alan = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.kaptan_radio_alan.setContentsMargins(0, 0, 0, 0)
        self.kaptan_radio_alan.setObjectName("kaptan_radio_alan")
        self.kaptan_ekle_mode = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.kaptan_ekle_mode.setObjectName("kaptan_ekle_mode")
        self.kaptan_radio_alan.addWidget(self.kaptan_ekle_mode, 0, 0, 1, 1)
        self.kaptan_ekle_mode.toggled.connect(self.inputkontrol)
        self.kaptan_guncelle_mode = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.kaptan_guncelle_mode.setObjectName("kaptan_guncelle_mode")
        self.kaptan_guncelle_mode.toggled.connect(self.inputkontrol)
        self.kaptan_radio_alan.addWidget(self.kaptan_guncelle_mode, 1, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(660, 40, 160, 80))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.yolcu_radio_alan = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.yolcu_radio_alan.setContentsMargins(0, 0, 0, 0)
        self.yolcu_radio_alan.setObjectName("yolcu_radio_alan")
        self.yolcu_guncelle_mode = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.yolcu_guncelle_mode.setObjectName("yolcu_guncelle_mode")
        self.yolcu_radio_alan.addWidget(self.yolcu_guncelle_mode, 2, 0, 1, 1)
        self.yolcu_guncelle_mode.toggled.connect(self.inputkontrol)
        self.yolcu_ekle_mode = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.yolcu_ekle_mode.setObjectName("yolcu_ekle_mode")
        self.yolcu_radio_alan.addWidget(self.yolcu_ekle_mode, 1, 0, 1, 1)
        self.yolcu_ekle_mode.toggled.connect(self.inputkontrol)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(1220, 40, 160, 80))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.liman_radio = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.liman_radio.setContentsMargins(0, 0, 0, 0)
        self.liman_radio.setObjectName("liman_radio")
        self.liman_ekle_mode = QtWidgets.QRadioButton(self.gridLayoutWidget_6)
        self.liman_ekle_mode.setObjectName("liman_ekle_mode")
        self.liman_radio.addWidget(self.liman_ekle_mode, 0, 0, 1, 1)
        self.liman_ekle_mode.toggled.connect(self.inputkontrol)
        self.liman_guncelle_mode = QtWidgets.QRadioButton(self.gridLayoutWidget_6)
        self.liman_guncelle_mode.setObjectName("liman_guncelle_mode")
        self.liman_guncelle_mode.toggled.connect(self.inputkontrol)
        self.liman_radio.addWidget(self.liman_guncelle_mode, 1, 0, 1, 1)
        self.konteyner_kayit_buton = QtWidgets.QPushButton(self.centralwidget)
        self.konteyner_kayit_buton.setGeometry(QtCore.QRect(220, 470, 181, 31))
        self.konteyner_kayit_buton.setObjectName("konteyner_kayit_buton")
        self.konteyner_kayit_buton.clicked.connect(lambda: self.veritabani_iletisim_ekle_guncelle(2))
        self.konteyner_gemi_id = QtWidgets.QLineEdit(self.centralwidget)
        self.konteyner_gemi_id.setGeometry(QtCore.QRect(220, 170, 181, 31))
        self.konteyner_gemi_id.setObjectName("konteyner_gemi_id")
        self.petrol_kayit_buton = QtWidgets.QPushButton(self.centralwidget)
        self.petrol_kayit_buton.setGeometry(QtCore.QRect(440, 470, 151, 31))
        self.petrol_kayit_buton.setObjectName("petrol_kayit_buton")
        self.petrol_kayit_buton.clicked.connect(lambda: self.veritabani_iletisim_ekle_guncelle(3))
        self.petrol_gemi_id = QtWidgets.QLineEdit(self.centralwidget)
        self.petrol_gemi_id.setEnabled(True)
        self.petrol_gemi_id.setGeometry(QtCore.QRect(440, 190, 151, 31))
        self.petrol_gemi_id.setObjectName("petrol_gemi_id")
        self.yolcu_kayit_buton = QtWidgets.QPushButton(self.centralwidget)
        self.yolcu_kayit_buton.setGeometry(QtCore.QRect(630, 470, 151, 31))
        self.yolcu_kayit_buton.setObjectName("yolcu_kayit_buton")
        self.yolcu_kayit_buton.clicked.connect(lambda: self.veritabani_iletisim_ekle_guncelle(4))
        self.yolcu_gemi_id = QtWidgets.QLineEdit(self.centralwidget)
        self.yolcu_gemi_id.setEnabled(True)
        self.yolcu_gemi_id.setGeometry(QtCore.QRect(630, 190, 151, 31))
        self.yolcu_gemi_id.setObjectName("yolcu_gemi_id")
        self.kaptan_kayit_buton = QtWidgets.QPushButton(self.centralwidget)
        self.kaptan_kayit_buton.setGeometry(QtCore.QRect(910, 470, 151, 31))
        self.kaptan_kayit_buton.setObjectName("kaptan_kayit_buton")
        self.kaptan_kayit_buton.clicked.connect(lambda: self.veritabani_iletisim_ekle_guncelle(5))
        self.liman_kayit_buton = QtWidgets.QPushButton(self.centralwidget)
        self.liman_kayit_buton.setGeometry(QtCore.QRect(1220, 470, 131, 31))
        self.liman_kayit_buton.setObjectName("liman_kayit_buton")
        self.liman_kayit_buton.clicked.connect(lambda: self.veritabani_iletisim_ekle_guncelle(6))
        self.konteyner_gemi_id_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.konteyner_gemi_id_2.setGeometry(QtCore.QRect(30, 130, 181, 31))
        self.konteyner_gemi_id_2.setObjectName("konteyner_gemi_id_2")
        self.mkaptan_id = QtWidgets.QLineEdit(self.centralwidget)
        self.mkaptan_id.setEnabled(True)
        self.mkaptan_id.setGeometry(QtCore.QRect(1050, 130, 131, 31))
        self.mkaptan_id.setObjectName("mkaptan_id")
        window.setCentralWidget(self.centralwidget)

        self.tablo_gosterici()
        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)
        
    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "VERİTABANI UYGULAMASI"))
        self.label.setText(_translate("window", "SEFER   BİLGİ  "))
        self.yol_cikis_tarih.setText(_translate("window", "YOLA ÇIKIŞ TARİHİ"))
        self.donus_tarih.setText(_translate("window", "DÖNÜŞ TARİHİ"))
        self.gidilen_liman.setText(_translate("window", "GİDİLEN LİMAN"))
        self.gidilen_ulke.setText(_translate("window", "GİDİLEN ÜLKE"))
        self.kaptan_id.setText(_translate("window", "KAPTAN İD"))
        self.gemi_seri_no.setText(_translate("window", "GEMİ SERİ NO"))
        self.sefer_kayit_buton.setText(_translate("window", "EKLE/GÜNCELLE"))
        self.label_2.setText(_translate("window", "  KAYIT SİLME"))
        self.silinecek_sefer_id.setText(_translate("window", "SİLİNECEK SEFER İD"))
        self.sefer_kayit_sil_buton.setText(_translate("window", "SEFER SİL"))
        item = self.sefer_tablo.horizontalHeaderItem(0)
        item.setText(_translate("window", "SEFER_İD"))
        item = self.sefer_tablo.horizontalHeaderItem(1)
        item.setText(_translate("window", "YOLA_CİKİS_TARİH"))
        item = self.sefer_tablo.horizontalHeaderItem(2)
        item.setText(_translate("window", "DONUS_TARİH"))
        item = self.sefer_tablo.horizontalHeaderItem(3)
        item.setText(_translate("window", "GİDİLEN_LİMAN"))
        item = self.sefer_tablo.horizontalHeaderItem(4)
        item.setText(_translate("window", "GİDİLEN_ULKE"))
        item = self.sefer_tablo.horizontalHeaderItem(5)
        item.setText(_translate("window", "KAPTAN_İD"))
        item = self.sefer_tablo.horizontalHeaderItem(6)
        item.setText(_translate("window", "GEMİ_SERİ_NO"))
        self.label_3.setText(_translate("window", "KONTEYNER GEMİ  "))
        self.konteyner_gemi_ad.setText(_translate("window", "GEMİ AD"))
        self.konteyner_gemi_agirlik.setText(_translate("window", "GEMİ AGİRLİK"))
        self.konteyner_yapimyil.setText(_translate("window", "YAPİM YİLİ"))
        self.konteyner_sayikapasite.setText(_translate("window", "KONTEYNER SAYI KAPASİTE"))
        self.konteyner_max_agirlik.setText(_translate("window", "MAX AGİRLİK"))
        self.label_4.setText(_translate("window", "  KAYIT SİLME"))
        self.silinecek_konteyner_id.setText(_translate("window", "SİLİNECEK KONTEYNER GEMİ ID"))
        self.konteyner_gemi_sil_buton.setText(_translate("window", "GEMİ SİL"))
        item = self.konteyner_tablo.horizontalHeaderItem(0)
        item.setText(_translate("window", "SERİ NO"))
        item = self.konteyner_tablo.horizontalHeaderItem(1)
        item.setText(_translate("window", "GEMİ AD"))
        item = self.konteyner_tablo.horizontalHeaderItem(2)
        item.setText(_translate("window", "GEMİ AGİRLİK"))
        item = self.konteyner_tablo.horizontalHeaderItem(3)
        item.setText(_translate("window", "YAPİM YİLİ"))
        item=self.konteyner_tablo.horizontalHeaderItem(4)
        item.setText(_translate("window", "KONTEYNER SAYİ KAPASİTE"))
        item = self.konteyner_tablo.horizontalHeaderItem(5)
        item.setText(_translate("window", "MAX AGİRLİK"))
        
        item = self.petrol_tablo.horizontalHeaderItem(0)
        item.setText(_translate("window", "SERİ NO"))
        item = self.petrol_tablo.horizontalHeaderItem(1)
        item.setText(_translate("window", "GEMİ AD"))
        item = self.petrol_tablo.horizontalHeaderItem(2)
        item.setText(_translate("window", "GEMİ AGİRLİK"))
        item = self.petrol_tablo.horizontalHeaderItem(3)
        item.setText(_translate("window", "YAPİM YİLİ"))
        item = self.petrol_tablo.horizontalHeaderItem(4)
        item.setText(_translate("window", "PETROL KAPASİTE"))
        self.label_5.setText(_translate("window", "PETROL GEMİ"))
        self.petrol_gemi_ad.setText(_translate("window", "GEMİ AD"))
        self.petrol_gemi_agirlik.setText(_translate("window", "GEMİ AGİRLİK"))
        self.petrol_yapimyil.setText(_translate("window", "YAPİM YİLİ"))
        self.konteyner_petrol_kapasite.setText(_translate("window", "PETROL KAPASİTE"))
        self.label_6.setText(_translate("window", "  KAYIT SİLME"))
        self.silinecek_petrol_id.setText(_translate("window", "SİLİNECEK PETROL GEMİ ID"))
        self.petrol_gemi_sil_buton.setText(_translate("window", "GEMİ SİL"))
        self.label_7.setText(_translate("window", "YOLCU GEMİ "))
        item = self.liman_tablo.horizontalHeaderItem(0)
        item.setText(_translate("window", "LİMAN AD"))
        item = self.liman_tablo.horizontalHeaderItem(1)
        item.setText(_translate("window", "ÜLKE AD"))
        item = self.liman_tablo.horizontalHeaderItem(2)
        item.setText(_translate("window", "NÜFUS"))
        item = self.liman_tablo.horizontalHeaderItem(3)
        item.setText(_translate("window", "PASAPORT VAR MI"))
        item = self.liman_tablo.horizontalHeaderItem(4)
        item.setText(_translate("window", "DEMİRLEME ÜCRETİ"))
        item = self.kaptan_tablo.horizontalHeaderItem(0)
        item.setText(_translate("window", "KAPTAN İD"))
        item = self.kaptan_tablo.horizontalHeaderItem(1)
        item.setText(_translate("window", "KAPTAN AD"))
        item = self.kaptan_tablo.horizontalHeaderItem(2)
        item.setText(_translate("window", "KAPTAN SOYAD"))
        item = self.kaptan_tablo.horizontalHeaderItem(3)
        item.setText(_translate("window", "ADRES"))
        item = self.kaptan_tablo.horizontalHeaderItem(4)
        item.setText(_translate("window", "DOGUM TARİH"))
        item = self.kaptan_tablo.horizontalHeaderItem(5)
        item.setText(_translate("window", "İSE GİRİS TARİH"))
        item = self.kaptan_tablo.horizontalHeaderItem(6)
        item.setText(_translate("window", "GÖREV"))
        item = self.kaptan_tablo.horizontalHeaderItem(7)
        item.setText(_translate("window", "KAPTAN LİSANS"))
        item = self.yolcu_tablo.horizontalHeaderItem(0)
        item.setText(_translate("window", "SERİ NO"))
        item = self.yolcu_tablo.horizontalHeaderItem(1)
        item.setText(_translate("window", "GEMİ AD"))
        item = self.yolcu_tablo.horizontalHeaderItem(2)
        item.setText(_translate("window", "GEMİ AGİRLİK"))
        item = self.yolcu_tablo.horizontalHeaderItem(3)
        item.setText(_translate("window", "YAPİM YİLİ"))
        item = self.yolcu_tablo.horizontalHeaderItem(4)
        item.setText(_translate("window", "YOLCU KAPASİTE"))
        self.yolcu_gemi_ad.setText(_translate("window", "GEMİ AD"))
        self.yolcu_gemi_agirlik.setText(_translate("window", "GEMİ AGİRLİK"))
        self.yolcu_yapimyil.setText(_translate("window", "YAPİM YİLİ"))
        self.yolcu_kapasite.setText(_translate("window", "YOLCU KAPASİTE"))
        self.label_8.setText(_translate("window", "  KAYIT SİLME"))
        self.silinecek_yolcu_id.setText(_translate("window", "SİLİNECEK YOLCU GEMİ ID"))
        self.yolcu_gemi_sil_buton.setText(_translate("window", "GEMİ SİL"))
        self.label_9.setText(_translate("window", "KAPTAN VE MÜRETTEBAT "))
        self.label_10.setText(_translate("window", "LİMAN "))
        self.kaptan_ad.setText(_translate("window", "KAPTAN AD"))
        self.kaptan_soyad.setText(_translate("window", "KAPTAN SOYAD"))
        self.kaptan_adres.setText(_translate("window", "ADRES"))
        self.kaptan_dogum_tarih.setText(_translate("window", "DOGUM TARİH"))
        self.kaptan_ise_giris_tarih.setText(_translate("window", "İSE GİRİS TARİH"))
        self.kaptan_gorev.setText(_translate("window", "GOREV"))
        self.kaptan_lisans.setText(_translate("window", "KAPTAN LİSANS"))
        self.label_11.setText(_translate("window", "  KAYIT SİLME"))
        self.silenecek_kaptan_id.setText(_translate("window", "SİLİNECEK KAPTAN  ID"))
        self.kaptan_sil_buton.setText(_translate("window", "KAPTAN SİL"))
        self.liman_ad.setText(_translate("window", "LIMAN AD"))
        self.liman_ulke_ad.setText(_translate("window", "ULKE AD"))
        self.liman_nufus.setText(_translate("window", "NUFUS"))
        self.pasaport_var_yok.setText(_translate("window", "PASAPORT VAR/YOK"))
        self.liman_demirleme_ucret.setText(_translate("window", "DEMİRLEME ÜCRET"))
        self.label_12.setText(_translate("window", "  KAYIT SİLME"))
        self.silinecek_liman_id.setText(_translate("window", "SİLİNECEK LIMAN,ULKE"))
        self.liman_sil_buton.setText(_translate("window", "LİMAN SİL"))
        self.sefer_guncelle_mode.setText(_translate("window", "GÜNCELLE"))
        self.sefer_ekle_mode.setText(_translate("window", "EKLE"))
        self.konteyner_ekle_mode.setText(_translate("window", "EKLE"))
        self.konteyner_guncelle_mode.setText(_translate("window", "GÜNCELLE"))
        self.petrol_guncelle_ekle.setText(_translate("window", "EKLE"))
        self.petrol_guncelle_mode.setText(_translate("window", "GÜNCELLE"))
        self.kaptan_ekle_mode.setText(_translate("window", "EKLE"))
        self.kaptan_guncelle_mode.setText(_translate("window", "GÜNCELLE"))
        self.yolcu_guncelle_mode.setText(_translate("window", "GÜNCELLE"))
        self.yolcu_ekle_mode.setText(_translate("window", "EKLE"))
        self.liman_ekle_mode.setText(_translate("window", "EKLE"))
        self.liman_guncelle_mode.setText(_translate("window", "GÜNCELLE"))
        self.konteyner_kayit_buton.setText(_translate("window", "EKLE/GÜNCELLE"))
        self.konteyner_gemi_id.setText(_translate("window", "GEMİ ID"))
        self.petrol_kayit_buton.setText(_translate("window", "EKLE/GÜNCELLE"))
        self.petrol_gemi_id.setText(_translate("window", "GEMİ ID"))
        self.yolcu_kayit_buton.setText(_translate("window", "EKLE/GÜNCELLE"))
        self.yolcu_gemi_id.setText(_translate("window", "GEMI ID"))
        self.kaptan_kayit_buton.setText(_translate("window", "EKLE/GÜNCELLE"))
        self.liman_kayit_buton.setText(_translate("window", "EKLE/GÜNCELLE"))
        self.konteyner_gemi_id_2.setText(_translate("window", "SEFER İD"))
        self.mkaptan_id.setText(_translate("window", "KAPTAN ID"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


