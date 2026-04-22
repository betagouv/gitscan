## Changelog : francetransfert (30 derniers jours, au 15 mai 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, notamment en ajoutant des types de fichiers à la liste noire pour la protection contre les menaces. Des ajustements ont également été apportés à la gestion des jobs et des limites d'envoi de mails pour optimiser la performance et la fiabilité du service. Enfin, des mises à jour de version et de configuration ont été déployées.

### Évolutions fonctionnelles
- Ajout de `html` et `htm` à la liste noire des types de fichiers autorisés pour renforcer la sécurité. [#6](https://github.com/numerique-gouv/francetransfert/issues/6)
- Limitation du nombre de mails envoyés pour certaines opérations (date check, téléchargement) afin d'éviter les abus et d'améliorer la délivrabilité.
- Amélioration de la gestion des jobs de verrouillage/séquestre.
- Restauration des paramètres de restauration dans le fichier `values.ft.yaml`.

### Évolutions techniques
- Mise à jour des tags d'image vers la version 4.0.13.
- Ajustement des paramètres HPA (Horizontal Pod Autoscaler) pour l'environnement de production afin d'optimiser la scalabilité.
- Mise à jour de la librairie `logback`.
- Mise à jour de la librairie `spring`.
- Préparation d'une nouvelle version du service.
- Mise à jour de la clé PPR.

### Autres changements
- Mise à jour de la version du service.
- Modifications de la configuration du service (pom, valeurs de production).
- Diverses corrections et améliorations mineures du code.
