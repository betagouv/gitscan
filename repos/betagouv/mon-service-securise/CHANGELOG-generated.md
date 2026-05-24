## Changelog : mon-service-securise (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des administrateurs et des superviseurs, ainsi que sur la refonte du parcours d'homologation pour une meilleure expérience utilisateur. Des corrections d'accessibilité et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles

*   **Gestion des administrateurs :**
    *   Ajout d'une route `/api/admin/verifieEmail` pour vérifier un email d'administrateur.
    *   Implémentation de l'invitation et de la gestion des administrateurs d'organisations, incluant l'envoi d'emails de notification.
    *   Affichage de la liste des administrateurs associés à une entité.
    *   Possibilité de nommer des administrateurs en tant que superviseurs.
    *   Affichage du nombre d'utilisateurs et de services supervisés par un administrateur.
*   **Parcours d'homologation :**
    *   Refonte complète du parcours d'homologation en SPA (Single Page Application).
    *   Ajout des étapes "Récapitulatif", "Avis", "Documents" et "Décision".
    *   Navigation entre les étapes avec des boutons "Précédent" et "Suivant".
    *   Affichage d'un étapier visuel pour suivre la progression.
    *   Possibilité de reprendre une homologation en cours.
*   **Autres améliorations :**
    *   Ajout d'une modale "Démarche d'homologation indicative".
    *   Affichage du nombre d'utilisateurs de chaque entité supervisée.
    *   Affichage du nom de l'entité en gras.
    *   Correction de l'affichage des admins sur plusieurs lignes.

### Évolutions techniques

*   **Refactoring et migration vers TypeScript :**
    *   Conversion de plusieurs services et modèles (Superviseur, Utilisateur) en TypeScript.
    *   Remplacement de mocks par l'utilisation de la persistance mémoire.
*   **Gestion des superviseurs :**
    *   Refonte de la gestion des superviseurs avec un nouveau dépôt de données orienté objet.
    *   Chiffrement des données des tables superviseur et admin\_organisations.
*   **Architecture :**
    *   Utilisation du nouveau dépôt d'admins dans le service d'administration des organisations.
    *   Séparation de la logique de rattachement d'une entité à un superviseur dans un service dédié.
*   **Dépendances :**
    *   Mise à jour de plusieurs dépendances (eslint, @axe-core/playwright, uuid, etc.).

### Autres changements

*   **Accessibilité :**
    *   Corrections de problèmes d'accessibilité sur plusieurs pages (Statistiques, CGU, Activation, Connexion, Création de service, Mentions Légales, Politique de Confidentialité, etc.).
    *   Ajout d'attributs `aria-label` pour améliorer l'accessibilité.
*   **Documentation :**
    *   Ajout d'articles Crisp aux pages testées pour l'accessibilité.
*   **Style et UI :**
    *   Améliorations de l'interface utilisateur sur la page d'accueil et d'autres pages.
    *   Correction de problèmes de contraste et de mise en page.
*   **Nettoyage de code :**
    *   Suppression de code obsolète et de mocks.
    *   Renommage de variables et de fonctions pour une meilleure cohérence.
    *   Extraction de composants et de fonctions réutilisables.
*   **Tests :**
    *   Corrections de tests et ajout de nouveaux tests.
