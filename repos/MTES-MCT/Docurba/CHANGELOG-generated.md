## Changelog : Docurba (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Docurba se concentrent sur l'amélioration de l'interface utilisateur, notamment dans la gestion des procédures et des événements, ainsi que sur des optimisations techniques importantes pour la performance et la sécurité de la plateforme. L'ajout d'une API interne et l'amélioration de l'authentification sont également des points clés.

### Évolutions fonctionnelles
- Amélioration de l'affichage et de la gestion des événements liés aux procédures, incluant la distinction des types d'événements et la gestion des dates de fin d'échéance liées à la loi Huwart.
- Possibilité de mettre à jour les procédures directement depuis la page d'administration des événements.
- Ajout d'informations sur les procédures antérieures à la loi Huwart dans l'interface utilisateur.
- Amélioration de la page de lecture des PAC (Plans d'Actions Climat) et suppression des restrictions d'accès.
- Ajout d'un indicateur visuel pour les procédures antérieures à la loi Huwart.
- Possibilité de filtrer les types de procédures en fonction de leur date de début.
- L'API interne permet désormais de récupérer les collectivités et communes.
- Ajout de la possibilité de filtrer les collectivités par département, région et type.
- Pagination des résultats de l'API interne pour une meilleure performance.
- Amélioration de la gestion des erreurs et des messages d'information dans l'interface utilisateur.
- Ajout du nom d'utilisateur et de l'adresse e-mail de l'utilisateur actuel comme auteur de commit lors de la mise à jour des PAC.
- Ajout d'une alerte Slack lors du lancement d'un déploiement.

### Évolutions techniques
- Refonte de l'architecture de déploiement avec l'utilisation de Nginx pour servir les fichiers statiques et la mise en place d'une limitation du débit (rate limiting).
- Suppression de dépendances inutiles (whitenoise, django-revproxy).
- Mise en place d'une authentification via Supabase, incluant l'ajout du header d'autorisation Supabase et la gestion des sessions.
- Amélioration des performances des requêtes Django, notamment en ajoutant des index et en optimisant les filtres.
- Utilisation de `curl` au lieu de `wget` pour les requêtes HTTP.
- Migration de l'application `internal_api` dans le répertoire `docurba`.
- Mise à jour de plusieurs dépendances : Django, djangorestframework, cryptography, urllib3, ruff, django-filter.
- Ajout de tests Pytest.
- Amélioration de la gestion des migrations Django.
- Utilisation explicite de la variable d'environnement `DOCURBA_API_URL` dans Nuxt.

### Autres changements
- Documentation mise à jour.
- Nettoyage du code et suppression de code commenté.
- Amélioration de la configuration et des variables d'environnement.
- Correction de conflits de migration Django.
- Ajout de champs manquants dans les modèles Django (Event, Procedure).
- Modification des types de champs dans les modèles Django pour une meilleure cohérence.
- Standardisation des noms de champs et des conventions de nommage.
- Ajout de verbose names pour les champs des modèles Django.
- Correction de bugs et amélioration de la stabilité de la plateforme.
