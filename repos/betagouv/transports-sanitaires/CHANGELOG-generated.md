## Changelog : transports-sanitaires (30 derniers jours, au 29 septembre 2026)

### Résumé
Cette période a été marquée par une mise à jour majeure du modèle d'éligibilité (passage à la version 9.7.3) et une refonte profonde du système de génération des formulaires administratifs. Le simulateur est désormais plus précis et cohérent, grâce à une liaison directe entre les règles métier et le remplissage automatique des documents officiels (Cerfa, DAP, PMT), tout en améliorant la lisibilité des exports PDF.

### Évolutions fonctionnelles
- **Mise à jour du modèle** : Intégration de la version 9.7.3 du modèle d'éligibilité ([#3](https://github.com/betagouv/transports-sanitaires/pull/3)).
- **Automatisation des formulaires** : Les tableaux de remplissage des documents (Cerfa, DAP, PMT et S3141) sont désormais pilotés par un mapping documentaire, garantissant que les données saisies correspondent exactement aux exigences des formulaires.
- **Optimisation du Cerfa** : Le texte médical est désormais intégré intégralement dans le formulaire Cerfa, supprimant la nécessité de fournir une annexe séparée ([#12](https://github.com/betagouv/transports-sanitaires/pull/12)).
- **Amélioration de l'expérience utilisateur** :
    - Possibilité de saisir les précisions médicales directement dans l'interface ([#15](https://github.com/betagouv/transports-sanitaires/pull/15)).
    - Déduction automatique de certains lieux pour éviter de poser des questions redondantes ([#11](https://github.com/betagouv/transports-sanitaires/pull/11)).
    - Meilleure lisibilité des adresses dans les documents PDF générés ([#14](https://github.com/betagouv/transports-sanitaires/pull/14)).
- **Corrections de bugs** :
    - Résolution de problèmes de cohérence sur les destinations d'urgence et les retours pénitentiaires ([#4](https://github.com/betagouv/transports-sanitaires/pull/4), [#5](https://github.com/betagouv/transports-sanitaires/pull/5)).
    - Correction des exceptions liées à la radiothérapie et aux établissements (EHPAD/USLD) ([#6](https://github.com/betagouv/transports-sanitaires/pull/6), [#7](https://github.com/betagouv/transports-sanitaires/pull/7), [#8](https://github.com/betagouv/transports-sanitaires/pull/8)).
    - Correction de l'affichage des adresses lors de la navigation arrière dans le simulateur.

### Évolutions techniques
- **Refactorisation de la logique métier** : Optimisation de l'ordre des questions (ex: l'urgence est désormais posée après le trajet) et découplage de certains composants pour une meilleure maintenance ([#17](https://github.com/betagouv/transports-sanitaires/pull/17), [51ed317]).
- **Restructuration du code** : Réorganisation du dossier `secretariat/` en dossiers dédiés pour clarifier l'architecture ([c43aed5]).
- **Sécurité** : Mise à jour de la dépendance `qs` pour corriger des vulnérabilités identifiées ([c30a967]).
- **Analytique** : Stabilisation du suivi des données en figeant le nommage des événements Matomo ([94b23bd]).

### Autres changements
- **Documentation** : Réorganisation complète de la documentation vers une structure de "divulgation progressive" (`docs/knowledge/`) et mise à jour systématique du README pour les nouvelles versions.
- **Tests** : Augmentation significative de la couverture de tests sur les nouveaux champs liés au mapping documentaire et mise à jour des suites de tests (recettes) pour accompagner les versions 9.7.x.
