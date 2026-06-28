## Changelog : anssi-portail (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, l'optimisation de l'expérience utilisateur autour du parcours sécurisation et des mesures, ainsi que des améliorations SEO et de maintenance technique. L'ajout de nouvelles fonctionnalités, comme l'affichage des mesures et la gestion des prises en compte, renforce l'utilité du portail pour les professionnels de la sécurité.

### Évolutions fonctionnelles
- Ajout de l'affichage des mesures et de leurs détails, incluant les risques, les actions prioritaires et les liens pour aller plus loin.
- Implémentation d'un système de prise en compte des mesures, avec affichage de la progression et encouragement à accéder à des mesures plus avancées.
- Amélioration de la page 404 pour une meilleure expérience utilisateur.
- Ajout de la possibilité de soumettre des avis sur les mesures.
- Affichage du badge cyberdépart et d'un toast de félicitation lors de la complétion du parcours sécurisation.
- Intégration des données structurées pour l'indexation SEO.
- Ajout des pages des contacts régionaux et des pages statiques associées au sitemap pour améliorer le référencement.
- Ajout des pages ressources, services et financements au sitemap.
- Correction de l'affichage des liens canoniques et redirection des URL avec un slash final.
- Amélioration de la hiérarchie des titres sur plusieurs pages (Accueil, Financements, Catalogue, Test de maturité).

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour renforcer la sécurité et bénéficier des dernières corrections (Multer, DomPurify, @babel/core, vite, form-data, shell-quote).
- Configuration de Renovate pour la gestion automatisée des dépendances.
- Amélioration de la gestion des erreurs et de la journalisation.
- Refonte de la gestion des sessions pour plus de sécurité.
- Optimisation de la récupération des mesures et de la gestion du cache Grist.
- Utilisation du composant de progression de l'UI Kit.
- Centralisation de la configuration d'Axios.
- Ajout de tests et correction de bugs.
- Migration vers Ruby 4.0.5 et mise à jour des actions Ruby dans la CI.
- Utilisation de l'UI Kit en version 1.54.0.

### Autres changements
- Ajout de fichiers robots.txt et sitemap.xml pour le SEO.
- Mise à jour de la documentation README.
- Correction de petites erreurs de typographie et de wording.
- Ajout et mise à jour des contacts régionaux.
- Suppression de vidéos obsolètes.
- Amélioration de la structure du code et refactoring de certains composants.
- Correction d'une vulnérabilité.
