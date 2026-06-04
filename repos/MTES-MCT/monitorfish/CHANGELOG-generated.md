## Changelog : monitorfish (30 derniers jours, au 3 juin 2026)

### Résumé
Ce mois-ci, monitorfish a bénéficié d'améliorations significatives en termes de gestion des préavis, de suivi des navires (notamment avec l'intégration de données AIS), et de correction de bugs impactant l'expérience utilisateur. Des optimisations techniques ont également été apportées à l'infrastructure et aux tests.

### Évolutions fonctionnelles
- **Préavis :**
    - Ajout de la mention "zéro" dans les notifications (mails, PDF, SMS) pour les préavis nuls [#4981].
    - Affichage de la raison pour laquelle un préavis est "à vérifier" (note, signalement, port état tiers) [#5108].
    - Invalidation automatique des préavis zéro BFT ou SWO créés il y a plus de 24 heures [#5069].
- **Signalements :**
    - Possibilité pour le pôle INN de mettre à jour facilement les signalements dans Navpro [#5113].
    - Rendre obligatoire la date de fin des signalements et proposer des options de fin [#5079].
- **Unités :**
    - Ajout d'une recherche par "type" et "base" lors de la création d'un nouveau moyen [#5110].
- **Suivi des navires :**
    - Intégration et affichage des données AIS (Automatic Identification System) sur la carte, permettant de visualiser les navires et leurs positions [#5090].
    - Ajout de filtres pour les navires absents dans les rapports INN [#5113].
- **Gestion des infractions :**
    - Ajout du NATINF 4789 [#5149].
    - Ajout du type de moyen des unités de contrôles [#5145].

### Évolutions techniques
- **Infrastructure :**
    - Mise à jour de TimescaleDB et PostGIS [#5096].
    - Amélioration du workflow de déploiement de la base de données.
    - Ajout de variables d'environnement manquantes pour Kafka et la génération du certificat .p12 [#5118, #5123, #5115].
- **Tests :**
    - Correction de tests flaky et ajout de nouveaux tests Cypress pour améliorer la couverture et la fiabilité [#5148, #5105].
    - Amélioration des tests backend.
- **AIS :**
    - Ajout de la gestion des positions AIS dans la base de données et l'API.
    - Correction de la lecture des coordonnées WKT pour l'AIS [#5125].
- **CI/CD :**
    - Modification du workflow CI/CD pour Sentry [#afbcc864].

### Autres changements
- Ajout d'un README pour la génération du certificat .p12 [#5123].
- Correction d'un bug dans le flow des catégories d'infractions [#5082].
- Correction de la hauteur d'un élément de l'interface utilisateur.
- Mise en avant de l'environnement d'intégration avec une bannière [#5024].
- Correction de typos et améliorations de la lisibilité du code.
- Suppression de configurations inutilisées.
- Amélioration de la gestion des erreurs lors de l'upload de fichiers.
- Correction de problèmes liés à l'affichage des champs de coordonnées.
- Ajout de la mention "Préavis zéro" dans l'objet des mails [#5060].
