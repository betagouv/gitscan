## Changelog : Docurba (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Docurba se concentrent sur l'amélioration de l'administration des événements et des procédures, avec un accent particulier sur l'intégration de l'historique des modifications, la gestion des utilisateurs et des permissions, ainsi que des optimisations de l'interface utilisateur et de l'API. Des améliorations de sécurité et de performance ont également été apportées.

### Évolutions fonctionnelles
- Possibilité de rechercher des utilisateurs dans l'interface d'administration par adresse email. [#3df9bea](https://github.com/MTES-MCT/Docurba/issues/3df9bea)
- Mise à jour du mot de passe des utilisateurs directement depuis l'interface d'administration. [#29e6ea8](https://github.com/MTES-MCT/Docurba/issues/29e6ea8)
- Ajout de la possibilité de lister les procédures incluant une commune spécifique dans l'interface d'administration. [#818abbd](https://github.com/MTES-MCT/Docurba/issues/818abbd)
- Historisation de toutes les modifications apportées aux événements, permettant un suivi précis des changements. [#cfb4754](https://github.com/MTES-MCT/Docurba/issues/cfb4754)
- Amélioration de la détection et de l'affichage des événements de prescription dans l'interface Nuxt. [#3d9205b](https://github.com/MTES-MCT/Docurba/issues/3d9205b) et [#13efcf1](https://github.com/MTES-MCT/Docurba/issues/13efcf1)
- Affichage du statut "avant loi Huwart" pour les procédures concernées dans l'interface Nuxt. [#b885455](https://github.com/MTES-MCT/Docurba/issues/b885455)
- Possibilité de filtrer les types de procédures par date de début dans l'interface Nuxt. [#4f89e20](https://github.com/MTES-MCT/Docurba/issues/4f89e20)
- Page de lecture des PAC (Prescriptions Archéologiques Collectives) rendue publique. [#b53a072](https://github.com/MTES-MCT/Docurba/issues/b53a072)
- Ajout de nouvelles catégories de PAC. [#a553a34](https://github.com/MTES-MCT/Docurba/issues/a553a34)
- Ajout d'une nouvelle catégorie d'événements. [#a26bfc2](https://github.com/MTES-MCT/Docurba/issues/a26bfc2)

### Évolutions techniques
- Refonte de l'authentification avec l'ajout de l'authentification Supabase et la gestion des sessions.
- Amélioration de la configuration des templates. [#d1b9b1e](https://github.com/MTES-MCT/Docurba/issues/d1b9b1e)
- Remplacement de `wget` par `curl` pour les requêtes HTTP. [#f040adc](https://github.com/MTES-MCT/Docurba/issues/f040adc)
- Mise en place d'un reverse proxy Nginx pour améliorer la sécurité et les performances.
- Configuration de la limitation de débit avec Nginx.
- Utilisation de variables d'environnement pour la configuration de l'URL de l'API Docurba dans Nuxt. [#bcaf256](https://github.com/MTES-MCT/Docurba/issues/bcaf256)
- Amélioration de la gestion des tests avec l'ajout d'un client staff pour les tests d'administration. [#b4cf286](https://github.com/MTES-MCT/Docurba/issues/b4cf286) et le regroupement des tests par modèle. [#8671872](https://github.com/MTES-MCT/Docurba/issues/8671872)
- Optimisation des performances de l'API interne Django avec la pagination et le filtrage.
- Ajout d'une alerte Slack lors des déploiements. [#6209a5c](https://github.com/MTES-MCT/Docurba/issues/6209a5c)
- Mise à jour de plusieurs dépendances (cryptography, pyjwt, ruff, supabase, django, django-filter).

### Autres changements
- Suppression de vues publiques inutiles. [#863748b](https://github.com/MTES-MCT/Docurba/issues/863748b)
- Suppression de paramètres Django obsolètes. [#e50d554](https://github.com/MTES-MCT/Docurba/issues/e50d554)
- Ajout de commentaires et de documentation.
- Amélioration de l'intégration de `pg_history`.
- Configuration de Dependabot pour vérifier les mises à jour des dépendances quotidiennement. [#12842da](https://github.com/MTES-MCT/Docurba/issues/12842da)
- Mise à jour de la configuration des applications de revue (review apps). [#92361da](https://github.com/MTES-MCT/Docurba/issues/92361da)
