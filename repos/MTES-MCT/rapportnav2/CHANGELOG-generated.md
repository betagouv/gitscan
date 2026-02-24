## Changelog : rapportnav2 (30 derniers jours)

### Résumé
Les dernières mises à jour de rapportnav2 apportent des améliorations significatives en matière de sécurité, notamment l'ajout de journaux d'audit pour l'authentification et les clés API, ainsi que le renforcement de la protection contre les vulnérabilités courantes. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été implémentées, notamment concernant la gestion des coordonnées GPS et l'affichage du nombre de cibles.

### Évolutions fonctionnelles
- Amélioration de l'affichage du nombre de cibles sur l'interface utilisateur (#1207).
- Correction d'un bug empêchant la suppression de missions (#1233).
- Correction d'un bug lié à la gestion des informations générales et des ressources (#1232).
- Correction d'un problème d'affichage des coordonnées GPS (#1218).
- Ajout d'une option pour indiquer si une ressource est complète pour les statistiques (#1159).
- Ajout d'une fonctionnalité de recherche dans le panneau d'administration (#1160).

### Évolutions techniques
- Renforcement de la sécurité avec l'ajout de journaux d'audit pour l'authentification et les clés API.
- Amélioration de la configuration CORS et CSRF pour une meilleure sécurité.
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité (npm audit fix).
- Refactorisation du code pour améliorer la gestion des erreurs et l'utilisation de JPA.
- Amélioration de la gestion des erreurs et implémentation des réponses RFC 7807 pour une meilleure communication des erreurs.
- Mise à jour des images Docker pour inclure des correctifs de sécurité.
- Amélioration de la configuration de Sentry pour le suivi des erreurs.

### Autres changements
- Mise à jour des dépendances frontend.
- Nettoyage du code et suppression de code inutile.
- Ajout de tests unitaires et d'intégration.
- Amélioration de la documentation.
- Correction de bugs mineurs et améliorations de la performance.
