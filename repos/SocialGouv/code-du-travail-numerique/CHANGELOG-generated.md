## Changelog : code-du-travail-numerique (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la recherche, l'ajout d'une section actualités, et des corrections de bugs pour une meilleure expérience utilisateur. La migration des tests E2E de Cypress vers Playwright est également un point important pour la qualité du projet.

### Évolutions fonctionnelles

*   **Recherche :**
    *   Amélioration de l'affichage des résultats de recherche.
    *   Ajout de définitions aux résultats de recherche.
    *   Modification du libellé du moteur de recherche pour plus de clarté.
    *   Ajout d'infographies dans la recherche et les outils.
    *   Renommage des labels pour les contributions et autres pages.
*   **Actualités :**
    *   Ajout d'une page listant les actualités.
    *   Ajout du JSON-LD et de la page au plan du site pour un meilleur référencement.
    *   Corrections sur les titres, marges et liens des actualités.
*   **Outils :** Ajout d'une illustration du bulletin de paie sur le préavis de démission.
*   **Modale de convention collective :** Améliorations de l'accessibilité (a11y) et corrections d'UI.
*   **Indemnité de licenciement :** Cohérence du message dans la description.
*   **Modèles de courrier :** Ajustement du breakpoint entre les tailles d'écran `md` et `lg`.

### Évolutions techniques

*   **Tests E2E :** Migration des tests E2E de Cypress vers Playwright [#7212](https://github.com/SocialGouv/code-du-travail-numerique/issues/7212).
*   **pnpm :** Mise à jour de pnpm.

### Autres changements

*   **Corrections de tests E2E :** Corrections suite aux modifications apportées à la recherche et aux actualités [#7220](https://github.com/SocialGouv/code-du-travail-numerique/issues/7220) et [#7190](https://github.com/SocialGouv/code-du-travail-numerique/issues/7190).
*   **Suppression d'un événement de tracking :** Suppression de l'événement de tracking `agreement search` dans la modale.
*   **Correction d'un pattern dans la recherche :** Correction du pattern `idccXXXX` et ajout de la classe `siret` dans la recherche [#7216](https://github.com/SocialGouv/code-du-travail-numerique/issues/7216).
*   **Correction d'un mismatch dans la recherche des définitions :** Correction d'un problème de correspondance dans la recherche des définitions [#7206](https://github.com/SocialGouv/code-du-travail-numerique/issues/7206).
*   **Correction d'un problème de focus sur les icônes :** Utilisation de `focusable: false` sur les icônes [#7192](https://github.com/SocialGouv/code-du-travail-numerique/issues/7192).
