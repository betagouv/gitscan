## Changelog : mon-aide-cyber (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la correction de bugs et l'amélioration de la robustesse de l'application, notamment en cas d'erreurs externes (API Géo). Des ajustements ont également été apportés à l'interface utilisateur et aux processus de build.

### Évolutions fonctionnelles
- Correction du calcul du nombre de jours pour le "cooldown" dans le module SOIN. [#issue à investiguer]
- Correction de l'affichage des encarts d'homologations dans le module SOIN. [#issue à investiguer]
- Amélioration de la gestion des erreurs lors de l'appel à l'API Géo pour l'EPCI, évitant ainsi des dysfonctionnements en cas de problème avec ce service externe. [#issue à investiguer]

### Évolutions techniques
- Mise à jour de certaines dépendances pour améliorer la sécurité et la stabilité de l'application.
- Suppression d'un UI Kit inutilisé, allégeant ainsi le code et simplifiant la maintenance.
- Mise à jour du UI Kit vers la version 1.28.4.

### Autres changements
- Mise à jour des tampons d'homologation MAC.
