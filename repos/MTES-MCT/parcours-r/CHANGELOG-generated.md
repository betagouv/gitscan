## Changelog : parcours-r (30 derniers jours, au 3 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration du processus de construction et de déploiement des images Docker utilisées pour les supports de formation, notamment en vue de leur intégration avec le SSP Cloud. Des ajustements ont également été apportés pour assurer la compatibilité avec des versions spécifiques de R et pour faciliter la gestion des secrets utilisés par les workflows GitHub Actions.

### Évolutions fonctionnelles
- Ajout du module M6 Rmd aux modules déployés.
- Mise à jour du journal.

### Évolutions techniques
- Passage des GitHub Actions à l'utilisation d'un secret `GITHUB_PAT` fixe pour la réinstallation des images Docker dans le SSP Cloud. Ceci améliore la fiabilité du processus de déploiement.
- Mise à jour de la version de `pak` dans les GitHub Actions pour assurer la compatibilité et la stabilité.
- Modification de la version de R pour assurer la compatibilité avec le SSP Cloud.
- Amélioration des workflows GitHub Actions pour la création des images R 4.6 sur `ghcr.io`.
- Mise à jour des workflows GitHub Actions `bookdown-build-and-deploy.yml`, `rstudio-image-build.yml` et `update-readme.yml` pour optimiser le processus de construction et de déploiement.

### Autres changements
- Mise à jour du fichier `CONTRIBUTING.md` avec un lien mis à jour vers la documentation des tokens SSP Cloud.
- Mise à jour du script `99_fork_parcours_r.sh`.
- Mise à jour du fichier `README.md` généré.
