## Changelog : seves (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions de Sèves se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des documents (prévisualisation, téléchargement groupé, dates de publication), de la navigation et de l'accessibilité. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations techniques pour la robustesse et la maintenance du code.

### Évolutions fonctionnelles
- Ajout d'une page d'accessibilité pour améliorer l'utilisation de l'outil par tous les utilisateurs.
- Possibilité de télécharger des documents en archive ZIP [#9a688f1](https://github.com/betagouv/seves/commit/9a688f1).
- Amélioration de l'affichage et de la précision des dates dans diverses vues et exports.
- Prévisualisation des images et des fichiers PDF directement dans l'interface.
- Correction de l'affichage du rich text editor pour une meilleure expérience de saisie.
- Ajout du numéro RASFF pour les objets TIAC.
- Amélioration de l'historique des modifications pour les modèles avec des relations complexes.
- Possibilité de télécharger des documents même sans date de publication [#cc771d9](https://github.com/betagouv/seves/commit/cc771d9).
- Ajout d'un bouton d'annulation sur la page d'édition TIAC [#e0be778](https://github.com/betagouv/seves/commit/e0be778).
- Amélioration de l'affichage des informations sur les prélèvements et les lieux.
- Ajout de la possibilité de filtrer par année et numéro.
- Correction de l'affichage des badges sur les modals de prélèvement et de lieu [#2668203](https://github.com/betagouv/seves/commit/2668203).

### Évolutions techniques
- Refactorisation des actions pour les tests.
- Correction d'un conflit de migration entre deux migrations (0121_lieu_site_inspection_new et 0121_add_on_phytophthora_kernoviae) [#ba0fb8a](https://github.com/betagouv/seves/commit/ba0fb8a).
- Mise à jour de plusieurs dépendances : Django, Django-DSFR, Django-Post-Office, Sentry-SDK, Ruff, Psycopg2-binary, Pre-commit, Lxml, Pytest, Cryptography, Django-Debug-Toolbar.
- Amélioration de la gestion des erreurs OIDC avec ajout d'un timeout pour éviter les blocages en production [#0d85baf](https://github.com/betagouv/seves/commit/0d85baf).
- Correction d'un problème de test intermittent.
- Utilisation de `and_more_ellipsis_tooltip` pour uniformiser l'affichage des ellipses.
- Suppression de l'utilisation de SSA dans l'application core.
- Amélioration des performances de la vue listant les SSA.
- Correction d'un problème lié à l'affichage de textes longs sans retour à la ligne.
- Ajout d'une gestion de la reconnexion à Redis pour Celery.
- Correction d'un problème avec l'affichage des synthèses d'enregistrement simple.
- Ajout d'un related name dans SV pour zone infestee.
- Correction d'un problème d'affichage des dates de publication dans les formulaires TIAC.
- Suppression de l'utilisation de placeholders "nc." et remplacement par un filtre plus générique.

### Autres changements
- Ajout d'un ON pour SV.
- Ajout d'un ON pour Phytophthora kernoviae.
- Mise à jour de la documentation.
- Corrections de style et de cohérence du code.
- Désactivation des warnings Python dans le CI pour améliorer la lisibilité.
- Migration du modèle SiteInspection vers un TextChoices.
- Ajout de la possibilité d'autoriser des lettres dans le numéro d'agrément d'un établissement [#2055cfe](https://github.com/betagouv/seves/commit/2055cfe).
- Amélioration de l'affichage des cartes d'établissement dans les tests.
