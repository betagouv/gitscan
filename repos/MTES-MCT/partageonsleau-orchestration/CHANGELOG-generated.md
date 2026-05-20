## Changelog : partageonsleau-orchestration (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, l'orchestrateur Partageons l'Eau a connu des améliorations significatives en termes de connectivité aux sources de données (Willie, Olo, Aquasys) et de gestion des tâches grâce à l'intégration de BullMQ.  Des travaux ont également été réalisés pour préparer l'intégration avec la plateforme PLE et améliorer la robustesse du projet via la dockerisation et la correction de problèmes de linting.

### Évolutions fonctionnelles
- Ajout de connecteurs pour les sources de données Olo et Aquasys [#4](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/4).
- Implémentation d'un connecteur initial pour Willie en mode incrémental.
- Prise en charge de la connexion à la plateforme PLE avec un service account et un token de déclarant [#6](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/6).
- Possibilité de gérer plusieurs connecteurs [#9](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/9).
- Gestion de plusieurs types de déclarations [#8](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/8).
- Amélioration du calcul des volumes à partir de l'index pour Willie [#7](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/7).

### Évolutions techniques
- Intégration de BullMQ pour la gestion des tâches [#5](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/5).
- Dockerisation du projet pour faciliter le déploiement et la reproductibilité [#1](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/1).
- Mise en place d'un pipeline CI/CD avec `deploy.yml`.
- Amélioration de la gestion des certificats Redis.
- Correction de problèmes de linting avec xo.

### Autres changements
- Mise à jour de la documentation et du fichier README.
- Modification du port par défaut.
- Ajout d'une administration BullMQ.
- Correction de regex et suppression de flags inutiles.
- Ajout de la possibilité de définir une politique de gestion des conflits.
- Amélioration de la liaison entre l'orchestration et la plateforme.
- Ajout d'un `pointId` pour l'envoi de données au backend.
- Mise à jour de la granularité pour Willie afin d'éviter les valeurs nulles.
