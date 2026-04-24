## Changelog : francetransfert (30 derniers jours, au 2026-04-15)

### Résumé
Cette version apporte des améliorations de sécurité en ajoutant des restrictions sur les types de fichiers autorisés, ainsi que des ajustements de configuration pour l'environnement de production, notamment au niveau de l'autoscaling et des limites de téléchargement/envoi. Des corrections et mises à jour diverses ont également été effectuées pour améliorer la stabilité et la maintenance du service.

### Évolutions fonctionnelles
- Restriction des types de fichiers autorisés en blacklistant les fichiers HTML et HTM pour des raisons de sécurité. [#6](https://github.com/numerique-gouv/francetransfert/issues/6)
- Limitation du nombre de mails envoyés pour certaines opérations (date check, téléchargement).
- Amélioration de la gestion des jobs de verrouillage/séquestre de fichiers.

### Évolutions techniques
- Ajustement des paramètres HPA (Horizontal Pod Autoscaler) pour l'environnement de production afin d'optimiser l'autoscaling.
- Mise à jour des images Docker vers la version 4.0.13.
- Mise à jour de la librairie Logback.
- Mise à jour de la librairie Spring.
- Modifications de la configuration (values.ft.yaml) pour réactiver les paramètres de restauration.

### Autres changements
- Mise à jour de la version du service.
- Préparation d'une nouvelle version.
- Corrections et mises à jour mineures de la configuration et du code.
- Mise à jour de la clé de chiffrement.
- Ajustement des valeurs de configuration pour l'environnement de production.
