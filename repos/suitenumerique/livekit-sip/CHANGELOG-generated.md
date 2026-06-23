## Changelog : livekit-sip (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité et la compatibilité du pont SIP vers WebRTC. Des corrections ont été apportées pour améliorer la gestion des erreurs, la qualité audio et la gestion des appels, notamment en ajoutant la prise en charge de codecs audio supplémentaires et en optimisant la gestion des ports RTP. Des améliorations internes ont également été réalisées pour une meilleure gestion de l'état et des dépendances.

### Évolutions fonctionnelles
- Ajout de la prise en charge des codecs audio PCMU et PCMA pour une meilleure compatibilité avec les équipements SIP existants. [#700](https://github.com/suitenumerique/livekit-sip/issues/700)
- Amélioration de la gestion des erreurs lors des transferts d'appels, avec une meilleure propagation des erreurs aux instances en attente. [#723](https://github.com/suitenumerique/livekit-sip/issues/723)
- Correction d'un problème de symétrie RTP pour une meilleure qualité audio. [#706](https://github.com/suitenumerique/livekit-sip/issues/706)
- Ajout d'une fonctionnalité permettant de récupérer les en-têtes distants des participants via RPC. [#699](https://github.com/suitenumerique/livekit-sip/issues/699)
- Activation de TURN pour LiveKit RTC, améliorant la connectivité dans des environnements réseau complexes. [#707](https://github.com/suitenumerique/livekit-sip/issues/707)

### Évolutions techniques
- Refactorisation de la gestion de l'état SIP, en utilisant un `StateHandler` public pour une meilleure organisation et maintenabilité. [#714](https://github.com/suitenumerique/livekit-sip/issues/714)
- Catégorisation plus précise des erreurs de temporisation des transactions B pour les appels sortants. [#718](https://github.com/suitenumerique/livekit-sip/issues/718)
- Séparation des états "indéterminé" et "erreur de serveur" pour une meilleure identification des problèmes. [#719](https://github.com/suitenumerique/livekit-sip/issues/719)
- Utilisation de noms de codecs corrects et mise à jour des dépendances. [#713](https://github.com/suitenumerique/livekit-sip/issues/713)
- Clonage de `CallInfo` pour éviter les accès concurrents et améliorer la sécurité. [#709](https://github.com/suitenumerique/livekit-sip/issues/709)
- Mise à jour de la bibliothèque `protocol/psrpc` et suppression du package `pkg/errors`. [#708](https://github.com/suitenumerique/livekit-sip/issues/708)
- Correction de l'utilisation des ports RTP, en utilisant des ports pairs. [#711](https://github.com/suitenumerique/livekit-sip/issues/711)
- Traitement des erreurs de limite de CPS comme des erreurs client. [#703](https://github.com/suitenumerique/livekit-sip/issues/703)

### Autres changements
- Suppression des logs de débogage WebRTC pour réduire le bruit dans les logs. [#715](https://github.com/suitenumerique/livekit-sip/issues/715)
- Limitation du taux d'impression des changements de source et de destination pour éviter le spam de logs. [#705](https://github.com/suitenumerique/livekit-sip/issues/705)
- Mise à jour de la bibliothèque `media-sdk` pour corriger des problèmes avec le codec AMR-WB. [#721](https://github.com/suitenumerique/livekit-sip/issues/721) et [#704](https://github.com/suitenumerique/livekit-sip/issues/704)
