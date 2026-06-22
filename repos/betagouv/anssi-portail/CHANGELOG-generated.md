## Changelog : anssi-portail (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du référencement (SEO) du site, la sécurisation des dépendances, l'implémentation du parcours sécurisation (notamment l'affichage des mesures et la prise en compte par les utilisateurs), et des corrections de bugs et améliorations de l'expérience utilisateur. Plusieurs mises à jour de composants DSFR ont également été intégrées.

### Évolutions fonctionnelles
- **Parcours sécurisation :** Implémentation de l'affichage des mesures de sécurité et de la possibilité pour les utilisateurs de les prendre en compte. Un badge indique si une mesure a été prise en compte.
- **Mesures :** Affichage des détails d'une mesure, incluant les risques, les actions prioritaires, les liens pour aller plus loin et les exigences ReCyF.
- **Avis sur les mesures :** Possibilité pour les utilisateurs de donner leur avis sur les mesures, avec stockage de cet avis.
- **Page 404 :** Amélioration de la page d'erreur 404.
- **Contact :** Mise à jour des contacts des régions PACA, Normandie et ARA. Ajout et suppression de COT (Contact d'Organisation Territoriale).
- **Collectivités :** Ajout d'une ancre pour afficher la demande de diagnostic.

### Évolutions techniques
- **SEO :** Amélioration du référencement avec suppression des titres `<h1>` dupliqués, redirection des URL avec `/` final, utilisation d'URL kebab-case, ajout de balises canoniques et ajout des fichiers `robots.txt` et `sitemap.xml`.
- **Sécurité :** Mise à jour de plusieurs dépendances pour corriger des vulnérabilités (dompurify, @babel/core, vite, form-data, shell-quote).
- **CI/CD :** Épinglage des versions des dépendances des GitHub Actions et configuration de prettier.
- **Architecture :** Refonte de la gestion des erreurs, centralisation de la configuration d'axios, utilisation d'un constructeur d'utilisateur, introduction d'un constructeur de mesures.
- **Base de données :** Adaptation de la base de données pour le parcours sécurisation.
- **Cache :** Amélioration de la gestion du cache Grist.
- **Nettoyage de code :** Suppression de code inutilisé et simplification de certains composants.
- **Typescript :** Rendre plus explicite les types des variables.

### Autres changements
- Ajout de tests pour éviter la création du sitemap à chaque test.
- Augmentation du rate limit global.
- Documentation mise à jour.
- Amélioration des messages d'erreur au démarrage.
- Tri des lignes des overrides.
- Mise à jour de la version de Ruby et des actions associées dans la CI.
- Ajout d'illustrations et d'un composant Toast.
- Amélioration de l'affichage de la progression du parcours sécurisation.
- Correction de bugs mineurs liés à l'affichage et au z-index.
