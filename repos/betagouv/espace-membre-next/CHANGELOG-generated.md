## Changelog : espace-membre-next (30 derniers jours)

### Résumé
Les dernières améliorations apportées à l'espace membre se concentrent sur l'amélioration de l'expérience utilisateur, notamment concernant l'onboarding des membres et la gestion des invitations par email. Des corrections ont été apportées pour assurer que tous les membres, y compris les anciens, voient l'onboarding et que les invitations par email fonctionnent correctement, même dans des cas spécifiques comme les adresses email supprimées. Une documentation a également été ajoutée pour clarifier le flux de travail.

### Évolutions fonctionnelles
- Correction : L'onboarding n'était pas affiché pour les membres existants, il est maintenant visible pour tous. [#1222](https://github.com/betagouv/espace-membre-next/issues/1222)
- Correction : L'affichage des instructions de création d'email a été simplifié. [#1223](https://github.com/betagouv/espace-membre-next/issues/1223)
- Correction : Affichage correct des invitations dimail même lorsque l'email a été supprimé. [#1216](https://github.com/betagouv/espace-membre-next/issues/1216)
- Correction : Résolution d'un problème avec l'invitation dimail. [#1215](https://github.com/betagouv/espace-membre-next/issues/1215)
- Correction : Affichage de l'invitation dimail pour les membres dont l'email est marqué comme supprimé. [#1214](https://github.com/betagouv/espace-membre-next/issues/1214)
- Correction : Correction de l'affichage de la page de vérification de compte. [#1219](https://github.com/betagouv/espace-membre-next/issues/1219)

### Évolutions techniques
- Correction : Format du cron job corrigé. [#1213](https://github.com/betagouv/espace-membre-next/issues/1213)

### Autres changements
- Ajout d'un diagramme de flux pour la documentation. [#1211](https://github.com/betagouv/espace-membre-next/issues/1211)
- Mise à jour du fichier `checklist.yml`. [#1221](https://github.com/betagouv/espace-membre-next/issues/1221)
