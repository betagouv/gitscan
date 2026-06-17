## Changelog : reva (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Reva se concentrent sur l'amélioration de la sécurité avec l'ajout d'une analyse antivirus des fichiers téléchargés et l'implémentation de l'authentification à deux facteurs (OTP) par email et via l'application TOTP. Des améliorations ont également été apportées à l'interface d'administration, notamment pour la gestion des comptes AAP et des certifications, ainsi qu'à l'intégration FranceConnect.

### Évolutions fonctionnelles
- Ajout d'une analyse antivirus sur les fichiers téléchargés par les utilisateurs [#2a404a0](https://github.com/betagouv/reva/commit/2a404a0).
- Implémentation de l'authentification à deux facteurs (OTP) par email pour les utilisateurs, avec un bouton de renvoi de code [#1d524f4](https://github.com/betagouv/reva/commit/1d524f4).
- Ajout d'une fonctionnalité permettant aux AAPs d'ajouter de nouveaux comptes collaborateurs depuis la liste des comptes [#843253c](https://github.com/betagouv/reva/commit/843253c).
- Possibilité pour les administrateurs d'accéder à la liste des comptes collaborateurs AAP [#6f7a5cd](https://github.com/betagouv/reva/commit/6f7a5cd).
- Ajout d'un tableau de bord pour les administrateurs AAP [#e295910](https://github.com/betagouv/reva/commit/e295910).
- Amélioration de l'affichage et de la gestion des certifications dans l'interface d'administration [#221454c](https://github.com/betagouv/reva/commit/221454c).
- Ajout d'une page de détails pour les certifications, accessible depuis le résumé de la candidature [#12ad8f8](https://github.com/betagouv/reva/commit/12ad8f8).
- Amélioration de l'expérience utilisateur pour la gestion des motifs de fin d'accompagnement [#d883cc5](https://github.com/betagouv/reva/commit/d883cc5).
- Ajout d'un filtre pour les candidatures archivées dans l'interface d'administration [#7be05d1](https://github.com/betagouv/reva/commit/7be05d1).
- Amélioration de la gestion des filtres pour les candidatures liées aux VAE collectives [#b27f7c8](https://github.com/betagouv/reva/commit/b27f7c8).
- Ajout de filtres pour le statut du jury, le type d'accompagnement et les résultats de la faisabilité dans l'interface d'administration [#121bf81](https://github.com/betagouv/reva/commit/121bf81), [#f3c18d6](https://github.com/betagouv/reva/commit/f3c18d6), [#170eee7](https://github.com/betagouv/reva/commit/170eee7).

### Évolutions techniques
- Mise en place d'un service ClamAV pour l'analyse antivirus des fichiers [#2c52afb](https://github.com/betagouv/reva/commit/2c52afb).
- Mise à jour de Keycloak pour activer les fonctionnalités token-exchange:v1 et admin-fine-grained-authz:v1 [#e295910](https://github.com/betagouv/reva/commit/e295910).
- Refactorisation du code pour améliorer la gestion des tokens et des OTP dans l'API [#027d26b](https://github.com/betagouv/reva/commit/027d26b).
- Amélioration de la gestion des erreurs et des exceptions dans l'API [#2a404a0](https://github.com/betagouv/reva/commit/2a404a0).
- Optimisation des requêtes Prisma pour améliorer les performances [#8467053](https://github.com/betagouv/reva/commit/8467053).
- Migration de certains tests Cypress vers Playwright [#72d5ae9](https://github.com/betagouv/reva/commit/72d5ae9).

### Autres changements
- Mise à jour de diverses dépendances (shell-quote, axios, uuid, brace-expansion).
- Amélioration de la documentation et des commentaires dans le code.
- Correction de bugs mineurs et amélioration de la qualité du code.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Correction de problèmes d'affichage et de navigation dans l'interface d'administration.
- Suppression de code obsolète et nettoyage du code source.
- Mise à jour des messages et des textes dans l'interface utilisateur pour une meilleure clarté.
- Correction de la gestion des codes pays dans l'API [#d931558](https://github.com/betagouv/reva/commit/d931558).
- Correction de la gestion des erreurs FranceConnect [#de57ce6](https://github.com/betagouv/reva/commit/de57ce6).
- Suppression de la notice de migration du magic link [#9bc16e5](https://github.com/betagouv/reva/commit/9bc16e5).
- Suppression de la possibilité d'utiliser un mot de passe pour s'inscrire si la fonctionnalité est désactivée [#b346fd7](https://github.com/betagouv/reva/commit/b346fd7).
- Suppression de la possibilité de modifier la certification depuis la page de faisabilité [#9726a19](https://github.com/betagouv/reva/commit/9726a19).
- Correction de l'URL de création de compte collaborateur AAP [#baba950](https://github.com/betagouv/reva/commit/baba950).
- Suppression du bouton de rupture d'accompagnement pour les AAP [#c48cb5b](https://github.com/betagouv/reva/commit/c48cb5b).
- Correction de l'affichage du bouton de fin d'accompagnement dans le résumé de la candidature [#e803e02](https://github.com/betagouv/reva/commit/e803e02).
- Ajout d'une liste blanche d'adresses IP pour le service d'authentification [#3225d8b](https://github.com/betagouv/reva/commit/3225d8b).
- Ajout d'un filtre pour les candidatures avec un statut "abandonné" [#7be05d1](https://github.com/betagouv/reva/commit/7be05d1).
- Amélioration de la gestion des filtres pour les candidatures liées aux VAE collectives [#b27f7c8](https://github.com/betagouv/reva/commit/b27f7c8).
- Correction de la gestion des erreurs lors de la réinitialisation du mot de passe [#da009cb](https://github.com/betagouv/reva/commit/da009cb).
- Amélioration de la gestion des erreurs FranceConnect [#de57ce6](https://github.com/betagouv/reva/commit/de57ce6).
- Correction de la gestion des codes pays dans l'API [#d931558](https://github.com/betagouv/reva/commit/d931558).
- Suppression de la notice de migration du magic link [#9bc16e5](https://github.com/betagouv/reva/commit/9bc16e5).
- Suppression de la possibilité d'utiliser un mot de passe pour s'inscrire si la fonctionnalité est désactivée [#b346fd7](https://github.com/betagouv/reva/commit/b346fd7).
- Suppression de la possibilité de modifier la certification depuis la page de faisabilité [#9726a19](https://github.com/betagouv/reva/commit/9726a19).
- Correction de l'URL de création de compte collaborateur AAP [#baba950](https://github.com/betagouv/reva/commit/baba950).
- Suppression du bouton de rupture d'accompagnement pour les AAP [#c48cb5b](https://github.com/betagouv/reva/commit/c48cb5b).
- Correction de l'affichage du bouton de fin d'accompagnement dans le résumé de la candidature [#e803e02](https://github.com/betagouv/reva/commit/e803e02).
- Ajout d'une liste blanche d'adresses IP pour le service d'authentification [#3225d8b](https://github.com/betagouv/reva/commit/3225d8b).
- Ajout d'un filtre pour les candidatures avec un statut "abandonné" [#7be05d1](https://github.com/betagouv/reva/commit/7be05d1).
- Amélioration de la gestion des filtres pour les candidatures liées aux VAE collectives [#b27f7c8](https://github.com/betagouv/reva/commit/b27f7c8).
- Correction de la gestion des erreurs lors de la réinitialisation du mot de passe [#da009cb](https://github.com/betagouv/reva/commit/da009cb).
- Amélioration de la gestion des erreurs FranceConnect [#de57ce6](https://github.com/betagouv/reva/commit/de57ce6).
- Correction de la gestion des codes pays dans l'API [#d931558](https://github.com/betagouv/reva/commit/d931558).
- Suppression de la notice de migration du magic link [#9bc16e5](https://github.com/betagouv/reva/commit/9bc16e5).
- Suppression de la possibilité d'utiliser un mot de passe pour s'inscrire si la fonctionnalité est désactivée [#b346fd7](https://github.com/betagouv/reva/commit/b346fd7).
- Suppression de la possibilité de modifier la certification depuis la page de faisabilité [#9726a19](https://github.com/betagouv/reva/commit/9726a19).
- Correction de l'URL de création de compte collaborateur AAP [#baba950](https://github.com/betagouv/reva/commit/baba950).
- Suppression du bouton de rupture d'accompagnement pour les AAP [#c48cb5b](https://github.com/betagouv/reva/commit/c48cb5b).
- Correction de l'affichage du bouton de fin d'accompagnement dans le résumé de la candidature [#e803e02](https://github.com/betagouv/reva/commit/e803e02).
- Ajout d'une liste blanche d'adresses IP pour le service d'authentification [#3225d8b](https://github.com/betagouv/reva/commit/3225d8b).
- Ajout d'un filtre pour les candidatures avec un statut "abandonné" [#7be05d1](https://github.com/betagouv/reva/commit/7be05d1).
- Amélioration de la gestion des filtres pour les candidatures liées aux VAE collectives [#b27f7c8](https://github.com/betagouv/reva/commit/b27f7c8).
- Correction de la gestion des erreurs lors de la réinitialisation du mot de passe [#da009cb](https://github.com/betagouv/reva/commit/da009cb).
- Amélioration de la gestion des erreurs FranceConnect [#de57ce6](https://github.com/betagouv/reva/commit/de57ce6).
- Correction de la gestion des codes pays dans l'API [#d931558](https://github.com/betagouv/reva/commit/d931558).
- Suppression de la notice de migration du magic link [#9bc16e5](https://github.com/betagouv/reva/commit/9bc16e5).
- Suppression de la possibilité d'utiliser un mot de passe pour s'inscrire si la fonctionnalité est désactivée [#b346fd7](https://github.com/betagouv/reva/commit/b346fd7).
- Suppression de la possibilité de modifier la certification depuis la page de faisabilité [#9726a19](https://github.com/betagouv/reva/commit/9726a19).
- Correction de l'URL de création de compte collaborateur AAP [#baba950](https://github.com/betagouv/reva/commit/baba950).
- Suppression du bouton de rupture d'accompagnement pour les AAP [#c48cb5b](https://github.com/betagouv/reva/commit/c48cb5b).
- Correction de l'affichage du bouton de fin d'accompagnement dans le résumé de la candidature [#e803e02](https://github.com/betagouv/reva/commit/e803e02).
- Ajout d'une liste blanche d'adresses IP pour le service d'authentification [#3225d8b](https://github.com/betagouv/reva/commit/3225d8b).
- Ajout d'un filtre pour les candidatures avec un statut "abandonné" [#7be05d1](https://github.com/betagouv/reva/commit/7be05d1).
- Amélioration de la gestion des filtres pour les candidatures liées aux VAE collectives [#b27f7c8](https://github.com/betagouv/reva/commit/b27f7c8).
- Correction de la gestion des erreurs lors de la réinitialisation du mot de passe [#da009cb](https://github.com/betagouv/reva/commit/da009cb).
- Amélioration de la gestion des erreurs FranceConnect [#de57ce6](https://github.com/betagouv/reva/commit/de57ce6).
- Correction de la gestion des codes pays dans l'API [#d931558](https://github.com/betagouv/reva/commit/d931558).
- Suppression de la notice de migration du magic link [#9bc16e5](https://github.com/betagouv/reva/commit/9bc16e5).
- Suppression de la possibilité d'utiliser un mot de passe pour s'inscrire si la fonctionnalité est désactivée [#b346fd7](https://github.com/betagouv/reva/commit/b346fd7).
- Suppression de la possibilité de modifier la certification depuis la page de faisabilité [#9726a19](https://github.com/betagouv/reva/commit/9726a19).
- Correction de l'URL de création de compte collaborateur AAP [#baba950](https://github.com/betagouv/reva/commit/baba950).
- Suppression du bouton de rupture d'accompagnement pour les AAP [#c48cb5b](https://github.com/betagouv/reva/commit/c48cb5b).
- Correction de l'affichage du bouton de fin d'accompagnement dans le résumé de la candidature [#e803e02](https://github.com/betagouv/reva/commit/e803e02).
- Ajout d'une liste blanche d'adresses IP pour le service d'authentification [#3225d8b](https://github.com/betagouv/reva/commit/3225d8b).
- Ajout d'un filtre pour les candidatures avec un statut "abandonné" [#7be05d1](https://github.com/betagouv/reva/commit/7be05d1).
- Amélioration de la gestion des filtres pour les candidatures liées aux VAE collectives [#b27f7c8](https://github.com/betagouv/reva/commit/b27f7c8).
- Correction de la gestion des erreurs lors de la réinitialisation du mot de passe [#da009cb](https://github.com/betagouv/reva/commit/da009cb).
- Amélioration de la gestion des erreurs FranceConnect [#de57ce6](https://github.com/betagouv/reva/commit/de57ce6).
- Correction de la gestion des codes pays dans l'API [#d931558](https://github.com/betagouv/reva/commit/d931558).
- Suppression de la notice de migration du magic link [#9bc16e5](https://github.com/betagouv/reva/commit/9bc16e5).
- Suppression de la possibilité d'utiliser un mot de passe pour s'inscrire si la fonctionnalité est désactivée [#b346fd7](https://github.com/betagouv/reva/commit/b346fd7).
- Suppression de la possibilité de modifier la certification depuis la page de faisabilité [#9726a19](https://github.com/betagouv/reva/commit/9726a19).
- Correction de l'URL de création de compte collaborateur AAP [#baba950](https://github.com/betagouv/reva/commit/baba950).
