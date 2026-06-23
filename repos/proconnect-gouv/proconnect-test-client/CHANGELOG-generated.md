## Changelog : proconnect-test-client (30 derniers jours, au 22 juin 2026)

### Résumé
Ce client de test ProConnect a bénéficié d'améliorations significatives concernant la gestion des niveaux d'authentification (ACR), notamment pour l'authentification multifacteur (MFA). Des corrections ont également été apportées pour assurer la cohérence de la configuration et la gestion des variables d'environnement. Des mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de connexion avec un ACR complet ([#207](https://github.com/proconnect-gouv/proconnect-test-client/pull/207)).
- Mise à jour des valeurs par défaut des ACR pour l'authentification multifacteur (MFA) ([#202](https://github.com/proconnect-gouv/proconnect-test-client/pull/202)).
- Amélioration de la structure des valeurs ACR pour le déclenchement de la MFA ([#193](https://github.com/proconnect-gouv/proconnect-test-client/pull/193)).

### Évolutions techniques
- Uniformisation des noms de variables d'environnement pour une meilleure cohérence ([#194](https://github.com/proconnect-gouv/proconnect-test-client/pull/194)).
- Nettoyage de la configuration dans le fichier `.env` ([#193](https://github.com/proconnect-gouv/proconnect-test-client/pull/193)).
- Correction d'une erreur liée au nom d'une variable et à la gestion des chaînes de caractères vides ([#194](https://github.com/proconnect-gouv/proconnect-test-client/pull/194)).

### Autres changements
- Mise à jour de la dépendance `form-data` de la version 4.0.5 à la version 4.0.6 dans le répertoire `/e2e` ([#203](https://github.com/proconnect-gouv/proconnect-test-client/pull/203)).
- Mise à jour de l'action `actions/checkout` de la version 6 à la version 7 ([#204](https://github.com/proconnect-gouv/proconnect-test-client/pull/204)).
- Mise à jour de la dépendance `body-parser` de la version 2.2.2 à la version 2.3.0 ([#205](https://github.com/proconnect-gouv/proconnect-test-client/pull/205)).
- Mises à jour de plusieurs dépendances de développement (Cypress, prettier, esbuild, tsx, morgan, ejs, qs, @cypress/request, tmp) via Dependabot.
