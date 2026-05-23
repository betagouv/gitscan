## Changelog : reva (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions de reva se concentrent sur l'amélioration de la sécurité avec l'implémentation de l'authentification à deux facteurs (2FA) via TOTP, l'ajout de nouvelles fonctionnalités pour les administrateurs (gestion des lieux d'accueil, tableaux de bord AAP, gestion des dates de jury), et des corrections de bugs pour améliorer la stabilité et l'expérience utilisateur. Des efforts ont également été faits pour moderniser l'infrastructure et les dépendances du projet.

### Évolutions fonctionnelles
- **Authentification:** Ajout de l'authentification à deux facteurs (TOTP) pour les candidats avec interface utilisateur dédiée et mutation API correspondante. [#027d26b](https://github.com/betagouv/reva/commit/027d26b)
- **Administration:**
    - Amélioration de la gestion des lieux d'accueil avec ajout d'un bouton de suppression et d'une confirmation pour éviter les suppressions accidentelles. [#bd214c5](https://github.com/betagouv/reva/commit/bd214c5)
    - Ajout de nouveaux tableaux de bord pour les gestionnaires AAP, incluant des informations sur les résultats des jurys. [#0c7a996](https://github.com/betagouv/reva/commit/0c7a996)
    - Possibilité pour les administrateurs de confirmer un abandon de candidature par un candidat. [#5f9bdb2](https://github.com/betagouv/reva/commit/5f9bdb2)
    - Amélioration de l'interface et de l'expérience utilisateur de la page d'archivage des candidatures. [#36bd05d](https://github.com/betagouv/reva/commit/36bd05d)
- **Candidatures:**
    - Ajout d'un bouton de suppression de candidature pour les candidats (sous conditions). [#1d1c02e](https://github.com/betagouv/reva/commit/1d1c02e)
    - Amélioration des messages d'information concernant l'abandon de candidature. [#27a0f41](https://github.com/betagouv/reva/commit/27a0f41)
- **API:**
    - Possibilité pour l'administrateur de confirmer un abandon de candidature. [#f8b6247](https://github.com/betagouv/reva/commit/f8b6247)
    - Ajout d'une fonction pour corriger les codes INSEE des pays de naissance, notamment pour France Connect. [#10efe8c](https://github.com/betagouv/reva/commit/10efe8c)
    - Amélioration des règles métier concernant la fin d'accompagnement. [#336a70d](https://github.com/betagouv/reva/commit/336a70d)
    - Ajout de la possibilité de planifier une date de jury uniquement après l'envoi du dossier de validation. [#670237f](https://github.com/betagouv/reva/commit/670237f)

### Évolutions techniques
- **Sécurité:**
    - Refonte de l'authentification de l'administration avec Keycloak, incluant l'utilisation de cookies httpOnly pour une meilleure sécurité. [#7c7b3cc](https://github.com/betagouv/reva/commit/7c7b3cc)
    - Amélioration de la gestion des tokens et des sessions. [#9c17500](https://github.com/betagouv/reva/commit/9c17500)
- **Infrastructure:**
    - Mise à jour de plusieurs dépendances (Next.js, Strapi, etc.).
    - Amélioration de la configuration de Traefik pour augmenter la limite de débit. [#f3bf3eb](https://github.com/betagouv/reva/commit/f3bf3eb)
- **Tests:**
    - Augmentation du nombre de shards Playwright pour améliorer la performance des tests. [#537c1d9](https://github.com/betagouv/reva/commit/537c1d9)
    - Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
- **Refactoring:**
    - Nettoyage et simplification du code dans divers modules. [#a45d459](https://github.com/betagouv/reva/commit/a45d459)
    - Extraction de composants réutilisables.

### Autres changements
- Amélioration de la documentation et des messages d'erreur.
- Mise à jour des dépendances pour corriger des vulnérabilités et améliorer la stabilité.
- Corrections de typographie et d'accessibilité.
- Suppression de code obsolète.
- Ajout de logs pour faciliter le débogage.
- Amélioration des performances de certaines requêtes API.
- Suppression de certaines fonctionnalités expérimentales.
