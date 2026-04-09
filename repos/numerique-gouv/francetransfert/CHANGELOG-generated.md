## Changelog : francetransfert (30 derniers jours, au 9 avril 2026)

### Résumé
Les dernières mises à jour de FranceTransfert se concentrent sur l'amélioration de la sécurité, la gestion des fichiers et la stabilité de la plateforme. Des ajustements ont été apportés aux configurations de production, notamment au niveau du HPA (Horizontal Pod Autoscaler) et des limites de taille des fichiers, ainsi que des corrections concernant la gestion des types de fichiers et la réinitialisation des codes.

### Évolutions fonctionnelles
- Ajout d'une liste noire pour le type de fichier HTML afin d'améliorer la sécurité. [#6](https://github.com/numerique-gouv/francetransfert/issues/6)
- Limitation de la taille des fichiers pouvant être envoyés par email.
- Amélioration de la gestion des dates de validité des fichiers et des emails associés.
- Possibilité de renvoyer le code de vérification.
- Réactivation des paramètres de restauration dans la configuration.

### Évolutions techniques
- Mise à jour de l'image vers la version 4.0.13.
- Ajustement des paramètres du HPA pour l'environnement de production afin d'optimiser la scalabilité.
- Modifications de la configuration Kubernetes (décommentaires, mises à jour de valeurs).
- Mise à jour de la librairie de logging (logback).
- Corrections et ajustements divers dans la configuration de la plateforme.

### Autres changements
- Mise à jour de la version du projet.
- Ajout des types de fichiers html et htm aux secrets.
- Renommage d'un job.
- Modification du job de verrouillage/séquestration.
