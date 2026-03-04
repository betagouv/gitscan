## Changelog : diagbruit.beta.gouv.fr (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'ajout de pages légales, l'amélioration de la gestion des zones de bruit et des sources de bruit, ainsi que des corrections et refactorisations pour optimiser l'expérience utilisateur et la stabilité de l'application. Des améliorations ont également été apportées à la gestion des données et à l'infrastructure de déploiement.

### Évolutions fonctionnelles
- Ajout de toutes les pages légales nécessaires au site [#44](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/44).
- Amélioration de la gestion des polygones pour les sources de bruit [#41](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/41).
- Ajout d'une alerte spécifique lorsque la zone de bruit est atteinte [#40](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/40).
- Ajout d'un iframe pour l'intégration de données de tally [#42](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/42).
- Refonte de la section "Résumé" pour une meilleure clarté et une expérience utilisateur améliorée [#42](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/42).
- Amélioration du libellé et de la description des zones de bruit [#43](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/43).
- Ajout d'une exception pour les topos blocs sonores [#37](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/37).

### Évolutions techniques
- Refactorisation des composants de réglementation dans le frontend [#37](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/37).
- Adaptation des scripts d'ingestion de données aux changements en production [#37](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/37).
- Mise à jour de la version de l'API [#35](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/35).
- Amélioration de la gestion des tests d'intégration dans l'API.
- Ajout de `serve` pour le démarrage en production du frontend.
- Correction de problèmes liés à Yarn et à la configuration des fichiers.
- Suppression de références obsolètes au PLU local dans le frontend.
- Ajout de la prise en charge de la whitelist 35 59 67.

### Autres changements
- Ajout de documentation locale au CMS et utilisation dans le frontend.
- Amélioration du texte dynamique concernant l'isolation affectée par le bruit.
- Corrections mineures de design et d'UX dans le frontend.
- Correction de titres et de comptages dans l'accordéon du frontend.
- Mise à jour des étiquettes et des descriptions des zones de bruit dans l'API.
- Nettoyage et optimisation de la configuration du CMS pour réduire la taille de l'image Docker.
- Ajout de fichiers `.yarnrc.yml` pour le déploiement sur Scalingo.
- Suppression de fichiers et de configurations inutiles.
