## Changelog : seves (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, les évolutions de Sèves se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans les modules SV (Surveillance Végétale) et SSA (Système de Surveillance Animale), avec des corrections de bugs, des améliorations de l'interface et l'ajout de nouvelles fonctionnalités comme la gestion des dates de publication et des documents. Des efforts ont également été faits pour améliorer la performance et la robustesse de l'application.

### Évolutions fonctionnelles
- **SV (Surveillance Végétale):**
  - Ajout de la gestion des "ON Phytophthora kernoviae".
  - Amélioration de l'interface pour les sites d'inspection, avec des renommages et un regroupement des éléments.
  - Correction de bugs et améliorations visuelles suite aux tests QA.
  - Ajout de la possibilité de saisir des numéros d'agrément d'établissement contenant des lettres.
  - Ajout d'un indicateur d'accessibilité pour les fiches de zone délimitée.
  - Ajout du numéro RASFF pour les objets TIAC.
  - Amélioration de l'affichage des dates dans les messages.
  - Ajout de la date de publication dans le formulaire d'Investigation TIAC.
  - Correction de l'affichage des badges sur les modals de prélèvement et de lieu.
- **SSA (Système de Surveillance Animale):**
  - Implémentation d'un nouveau sélecteur d'arbre (Treeselect) pour la vue de mise à jour des événements.
  - Amélioration de la vue liste des SSA pour de meilleures performances.
  - Ajout de la possibilité de télécharger des documents en archive ZIP.
  - Amélioration de la vue historique pour les modèles avec des relations profondes.
  - Ajout de la possibilité de mettre à jour une fiche ayant un lien vers un objet supprimé.
- **Général:**
  - Amélioration de la prévisualisation des images et des fichiers PDF.
  - Ajout d'une page d'accessibilité.
  - Amélioration de l'éditeur de texte enrichi pour les messages.
  - Correction de problèmes de CSP (Content Security Policy) pour Brave/Chromium.
  - Possibilité de télécharger des documents même sans date de publication.
  - Correction d'un problème d'affichage pour l'éditeur de texte enrichi.
  - Amélioration de la gestion des dates de réception.
  - Ajout d'une option pour afficher "Fin de suivi" dans l'export CSV.
  - Correction d'un bug empêchant le téléchargement de documents sur Chrome.

### Évolutions techniques
- Refactoring des actions pour les tests.
- Mise à jour de plusieurs dépendances : Django, Django-DSFR, Django-Post-Office, Ruff, Cryptography, Pytest, Psycopg2-binary, Pre-commit, Lxml, Sentry-SDK, Playwright.
- Correction d'un conflit de migration entre les migrations 0121_lieu_site_inspection_new et 0121_add_on_phytophthora_kernoviae.
- Amélioration de la robustesse des requêtes OIDC avec l'ajout d'un timeout.
- Correction d'un problème de test intermittent.
- Désactivation des warnings Python sur CI pour améliorer la lisibilité.
- Ajout de `related_name` dans SV pour `zone infestee`.
- Amélioration de la connexion à Redis pour Celery.
- Migration du modèle `SiteInspection` vers un `TextChoices`.
- Utilisation du filtre `or_empty_value_tag` pour remplacer le placeholder 'nc.'.
- Correction d'un bug lié à l'affichage des synthèses d'enregistrement simple.

### Autres changements
- Documentation mise à jour.
- Nettoyage de code et refactoring divers.
- Amélioration de la lisibilité des tests.
- Correction de l'affichage des ellipses sur les éléments TIAC.
- Ajout d'un bouton d'annulation sur la page d'édition TIAC.
- Uniformisation des liens d'annulation sur les fiches objets.
- Changement de format des filtres d'année et de numéro.
