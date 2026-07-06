## Changelog : anssi-portail (30 derniers jours, au 03 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment avec l'introduction du rendu côté serveur (SSR) pour une meilleure performance et l'optimisation du parcours de sécurisation. Des corrections et améliorations ont également été apportées au SEO, à la gestion des contacts régionaux et à la robustesse générale du site.

### Évolutions fonctionnelles
- Implémentation du rendu côté serveur (SSR) pour améliorer la performance et l'accessibilité du site.
- Ajout de métadonnées Open Graph et Twitter pour améliorer le partage sur les réseaux sociaux.
- Amélioration du parcours de sécurisation avec l'ajout d'un système de prise en compte des mesures et d'un affichage de la progression.
- Ajout de la possibilité de donner un avis sur les mesures.
- Mise à jour des informations de contact des COT (Contact d'Organisation Territoriale) pour les régions ARA et Normandie.
- Ajout des pages des contacts régionaux dans le sitemap et amélioration de leur SEO.
- Ajout des pages ressources, services, guides et financements dans le sitemap.
- Amélioration de l'affichage des mesures avec un encart indiquant si elles ont été prises en compte.
- Ajout d'un toast pour informer l'utilisateur de l'état de ses actions.

### Évolutions techniques
- Migration vers des versions plus récentes de plusieurs dépendances pour améliorer la sécurité et la stabilité (esbuild, prettier-plugin-svelte, cssnano, diff, @napi-rs/canvas, @lab-anssi/lib, dompurify, @babel/core, vite, shell-quote, @types/node, @types/estree).
- Refactorisation du code pour améliorer la modularité et la maintenabilité.
- Amélioration de la gestion du cache Grist.
- Centralisation de la configuration d'Axios.
- Utilisation de types plus explicites dans le code.
- Introduction d'un constructeur d'utilisateur.
- Amélioration de la gestion des erreurs et des logs.
- Configuration de Renovate pour la gestion automatisée des dépendances.
- Utilisation du composant de présentation de l'ANSSI pour les sélecteurs multiples.
- Utilisation des composants DSFR pour les tags.

### Autres changements
- Mise à jour de la documentation.
- Correction de liens et d'URL canoniques pour améliorer le SEO.
- Suppression de code inutilisé et nettoyage du code.
- Amélioration de la hiérarchie des titres sur certaines pages pour le SEO.
- Ajout d'un fichier robots.txt et d'un sitemap.xml pour le SEO.
- Correction de bugs mineurs et amélioration de la robustesse du site.
- Modification du wording sur certaines pages.
- Suppression de la vidéo sur la page Collectivités.
- Ajout d'une ancre pour afficher la demande de diagnostic sur la page Collectivités.
- Mise à jour de la version de l'UI Kit.
- Ajout de tests unitaires.
