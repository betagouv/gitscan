## Changelog : Docurba (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Docurba se concentrent sur l'amélioration de l'infrastructure, la gestion des procédures et des événements, ainsi que sur l'ajout de nouvelles fonctionnalités pour les utilisateurs, notamment concernant l'affichage et la manipulation des données relatives aux procédures et aux collectivités. Des améliorations de performance et de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de l'affichage des procédures et des événements dans l'interface utilisateur, notamment avec l'ajout d'informations sur la date d'application de la loi Huwart. [#992c635](https://github.com/MTES-MCT/Docurba/commit/992c635)
- Possibilité d'exposer les thématiques des procédures dans les API SCoT et communes. [#626398f](https://github.com/MTES-MCT/Docurba/commit/626398f)
- Ajout d'un indicateur pour les procédures antérieures à la loi Huwart. [#3815c89](https://github.com/MTES-MCT/Docurba/commit/3815c89)
- Amélioration de la gestion des événements, avec l'ajout de types d'événements et la correction de bugs liés à leur affichage. [#4e69d8e](https://github.com/MTES-MCT/Docurba/commit/4e69d8e)
- Possibilité de rendre la page PAC publique. [#b53a072](https://github.com/MTES-MCT/Docurba/commit/b53a072)
- Amélioration de la gestion des procédures et des collectivités dans l'interface d'administration Django. [#f77b6bd](https://github.com/MTES-MCT/Docurba/commit/f77b6bd)
- Ajout d'une alerte Slack lors du lancement d'un déploiement. [#6209a5c](https://github.com/MTES-MCT/Docurba/commit/6209a5c)

### Évolutions techniques
- Refonte de l'infrastructure de déploiement avec l'utilisation de Nginx pour servir les fichiers statiques et gérer le reverse proxy. [#dcb5c6e](https://github.com/MTES-MCT/Docurba/commit/dcb5c6e)
- Ajout de la limitation de débit avec Nginx. [#9e8e1a9](https://github.com/MTES-MCT/Docurba/commit/9e8e1a9)
- Intégration de Supabase pour l'authentification. [#9b990ef](https://github.com/MTES-MCT/Docurba/commit/9b990ef)
- Création d'une application API interne pour séparer les responsabilités. [#6527b39](https://github.com/MTES-MCT/Docurba/commit/6527b39)
- Amélioration des performances des requêtes Django, notamment en optimisant les requêtes et en ajoutant des index. [#4388d43](https://github.com/MTES-MCT/Docurba/commit/4388d43)
- Mise à jour des dépendances (Django, djangorestframework, urllib3, pre-commit, ruff, cryptography).
- Remplacement de `wget` par `curl`. [#f040adc](https://github.com/MTES-MCT/Docurba/commit/f040adc)

### Autres changements
- Amélioration de la documentation interne et des tests.
- Nettoyage du code et suppression de code obsolète.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Configuration de Dependabot pour des mises à jour quotidiennes. [#12842da](https://github.com/MTES-MCT/Docurba/commit/12842da)
- Application du nom et de l'email de l'utilisateur comme auteur de commit lors de la mise à jour des PAC. [#29296c3](https://github.com/MTES-MCT/Docurba/commit/29296c3)
- Ajout du champ `last_sign_in_at` au modèle User. [#fff6e6f](https://github.com/MTES-MCT/Docurba/commit/fff6e6f)
- Ajout d'un modèle Session et d'une factory associée. [#e4364f2](https://github.com/MTES-MCT/Docurba/commit/e4364f2)
- Ajout de l'en-tête HTTP Supabase-Authorization. [#aee4d1e](https://github.com/MTES-MCT/Docurba/commit/aee4d1e)
- Ajout de la table Session dans le docker-compose de test. [#5fb90e3](https://github.com/MTES-MCT/Docurba/commit/5fb90e3)
- Ajout du champ email à la ProfileFactory. [#45a42e5](https://github.com/MTES-MCT/Docurba/commit/45a42e5)
- Ajout de la dépendance Supabase. [#03c9e9a](https://github.com/MTES-MCT/Docurba/commit/03c9e9a)
