## Changelog : domifa (30 derniers jours, au 27 juin 2026)

### Résumé
Cette période a été marquée par de nombreuses corrections de bugs et améliorations de la sécurité, notamment concernant la gestion des utilisateurs, l'authentification et la protection contre les vulnérabilités. Des améliorations ont également été apportées à la gestion des organismes et à l'expérience utilisateur, notamment sur le portail usagers.

### Évolutions fonctionnelles
- Ajout de la possibilité de sélectionner "autre" pour le type d'organisme et la raison de sa domiciliation.
- Amélioration de la gestion des utilisateurs bloqués, avec suppression de la possibilité de les éditer.
- Ajout de filtres pour la recherche d'organismes supprimés.
- Amélioration de la gestion des téléchargements avec ajout d'un blocage.
- Ajout de statistiques sur les sessions utilisateurs.
- Correction de l'affichage du portail usagers.

### Évolutions techniques
- Ajout de filtres HTTP pour améliorer la sécurité.
- Ajout d'un filtre d'exception pour une meilleure gestion des erreurs.
- Ajout de logs pour les téléchargements et les tentatives de connexion inconnues.
- Mise en place d'une table IP pour la gestion des accès.
- Correction d'une potentielle vulnérabilité de type "Type confusion through parameter tampering" (CodeQL).
- Amélioration des tests unitaires et correction de bugs dans les tests existants.
- Ajout de tests pour la mise à jour du mot de passe.
- Implémentation de l'envoi d'emails via Tipimail.

### Autres changements
- Correction de plusieurs erreurs de typage et de linting.
- Mise à jour de la documentation et des pages de titre.
- Correction de bugs mineurs dans le frontend (correction de l'arobase, suppression de l'édition des utilisateurs bloqués).
- Plusieurs releases intermédiaires (2.250.1, 2.250.2, 2.250.3, 2.250.4, 2.250.5, 2.250.6, 2.250.7, 2.250.8, 2.250.9, 2.250.10, 2.250.11, 2.250.12) avec des corrections mineures et des améliorations continues.
