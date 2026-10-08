## Changelog : envergo (30 derniers jours, au 06/10/2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'expérience de simulation (V2) et une modernisation profonde de la gestion des Démarches Numériques (DN). Les capacités de gestion des données de biodiversité ont été enrichies, notamment par une meilleure catégorisation des espèces, tandis que l'interface utilisateur a été affinée pour améliorer la clarté des informations et la navigation.

### Évolutions fonctionnelles
- **Nouvelle expérience de simulation (V2) :** Déploiement de nouveaux parcours de simulation, incluant de nouvelles pages d'affichage et de gestion des alternatives ([#1236](https://github.com/MTES-MCT/envergo/issues/1236), [#1254](https://github.com/MTES-MCT/envergo/issues/1254), [#1255](https://github.com/MTES-MCT/envergo/issues/1255)).
- **Gestion des Démarches Numériques (DN) :** Amélioration du suivi avec l'envoi automatique de récépissés lors de la soumission ou du redémarrage d'une instruction ([#1292](https://github.com/MTES-MCT/envergo/issues/1292)).
- **Biodiversité et Espèces :** Possibilité de multi-catégoriser les espèces (Natura 2000, sites protégés, etc.) et amélioration de la présentation des tableaux d'espèces.
- **Interface et Ergonomie :**
    - Ajout d'un bloc d'alerte d'urgence sur la page d'accueil ([#1322](https://github.com/MTES-MCT/envergo/issues/1322)).
    - Mise à jour globale des libellés (Urbanisme, Haies, etc.) pour plus de clarté et de précision.
    - Amélioration de la recherche de projets et de la gestion des contacts.
    - Correction de bugs d'affichage (écrans blancs sur anciens navigateurs, problèmes de recherche).
- **Cartographie :** Ajout de nouvelles cartes dans les paramètres départementaux et correction de problèmes d'affichage des cartes de haies ([#1315](https://github.com/MTES-MCT/envergo/issues/1315)).

### Évolutions techniques
- **Architecture :** Refactorisation majeure de la logique "Démarche Numérique" dans un module dédié pour une meilleure maintenabilité ([#1317](https://github.com/MTES-MCT/envergo/issues/1317)).
- **Stockage et Infrastructure :**
    - Mise en place d'un nouveau système de stockage via S3 pour la gestion sécurisée des fichiers privés ([#1261](https://github.com/MTES-MCT/envergo/issues/1261)).
    - Optimisation de la configuration Nginx pour le proxy de fichiers.
- **Performances :** Optimisation des calculs de densité et des requêtes de base de données pour les zones HRU/RU ([#1267](https://github.com/MTES-MCT/envergo/issues/1267), [#1238](https://github.com/MTES-MCT/envergo/issues/1238)).
- **Base de données :** Migrations importantes pour supporter le nouveau modèle d'objets DN et la catégorisation complexe des espèces.

### Autres changements
- **Documentation :** Mise à jour du README (mention de l'anonymisation et de la stack technique) et de la documentation de collaboration.
- **Qualité du code :** Nettoyage des commentaires, corrections de linting et amélioration de la suite de tests automatisés.
