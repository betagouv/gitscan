## Changelog : Docurba (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Docurba se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des procédures et des collectivités, ainsi que sur des optimisations techniques de l'infrastructure et de l'API. Des améliorations significatives ont été apportées à l'administration et à la gestion des événements, et une nouvelle méthode d'authentification via Supabase a été implémentée.

### Évolutions fonctionnelles
- Ajout de l'ID de la procédure dans l'onglet Procédures et Validations pour une meilleure identification.
- Amélioration de la gestion des événements : affichage des dates de procédure sur les pages procédures et collectivités.
- Possibilité de modifier les événements directement depuis la page de la procédure correspondante dans l'interface d'administration.
- Amélioration de la recherche et de la détection des événements de lancement.
- Ajout de la possibilité de filtrer les procédures par compétence, département, région et type via une nouvelle API interne.
- L'interface d'administration permet désormais de rechercher des utilisateurs par email et de mettre à jour leur mot de passe.
- Ajout de catégories PAC (Plan d'Actions et de Coopération) pour une meilleure organisation.
- Amélioration de l'affichage des procédures sur les écrans étroits.

### Évolutions techniques
- Implémentation de l'authentification via Supabase, incluant l'ajout de la dépendance et la configuration nécessaire.
- Refonte de l'infrastructure de déploiement avec l'utilisation de Nginx pour servir les fichiers statiques et la mise en place d'une limitation de débit.
- Amélioration de la performance des requêtes et des tests Django.
- Harmonisation de la gestion des paramètres de requête dupliqués dans l'API Django.
- Mise à jour de plusieurs dépendances : pytest, ruff, cryptography, pyjwt, django-filter, supabase.
- Utilisation de l'API Django pour récupérer les procédures et les collectivités, remplaçant l'API Node.js.
- Ajout de tests API pour garantir la qualité du code.
- Amélioration de la gestion des erreurs et des logs.

### Autres changements
- Ajout de webhooks avec limitation des champs envoyés pour améliorer la sécurité et la performance.
- Documentation et commentaires améliorés dans le code.
- Nettoyage du code et suppression de code obsolète.
- Configuration améliorée pour les environnements de développement et de production.
- Ajout d'un header Supabase-Authorization.
- Ajout d'une alerte Slack lors des déploiements.
- Historisation de toutes les modifications d'événements.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
