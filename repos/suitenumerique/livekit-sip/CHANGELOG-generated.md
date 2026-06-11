## Changelog : livekit-sip (30 derniers jours, au 10 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées au pont SIP vers WebRTC pour LiveKit au cours du dernier mois. Les mises à jour se concentrent sur l'amélioration de la stabilité des appels, la correction de problèmes liés à la gestion des médias (codec AMR-WB, TURN, RTP symétrique), l'amélioration de la catégorisation des erreurs SIP et l'ajout de configurations avancées (ALPN, realm d'authentification).

### Évolutions fonctionnelles
- Ajout du support du codec AMR-WB, offrant une meilleure qualité audio pour les appels (optionnel) [#693](https://github.com/suitenumerique/livekit-sip/issues/693).
- Amélioration de la gestion des erreurs d'appels sortants, avec une meilleure catégorisation des échecs d'invitation, notamment en cas de déconnexion de la salle [#692](https://github.com/suitenumerique/livekit-sip/issues/692), [#691](https://github.com/suitenumerique/livekit-sip/issues/691), [#690](https://github.com/suitenumerique/livekit-sip/issues/690), [#703](https://github.com/suitenumerique/livekit-sip/issues/703).
- Correction d'un problème de RTP symétrique, améliorant la compatibilité avec certains équipements SIP [#706](https://github.com/suitenumerique/livekit-sip/issues/706).
- Ajout d'un mécanisme de cache pour les appels ayant échoué, permettant de réessayer plus efficacement [#694](https://github.com/suitenumerique/livekit-sip/issues/694).
- Possibilité de configurer le realm d'authentification pour les appels entrants [#688](https://github.com/suitenumerique/livekit-sip/issues/688).
- Possibilité de configurer les protocoles ALPN pour TLS [#686](https://github.com/suitenumerique/livekit-sip/issues/686).

### Évolutions techniques
- Mise à jour de la librairie media SDK pour corriger des problèmes avec le codec AMR-WB [#704](https://github.com/suitenumerique/livekit-sip/issues/704), [#695](https://github.com/suitenumerique/livekit-sip/issues/695).
- Activation de TURN pour LiveKit RTC, améliorant la connectivité dans des environnements réseau complexes [#707](https://github.com/suitenumerique/livekit-sip/issues/707).
- Désactivation de TURN pour LiveKit RTC, permettant une configuration plus fine en fonction des besoins [#689](https://github.com/suitenumerique/livekit-sip/issues/689).
- Correction d'une condition de course (race condition) lors de l'annulation d'appels, améliorant la stabilité des tests [#684](https://github.com/suitenumerique/livekit-sip/issues/684).
- Amélioration de la gestion du timeout média, avec une configuration par appel [#673](https://github.com/suitenumerique/livekit-sip/issues/673), [#683](https://github.com/suitenumerique/livekit-sip/issues/683).
- Consolidation des logs liés aux tracks, facilitant le débogage [#677](https://github.com/suitenumerique/livekit-sip/issues/677).
- Correction de la catégorisation des erreurs SIP [#687](https://github.com/suitenumerique/livekit-sip/issues/687).
- Clonage de `CallInfo` pour éviter les accès concurrents [#709](https://github.com/suitenumerique/livekit-sip/issues/709).
- Suppression du cache inutile dans le workflow "Release to Docker" [#681](https://github.com/suitenumerique/livekit-sip/issues/681).

### Autres changements
- Mise à jour de la dépendance `protocol/psrpc` et suppression du package `pkg/errors` [#708](https://github.com/suitenumerique/livekit-sip/issues/708).
- Limitation du nombre d'impressions des changements de source et de destination dans les logs [#705](https://github.com/suitenumerique/livekit-sip/issues/705).
