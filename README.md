# Revers@ndroid
Workshop básico para analisar ransomwares mobile da família Simplocker e Lockerpin

### Overview

Nessa atividade, a ideia é analisar conceitos básicos sobre análise de [APKs](https://pt.wikipedia.org/wiki/APK) e verificar como fazer a engenharia reversa de ransomwares mobile das famílias [Simplocker](http://www.virusradar.com/en/Android_Simplocker/detail) e [Lockerpin](http://www.virusradar.com/en/Android_Lockerpin/detail).

A atividade pode ser seguida através dos [slides](https://github.com/puodzius/ReversAndroid/raw/master/Revers%40ndroid%20(BSides).pptx) (disponíveis também no [SlideShare](https://www.slideshare.net/cpuodzius/reversndroid-bsidessp)). As ferramentas utilizadas na atividade são:

  * [Análise dinâmica] [Droibox](https://github.com/pjlantz/droidbox)
  * [Análise estática] [DEX2JAR](https://github.com/pxb1988/dex2jar)/[JD-GUI](https://github.com/java-decompiler/jd-gui)

Como ambiente de análise foi escolhida a distribuição Linux [Santoku](https://santoku-linux.com/). Nessa distribuição as ferramentas utilizadas para análise estática já estão disponíveis por padrão, enquanto o Droidbox não está presente.

No entanto, o Droidbox é de fácil instalação e os passos estão bem detalhados no GitHub do projeto.

> **Droidbox**: Atenção ao configurar [AVD](https://developer.android.com/studio/run/managing-avds.html?hl=pt-br)!
>
> O AVD deve ter as seguintes características:
>
>   * Android 4.1.2 (API Level 16)
>   * Nexus 4
>   * CPU: ARM

Veja mais no [post](https://www.welivesecurity.com/br/2017/05/26/engenharia-reversa-bsides/) que escrive no WeLiveSecurity.

### Download

Apliance virtual da atividade: VirtualBox ([torrent](http://mgnet.me/cuTF1CW))

---
Twitter: [@cpuodzius](https://twitter.com/cpuodzius)

[Veja mais](https://goo.gl/v8visd) sobre a atividade
