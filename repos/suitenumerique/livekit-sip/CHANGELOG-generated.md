## Changelog : livekit-sip (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au pont SIP vers WebRTC pour LiveKit. Les récentes mises à jour se concentrent sur l'amélioration de la stabilité, du diagnostic et des performances, notamment en gérant mieux les paquets RTP, en ajoutant des logs plus détaillés et en optimisant le traitement des requêtes SIP.

### Évolutions fonctionnelles
- Amélioration de la gestion des appels entrants avec des ajustements au traitement des messages INVITE [#589](https://github.com/suitenumerique/livekit-sip/pull/589).
- Ajout du support pour les trames UDP jumbo, permettant potentiellement d'améliorer le débit et de réduire la latence dans certaines configurations réseau [#527](https://github.com/suitenumerique/livekit-sip/pull/527).

### Évolutions techniques
- Collecte de statistiques sur le buffer de gigue (jitter buffer) pour aider au diagnostic des problèmes de qualité audio [#596](https://github.com/suitenumerique/livekit-sip/pull/596).
- Correction d'une erreur dans la mise à jour des statistiques `packets_input` après un traitement RTP réussi [#591](https://github.com/suitenumerique/livekit-sip/pull/591).
- Mise en cache des identifiants attribués avant le dialogue pour optimiser le traitement des requêtes SIP [#590](https://github.com/suitenumerique/livekit-sip/pull/590).
- Modification du code d'erreur `psrpc.Canceled` en `psrpc.DeadlineExceeded` pour une meilleure conformité et clarté [#581](https://github.com/suitenumerique/livekit-sip/pull/581).
- Gestion améliorée des paquets RTP entrants, avec un rejet des paquets avant le démarrage de la boucle RTP pour éviter les pertes et les erreurs [#576](https://github.com/suitenumerique/livekit-sip/pull/576).
- Ajout de logs plus détaillés pour les erreurs de terminaison et le signal SIP [#569](https://github.com/suitenumerique/livekit-sip/pull/569) et [#558](https://github.com/suitenumerique/livekit-sip/pull/558).
- Correction d'un log excessif pour les paquets RTP plus grands que la MTU [#586](https://github.com/suitenumerique/livekit-sip/pull/586).

### Autres changements
- Amélioration des tests E2E, notamment en déplaçant les tests de sonnerie et en permettant une configuration plus flexible des participants SIP [#587](https://github.com/suitenumerique/livekit-sip/pull/587) et [#584](https://github.com/suitenumerique/livekit-sip/pull/584).
