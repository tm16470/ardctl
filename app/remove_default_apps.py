#!/usr/bin/env python

import sys
import subprocess
import re
	
def main():

    if not len(sys.argv) > 1:
        subprocess.run('adb devices', shell=True)
        print('Argument is required. exit.')
        sys.exit(1)

    sn = sys.argv[1]

    cmd = f'adb -s {sn} shell pm list package'
    output = subprocess.run(cmd, shell=True, capture_output=True)

    keywords = [
    # NTT Docomo
	"nttdocomo", "docomo", "ntt",

    # au / UQ mobile
	"kddi",

    # Softbank / Y!mobile
	"softbank", "yahoo", "paypay",

    # Google Apps
	"com.google.android.apps.fitness", "com.google.android.apps.chromecast.app",
	"com.google.android.gms.pay.sidecar", "com.google.android.apps.adm",

	# Meet
	"com.google.android.apps.tachyon",

	# Home

	# Keep
	"com.google.android.keep",

	# News
	"com.google.android.apps.magazines",

	# One
	"com.google.android.apps.subscriptions.red",

	# Wallet
	"com.google.android.apps.walletnfcrel",

	# Translater

	# Google TV
	"com.google.android.videos",

	# Youtube Music
	"com.google.android.apps.youtube.music",

	# Googleドライブ
	"com.google.android.apps.docs",


    # Common Apps
    	"facebook", "netflix", "radiko", "adobe", "linkedin", "amazon",
	"disney", "tiktok",


    # Fujitsu A101FC (arrows we)
    	"sony.nfx.app.sfrc", "fcnt.mobile_phone.lamembers", "fujitsu.mobile_phone.NXwidget", 
	"package:com.fcnt.mobile_phone.gamegallery", "package:com.fcnt.mobile_phone.gamelauncher",
	"package:com.fcnt.mobile_phone.gamemode", "fcnt.mobile_phone.fastmemo",
	"fcnt.mobile_phone.arrowswallet", "fujitsu.mobile_phone.Recommend",
	"fujitsu.mobile_phone.fjhome_simple", "fujitsu.mobile_phone.simplemode",
	"fujitsu.mobile_phone.TransferSupport", "fujitsu.mobile_phone.easydialer",
	"fujitsu.mobile_phone.easycontacts", "fcnt.mobile_phone.fcntappdownloader",
	"fcnt.mobile_phone.rakurakucommunity", "fujitsu.mobile_phone.healthcare",
	"fujitsu.mobile_phone.Araikata", "fujitsu.mobile_phone.passwordmanager",
	"atok",

    # Fujitsu FCG02 (Docomo)
	"us.mitene", "fcnt.mobile_phone.onlinemanual",
	"fujitsu.mobile_phone.exlidertutorial", 
	"fujitsu.mobile_phone.exliderservice",
	"ss.android.ugc.trill",
	

    # Sharp A103SH
	"sharp.android.karadamate", "sharp.jp.android.makersiteappli",
	"sharp.android.smarthomehub", "sharp.android.soundmemo",
	"sharp.android.qrreader", "sharp.android.emopar",
	"com.mcafee.vsm_android_sbm",

    # Sony SO-53C (Docomo)
	"sonyericsson.androidapp.sehome", "sonymobile.xperia.guide",
	"sonymobile.simplehome", "sonyericsson.music",
	"sonymobile.fmradio", "sony.mc.so53c.manual", 
	"sonymobile.xperia.cover", "sony.drbd.reader.other.jp",
	"id_credit_sp.android",

    # motorola moto g64y 5G (Y!mobile)
	"com.motorola.moto", "motorola.securityhub",
	"motorola.securevault", "motorola.spaces",
	"motorola.gamemode", "motorola.dolby.dolbyui",
	"dolby.daxservice", "motorola.android.fmradio",
	"motorola.fmplayer", "motorola.ccc.notification",
	"motorola.audiorecorder",


    ]

    pattern = re.compile( "|".join(keywords), re.IGNORECASE)
    for i in output.stdout.decode('utf-8').split('\n'):
        if pattern.search(i):
            cmd = (
                f'adb -s {sn} '
                'shell pm uninstall -k --user 0 '
                f'{i[8:]}'
            )
            subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    main()
