## Changelog : anssi-portail (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du référencement (SEO), la sécurisation du site (mise à jour de dépendances, protection contre les failles), l'implémentation du parcours sécurisation (notamment l'affichage des mesures et la prise en compte par les utilisateurs), et l'amélioration de l'expérience utilisateur grâce à l'utilisation de composants du Design System Français (DSFR).

### Évolutions fonctionnelles
- Ajout de la possibilité pour les utilisateurs de donner leur avis sur les mesures de sécurité et de les marquer comme prises en compte.
- Amélioration de l'affichage et de la navigation dans le parcours sécurisation, avec l'ajout de badges de progression et de liens vers des mesures plus avancées.
- Affichage des mesures de sécurité pour les 5 modules du parcours sécurisation.
- Ajout d'un fil d'Ariane utilisant les composants DSFR pour une meilleure navigation.
- Amélioration de la page 404.
- Ajout des mesures pour les 5 modules.
- Affichage des contact de la région PACA, ARA et Normandie.

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité (dompurify, @babel/core, vite, form-data, shell-quote, svelte, qs).
- Refonte de la gestion des erreurs et des logs pour une meilleure robustesse.
- Utilisation accrue des composants du Design System Français (DSFR) pour l'interface utilisateur (boutons, badges, segmented control, fil d'Ariane).
- Amélioration de la configuration et du déploiement (utilisation de corepack, gestion des versions de Node.js).
- Optimisation de la configuration d'Axios.
- Centralisation de la configuration et des chemins.
- Amélioration de la gestion du cache Grist.
- Ajout d'un constructeur d'utilisateur.
- Introduction d'un constructeur de mesures.
- Suppression de code inutilisé et simplification de certains composants.
- Ajout de tests et correction de bugs.
- Mise en place d'un système de notification à MQC lors des changements.

### Autres changements
- Amélioration des messages d'erreurs.
- Nettoyage du code et refactoring de certains composants.
- Ajout de documentation.
- Mise à jour des informations de contact.
- Suppression de vidéos et d'éléments obsolètes.
- Correction de problèmes de z-index et de styles.
- Ajout de fichiers robots.txt et sitemap.xml pour le SEO.
- Suppression des titres <h1> dupliqués pour le SEO.
- Redirection des URL avec un slash final vers les URL sans slash.
- Utilisation d'URL kebab-case pour les pages Mentions Légales et À propos.
- Ajout d'un lien canonique pour le SEO.
- Tri des lignes des overrides.
- Ajout de la signature de base64.
- Ajout de la signature de base64.
- Ajout des fichiers de skills pour l'IA.
- Suppression des jobs d’approbation.
- Utilise les valeurs paramétrées pour MQC.
- Appelle MQC avec les modifications.
- Décide de notifier MQC de changement.
- Échoue lorsque l’appel à MQC échoue.
- Ajoute les différences dans l’artefact.
- Filtre les erreurs 'Network error' d’axios.
- Filtre les erreurs qui ne viennent pas d’MSC.
- N’efface pas la preuve de sauvegarde.
- Aligne la vérification sur la synchro.
