# MegaV для OpenWrt 25.12+

Фид пакетов apk. Установка на роутере:

    wget -O /etc/apk/keys/megav-feed.pem https://raw.githubusercontent.com/Romaxa55/MegaV_Public/openwrt/megav-feed.pem
    echo "https://raw.githubusercontent.com/Romaxa55/MegaV_Public/openwrt/packages.adb" >> /etc/apk/repositories.d/customfeeds.list
    apk update && apk add luci-app-megav luci-i18n-megav-ru

Обновление: `apk upgrade`. Ветка пишется сборкой MegaV, руками её не менять.
