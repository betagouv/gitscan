## Changelog : francetransfert (30 derniers jours, au 9 mai 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, notamment en ajoutant des types de fichiers à la liste noire pour la protection contre les menaces. Des ajustements ont également été apportés à la gestion des envois et téléchargements, incluant des limites et des vérifications de dates, ainsi que des optimisations de l'infrastructure pour la production.

### Évolutions fonctionnelles
- Ajout de types de fichiers HTML et HTM à la liste noire pour renforcer la sécurité des transferts [#6](https://github.com/numerique-gouv/francetransfert/issues/6).
- Limitation du nombre d'emails envoyés pour certains processus (mails de relance, téléchargements).
- Amélioration de la gestion des dates de validité des liens de téléchargement.
- Possibilité de restaurer les paramètres de restauration dans le fichier `values.ft.yaml`.

### Évolutions techniques
- Ajustement des paramètres HPA (Horizontal Pod Autoscaler) pour optimiser la gestion des ressources en production.
- Mise à jour des images Docker vers la version 4.0.13.
- Mises à jour de dépendances internes (Spring, Logback, POM).
- Amélioration de la gestion des jobs de verrouillage/séquestre.
- Préparation d'une nouvelle version du service.

### Autres changements
- Mise à jour de la clé de chiffrement.
- Corrections et améliorations diverses du code.
- Mise à jour de la version du service.
