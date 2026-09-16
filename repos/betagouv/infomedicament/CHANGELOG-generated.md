## Changelog : infomedicament (30 derniers jours, au 15 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'enrichissement de l'information médicale et l'amélioration de l'expérience utilisateur. Le service propose désormais des informations de stock détaillées, l'intégration de vidéos sur les pages de spécialités et un affichage plus direct des notices. Parallèlement, la robustesse technique a été renforcée par la mise en place de nouveaux tests et une optimisation des mécanismes de recherche.

### Évolutions fonctionnelles
- **Enrichissement du contenu** :
    - Gestion et affichage des informations de stock pour les spécialités.
    - Ajout de vidéos sur les pages de spécialités.
    - Rendu direct des notices et des RCP au format HTML [#290](https://github.com/betagouv/infomedicament/issues/290).
- **Améliorations de l'interface (UI)** :
    - Correction de l'affichage des icônes dans le menu mobile [#305](https://github.com/betagouv/infomedicament/issues/305).
    - Ajustements du sous-menu et des indications dans l'en-tête [#298](https://github.com/betagouv/infomedicament/issues/298).
    - Amélioration visuelle des blocs de stock (ajout de bordures).
    - Optimisation de l'affichage des lignes CIP (agrégation intelligente selon les dates et statuts).
- **Qualité des données** :
    - Nettoyage des données relatives à la pédiatrie.

### Évolutions techniques
- **Optimisation des performances et de la recherche** :
    - Refonte de l'autocomplétion avec la création d'un endpoint et d'une logique dédiés [#279](https://github.com/betagouv/infomedicament/issues/279).
- **Qualité logicielle et tests** :
    - Initialisation des tests de bout en bout (E2E) [#281](https://github.com/betagouv/infomedicament/issues/281).
    - Ajout de tests pour les codes CIS.
- **Infrastructure et maintenance** :
    - Amélioration du proxy [#301](https://github.com/betagouv/infomedicament/issues/301).
    - Ajout de scripts de restauration [#299](https://github.com/betagouv/infomedicament/issues/299) et d'un système de journalisation (logger) [#292](https://github.com/betagouv/infomedicament/issues/292).
    - Nettoyage de la base de données via la suppression de tables de contenu inutilisées [#297](https://github.com/betagouv/infomedicament/issues/297).
    - Correction de la gestion des valeurs nulles pour les stocks.
