## Changelog : labonnealternance-lab (30 derniers jours)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives en termes de gestion de la configuration, de déploiement et de performance du modèle de classification. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment concernant l'affichage de la version et la gestion des datasets. Un nouveau modèle d'apprentissage a été intégré et entraîné.

### Évolutions fonctionnelles
- Affichage du numéro de version de l'application.
- Intégration d'un nouveau modèle d'apprentissage pour la classification des offres d'emploi ([#14](https://github.com/mission-apprentissage/labonnealternance-lab/pull/14)).
- Amélioration de l'évaluation du modèle avec la possibilité d'évaluer un seul modèle.
- Correction de l'utilisation du jeton PAT pour l'authentification.
- Correction de la route `/model/scores`.

### Évolutions techniques
- Migration de la gestion des secrets d'Ansible Vault vers SOPS ([#15](https://github.com/mission-apprentissage/labonnealternance-lab/pull/15)).
- Amélioration du processus de CI/CD avec des corrections et des ajustements.
- Simplification de l'entraînement et de l'évaluation du modèle, avec ajout d'une technique d'undersampling ([#13](https://github.com/mission-apprentissage/labonnealternance-lab/pull/13)).
- Correction de la prise en compte des sous-modules Git ([#17](https://github.com/mission-apprentissage/labonnealternance-lab/pull/17)).
- Mise à jour des dépendances locales pour l'entraînement du modèle.
- Déplacement de la version du modèle vers un fichier de configuration.

### Autres changements
- Correction de fautes de frappe dans divers fichiers ([#16](https://github.com/mission-apprentissage/labonnealternance-lab/pull/16), [#18](https://github.com/mission-apprentissage/labonnealternance-lab/pull/18)).
- Mise à jour de la documentation.
- Correction de problèmes liés au chargement des images lors du déploiement.
- Correction de la gestion du dataset de validation.
- Le dataset est maintenant lu comme un fichier JSON classique.
