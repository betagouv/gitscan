## Changelog : ami-notifications-api (30 derniers jours, au 8 juin 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'interface utilisateur de l'application mobile, notamment la gestion des préférences d'adresse et des zones géographiques. Des corrections et des optimisations ont également été apportées à la gestion des notifications et à l'infrastructure, incluant la réplication de la base de données et la gestion des certificats SSL locaux. Des fonctionnalités expérimentales liées à FranceConnect et à l'authentification sont en cours de développement.

### Évolutions fonctionnelles
- Amélioration de l'expérience utilisateur sur l'application mobile :
    - Ajout de la possibilité de supprimer des adresses dans les préférences utilisateur [#789].
    - Gestion des zones géographiques améliorée, avec la possibilité de sélectionner une zone en fonction de la ville choisie [#789].
    - Navigation vers les préférences de zone lors de la première connexion [#788].
    - Refonte de l'affichage des éléments d'agenda pour une meilleure clarté [#802].
- Gestion des notifications :
    - Mise à jour du lien de notification pour rediriger vers la page de suivi correspondante [#794].
    - Ajout d'un champ `content_private_body` aux modèles de notification et aux sérialiseurs associés, permettant de stocker un contenu privé pour les notifications [#875].
    - Désactivation des notifications lors de la déconnexion [#721].
- Amélioration de l'interface utilisateur de l'administration :
    - Ajout de vues pour la gestion des utilisateurs (recherche, détails, suppression) [#774].
    - Implémentation de messages de confirmation (toasts) pour les actions d'administration [#774].
    - Amélioration de la mise en page du bouton "gérer" dans l'écran des notifications [#874].

### Évolutions techniques
- Infrastructure :
    - Mise en place d'une réplication de la base de données vers un datawarehouse [#904].
    - Utilisation de `mkcert` pour la gestion des certificats SSL locaux, facilitant le développement en environnement local [#828].
    - Amélioration de la gestion des logs [#791].
- Architecture :
    - Refonte de la structure des vues, URLs et tests pour l'administration [#774].
    - Création d'un composant `PageWrapper` pour une mise en page cohérente et réactive [#801].
    - Suppression du flag de fonctionnalité "requests enabled" qui n'est plus utilisé [#823].
- Divers :
    - Mise à jour de plusieurs dépendances (uv, vitest, svelte, etc.)
    - Amélioration de la gestion des variables d'environnement.

### Autres changements
- Ajout de la prise en charge de l'authentification via FranceConnect et implémentation des fonctionnalités associées (FI app, token, autorisation, logout) [#708]. Ces fonctionnalités sont encore en développement.
- Ajout de la traçabilité des zones de vacances sur Matomo [#750].
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression de dossiers et fichiers inutiles.
- Amélioration de la gestion des erreurs et des messages d'information.
- Ajout de tests unitaires et d'intégration.
