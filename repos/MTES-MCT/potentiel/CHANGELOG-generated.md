## Changelog : potentiel (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, l'équipe a déployé des améliorations significatives sur la gestion des documents, les rôles utilisateurs et l'importation de données, notamment depuis le DN (Données Nationales). Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant les notifications et les garanties financières. Plusieurs optimisations ont été réalisées pour améliorer la performance et la maintenance du code.

### Évolutions fonctionnelles
- **Gestion des documents :**
    - Correction d'un bug empêchant la suppression correcte des raccordements abandonnés [#4187](https://github.com/MTES-MCT/potentiel/issues/4187).
    - Amélioration de l'importation des références de raccordement depuis le DN [#4103](https://github.com/MTES-MCT/potentiel/issues/4103).
    - Correction d'un problème d'importation de la date d'échéance GF depuis le DN [#4197](https://github.com/MTES-MCT/potentiel/issues/4197), [#4162](https://github.com/MTES-MCT/potentiel/issues/4162).
    - Correction d'un bug lié au téléchargement de documents [#4154](https://github.com/MTES-MCT/potentiel/issues/4154).
    - Correction d'un problème avec la modification des DCR (Dépôt de Conformité Règlementaire) [#4171](https://github.com/MTES-MCT/potentiel/issues/4171).
- **Rôles et permissions :**
    - Ajout d'un nouveau rôle "admin" (anciennement DGEc) [#4183](https://github.com/MTES-MCT/potentiel/issues/4183).
    - Ajout d'une permission spécifique pour exporter les dossiers de raccordement [#4169](https://github.com/MTES-MCT/potentiel/issues/4169).
    - Les DREALS peuvent maintenant copier l'ID projet en production [#4151](https://github.com/MTES-MCT/potentiel/issues/4151).
- **Garanties financières :**
    - Refonte des pages "Garanties financières" pour une meilleure expérience utilisateur [#4175](https://github.com/MTES-MCT/potentiel/issues/4175).
- **Attestations :**
    - Modification et amélioration de l'attestation de conformité [#4159](https://github.com/MTES-MCT/potentiel/issues/4159), [#4102](https://github.com/MTES-MCT/potentiel/issues/4102).
- **Notifications :**
    - Correction d'un bug concernant l'envoi de notifications aux GRD (Gestionnaires de Réseau de Distribution) [#4180](https://github.com/MTES-MCT/potentiel/issues/4180).
    - Suppression des notifications d'étapes de projet en cas de recours [#4179](https://github.com/MTES-MCT/potentiel/issues/4179).
    - Correction d'un bug d'envoi de notifications pour les cocontractants hors de leur zone [#4178](https://github.com/MTES-MCT/potentiel/issues/4178).
- **Autres améliorations UI/UX :**
    - Ajout de liens ARIA pour l'accessibilité sur les listes de réclamations, documents et utilisateurs [#4186](https://github.com/MTES-MCT/potentiel/issues/4186).
    - Amélioration de l'intégration des valeurs par défaut pour le coefficient K [#4160](https://github.com/MTES-MCT/potentiel/issues/4160).

### Évolutions techniques
- **Infrastructure :**
    - Ajout de la variable d'environnement `AWS_REGION` pour le schéma S3 de la partie CLI [#4188](https://github.com/MTES-MCT/potentiel/issues/4188).
- **Données :**
    - Ajout du champ "Région" manquant dans les données exportées vers data.gouv [#4153](https://github.com/MTES-MCT/potentiel/issues/4153).
    - Mise à jour des données de test [#4181](https://github.com/MTES-MCT/potentiel/issues/4181).
- **Code :**
    - Simplification de la modélisation des Autorisations d'Opérer (AO) [#4114](https://github.com/MTES-MCT/potentiel/issues/4114).
    - Refactorisation du code pour la gestion des domaines et des champs supplémentaires [#4147](https://github.com/MTES-MCT/potentiel/issues/4147).
    - Amélioration de la gestion des types dans le fichier `tsconfig` [#4166](https://github.com/MTES-MCT/potentiel/issues/4166).
    - Suppression de projections GF en attente et d'archives obsolètes [#4150](https://github.com/MTES-MCT/potentiel/issues/4150).
    - Intégration des dernières modifications des versions 3.76 et 3.77 [#4199](https://github.com/MTES-MCT/potentiel/issues/4199), [#4177](https://github.com/MTES-MCT/potentiel/issues/4177), [#4170](https://github.com/MTES-MCT/potentiel/issues/4170), [#4155](https://github.com/MTES-MCT/potentiel/issues/4155).

### Autres changements
- Mise à jour de la documentation.
- Corrections de typos et améliorations de la lisibilité du code.
- Mise à jour des dépendances (dompurify, basic-ftp) via Dependabot.
