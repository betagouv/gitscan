## Changelog : mednum-cli (30 derniers jours, au 29 juin 2026)

### Résumé
Cette version apporte des mises à jour importantes des sources de données utilisées par `mednum-cli`. Les zones "ZRR" ont été remplacées par les zones "France Ruralités Revitalisation (FRR)", la source QPV a été migrée vers le jeu de données des quartiers prioritaires ANCT 2024, et une nouvelle source, "francilin", a été ajoutée. Des améliorations de la stabilité et de la publication des données ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de la source de données "francilin" [#357](https://github.com/anct-cartographie-nationale/mednum-cli/issues/357).
- Remplacement des zones "ZRR" par les zones "France Ruralités Revitalisation (FRR)" [#360](https://github.com/anct-cartographie-nationale/mednum-cli/issues/360).
- Migration de la source QPV vers le jeu de données des quartiers prioritaires ANCT 2024 [#359](https://github.com/anct-cartographie-nationale/mednum-cli/issues/359).
- Publication du jeu de données national à partir des données dédupliquées [#354](https://github.com/anct-cartographie-nationale/mednum-cli/issues/354).
- Suppression des ressources DI et renommage en "national" [#355](https://github.com/anct-cartographie-nationale/mednum-cli/issues/355).

### Évolutions techniques
- Amélioration de la stabilité de l'ordre de fusion des doublons internes avec une règle de départage par ID [#358](https://github.com/anct-cartographie-nationale/mednum-cli/issues/358).
- Modification du planning de la publication nocturne pour éviter la congestion des Actions (passage à 22h48 UTC) [#356](https://github.com/anct-cartographie-nationale/mednum-cli/issues/356).
