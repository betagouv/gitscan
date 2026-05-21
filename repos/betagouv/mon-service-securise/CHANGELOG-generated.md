## Changelog : mon-service-securise (30 derniers jours, au 2026-05-20)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'accessibilité, la correction de bugs et l'implémentation de nouvelles fonctionnalités liées à la gestion des administrateurs d'organisations et au parcours d'homologation. Une migration vers les composants DSFR (Design System for French Administration) a également été initiée, notamment pour le header et la navigation.

### Évolutions fonctionnelles

*   **Gestion des Administrateurs :**
    *   Implémentation de la lecture des administrateurs d'organisations.
    *   Ajout d'une méthode pour lister les entités d'un administrateur ou superviseur.
    *   Possibilité d'ajouter des entités administrées.
    *   Affichage des utilisateurs administrés dans une nouvelle page dédiée.
    *   Ajout d'un nouveau dépôt pour la gestion des administrateurs d'organisations.
*   **Parcours d'Homologation :**
    *   Implémentation du parcours d'homologation en SPA (Single Page Application).
    *   Ajout des étapes "Avis", "Téléchargement du dossier", "Récapitulatif" et "Décision".
    *   Possibilité de reprendre une homologation.
    *   Affichage d'un étapier pour suivre la progression.
    *   Ajout de boutons "Précédent" et "Suivant" pour naviguer dans le parcours.
*   **Indice Cyber :**
    *   Affichage de l'indice cyber personnalisé dans la page dédiée.
    *   Affichage des valeurs d'indice cyber ANSSI et personnalisé dans le tableau de bord.
*   **Améliorations diverses :**
    *   Correction de liens et de l'affichage de la page de connexion.
    *   Ajout d'une landing page pour "Sécurisez votre service numérique".
    *   Ajout d'une landing page pour "Industrialisez vos homologations".
    *   Ajout d'un bloc "Communauté" sur la page d'accueil.

### Évolutions techniques

*   **Accessibilité :** Correction de nombreux problèmes d'accessibilité sur différentes pages (conseils cyber, statistiques, CGU, activation, mentions légales, à propos, accessibilité, politique de confidentialité, inscription, création de service).
*   **Refactoring :**
    *   Conversion de plusieurs modules en TypeScript (superviseur, utilisateur, dépôt de données admin).
    *   Extraction de code réutilisable dans de nouvelles fonctions et composants.
    *   Suppression de code obsolète.
*   **DSFR :** Migration progressive vers les composants du Design System for French Administration (DSFR) pour le header et la navigation.
*   **Infrastructure :** Suppression d'un ancien dépôt d'admins d'organisations.
*   **Tests :** Correction de tests et ajout de tests d'accessibilité.

### Autres changements

*   Mise à jour de plusieurs dépendances (eslint, axe-core/playwright, vitest/eslint-plugin, electric-sql/pglite, uuid, @tiptap/*, @sentry/vite-plugin, basic-ftp, axios).
*   Amélioration de la structure du code et de la documentation.
*   Correction de typos et de problèmes de style.
*   Ajout de commentaires et de documentation pour faciliter la maintenance.
*   Correction de fuites CSS.
*   Suppression de fichiers inutiles.
*   Amélioration de la gestion des erreurs.
*   Ajout de logs pour faciliter le débogage.
