## Changelog : livekit-sip (30 derniers jours, au 12 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées au pont SIP vers WebRTC pour LiveKit. Les récentes mises à jour se concentrent sur l'amélioration de la stabilité des appels, la gestion des erreurs SIP, le support de codecs audio supplémentaires et des optimisations de la configuration réseau. Ces changements visent à offrir une meilleure expérience aux utilisateurs finaux et aux intégrateurs du système.

### Évolutions fonctionnelles
- Support du codec audio AMR-WB, offrant une meilleure qualité audio pour les appels (optionnel) [#693](https://github.com/suitenumerique/livekit-sip/issues/693).
- Amélioration de la catégorisation des erreurs d'appel sortantes, facilitant le diagnostic des problèmes de connectivité [#692](https://github.com/suitenumerique/livekit-sip/issues/692).
- Gestion améliorée des erreurs de limite de CPS (Call Processing System), traitées comme des erreurs client [#703](https://github.com/suitenumerique/livekit-sip/issues/703).
- Correction d'un problème de symétrie RTP, améliorant la qualité et la stabilité des flux audio [#706](https://github.com/suitenumerique/livekit-sip/issues/706).
- Mise à jour du SDK média pour corriger des problèmes avec le codec AMR-WB [#704](https://github.com/suitenumerique/livekit-sip/issues/704).
- Possibilité de personnaliser le realm d'authentification pour les appels entrants [#688](https://github.com/suitenumerique/livekit-sip/issues/688).
- Amélioration de la gestion des timeouts média pour une meilleure fiabilité [#683](https://github.com/suitenumerique/livekit-sip/issues/683).

### Évolutions techniques
- Ajout d'une RPC pour obtenir les headers distants des participants, permettant une meilleure flexibilité et contrôle [#699](https://github.com/suitenumerique/livekit-sip/issues/699).
- Mise à jour du SDK LiveKit pour activer TURN, améliorant la connectivité dans des environnements réseau complexes [#707](https://github.com/suitenumerique/livekit-sip/issues/707).
- Correction de la catégorisation des erreurs SIP pour une meilleure identification des causes de problèmes [#690](https://github.com/suitenumerique/livekit-sip/issues/690).
- Amélioration de la catégorisation de la complétion des appels lors de la déconnexion de la salle [#691](https://github.com/suitenumerique/livekit-sip/issues/691).
- Mise en cache des appels échoués et tentative de réponse aux appels réessayés [#694](https://github.com/suitenumerique/livekit-sip/issues/694).
- Suppression du cache inutile du workflow "Release to Docker" [#681](https://github.com/suitenumerique/livekit-sip/issues/681).
- Désactivation de TURN pour LiveKit RTC [#689](https://github.com/suitenumerique/livekit-sip/issues/689).
- Autorisation à ignorer l'IP locale dans le SDP et activation du mode symétrique [#687](https://github.com/suitenumerique/livekit-sip/issues/687).
- Correction d'une condition de concurrence dans l'accès à `CallInfo` [#709](https://github.com/suitenumerique/livekit-sip/issues/709).

### Autres changements
- Mise à jour des dépendances protocol/psrpc et suppression du package pkg/errors [#708](https://github.com/suitenumerique/livekit-sip/issues/708).
- Limitation du nombre d'impressions des changements de source et de destination [#705](https://github.com/suitenumerique/livekit-sip/issues/705).
