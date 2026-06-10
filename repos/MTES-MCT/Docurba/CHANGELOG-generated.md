## Changelog : Docurba (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, Docurba a connu des améliorations significatives en termes de performance, de sécurité et de fonctionnalités. L'authentification Supabase a été intégrée, l'infrastructure a été renforcée avec l'ajout de Nginx pour la gestion du trafic et la sécurité, et l'interface utilisateur a été améliorée avec des corrections et des nouvelles fonctionnalités, notamment concernant la gestion des procédures et des événements. Des efforts importants ont également été déployés pour la préparation des données en vue de la conformité à la loi Huwart.

### Évolutions fonctionnelles
- **Authentification:** Intégration de l'authentification via Supabase, offrant une nouvelle méthode de connexion pour les utilisateurs. [#9b990ef](https://github.com/MTES-MCT/Docurba/commit/9b990ef)
- **Interface utilisateur (Nuxt):**
    - Amélioration de l'affichage des procédures et des événements, avec notamment l'ajout d'informations sur la date de la loi Huwart. [#802c499](https://github.com/MTES-MCT/Docurba/commit/802c499), [#6462351](https://github.com/MTES-MCT/Docurba/commit/6462351)
    - Correction de bugs liés à la sélection des procédures et à la création de PLU. [#b82b53a](https://github.com/MTES-MCT/Docurba/commit/b82b53a), [#9553d70](https://github.com/MTES-MCT/Docurba/commit/9553d70)
    - La page de lecture des PAC est désormais publique. [#b53a072](https://github.com/MTES-MCT/Docurba/commit/b53a072)
- **Gestion des procédures:**
    - Possibilité de mettre à jour les événements directement depuis la page de la procédure dans l'interface d'administration Django. [#f77b6bd](https://github.com/MTES-MCT/Docurba/commit/f77b6bd)
    - Amélioration de la gestion des types de collectivités et des procédures. [#399bc60](https://github.com/MTES-MCT/Docurba/commit/399bc60)
- **API Interne:** Création d'une API interne pour les collectivités et les communes. [#0af9778](https://github.com/MTES-MCT/Docurba/commit/0af9778)

### Évolutions techniques
- **Infrastructure:**
    - Ajout de Nginx pour servir les fichiers statiques et gérer le reverse proxy, améliorant ainsi les performances et la sécurité. [#dcb5c6e](https://github.com/MTES-MCT/Docurba/commit/dcb5c6e), [#44144b9](https://github.com/MTES-MCT/Docurba/commit/44144b9), [#74ec84d](https://github.com/MTES-MCT/Docurba/commit/74ec84d)
    - Mise en place de la limitation de débit avec Nginx. [#9e8e1a9](https://github.com/MTES-MCT/Docurba/commit/9e8e1a9)
    - Remplacement de `wget` par `curl` pour plus de robustesse. [#f040adc](https://github.com/MTES-MCT/Docurba/commit/f040adc)
- **Backend (Django):**
    - Amélioration des performances des requêtes et des modèles Django. [#4388d43](https://github.com/MTES-MCT/Docurba/commit/4388d43), [#60194b2](https://github.com/MTES-MCT/Docurba/commit/60194b2)
    - Ajout de champs manquants et correction de types de données dans les modèles. [#55f3a41](https://github.com/MTES-MCT/Docurba/commit/55f3a41), [#6018fcc](https://github.com/MTES-MCT/Docurba/commit/6018fcc)
    - Mise à jour des dépendances Django et djangorestframework. [#696384d](https://github.com/MTES-MCT/Docurba/commit/696384d), [#b4144b9](https://github.com/MTES-MCT/Docurba/commit/b4144b9)
- **CI/CD:** Ajout d'une alerte Slack lors des déploiements. [#6209a5c](https://github.com/MTES-MCT/Docurba/commit/6209a5c)

### Autres changements
- **Données:** Préparation des données pour la conformité à la loi Huwart, incluant la mise à jour des types de documents et la suppression des événements obsolètes. [#32cde71](https://github.com/MTES-MCT/Docurba/commit/32cde71), [#28ef793](https://github.com/MTES-MCT/Docurba/commit/28ef793), [#0d6cf9a](https://github.com/MTES-MCT/Docurba/commit/0d6cf9a)
- **Documentation:** Amélioration de la documentation interne.
- **Configuration:** Mise à jour de la configuration pour utiliser les variables d'environnement pour l'URL de l'API. [#bcaf256](https://github.com/MTES-MCT/Docurba/commit/bcaf256), [#59b1540](https://github.com/MTES-MCT/Docurba/commit/59b1540)
- **Tests:** Ajout et amélioration des tests unitaires.
- **Nettoyage de code:** Suppression de code commenté et amélioration de la lisibilité du code.
