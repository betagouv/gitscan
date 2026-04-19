## Changelog : francetransfert (30 derniers jours, au 2026-04-15)

### Résumé
Cette version apporte des améliorations de sécurité, notamment en ajoutant des types de fichiers à la liste noire pour éviter les téléchargements potentiellement dangereux. Des ajustements ont été effectués sur la gestion des dates d'expiration des fichiers et des limites d'envoi de notifications par email. Des optimisations de l'infrastructure et des mises à jour de versions ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de types de fichiers HTML et HTM à la liste noire pour interdire leur transfert [#6](https://github.com/numerique-gouv/francetransfert/issues/6).
- Amélioration de la gestion des dates d'expiration des fichiers et des téléchargements.
- Limitation du nombre de notifications par email envoyées pour certains événements.

### Évolutions techniques
- Ajustement des paramètres HPA (Horizontal Pod Autoscaler) pour l'environnement de production afin d'optimiser la scalabilité.
- Mise à jour des images Docker vers la version 4.0.13.
- Mise à jour des dépendances Spring.
- Mise à jour de la librairie Logback.
- Modifications de la configuration Kubernetes (décommentage des paramètres de restauration).

### Autres changements
- Préparation d'une nouvelle version (mise à jour des numéros de version et des clés).
- Diverses corrections et ajustements de code.
- Mise à jour de la configuration `values.ft.yaml`.
