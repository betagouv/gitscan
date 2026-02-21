## Changelog : mobilic (30 derniers jours)

### Résumé
Les dernières mises à jour de mobilic se concentrent sur l'amélioration de l'interface d'administration, notamment la gestion des employés et des activités. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment au niveau de l'affichage des informations sur les missions et les alertes. Une nouvelle fonctionnalité permettant de contrôler l'API de localisation a été implémentée.

### Évolutions fonctionnelles
- Amélioration de l'interface de gestion des employés dans l'administration : ajout de badges pour l'état des employés (actifs/inactifs), amélioration des modales de terminaison d'emploi, et ajout de la possibilité de terminer plusieurs emplois en batch (#789).
- Ajout de la possibilité de réactiver un employé (#789).
- Amélioration de l'affichage des informations sur les missions dans l'interface, notamment la gestion des jours fériés et des alertes (#782).
- Correction de l'affichage des infractions dans l'en-tête et le tiroir (#791).
- Implémentation d'une nouvelle fonctionnalité pour contrôler l'API de localisation (#784).
- Amélioration de l'affichage des dates et des titres de mission (#77ca58ae, #4a5c49ce, #a5f9968f).
- Correction de l'affichage des tags "mission en cours" et "mission à valider" (#4c4ee5b1).

### Évolutions techniques
- Mise à jour de la configuration de Webpack pour la compatibilité avec la version 5 (#799).
- Correction de l'utilisation de HTTP/1.1 pour les requêtes à l'API backend (#802).
- Refactoring du code pour améliorer la qualité et la maintenabilité, notamment dans la gestion des employés et des styles DSFR (#789).
- Correction de vulnérabilités potentielles dans les expressions régulières (#784).
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité (#791, #9bdd4ab8).
- Adaptation de Webpack pour charger tous les fichiers du playground (#806).
- Ajout de la possibilité d'autoriser le domaine geoplatform dans la politique de sécurité du contenu (CSP) (#784).

### Autres changements
- Amélioration de la documentation et des commentaires dans le code.
- Correction de divers problèmes d'affichage et de style mineurs (#793, #794, #795, #796, #797).
- Résolution de warnings ESLint (#789).
- Correction de l'import d'un composant (#782).
