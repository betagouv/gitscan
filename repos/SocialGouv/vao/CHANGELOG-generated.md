## Changelog : vao (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives au parcours d'agrément des Directeurs Régionaux des Entreprises, des Établissements, du Travail et des Solidarités (DREETS), notamment pour le premier agrément. De nombreuses corrections d'accessibilité (RGAA) ont été implémentées sur l'ensemble de l'application. Des optimisations de performance ont également été réalisées sur les requêtes en base de données.

### Évolutions fonctionnelles
- **Agrément DREETS :** Ajout complet du support du premier agrément DREETS, incluant les étapes de demande de compléments, de confirmation de complétude, de refus et d'acceptation.  Les pages "bienvenue", "demande de compléments" et de confirmation ont été implémentées. [#1471, #1492, #1493, #1495, #1497, #1498]
- **Back-office :** Prise en charge du premier agrément DREETS dans le back-office. [#1487]
- **Documents :** Amélioration de l'onglet "Documents" dans "Mon agrément". [#1490]
- **RGAA :** Améliorations de l'accessibilité (RGAA) sur plusieurs pages : création de compte, page de login, étapes de renouvellement, page mot de passe oublié. [#1440, #1474, #1477, #1478, #1488]
- **Workflow d'agrément :** Mise à jour du wording des emails liés au workflow d'agrément. [#1423]

### Évolutions techniques
- **Performance :** Optimisation des requêtes en base de données grâce à l'ajout d'index, corrigeant des problèmes de timeout en production. [#1489]
- **CI/CD :** Migration de la construction des images Docker de buildkit-service vers buildkit-operator. [#1464]
- **Schéma de route DS :** Ajout d'un contrôle du schéma de route DS. [#1458]

### Autres changements
- Correction d'un bug d'affichage de la date dans les messages internes. [#1460]
- Publication de la version 1.28.1 en pré-production. [#1462]
- Amélioration du wording de certaines pages pour une meilleure clarté. [#1475, #1479]
- Ajout de la prise en charge RGAA pour la hiérarchie des vacanciers. [#1486]
- Ajout du fusager pour le suivi de mon agrément. [#1473]
- Ajout du fusager pour le reliquat du stepper. [#1470]
- Ajout du fusager pour le DF hébergement RGAA. [#1476]
