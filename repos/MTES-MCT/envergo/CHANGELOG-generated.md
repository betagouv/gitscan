## Changelog : envergo (30 derniers jours, au 29 mai 2026)

### Résumé
Cette version apporte des améliorations significatives en termes de performance, notamment au niveau des requêtes en base de données et de l'affichage des données. L'importation et la gestion des espèces ont été refactorisées, avec une meilleure prise en compte des données de sensibilité et une simplification de l'interface d'administration. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment concernant les pétitions et les messages d'information.

### Évolutions fonctionnelles
- Amélioration de l'affichage des haies dans l'interface d'administration.
- Ajout d'un message d'information pour les espèces sensibles.
- Correction de l'affichage des messages d'erreur liés à l'expiration du token.
- Amélioration de la gestion des états de changement dans les pétitions, avec notification au DS.
- Correction de l'affichage des dates dans les formulaires.
- Correction du comportement de fin de dessin sur la carte.
- Amélioration de l'affichage des haies dans l'éditeur.
- Modification du libellé "Administration" en "Espace instruction".
- Ajout d'un message d'information lors de l'envoi par le DS.
- Possibilité de compléter le contexte après évaluation.
- Affichage des conditions de plantation.
- Amélioration de l'interface d'administration des habitats d'espèces.

### Évolutions techniques
- Optimisation des performances des requêtes en base de données, notamment pour les zones et les données de la Moulinette.
- Mise en cache de divers résultats de requêtes pour réduire la charge sur la base de données.
- Refactorisation du code lié aux coefficients RU.
- Refactorisation du code d'importation des données Taxref pour s'adapter aux nouveaux modèles de données.
- Simplification de la logique de calcul de la longueur des haies.
- Amélioration de la gestion des événements Brevo et suppression des éléments inutiles liés à la RGPD.
- Suppression de code obsolète et nettoyage général du code.
- Correction de plusieurs erreurs PEP8.
- Amélioration de la robustesse du script d'importation des espèces.
- Ajout de tests unitaires pour certaines corrections.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.

### Autres changements
- Mise à jour des dépendances.
- Correction de commentaires et documentation.
- Amélioration de la gestion des erreurs et des logs.
- Génération de migrations pour les modifications de modèles.
- Correction de problèmes liés aux caractères spéciaux dans les données.
- Amélioration de la gestion des fichiers temporaires.
- Correction de problèmes liés à l'affichage des messages d'erreur.
