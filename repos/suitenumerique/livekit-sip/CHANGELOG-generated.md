## Changelog : livekit-sip (30 derniers jours, au 26 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées à livekit-sip au cours du dernier mois. Les mises à jour se concentrent sur l'amélioration de la stabilité des appels, l'ajout de support pour de nouveaux codecs audio, et des corrections de bugs liés à la gestion des erreurs et des transactions SIP. Des optimisations internes ont également été réalisées pour améliorer la robustesse du système.

### Évolutions fonctionnelles
- **Support de codecs audio supplémentaires :** Ajout du support des codecs PCMU et PCMA pour une meilleure compatibilité avec les équipements téléphoniques existants. [#700](https://github.com/suitenumerique/livekit-sip/issues/700)
- **Amélioration de la gestion des erreurs :**  Catégorisation plus précise des erreurs lors des appels, notamment la distinction entre erreurs serveur, erreurs client et problèmes de temporisation. [#718](https://github.com/suitenumerique/livekit-sip/issues/718), [#719](https://github.com/suitenumerique/livekit-sip/issues/719)
- **Activation de TURN pour LiveKit RTC :** Permet d'améliorer la connectivité et la qualité des appels dans des environnements réseau complexes. [#707](https://github.com/suitenumerique/livekit-sip/issues/707)
- **Correction du problème de symétrie RTP :** Résolution d'un problème affectant la transmission RTP. [#706](https://github.com/suitenumerique/livekit-sip/issues/706)

### Évolutions techniques
- **Refactoring de la gestion de l'état SIP :** Introduction d'un `StateHandler` public pour une meilleure organisation et maintenabilité du code. [#714](https://github.com/suitenumerique/livekit-sip/issues/714)
- **Mise à jour de la librairie media-sdk :** Correction de bugs et améliorations de la gestion des codecs AMR-WB. [#721](https://github.com/suitenumerique/livekit-sip/issues/721), [#704](https://github.com/suitenumerique/livekit-sip/issues/704)
- **Gestion des erreurs de dépassement de limite CPS :** Traitement des erreurs de limite de CPS comme des erreurs client pour une meilleure gestion des appels. [#703](https://github.com/suitenumerique/livekit-sip/issues/703)
- **Correction de l'utilisation des noms de codecs :** Amélioration de la cohérence et de la précision dans l'utilisation des noms de codecs. [#713](https://github.com/suitenumerique/livekit-sip/issues/713)
- **Mise à jour des dépendances :**  Mise à jour de `protocol/psrpc` et suppression de `pkg/errors`. [#708](https://github.com/suitenumerique/livekit-sip/issues/708)
- **Prévention des accès concurrents :** Clonage de `CallInfo` pour éviter les problèmes d'accès concurrents. [#709](https://github.com/suitenumerique/livekit-sip/issues/709)

### Autres changements
- **Gestion des logs :** Suppression des logs de débogage WebRTC pour réduire le bruit et améliorer la lisibilité des logs. [#715](https://github.com/suitenumerique/livekit-sip/issues/715)
- **Amélioration de la gestion des ports RTP :** Utilisation de ports RTP pairs pour une meilleure compatibilité. [#711](https://github.com/suitenumerique/livekit-sip/issues/711)
- **Limitation du taux d'impression des changements de source et destination :** Réduction du nombre d'impressions pour améliorer les performances. [#705](https://github.com/suitenumerique/livekit-sip/issues/705)
- **Gestion des erreurs de transfert :** Ajout d'une gestion des erreurs pour les instances en attente de transfert. [#723](https://github.com/suitenumerique/livekit-sip/issues/723)
