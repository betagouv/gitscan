## Changelog : passemarche (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment en matière de configuration des marchés et de gestion des lots. Des corrections de bugs et des mises à jour de sécurité ont également été apportées pour assurer la stabilité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'icônes de type de marché (travaux, services, fournitures) dans l'attestation acheteur et le wizard candidat [#447](https://github.com/datagouv/passemarche/pull/447).
- Amélioration de l'affichage des badges de type de marché dans la configuration des lots acheteur [#448](https://github.com/datagouv/passemarche/pull/448).
- Possibilité de télécharger une synthèse PDF de la configuration du marché [#452](https://github.com/datagouv/passemarche/pull/452).
- Inclusion des lots sélectionnés par le candidat dans le webhook de candidature [#475](https://github.com/datagouv/passemarche/pull/475).
- Amélioration de la gestion des motifs d'exclusion, avec un wording spécifique et un rappel dans les attestations [#486](https://github.com/datagouv/passemarche/pull/486).
- Correction de l'affichage des marchés publiés côté candidat dans l'interface de test (fake editor) [#471](https://github.com/datagouv/passemarche/pull/471).
- Clarification du message d'erreur lorsque le marché n'est pas encore publié [#472](https://github.com/datagouv/passemarche/pull/472).
- Amélioration de l'organisation du dossier ZIP généré, avec une structure par type de lot [#466](https://github.com/datagouv/passemarche/pull/466).

### Évolutions techniques
- Mise à jour de Rails vers la version 8.1.3.1 pour corriger une vulnérabilité de sécurité (CVE-2026-66066) [#485](https://github.com/datagouv/passemarche/pull/485).
- Refactor de la logique de scope des attributs de marché pour une meilleure organisation [#450](https://github.com/datagouv/passemarche/pull/450).
- Suppression de code mort et nettoyage de la base de code [#468](https://github.com/datagouv/passemarche/pull/468).
- Amélioration de la gestion des données manuelles lors de la re-candidature et du refetch des données API [#442](https://github.com/datagouv/passemarche/pull/442) et [#449](https://github.com/datagouv/passemarche/pull/449).
- Correction d'une race condition lors de la publication d'un marché [#457](https://github.com/datagouv/passemarche/pull/457).
- Ajout de la gem `aws-sdk-s3` pour l'environnement de test (sandbox) [#444](https://github.com/datagouv/passemarche/pull/444).

### Autres changements
- Suppression de la documentation technique locale, synchronisée avec guides.data.gouv.fr [#473](https://github.com/datagouv/passemarche/pull/473).
- Mise à jour des dépendances : `simplecov`, `solid_queue`, `pagy`, `csv`, `thruster`, `cucumber-rails` et `aws-sdk-s3`.
- Corrections de tests et ajout de nouveaux tests pour couvrir les nouvelles fonctionnalités et corrections de bugs.
- Amélioration de l'espacement de l'interface utilisateur et correction de problèmes d'affichage [#482](https://github.com/datagouv/passemarche/pull/482).
- Correction de la largeur d'un bouton sur la page marché publié [#481](https://github.com/datagouv/passemarche/pull/481).
