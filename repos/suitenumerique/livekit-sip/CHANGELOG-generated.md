## Changelog : livekit-sip (30 derniers jours, au 26 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées au pont SIP vers WebRTC pour LiveKit au cours du dernier mois. Les mises à jour se concentrent sur l'amélioration de la stabilité des appels, l'ajout de support pour de nouveaux codecs audio, et l'optimisation de la gestion des erreurs et des transactions SIP. Des améliorations techniques ont également été apportées à l'architecture interne pour une meilleure maintenabilité et performance.

### Évolutions fonctionnelles
- **Support de codecs audio supplémentaires:** Ajout du support des codecs PCMU et PCMA pour une meilleure compatibilité avec les équipements téléphoniques existants. [#700](https://github.com/suitenumerique/livekit-sip/issues/700)
- **Amélioration de la gestion des erreurs:**  Les erreurs liées aux limites de CPS (Calls Per Second) sont maintenant traitées comme des erreurs client, améliorant la robustesse du système. [#703](https://github.com/suitenumerique/livekit-sip/issues/703)
- **Correction de la symétrie RTP:** Correction d'un problème de symétrie RTP pour une meilleure qualité audio. [#706](https://github.com/suitenumerique/livekit-sip/issues/706)
- **Activation de TURN pour LiveKit RTC:** Activation de TURN pour LiveKit RTC, améliorant la connectivité dans des environnements réseau complexes. [#707](https://github.com/suitenumerique/livekit-sip/issues/707)

### Évolutions techniques
- **Refactoring de la gestion de l'état SIP:** La gestion de l'état SIP a été refactorisée pour utiliser un `StateHandler` public, améliorant la modularité et la testabilité du code. [#714](https://github.com/suitenumerique/livekit-sip/issues/714)
- **Gestion améliorée des erreurs de transaction SIP:** Catégorisation et gestion améliorée des erreurs de transaction SIP, notamment les timeouts de type B pour les appels sortants. [#718](https://github.com/suitenumerique/livekit-sip/issues/718) et [#719](https://github.com/suitenumerique/livekit-sip/issues/719)
- **Gestion des erreurs de transfert d'appel:** Ajout d'une gestion des erreurs de type "fan-out" pour toutes les instances en attente de transfert d'appel. [#723](https://github.com/suitenumerique/livekit-sip/issues/723)
- **Correction des noms de codecs:** Correction de l'utilisation des noms de codecs pour assurer la compatibilité. [#713](https://github.com/suitenumerique/livekit-sip/issues/713)
- **Utilisation de ports RTP pairs:** Utilisation de ports RTP pairs pour une meilleure gestion des flux média. [#711](https://github.com/suitenumerique/livekit-sip/issues/711)
- **Mise à jour de la librairie `media-sdk`:** Correction de bugs liés à AMR-WB dans la librairie `media-sdk`. [#721](https://github.com/suitenumerique/livekit-sip/issues/721)
- **Suppression de dépendances obsolètes:** Suppression du package `pkg/errors` et mise à jour de `protocol/psrpc`. [#708](https://github.com/suitenumerique/livekit-sip/issues/708)
- **Prévention des accès concurrents:** Clonage de `CallInfo` pour éviter les accès concurrents et améliorer la sécurité des threads. [#709](https://github.com/suitenumerique/livekit-sip/issues/709)

### Autres changements
- Suppression des logs de débogage WebRTC pour réduire le bruit dans les logs. [#715](https://github.com/suitenumerique/livekit-sip/issues/715)
