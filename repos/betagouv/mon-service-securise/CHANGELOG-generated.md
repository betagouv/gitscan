## Changelog : mon-service-securise (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'interface utilisateur, notamment la refonte de la page d'accueil et l'intégration du nouveau design système (DSFR). L'accès aux données et la navigation ont été optimisés, avec l'ajout de nouvelles pages et fonctionnalités liées à la gestion des risques et des indices cyber. Des corrections et améliorations ont également été apportées pour améliorer l'accessibilité et la stabilité de l'application.

### Évolutions fonctionnelles
- Intégration du header DSFR pour une expérience utilisateur plus cohérente.
- Ajout de la page "Risques" dans la navigation "Sécuriser".
- Affichage des dossiers d'homologation dans la SPA, avec des boutons pour la création, la reprise et le téléchargement du tampon d'homologation.
- Affichage des données de dossiers d'homologation dans le service complet.
- Ajout d'une page squelette pour l'Indice Cyber, avec l'affichage du radar et des tranches d'indice.
- Affichage des contacts utiles du service.
- Implémentation de l'objet de données pour l'annexe PDF des risques V2.
- Génération des matrices de risque V2 dans le PDF d'annexes.
- Affichage des indices cyber ANSSI et personnalisé dans l'entête des pages service.
- Ajout du bouton de suppression de dossier courant.
- Ajout du bandeau de simulation vers le référentiel V2.
- Amélioration de l'affichage des risques résiduels.

### Évolutions techniques
- Migration vers le nouveau design système (DSFR) pour le header, le footer et la navigation.
- Refonte de la page d'accueil pour les différentes tailles d'écran (mobile, tablette, desktop).
- Transformation de plusieurs pages (Décrire V2, Mesures, Contacts Utiles) en Single Page Application (SPA).
- Utilisation de l'API pour charger les données des services.
- Refactoring du code pour utiliser TypeScript et améliorer la structure.
- Ajout de tests d'accessibilité avec Playwright et Axe.
- Mise à jour des dépendances (Express, PostgreSQL, bcrypt, jsonwebtoken, axios, pg, knex, dotenv, Svelte, Vite, etc.).
- Amélioration de la gestion des erreurs et des états de chargement.
- Optimisation des performances et de la réactivité de l'interface utilisateur.

### Autres changements
- Correction de typos et de bugs mineurs.
- Amélioration de la documentation.
- Suppression de code obsolète.
- Mise à jour des workflows CI/CD.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
- Correction de problèmes d'accessibilité.
- Suppression de styles CSS obsolètes.
- Amélioration de la gestion des erreurs dans les tests.
- Ajout de retries pour la recherche d'entreprise.
- Publication des rapports d'accessibilité dans Mattermost.
