## Changelog : anssi-portail (30 derniers jours, au 09 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration du parcours sécurisation, notamment l'ajout de fonctionnalités de suivi des mesures, l'amélioration de l'expérience utilisateur et la correction de bugs. Des améliorations SEO ont également été apportées, ainsi que des optimisations techniques et de sécurité.

### Évolutions fonctionnelles
- Ajout de la possibilité de suivre la prise en compte des mesures dans le parcours sécurisation.
- Affichage d'un badge et d'un message de félicitations à l'utilisateur après avoir complété un module du parcours sécurisation.
- Amélioration de l'affichage des liens et du contenu des cartes DSFR.
- Correction de l'affichage des images et des contrôles segmentés.
- Ajout de la possibilité de hacher l'email.
- Amélioration de l'affichage des pages "Collectivités" et "Catalogue".
- Ajout de liens canoniques et d'un fichier sitemap pour améliorer le référencement.
- Ajout de données structurées pour l'indexation.
- Ajout de la possibilité de rediriger les URL avec un slash final.
- Affichage du nombre de mesures sur le parcours sécurisation.
- Ajout d'une ancre pour afficher la demande de diagnostic sur la page "Collectivités".

### Évolutions techniques
- Mise en place du rendu côté serveur (SSR) pour plusieurs pages et composants (guides, collectivités, associations, etc.).
- Refonte de la configuration et des dépendances avec Nix et Renovate.
- Amélioration de la gestion des erreurs et de la sécurité (validation des configurations, désactivation des identifiants git, etc.).
- Optimisation des performances et du code (suppression de CSS inutilisé, mutualisation de code, etc.).
- Mise à jour de plusieurs dépendances (esbuild, dompurify, @babel/core, vite, form-data, etc.).
- Amélioration de la gestion du cache Grist.
- Introduction d'un constructeur de mesures.
- Utilisation de types plus explicites.
- Centralisation de la configuration d'Axios.
- Amélioration de la gestion des secrets dans les workflows.

### Autres changements
- Ajout de tests Playwright et amélioration de la couverture de tests.
- Ajout de métadonnées Open Graph et Twitter pour le partage sur les réseaux sociaux.
- Documentation mise à jour.
- Corrections de style et d'indentation.
- Ajout de commentaires et de documentation au code.
- Amélioration de la structure du projet et de la lisibilité du code.
- Ajout d'un fichier robots.txt.
- Ajout d'un outil `zizmor` pour valider la configuration.
- Suppression de la vidéo sur la page "Collectivités".
- Mise à jour du nombre d'organisations pour la demande d'aide.
- Amélioration de la hiérarchie des titres sur certaines pages pour le SEO.
