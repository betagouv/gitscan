## Changelog : envergo (30 derniers jours)

### Résumé
Les dernières mises à jour d'envergo incluent des améliorations significatives de l'interface utilisateur, notamment pour la gestion des configurations et des haies, ainsi que des corrections de bugs pour améliorer la stabilité et l'expérience utilisateur. Des optimisations ont également été apportées à la gestion des données et des requêtes, et des mises à jour de sécurité ont été implémentées. Plusieurs améliorations de la documentation et des tests ont également été réalisées.

### Évolutions fonctionnelles
- Amélioration de l'affichage et de la gestion des configurations, avec l'ajout de plages de validité et de filtres (#1031, #1032).
- Ajout de la possibilité de visualiser les cartes pour chaque département dans la configuration (#981).
- Amélioration du calcul et de l'affichage de la densité de haies (#1016, #1018, #1019).
- Correction d'un bug empêchant l'affichage correct des projets (#999).
- Amélioration de la gestion des réglementations Natura 2000 (#1008, #1023).
- Ajout de la possibilité de filtrer les configurations par date (#1033).
- Correction de l'affichage des boutons "en savoir plus" (#1015).
- Amélioration de la gestion des URL des projets (#1006).
- Ajout de la gestion des champs de surface avec unités (#988).
- Amélioration de l'affichage des comptes (#1020).

### Évolutions techniques
- Mise à jour de Django en version 4.2.28 (#989).
- Optimisation des requêtes pour améliorer les performances (#965).
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Suppression de dépendances inutiles (bs4).
- Utilisation de filtres plus performants pour la gestion des haies.
- Amélioration de la gestion des dates et des intervalles de temps.
- Ajout de contraintes de base de données pour la validation des chevauchements de configurations.
- Amélioration de la gestion des URL et des liens.

### Autres changements
- Mise à jour de la documentation pour refléter les dernières modifications.
- Corrections de fautes de frappe et améliorations de la qualité du code.
- Mise à jour des messages et des textes d'interface utilisateur.
- Amélioration de la sécurité en supprimant des tokens inutiles et en protégeant contre les attaques XSS.
- Mise à jour des dépendances et des bibliothèques.
- Amélioration de la gestion des logs et des erreurs.
- Ajout de commentaires pour faciliter la compréhension du code.
- Mise à jour des définitions terrain et assiette.
- Amélioration de l'affichage des numéros de page.
- Suppression de l'analyse des tokens de consultation.
- Mise à jour de la mise en page de l'historique.
- Correction de l'affichage de la mention "PAC ou pas PAC".
- Amélioration de l'affichage de la date d'échéance.
- Suppression des événements analytics liés aux tokens de consultation.
