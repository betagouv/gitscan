## Changelog : envergo (30 derniers jours, au 22 septembre 2026)

### Résumé
Ce mois-ci, envergo franchit une étape majeure avec le déploiement de la version 2 de l'outil de simulation, offrant une interface nettement améliorée pour visualiser les résultats et explorer des parcours alternatifs. Le projet a également renforcé la précision de ses données réglementaires (notamment sur les périodes d'interdiction et la gestion des haies) tout en consolidant la sécurité et la gestion du stockage des fichiers.

### Évolutions fonctionnelles
- **Déploiement de la Simulation V2** : Nouvelle interface de visualisation des résultats, gestion des parcours de simulation alternatifs et possibilité de partager des résultats spécifiques. [#1236](https://github.com/MTES-MCT/envergo/pull/1236), [#1254](https://github.com/MTES-MCT/envergo/pull/1254), [#1255](https://github.com/MTES-MCT/envergo/pull/1255)
- **Amélioration de la gestion réglementaire** : 
    - Gestion précise des périodes d'interdiction (AHR) avec de nouveaux champs et contrôles de validité. [#1272](https://github.com/MTES-MCT/envergo/pull/1272)
    - Restructuration des contacts pour les haies (GUH) et mise à jour des informations de contact. [#1262](https://github.com/MTES-MCT/envergo/pull/1262)
    - Support multi-catégories pour les évaluateurs BCAE8. [#1268](https://github.com/MTES-MCT/envergo/pull/1268), [#1263](https://github.com/MTES-MCT/envergo/pull/1263)
- **Optimisation de l'expérience utilisateur (UX)** : 
    - Refonte complète du menu de navigation pour une meilleure clarté.
    - Amélioration de l'accessibilité (annonce de la page active).
    - Mise à jour de la terminologie pour plus de cohérence (ex: passage de "instructeur" à "coordonnateur").
    - Ajout de bulles d'aide (tooltips) pour les commentaires et amélioration de l'affichage des tableaux.

### Évolutions techniques
- **Sécurité** : Correction de vulnérabilités XSS par l'échappement des données soumises par les utilisateurs et renforcement de l'API d'autorisation. [#1251](https://github.com/MTES-MCT/envergo/pull/1251), [#1244](https://github.com/MTES-MCT/envergo/pull/1244)
- **Infrastructure & Stockage** : Intégration de Scaleway S3 pour le stockage des fichiers et configuration de l'accès sécurisé via un proxy Nginx. [#1261](https://github.com/MTES-MCT/envergo/pull/1261)
- **Performance** : Optimisation des requêtes de zones (HRU) et mise en place d'un système de cache pour la densité. [#1266](https://github.com/MTES-MCT/envergo/pull/1266), [#1238](https://github.com/MTES-MCT/envergo/pull/1238)
- **CI/CD & Data** : 
    - Automatisation de la détection des migrations de base de données manquantes dans le pipeline CI. [#1259](https://github.com/MTES-MCT/envergo/pull/1259)
    - Création de nouveaux scripts pour la synchronisation des données de production vers la base de statistiques et pour l'anonymisation des données.

### Autres changements
- Nettoyage général du code (suppression de commentaires obsolètes et de variables inutiles).
- Mise à jour de la documentation, notamment concernant les processus d'anonymisation.
