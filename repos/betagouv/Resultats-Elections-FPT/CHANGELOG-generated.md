## Changelog : Resultats-Elections-FPT (30 derniers jours, au 06/08/2026)

### Résumé
Ce mois-ci, le projet a connu une modernisation importante avec la migration de composants clés vers Vue 3 et l'ajout de nouveaux modes de consultation, notamment une vue de recherche et une vue pour intégration en iframe. L'expérience utilisateur a été simplifiée pour la création de scrutins et l'accessibilité a été renforcée, tout en stabilisant la gestion des données cartographiques.

### Évolutions fonctionnelles
- **Nouvelles interfaces de consultation** : création d'une nouvelle vue dédiée à la recherche [#66](https://github.com/betagouv/Resultats-Elections-FPT/pull/66) et d'une vue optimisée pour l'intégration en iframe [#67](https://github.com/betagouv/Resultats-Elections-FPT/pull/67).
- **Simplification du parcours utilisateur** : l'interface de création de scrutin a été épurée pour se concentrer uniquement sur les étapes de création [#68](https://github.com/betagouv/Resultats-Elections-FPT/pull/68).
- **Corrections et accessibilité** :
    - Amélioration de l'accessibilité de la barre de recherche dans la cartographie des scrutins [#64](https://github.com/betagouv/Resultats-Elections-FPT/pull/64).
    - Correction de l'affichage des scrutins organisés lors des phases de création et de rattachement (notamment pour les CAP) [#62](https://github.com/betagouv/Resultats-Elections-FPT/pull/62) [#63](https://github.com/betagouv/Resultats-Elections-FPT/pull/63).
    - Diverses améliorations de l'interface utilisateur [#69](https://github.com/betagouv/Resultats-Elections-FPT/pull/69).

### Évolutions techniques
- **Modernisation technologique** : migration de l'ancienne vue de cartographie des scrutins vers une architecture Vue 3 [#73](https://github.com/betagouv/Resultats-Elections-FPT/pull/73).
- **Optimisation de la gestion des données** :
    - Amélioration de la robustesse des formules d'initialisation pour accepter des chaînes de caractères [#74](https://github.com/betagouv/Resultats-Elections-FPT/pull/74).
    - Automatisation de la sauvegarde des informations de table dans les options de vue [#65](https://github.com/betagouv/Resultats-Elections-FPT/pull/65).
    - Mise à jour de la logique de cartographie suite à une modification de la structure des données (suppression de colonne) [#61](https://github.com/betagouv/Resultats-Elections-FPT/pull/61).

### Autres changements
- **Nettoyage du code** : suppression de segments de code inutilisés pour alléger le projet [#71](https://github.com/betagouv/Resultats-Elections-FPT/pull/71).
